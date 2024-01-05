
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils, MType, Symbol
from StaticError import *
from functools import reduce


import copy

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
class Symbol:
    def __init__(self, name, mptype, value = None):
        self.name = name
        self.mptype = mptype
        self.value = value

class ExpUtils:
    @staticmethod
    def isNotConstOperand(exprType):
        return type(exprType) in [NewExpr]

    @staticmethod
    def isNotIntFloatType(exprType):
        return type(exprType) not in [IntType, FloatType]

    @staticmethod
    def isNotIntBoolType(exprType):
        return type(exprType) not in [IntType, BoolType]

    @staticmethod
    def isNotAccess(exprType):
        return type(exprType) not in [CallExpr, FieldAccess, CallStmt]


class StaticChecker(BaseVisitor):
    inttype = IntType()
    floattype = FloatType()
    voidtype = VoidType()
    booltype = BoolType()
    stringtype = StringType() 
    global_envi = [
        Symbol("@readInt", MType([], IntType()),False),
        Symbol("@writeIntLn", MType([IntType()],VoidType()),False),
        Symbol("@readFloat", MType([],FloatType()),False),
        Symbol("@writeFloat", MType([FloatType()],VoidType()),False),
        Symbol("@readBool", MType([],BoolType()),False),
        Symbol("@writeBool", MType([BoolType()],BoolType()),False),
        Symbol("@readStr", MType([],StringType()),False),   
        Symbol("@writeStr", MType([StringType()],StringType()),False)

    ]

    
    def __init__(self, ast):
        self.class_envi = []
        self.ast = ast
        self.global_env = {}
        self.scope = 0
        self.illegal_array_lit = False

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        #decl : List[ClassDecl]
        c = self.global_env
        flag = False

        classenv = self.class_envi
        for x in ast.decl:
            classenv += [x.classname.name]

        for x in ast.decl:
                # classname : Id
                # memlist : List[MemDecl]
                # parentname : Id = None # None if there is no parent
            if x.classname.name == "Program":
                for y in x.memlist:
                    if type(y) is MethodDecl:
                        # name: Id
                        # param: List[VarDecl]
                        # returnType: Type  # VoidType for constructor
                        # body: Block
                        if y.name.name == "@main" and len(y.param) == 0:
                            flag = True
            self.visit(x, c)
        if flag == False:
            raise NoEntryPoint()
        return []

    def visitClassDecl(self,ast: ClassDecl, c):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent

        class_name = ast.classname.name
        if c.get(class_name) is not None:
            raise Redeclared(Class(),class_name)
        if ast.parentname is not None:
            parent_name = ast.parentname.name
            if c.get(parent_name) is None:
                raise Undeclared(Class(),parent_name)

        c[class_name] = {}
        for x in ast.memlist:
            self.visit(x, (c[class_name], c))
        if c[class_name].get("constructor") is None:
            c[class_name]["constructor"] = ["instance","method", VoidType(), []] ##
    

    def visitAttributeDecl(self,ast:AttributeDecl, c):
        #decl: StoreDecl #VarDecl or ConstDecl
        #type c: (c[class_name], c)
        (inner_envi, outer_envi) = c
        
        if type(ast.decl) is VarDecl:
            
            if (ast.decl.variable.name[0] == '@'):
                
                self.visit(ast.decl, ("static", False, [], inner_envi, outer_envi))
            else:
                self.visit(ast.decl, ("instance", False, [], inner_envi, outer_envi))
        elif type(ast.decl) is ConstDecl:
            if (ast.decl.constant.name[0] == '@'):
                self.visit(ast.decl, ("static", False, [], inner_envi, outer_envi))
            else:
                self.visit(ast.decl, ("instance", False, [], inner_envi, outer_envi))

    def visitVarDecl(self, ast: VarDecl, c):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        (kind, inBlock, symbol_stack, inner_envi, outer_envi) = c
        #kind = 'instance' && inner_env = inner_dict (c[class_name] = {})
        var_name = ast.variable.name
        if inBlock == False:
            if inner_envi.get(var_name) is not None and type(inner_envi[var_name]) is tuple:
                raise Redeclared(Attribute(),var_name)
        var_type = self.visit(ast.varType, outer_envi)
        
        
        

        if ast.varInit is not None:
            value = self.visit(ast.varInit, (symbol_stack, inner_envi, outer_envi, False))
            # print (value)
            # print(type(value[2]))
            # print(type(var_type))
            # if type(value[2]) is type(var_type):
            #     print("ok")
            if self.illegal_array_lit:
                raise IllegalArrayLiteral(ast.varInit)
            #check if value is variable -> var qa : int = self.b
            if value[0] in ["instance", "static"]:
                
                if ExpUtils.isNotAccess(ast.varInit):
                    raise Undeclared(Identifier(), ast.varInit.name)
                
            if type(var_type) is ClassType:
                if type(value[2]) is ClassType:
                    
                    if var_type.classname.name != value[2].classname.name:
                        raise TypeMismatchInStatement(ast)
                elif type(value[2]) not in [NullLiteral, NewExpr]:
                    
                    raise TypeMismatchInStatement(ast)
                
            elif type(var_type) is ArrayType and type(value[2]) is ArrayType:
                if var_type.size != value[2].size:
                    raise TypeMismatchInStatement(ast)
                var_element_type = var_type.eleType             
                value_element_type = value[2].eleType

                if not(type(var_element_type) is type(value_element_type)):
                    if not (type(var_element_type) is FloatType and type(value_element_type) is IntType):
                        raise TypeMismatchInStatement(ast)
                
            elif not(type(value[2]) is type(var_type)):
                

                if not(type(var_type) is FloatType and type(value[2]) is IntType):
                    
                    raise TypeMismatchInStatement(ast)
                


        if inBlock == False:
            inner_envi[var_name] = (kind, "mutable", var_type) 

    def visitConstDecl(self,ast: ConstDecl, c):  
        # constant : Id
        # constType : Type
        # value : Expr
        (kind, inBlock, symbol_stack, inner_envi, outer_envi) = c
        const_name = ast.constant.name
        if inBlock == False:
            if inner_envi.get(const_name) is not None and type(inner_envi[const_name]) is tuple:
                raise Redeclared(Attribute(),const_name)

        const_type = self.visit(ast.constType, outer_envi)
        if ast.value is None:
            if not(type(const_type) is ClassType):
                raise TypeMismatchInDeclaration(ast)
            #     ###
            

        else:
            value = self.visit(ast.value, (symbol_stack, inner_envi, outer_envi, True))
            if self.illegal_array_lit:
                raise IllegalArrayLiteral(ast.value)
            if value[0] in ["instance", "static"]:
                if ExpUtils.isNotAccess(ast.value):
                    raise Undeclared(Identifier(), ast.value.name)
            # if value[1] == "mutable":
            #     raise TypeMismatchInDeclaration(ast)
            #     ###

            if type(const_type) is ClassType:
                if type(value[2]) is ClassType:
                    if const_type.classname.name != value[2].classname.name:
                        raise TypeMismatchInDeclaration(ast)
                    ####
                elif type(value[2]) not in [NullLiteral, NewExpr]:
                    raise TypeMismatchInDeclaration(ast)
                
            elif type(const_type) is ArrayType and type(value[2]) is ArrayType:
                if const_type.size != value[2].size:
                    raise TypeMismatchInDeclaration(ast)
                const_element_type = const_type.eleType             
                value_element_type = value[2].eleType

                if not(type(const_element_type) is type(value_element_type)):
                    if not (type(const_element_type) is FloatType and type(value_element_type) is IntType):
                        raise TypeMismatchInDeclaration(ast)
                    
            elif not(type(value[2]) is type(const_type)):
                if not (type(const_type) is FloatType and type(value[2]) is IntType):
                    raise TypeMismatchInDeclaration(ast)
                ####
                
        if inBlock == False:
            inner_envi[const_name] = (kind, "immutable", const_type)

    def visitMethodDecl(self, ast: MethodDecl, c):
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # VoidType for constructor
        # body: Block

        (inner_envi, outer_envi) = c

        if (ast.name.name[0] == "@"):
            kind = "static"
        else:
            kind = "instance"

        method_name = ast.name.name 
        

        if inner_envi.get(method_name) is not None and (method_name != "constructor"):
            raise Redeclared(Method(),method_name)

        # if (ast.name.name in inner_envi):
        #     raise Redeclared(Method(),ast.name.name)

        symbol_stack = [] # struct [(name, 'immmutable', 'rettype')]
        scope_stack = [] #keep the scope
        paramTypeList = []
        for x in ast.param:
            var_name = x.variable.name
            var_type = x.varType
            for y in symbol_stack:
                if y[0] == var_name:
                    raise Redeclared(Parameter(),var_name)
            symbol_stack += [(var_name, "mutable", var_type)]
            paramTypeList += [var_type]

        inner_envi[method_name] = [kind, "method", None,  paramTypeList]
        self.visit(ast.body, (symbol_stack, scope_stack, False, inner_envi, outer_envi, False))

        if inner_envi[method_name][2] is None:
            inner_envi[method_name][2] = VoidType()

    def visitBlock(self, ast: Block, c):
        #stmt:List[Stmt]

        

        (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        
        scope_stack.append(self.scope)
        
        
        for x in ast.stmt:
            #vardecl
            if type(x) is VarDecl:
                var_name = x.variable.name
                var_type = self.visit(x.varType, outer_envi)
                
                for y in symbol_stack[scope_stack[-1]:]:
                    if y[0] == var_name:
                        raise Redeclared(Variable(),var_name)

                self.visit(x, ("instance", True, symbol_stack, inner_envi, outer_envi))
                symbol_stack += [(var_name, "mutable", var_type)]
                
            #constdecl
            elif type(x) is ConstDecl:
                const_name = x.constant.name
                const_type = self.visit(x.constType, outer_envi)
                for y in symbol_stack[scope_stack[-1]:]:
                    if y[0] == const_name:
                        raise Redeclared(Constant(),const_name)

                self.visit(x, ("instance", True, symbol_stack, inner_envi, outer_envi))
                symbol_stack += [(const_name, "immutable", const_type)]

            else:
                if type(x) is Block or type(x) is For or type(x) is If:
                    
                    self.scope += len(symbol_stack)
                    self.visit(x, (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag))

                elif type(x) is Return:
                    # current_class = list(outer_envi)[-1]
                    #current_method = list(outer_envi[current_class])[-1]
                    self.visit(x, (symbol_stack, inLoop, inner_envi, outer_envi, False))
                
                else:
                    self.visit(x, (symbol_stack, inLoop, inner_envi, outer_envi, False))


        symbol_stack = symbol_stack[:scope_stack[-1]]
        scope_stack.pop()

    def visitId(self, ast: Id, c):
        # name : str
        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        for x in symbol_stack[::-1]:
            if x[0] == ast.name:
                return x # (name, mutable, rettype)
        if inner_envi.get(ast.name) is not None:
            return inner_envi[ast.name]
        
        if outer_envi.get(ast.name) is not None:
            return ast.name
        
        raise Undeclared(Identifier(),ast.name) 
    
    def visitAssign(self, ast, c):
        # lhs:Expr
        # exp:Expr
        
        (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        lhs = self.visit(ast.lhs, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        expr = self.visit(ast.exp, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        

        if lhs[0] in ["instance", "static"]:
            if ExpUtils.isNotAccess(ast.lhs):
                raise Undeclared(Identifier(), ast.lhs.name)
            if lhs[1] == "immutable":
                raise CannotAssignToConstant(ast)
        else:
            if lhs[1] == "immutable":
                raise CannotAssignToConstant(ast)
            
        if expr[0] in ["instance", "static"]:
            if ExpUtils.isNotAccess(ast.exp):
                raise Undeclared(Identifier(), ast.exp.name)
            
        lhs_typ = lhs[2]
        expr_typ = expr[2]
        
        if type(lhs_typ) is VoidType:
            raise TypeMismatchInStatement(ast)
        
        if type(lhs_typ) is ArrayType and type(expr_typ) is ArrayType:
            if lhs_typ.size != expr_typ.size:
                raise TypeMismatchInStatement(ast)
            lhs_element_type = lhs_typ.eleType             
            expr_element_type = expr_typ.eleType

            if not(type(lhs_element_type) is type(expr_element_type)):
                if not (type(lhs_element_type) is FloatType and type(expr_element_type) is IntType):
                    raise TypeMismatchInStatement(ast)
                
        if type(lhs_typ) is ClassType and type(expr_typ) is ClassType:
            if lhs_typ.classname.name != expr_typ.classname.name:
                raise TypeMismatchInStatement(ast)
            
        elif not(type(lhs_typ) is type(expr_typ)):

            if type(lhs_typ) is ArrayType:
                lhs_element_type = lhs_typ.eleType
                if not(type(lhs_element_type) is type(expr_typ)):
                    if not(type(lhs_element_type) is FloatType and type(expr_typ) is IntType):
                        raise TypeMismatchInStatement(ast)
                    
            elif not (type(lhs_typ) is FloatType and type(expr_typ) is IntType):
                raise TypeMismatchInStatement(ast)
            

    def visitIf(self, ast: If, c):
        # expr:Expr
        # thenStmt:Block
        # preStmt:Block = None # None if there is no pre-statement
        # elseStmt:Block = None # None if there is no else branch
        
        (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        if ast.preStmt is not None:
            self.visit(ast.preStmt, (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag))
        expr = self.visit(ast.expr, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        if expr[0] in ["instance", "static"]:
            if ExpUtils.isNotAccess(ast.expr):
                raise Undeclared(Identifier(), ast.expr.name)
        if type(expr[2]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag))
        

        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag))


    def visitFor(self, ast: For, c):
        # initStmt:Assign
        # expr:Expr
        # postStmt:Assign
        # loop:Block
        
        (symbol_stack, scope_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        self.visit(ast.initStmt, (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag))
        expr_ = self.visit(ast.expr, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        if type(expr_[2]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.postStmt, (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag))
         

        self.visit(ast.loop, (symbol_stack, scope_stack, True, inner_envi, outer_envi, const_decl_flag))

    def visitBreak(self, ast, c):
        # no child
        (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        if not inLoop:
            raise MustInLoop(ast)
        
    def visitContinue(self, ast, c):
        # no child
        (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        if not inLoop:
            raise MustInLoop(ast)
        
    
    def visitReturn(self, ast, c):
        # expr: Expr = None

        (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        current_class = list(outer_envi)[-1]
        current_method = list(outer_envi[current_class])[-1]
        if current_method == "constructor":
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
            
        if ast.expr is not None:
            return_typ = self.visit(ast.expr, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
            if return_typ[0] in ["instance", "static"]:
                if ExpUtils.isNotAccess(ast.expr):
                    raise Undeclared(Identifier(), ast.expr.name)
                
        method_rettyp = outer_envi[current_class][current_method][2]
        if method_rettyp is None:
            if ast.expr is None:
                outer_envi[current_class][current_method][2] = VoidType()
            else:
                outer_envi[current_class][current_method][2] = return_typ[2]
        else:
            if not(type(method_rettyp) is type(return_typ[2])):
                raise TypeMismatchInStatement(ast)
                
    def visitCallStmt(self, ast, c):
            # obj: Expr  # None if there is no obj 
            # method:Id
            # param:List[Expr]

        (symbol_stack, inLoop, inner_envi, outer_envi, const_decl_flag) = c
        isAt = False
        if ast.method.name[0] == "@":
            isAt = True

        if type(ast.obj) is SelfLiteral:
            curr_class = list(outer_envi)[-1]
            method = self.getInforAcc(ast.method, (Method(), curr_class, outer_envi))
            # if method[0] == "static":
            #     raise IllegalMemberAccess(ast)
    
        else:
            if isAt:
                if outer_envi.get(ast.obj.name) is not None:
                    class_name = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
                
            else:
                class_name = self.visit(ast.obj, (symbol_stack, inner_envi, outer_envi, const_decl_flag))

            # x.b()
            if type(class_name) is tuple:
                if not(type(class_name[2]) is ClassType):
                    raise TypeMismatchInExpression(ast)
                method = self.getInforAcc(ast.method, (Method(), class_name[2].classname.name, outer_envi))
                # if method[0] == "static":
                #     raise IllegalMemberAccess(ast)
                
            # A.b()
            if type(class_name) is str:
                method = self.getInforAcc(ast.method, (Method(), class_name, outer_envi))
                if method[0] == "instance":
                    raise IllegalMemberAccess(ast)
            
            if method[1] != "method":
                raise TypeMismatchInExpression(ast)
            

        if not(type(method[2]) is VoidType):
            raise TypeMismatchInStatement(ast)
        
        args = list(map(lambda x: self.visit(x, (symbol_stack, inner_envi, outer_envi, const_decl_flag)), ast.param))
        if len(args) != len(method[3]):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(args)): 
            args_typ = args[i][2]
            param_typ = method[3][i]
            if not(type(args_typ) is type(param_typ)):
                if not (type(param_typ) is FloatType and type(args_typ) is IntType):
                    raise TypeMismatchInStatement(ast)
                
    def visitBinaryOp(self, ast: BinaryOp, c):
        # op:str
        # left:Expr
        # right:Expr

        ####
        if ExpUtils.isNotConstOperand(ast.left) or ExpUtils.isNotConstOperand(ast.right):
            raise TypeMismatchInDeclaration(ast)
        
        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        lhs = self.visit(ast.left, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        rhs = self.visit(ast.right, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        if lhs[0] in ["instance", "static"]:
            if ExpUtils.isNotAccess(ast.left):
                raise Undeclared(Identifier(), ast.left.name)
            
        if rhs[0] in ["instance", "static"]:
            if ExpUtils.isNotAccess(ast.right):
                raise Undeclared(Identifier(), ast.right.name)
            
        ###
        if const_decl_flag:
            if lhs[1] == "mutable" or rhs[1] == "mutable":
                raise TypeMismatchInDeclaration(ast)
            
        op = str(ast.op)

        #------------------Arithmetic Operator------------------
        if op in ["+", "-", "*"]:
            
            if ExpUtils.isNotIntFloatType(lhs[2]) or ExpUtils.isNotIntFloatType(rhs[2]):
                raise TypeMismatchInExpression(ast)
            elif type(lhs[2]) is FloatType or type(rhs[2]) is FloatType:
                return (None, None, FloatType())
            return (None, None, IntType())
        
        elif op in ["/"]:
            if not(type(lhs[2]) is FloatType) or not(type(rhs[2]) is FloatType):
                raise TypeMismatchInExpression(ast)
            return (None, None, FloatType())
        elif op in ["\\", "%"]:
            if not(type(lhs[2]) is IntType) or not(type(rhs[2]) is IntType):
                raise TypeMismatchInExpression(ast)
            return (None, None, IntType())
        
        #------------------Boolean Operator------------------
        elif op in ["&&", "||"]:
            if type(lhs[2]) is BoolType and type(rhs[2]) is BoolType:
                return (None, None, BoolType())
            raise TypeMismatchInExpression(ast)
        
        #------------------String Operator------------------
        elif op in ["^"]:
            if type(lhs[2]) is StringType and type(rhs[2]) is StringType:
                return (None, None, StringType())
            raise TypeMismatchInExpression(ast)
        
        #------------------Relational Operator------------------
        elif op in ["==", "!="]:
            if ExpUtils.isNotIntBoolType(lhs[2]) or ExpUtils.isNotIntBoolType(rhs[2]):
                raise TypeMismatchInExpression(ast)
            return (None, None, BoolType())
        elif op in ["<", "<=", ">", ">="]:
            if ExpUtils.isNotIntFloatType(lhs[2]) or ExpUtils.isNotIntFloatType(rhs[2]):
                raise TypeMismatchInExpression(ast)
            return (None, None, BoolType())
        
    def visitUnaryOp(self, ast: UnaryOp, c):
        # op:str
        # body:Expr

        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        expr = self.visit(ast.body, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        op = str(ast.op)
        if (op == "-" and ExpUtils.isNotIntFloatType(expr[2])) or (op == "!" and type(expr[2]) is not BoolType):
            raise TypeMismatchInExpression(ast)
        return (None, None, expr[2])
    
    def visitCallExpr(self, ast, c):
        # obj: Expr # None if there is no obj
        # method:Id
        # param:List[Expr]
        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        isAt = False
        if ast.method.name[0] == "@":
            isAt = True
        if type(ast.obj) is SelfLiteral:
            curr_class = list(outer_envi)[-1]
            method = self.getInforAcc(ast.method, (Method(), curr_class, outer_envi))
            # if method[0] == "static":
            #     raise IllegalMemberAccess(ast)
            
        else:
            if isAt:
                if outer_envi.get(ast.obj.name) is not None:
                    class_name = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
                
            else:
                class_name = self.visit(ast.obj, (symbol_stack, inner_envi, outer_envi, const_decl_flag))

            # x.b()
            if type(class_name) is tuple:
                if not(type(class_name[2]) is ClassType):
                    raise TypeMismatchInExpression(ast)
                method = self.getInforAcc(ast.method, (Method(), class_name[2].classname.name, outer_envi))
                # if method[0] == "static":
                #     raise IllegalMemberAccess(ast)
                if method[1] != "method":
                    raise TypeMismatchInExpression(ast)
                
            # A.b()
            if type(class_name) is str:
                method = self.getInforAcc(ast.method, (Method(), class_name, outer_envi))
                # if method[0] == "instance":
                #     raise IllegalMemberAccess(ast)
                if method[1] != "method":
                    raise TypeMismatchInExpression(ast)
                
        args = list(map(lambda x: self.visit(x, (symbol_stack, inner_envi, outer_envi, const_decl_flag)), ast.param))
        if len(args) != len(method[3]):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(args)):
            args_typ = args[i][2]
            param_typ = method[3][i]
            if not(type(args_typ) is type(param_typ)):
                if not (type(param_typ) is FloatType and type(args_typ) is IntType):
                    raise TypeMismatchInExpression(ast)
                
        return (None, None, method[2])
    
    def getInforAcc(self, ast, c):

        kind, class_name, envi = c
        # if class E really has b()
        if type(kind) is Method:
            if envi[class_name].get(ast.name) is not None:
                return envi[class_name][ast.name]
            
        else:
            if envi[class_name].get(ast.name) is not None:
                return envi[class_name][ast.name]

        
        if type(kind) is Method:
            
            raise Undeclared(kind, ast.name)
        raise Undeclared(kind, ast.name)
    
    def visitNewExpr(self, ast, c): 
        # classname:Id
        # param:List[Expr]

        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        class_name = ast.classname.name
        if outer_envi.get(class_name) is None:
            raise Undeclared(Class(), class_name)
        
        if outer_envi[class_name]["constructor"][1] == "method" and outer_envi[class_name]["constructor"][0] == "instance":
            constructor = outer_envi[class_name]["constructor"]

        args = list(map(lambda x: self.visit(x, (symbol_stack, inner_envi, outer_envi, const_decl_flag)), ast.param))
        
        if len(args) != len(constructor[3]):
            raise TypeMismatchInExpression(ast)
        if len(ast.param) != 0:
            for i in range(len(args)):
                args_typ = args[i][2]
                param_typ = constructor[3][i]
                if not(type(args_typ) is type(param_typ)):
                    if not (type(param_typ) is FloatType and type(args_typ) is IntType):
                        raise TypeMismatchInExpression(ast)
                    
        return (None, None, ClassType(ast.classname))
    
    def visitArrayCell(self, ast, c):
        # arr:Expr
        # idx:Expr
        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        arrtyp = self.visit(ast.arr, (symbol_stack, inner_envi, outer_envi, const_decl_flag))

        clone = arrtyp[2]
        clone = clone.eleType
        
        
        idxtyp = self.visit(ast.idx, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
        
        if not(type(idxtyp[2]) is IntType) or not(type(arrtyp[2]) is ArrayType):
            raise TypeMismatchInExpression(ast)
        
        return (None, arrtyp[1], clone)
    
    def visitFieldAccess(self, ast, c):
        # obj:Expr # None if there is no obj
        # fieldname:Id
        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        isAt = False
        if ast.fieldname.name[0] == "@":
            isAt = True
        if type(ast.obj) is SelfLiteral:
            curr_class = list(outer_envi)[-1]
            field = self.getInforAcc(ast.fieldname, (Attribute(), curr_class, outer_envi))
            # if field[0] == "static":
            #     raise IllegalMemberAccess(ast)
            
        else:
            if isAt:
                if outer_envi.get(ast.obj.name) is not None:
                    class_name = ast.obj.name
                else:
                    raise Undeclared(Class(), ast.obj.name)
                
            else:
                class_name = self.visit(ast.obj, (symbol_stack, inner_envi, outer_envi, const_decl_flag))
                

            # x.b
            if type(class_name) is tuple:
                if not(type(class_name[2]) is ClassType):
                    raise TypeMismatchInExpression(ast)
                field = self.getInforAcc(ast.fieldname, (Attribute(), class_name[2].classname.name, outer_envi))
                # if field[0] == "static":
                #     raise IllegalMemberAccess(ast)
                
                
            # A.b()
            if type(class_name) is str:
                field = self.getInforAcc(ast.fieldname, (Attribute(), class_name, outer_envi))
                # if field[0] == "instance":
                #     raise IllegalMemberAccess(ast)
                
            if field[1] == "method":
                raise TypeMismatchInExpression(ast)
            
        return field
    
    def visitIntLiteral(self, ast: IntLiteral, c):
        # value:int
        return (None, None, IntType())
    
    def visitFloatLiteral(self, ast, c):
        # value:float
        return (None, None, FloatType())
    
    def visitBooleanLiteral(self, ast, c):
        # value:boolean
        return (None, None, BoolType())
    
    def visitStringLiteral(self, ast, c):
        # value:str
        return (None, None, StringType())
    
    def visitNullLiteral(self, ast, c):
        # no child
        return (None, None, NullLiteral())
    
    def visitSelfLiteral(self, ast, c):
        # no child
        return (None, None, SelfLiteral())
    
    def visitArrayLiteral(self, ast, c):
        # value: List[Literal]
        (symbol_stack, inner_envi, outer_envi, const_decl_flag) = c
        valueList = list(map(lambda x: self.visit(x, (symbol_stack, inner_envi, outer_envi, const_decl_flag)), ast.value))

        if type(valueList[0][2]) is ArrayType:
            typList = []
            for i in valueList:
                typList.append(i[2])
            first_ele = typList[0]
            for i in typList:
                if i.size != first_ele.size:
                    raise TypeMismatchInStatement(ast)
                if not(type(i.eleType) is type(first_ele.eleType)) or self.illegal_array_lit:
                    raise IllegalArrayLiteral(ast)
            return (None, None, ArrayType(len(valueList), first_ele))
        
        first_ele_typ = valueList[0][2]
        for ele in valueList:
            if not(type(ele[2]) is type(first_ele_typ)):
                self.illegal_array_lit = True
        return (None, None, ArrayType(len(valueList), first_ele_typ))
                    



        

    def visitIntType(self,ast, c):
        return IntType()
    
    def visitFloatType(self,ast, c):
        return FloatType()
    
    def visitBoolType(self,ast, c):
        return BoolType()
    
    def visitStringType(self,ast, c):
        return StringType()

    def visitArrayType(self,ast, c):
        return ast
    
    def visitClassType(self,ast, c):

        # classname:Id
        if ast.classname.name in self.class_envi:
            return ast
        raise Undeclared(Class(), ast.classname.name)
    









#class Member:
#     def __init__(self,n,t,isMu=False):
#         self.name = n
#         self.typ = t
#         self.isMu = isMu
#     def __str__(self):
#         return "Member("+self.name+","+str(self.typ)+","+str(self.kind)+","+str(self.isMu)+")"

# class BKClass:
#     def __init__(self,n,p,m):
#         self.name = n
#         self.parent = p
#         self.member = m
#     def __str__(self):
#         return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"


# class StaticChecker(BaseVisitor,Utils):
#     inttype = IntType()
#     floattype = FloatType()
#     voidtype = VoidType()
#     booltype = BoolType()
#     stringtype = StringType() 
#     def __init__(self,ast):
#         self.ast = ast
#         self.io = [BKClass("io",None,[
#                             Member("@readInt",MType([],StaticChecker.inttype),False),
#                             Member("@writeIntLn",MType([StaticChecker.inttype],StaticChecker.voidtype),False),
#                             ])]
#     def check(self):
#         self.visit(self.ast,self.io)
#         return "successful"

#     def visitProgram(self,ast, c):
#         env = reduce(lambda a,e: self.visit(e,a), ast.decl,c)
        
#     def visitClassDecl(self, ast, c):
#         if ast.classname.name in map(lambda x: x.name,c):
#             raise Redeclared(Class(),ast.classname.name)
#         mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
#         return [BKClass(ast.classname.name,ast.parentname,mem)]+c

#     def visitAttributeDecl(self,ast,c):
#         field = self.visit(ast.decl,c) 
#         return [field]+c

#     def visitVarDecl(self, ast, c):
#         if ast.variable.name in map(lambda x: x.name,c):
#             raise Redeclared(Attribute(),ast.variable.name)
#         return Member(ast.variable.name,ast.varType,True)
