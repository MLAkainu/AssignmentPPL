from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):
    #program: class_declarelist EOF ;
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program(self.visit(ctx.class_declarelist()))

    #class_declarelist: class_declare class_declarelist | class_declare;
    def visitClass_declarelist(self,ctx:CSlangParser.Class_declarelistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.class_declare())]
        return [self.visit(ctx.class_declare())] + self.visit(ctx.class_declarelist())

    #class_declare: CLASS name_class name_superclass LB body_class_list RB;
    def visitClass_declare(self,ctx:CSlangParser.Class_declareContext):
        name = self.visit(ctx.name_class())
        memList = self.visit(ctx.body_class_list())
        parentname = self.visit(ctx.name_superclass())
        return ClassDecl(name, memList, parentname)
    

    #name_class: ID;
    def visitName_class(self,ctx:CSlangParser.Name_classContext):
        return Id(ctx.ID().getText())

    #name_superclass: ID | ;
    def visitName_superclass(self,ctx:CSlangParser.Name_superclassContext):
        if ctx.getChildCount() == 0:
            return None
        return Id(ctx.ID().getText())
    #body_class_list: body_class_prime | ;
    def visitBody_class_list(self,ctx:CSlangParser.Body_class_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.body_class_prime())
    #body_class_prime: body_class body_class_prime | body_class;
    def visitBody_class_prime(self,ctx:CSlangParser.Body_class_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.body_class())
        return self.visit(ctx.body_class()) + self.visit(ctx.body_class_prime())
    #body_class: attribute_declare| method_declare| constructor_declare;
    def visitBody_class(self,ctx:CSlangParser.Body_classContext):
        if ctx.attribute_declare():
            return self.visit(ctx.attribute_declare())
        elif ctx.method_declare():
            return self.visit(ctx.method_declare())
        return self.visit(ctx.constructor_declare())
    #attribute_declare: attdecl_ | attdecl ;
    # def visitAttribute_declare(self,ctx:CSlangParser.Attribute_declareContext):
    #     if ctx.attdecl():
    #         return self.visit(ctx.attdecl())
    #     return self.visit(ctx.attdecl_())
    #attdecl_: Attribute_name indenlist COLON type_att SEMI;
    def visitAttdecl_(self,ctx:CSlangParser.Attdecl_Context):
        idlist = self.visit(ctx.indenlist())
        typ = self.visit(ctx.type_att())
        ans = []
        # check ClassType
        if isinstance(typ, ClassType):
            check_class = True
        else:
            check_class = False

        if ctx.Attribute_name().getText() == "const":
            for i in idlist:
                ans += [AttributeDecl(ConstDecl(i, typ, None))]
        else:
            for i in idlist:
                if check_class:
                    ans += [AttributeDecl(VarDecl(i, typ, NullLiteral()))]
                else:
                    ans += [AttributeDecl(VarDecl(i, typ))]
        return ans
                

    #indenlist: identifier_name COMMA indenlist | identifier_name;
    def visitIndenlist(self,ctx:CSlangParser.IndenlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.identifier_name())]
        return [self.visit(ctx.identifier_name())] + self.visit(ctx.indenlist())
    #attdecl: Attribute_name identifier_name varlist expr SEMI;  
    #varlist: COMMA identifier_name varlist expr COMMA
	#   COLON type_att EQ ;
    def visitAttdecl(self,ctx:CSlangParser.AttdeclContext):
        result = []
        exprlist = []
        if ctx.Attribute_name().getText() == "const":
            check_const = True
        else:
            check_const = False

        result += [self.visit(ctx.identifier_name())]
        exprlist += [self.visit(ctx.expr())]

        ctx = ctx.varlist()
        while ctx.type_att() is None:
            result += [self.visit(ctx.identifier_name())]
            exprlist += [self.visit(ctx.expr())]
            ctx = ctx.varlist()
        
        typ = self.visit(ctx.type_att())
        exprlist = exprlist[::-1]
        if check_const:
            return list(map(lambda x, y: AttributeDecl(ConstDecl(x, typ, y)), result, exprlist))
        else:
            return list(map(lambda x, y: AttributeDecl(VarDecl(x, typ, y)), result, exprlist))
            
                
        
        # vartype = self.visit(ctx.type_att())
        # exprlist = exprlist[::-1]
        # if check_const:
        #     for id, x in enumerate(idlist):
        #         ans += [AttributeDecl(ConstDecl(x, vartype, exprlist[id]))]
        # else:
        #     for id, x in enumerate(idlist):
        #         ans += [AttributeDecl(VarDecl(x, vartype, exprlist[id]))]
        # return ans

    #type_att: primitive_type | array_type | class_type;
    def visitType_att(self,ctx:CSlangParser.Type_attContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            return self.visit(ctx.class_type())

    #primitive_type: INT | FLOAT | BOOL | STRING ;
    def visitPrimitive_type(self,ctx:CSlangParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()
    #primitive_type_ : INT | FLOAT | BOOL | STRING | VOID;
    def visitPrimitive_type_(self,ctx:CSlangParser.Primitive_type_Context):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        return VoidType()
    #array_type: LSB INTARR RSB element_type;
    def visitArray_type(self,ctx:CSlangParser.Array_typeContext):
        array_size = int(ctx.INTARR().getText())
        element_type = self.visit(ctx.element_type())
        return ArrayType(array_size, element_type)
    #element_type: primitive_type | class_type;
    def visitElement_type(self,ctx:CSlangParser.Element_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        return self.visit(ctx.class_type())
    #class_type: ID;
    def visitClass_type(self,ctx:CSlangParser.Class_typeContext):
        return ClassType(Id(ctx.ID().getText()))
    #method_declare: FUNC identifier_name LP paramlist RP COLON type_return blockstmt;
    def visitMethod_declare(self,ctx:CSlangParser.Method_declareContext):
        return [MethodDecl(self.visit(ctx.identifier_name()), self.visit(ctx.paramlist()), self.visit(ctx.type_return()), self.visit(ctx.blockstmt()))]
    #paramlist: paramprime | ;
    def visitParamlist(self,ctx:CSlangParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramprime())
    #paramprime: param COMMA paramprime | param;
    def visitParamprime(self,ctx:CSlangParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        return self.visit(ctx.param()) + self.visit(ctx.paramprime())
    #param: idlist COLON type_att;
    def visitParam(self,ctx:CSlangParser.ParamContext):
        idlist = self.visit(ctx.idlist())
        type_att = self.visit(ctx.type_att())
        return list(map(lambda x: VarDecl(x, type_att), idlist))
    #idlist: ID COMMA idlist | ID;
    def visitIdlist(self,ctx:CSlangParser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())
        
    #type_return: primitive_type_ | array_type | class_type;	
    def visitType_return(self,ctx:CSlangParser.Type_returnContext):
        if ctx.primitive_type_():
            return self.visit(ctx.primitive_type_())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        return self.visit(ctx.class_type())

    #constructor_declare: FUNC CONSTRUCTOR LP paramlist RP blockstmt;
    def visitConstructor_declare(self,ctx:CSlangParser.Constructor_declareContext):
        param = self.visit(ctx.paramlist())
        body = self.visit(ctx.blockstmt())
        name = Id("constructor")
        typ = VoidType()
        return [MethodDecl(name, param, typ, body)]
    #blockstmt: LB stmtlist RB;
    def visitBlockstmt(self,ctx:CSlangParser.BlockstmtContext):
        return Block (self.visit(ctx.stmtlist()))
    #stmtlist: stmtprime | ;
    def visitStmtlist(self,ctx:CSlangParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtprime())
    #stmtprime: stmt stmtprime | stmt;
    def visitStmtprime(self,ctx:CSlangParser.StmtprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmt())
        return self.visit(ctx.stmt()) + self.visit(ctx.stmtprime())
    # stmt: var_and_const_declstmt | stmt1
    def visitStmt(self,ctx:CSlangParser.StmtContext):
        if ctx.var_and_const_declstmt():
            return self.visit(ctx.var_and_const_declstmt())
        return [self.visit(ctx.stmt1())]


	# stmt1: assignment_stmt
	# | if_stmt
	# | for_stmt
	# | break_stmt
	# | continue_stmt
	# | return_stmt
	# | method_invocation_stmt
	# | blockstmt ;
    def visitStmt1(self,ctx:CSlangParser.Stmt1Context):
        return self.visit(ctx.getChild(0))
    
    #     var_and_const_declstmt: varstmt_decl | varstmt_declass  SEMI;
    # varstmt_decl: Attribute_name variable_namelist COLON type_att ;
    # variable_namelist:  ID COMMA  variable_namelist | ID;


    # varstmt_declass: Attribute_name ID COMMA varstmt_declass COMMA expr
    # 				| ID COLON type_att EQ expr ;
    def visitVar_and_const_declstmt(self,ctx:CSlangParser.Var_and_const_declstmtContext):
        if ctx.varstmt_decl():
            return self.visit(ctx.varstmt_decl())
        return self.visit(ctx.varstmt_declass())

    #varstmt_decl: Attribute_name variable_namelist COLON type_att ;
    def visitVarstmt_decl(self,ctx:CSlangParser.Varstmt_declContext):
        idlist = self.visit(ctx.variable_namelist())
        typ = self.visit(ctx.type_att())
        ans = []
        if isinstance(typ, ClassType):
            check_class = True
        else:
            check_class = False

        if ctx.Attribute_name().getText() == "const":
            for i in idlist:
                ans += [ConstDecl(i, typ, None)]
        else:
            for i in idlist:
                if check_class:
                    ans += [VarDecl(i, typ, NullLiteral())]
                else:
                    ans += [VarDecl(i, typ)]
        return ans
    
    #variable_namelist:  ID COMMA  variable_namelist | ID;
    def visitVariable_namelist(self,ctx:CSlangParser.Variable_namelistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.variable_namelist())

    #varstmt_declass: Attribute_name ID varstmt_list expr;
    # varstmt_list: COMMA ID varstmt_list expr COMMA
    # 			| COLON type_att EQ  ;
    def visitVarstmt_declass(self,ctx:CSlangParser.Varstmt_declassContext):
        result = []
        exprlist = []
        
        if ctx.Attribute_name().getText() == "const":
            check_const = True
        else:
            check_const = False

        result += [Id(ctx.ID().getText())]
        exprlist += [self.visit(ctx.expr())]
        ctx = ctx.varstmt_list()
        while ctx.type_att() is None:
            result += [Id(ctx.ID().getText())]
            exprlist += [self.visit(ctx.expr())]
            ctx = ctx.varstmt_list()
        
        vartype = self.visit(ctx.type_att())
        exprlist = exprlist[::-1]
        if check_const:
            return list(map(lambda x, y: ConstDecl(x, vartype, y), result, exprlist))
        else:
            return list(map(lambda x, y: VarDecl(x, vartype, y), result, exprlist))
    

    #assignment_stmt:  assign_lhs ASSIGN expr SEMI;
    def visitAssignment_stmt(self,ctx:CSlangParser.Assignment_stmtContext):
        lhs = self.visit(ctx.assign_lhs())
        rhs = self.visit(ctx.expr())
        return Assign(lhs, rhs)
    # assign_lhs: ID //bien thuong
	# 		|  name_class_access STATIC_ID 		// bien static	
	# 		| expr8 DOT ID
	# 		| expr8 index_operator DOT ID
	# 		| index_exp_for_scalar_variable ;
    def visitAssign_lhs(self,ctx:CSlangParser.Assign_lhsContext):
        if ctx.name_class_access():
            obj = self.visit(ctx.name_class_access())
            method = Id(ctx.STATIC_ID().getText())
            return FieldAccess(obj, method)
        elif ctx.expr8() and ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.expr8()), Id(ctx.ID().getText()))
        elif ctx.expr8() and ctx.index_operator():
            # example: a[1].b
            indexlist = self.visit(ctx.index_operator())
            obj = self.visit(ctx.expr8())
            method = Id(ctx.ID().getText())
            return FieldAccess(ArrayCell(obj, indexlist), method)
        elif ctx.index_exp_for_scalar_variable():
            return self.visit(ctx.index_exp_for_scalar_variable())
        return Id(ctx.ID().getText())

    

    #index_exp_for_scalar_variable:  expr7 LSB expr RSB;
    def visitIndex_exp_for_scalar_variable(self,ctx:CSlangParser.Index_exp_for_scalar_variableContext):
        return ArrayCell(self.visit(ctx.expr7()), self.visit(ctx.expr()))

    #if_stmt: IF blockstmt? expr blockstmt (ELSE blockstmt)?;
    def visitIf_stmt(self,ctx:CSlangParser.If_stmtContext):
        expr = self.visit(ctx.expr())
        preStmt = None
        elseStmt = None
        thenStmt = None
        if ctx.ELSE() and ctx.getChildCount() == 6:
            preStmt = self.visit(ctx.blockstmt(0))
            thenStmt = self.visit(ctx.blockstmt(1))
            elseStmt = self.visit(ctx.blockstmt(2))
        elif ctx.ELSE() and ctx.getChildCount() == 5:
            thenStmt = self.visit(ctx.blockstmt(0))
            elseStmt = self.visit(ctx.blockstmt(1))
        elif ctx.ELSE() is None and ctx.getChildCount() == 4:
            preStmt = self.visit(ctx.blockstmt(0))
            thenStmt = self.visit(ctx.blockstmt(1))
        else:
            thenStmt = self.visit(ctx.blockstmt(0))
        return If(expr ,thenStmt, preStmt, elseStmt)
    
    #for_stmt: FOR assignstmt SEMI expr SEMI assignstmt blockstmt;
    def visitFor_stmt(self,ctx:CSlangParser.For_stmtContext):
        initStmt = self.visit(ctx.assignstmt(0))
        expr = self.visit(ctx.expr())
        postStmt = self.visit(ctx.assignstmt(1))
        loop = self.visit(ctx.blockstmt())
        return For(initStmt, expr, postStmt, loop)
    #assignstmt: assign_lhs ASSIGN expr ;
    def visitAssignstmt(self,ctx:CSlangParser.AssignstmtContext):
        assign_lhs = self.visit(ctx.assign_lhs())
        expr = self.visit(ctx.expr())
        return Assign(assign_lhs, expr)
    #break_stmt: BREAK SEMI;
    def visitBreak_stmt(self,ctx:CSlangParser.Break_stmtContext):
        return Break()
    #continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self,ctx:CSlangParser.Continue_stmtContext):
        return Continue()
    #return_stmt: RETURN expr? SEMI;
    def visitReturn_stmt(self,ctx:CSlangParser.Return_stmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return Return(expr)

    #method_invocation_stmt: method_invocation SEMI ;
    def visitMethod_invocation_stmt(self,ctx:CSlangParser.Method_invocation_stmtContext):
        return self.visit(ctx.method_invocation())
    #method_invocation: static_method_invocation
	#				| instance_method_invocation;
    def visitMethod_invocation(self,ctx:CSlangParser.Method_invocationContext):
        if ctx.static_method_invocation():
            return self.visit(ctx.static_method_invocation())
        return self.visit(ctx.instance_method_invocation())
    #static_method_invocation: name_class_access STATIC_ID LP exp_list? RP;
    def visitStatic_method_invocation(self,ctx:CSlangParser.Static_method_invocationContext):
        obj = self.visit(ctx.name_class_access())
        method = Id(ctx.STATIC_ID().getText())
        param = []
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
        return CallStmt(obj, method, param)
    #name_class_access: (SELF | ID) DOT | ;
    def visitName_class_access(self,ctx:CSlangParser.Name_class_accessContext):
        if ctx.getChildCount() == 0:
            return None
        elif ctx.SELF():
            return SelfLiteral()
        return Id(ctx.ID().getText())
    #instance_method_invocation: pre_exp DOT ID LP exp_list? RP;
    def visitInstance_method_invocation(self,ctx:CSlangParser.Instance_method_invocationContext):
        obj = self.visit(ctx.pre_exp())
        method = Id(ctx.ID().getText())
        param = []
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
        return CallStmt(obj, method, param)
    #pre_exp: pre_exp DOT ID
	# | pre_exp DOT ID LP exp_list? RP
	# |expr9 ;
    def visitPre_exp(self,ctx:CSlangParser.Pre_expContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.pre_exp()), Id(ctx.ID().getText()))
        else:
            obj = self.visit(ctx.pre_exp())
            method = Id(ctx.ID().getText())
            param = []
            if ctx.exp_list():
                param = self.visit(ctx.exp_list())
            return CallStmt(obj, method, param)
    #expr: expr1 STRING_CONCAT expr1 | expr1;
    def visitExpr(self,ctx:CSlangParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        op = ctx.STRING_CONCAT().getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)

    #expr1: expr2 (EQUAL | NOT_EQUAL | LESS_THAN_EQUAL |  GREATER_THAN_EQUAL | LESS_THAN | GREATER_THAN) expr2 | expr2;
    def visitExpr1(self,ctx:CSlangParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinaryOp(op, left, right)
    #expr2: expr2 (AND | OR ) expr3 | expr3;
    def visitExpr2(self,ctx:CSlangParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)
    #expr3: expr3 (ADD | SUB) expr4 | expr4;	
    def visitExpr3(self,ctx:CSlangParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)
    #expr4: expr4 (MUL | DIV_FLOAT | DIV_INT | MOD) expr5 | expr5;
    def visitExpr4(self,ctx:CSlangParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)
    #expr5: NOT expr5 | expr6;
    def visitExpr5(self,ctx:CSlangParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        body = self.visit(ctx.expr5())
        return UnaryOp(op, body)
    #expr6: SUB expr6 | expr7;
    def visitExpr6(self,ctx:CSlangParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        op = ctx.SUB().getText()
        body = self.visit(ctx.expr6())
        return UnaryOp(op, body)
    #expr7: expr7 index_operator | expr8;
    def visitExpr7(self,ctx:CSlangParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        indexlist = self.visit(ctx.index_operator())
        body = self.visit(ctx.expr7())
        #indexlist = indexlist[::-1]
        return ArrayCell(body, indexlist)

    #expr8: expr8  DOT (ID | funcall)
	#  | expr9;
    #funcall: ID LP exp_list? RP;
    def visitExpr8(self,ctx:CSlangParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        obj = self.visit(ctx.expr8())
        if ctx.ID():
            method = Id(ctx.ID().getText())
            return FieldAccess(obj, method)
        return self.visitFuncall(ctx.funcall(), obj)
        
        
    #expr9:  name_class_access (STATIC_ID | static_funcall)  
	#	| expr10;
    def visitExpr9(self,ctx:CSlangParser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        obj = self.visit(ctx.name_class_access())
        if ctx.STATIC_ID():
            method = Id(ctx.STATIC_ID().getText())
            return FieldAccess(obj, method)
        return self.visitStatic_funcall(ctx.static_funcall(), obj)
        
        
    #expr10: NEW ID LP exp_list? RP
	#	| operands ;
    def visitExpr10(self,ctx:CSlangParser.Expr10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        classname = Id(ctx.ID().getText())
        param = []
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
        return NewExpr(classname, param)
        
    # #funcall: ID LP exp_list? RP;
    def visitFuncall(self,ctx:CSlangParser.FuncallContext, obj:Expr):
        method = Id(ctx.ID().getText())
        param = []
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
        return CallExpr(obj, method, param)
    #static_funcall: STATIC_ID LP exp_list? RP;
    def visitStatic_funcall(self,ctx:CSlangParser.Static_funcallContext, obj:Expr):
        method = Id(ctx.STATIC_ID().getText())
        param = []
        if ctx.exp_list():
            param = self.visit(ctx.exp_list())
        return CallExpr(obj, method, param)
        
    #operands: ID | LP expr RP | literals | SELF | NULL ;
    def visitOperands(self,ctx:CSlangParser.OperandsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.SELF():
            return SelfLiteral()
        return NullLiteral()
    #literals: INTARR | INTLIT | FLOATLIT | STRINGLIT | boolean_literal | array_literal;
    def visitLiterals(self,ctx:CSlangParser.LiteralsContext):
        if ctx.INTARR():
            return IntLiteral(int(ctx.INTARR().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():    
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.boolean_literal():
            return self.visit(ctx.boolean_literal())
        return self.visit(ctx.array_literal())
    #literal_array: INTARR | INTLIT | FLOATLIT | STRINGLIT | boolean_literal ;
    def visitLiteral_array(self,ctx:CSlangParser.Literal_arrayContext):
        if ctx.INTARR():
            return IntLiteral(int(ctx.INTARR().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():    
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        return self.visit(ctx.boolean_literal())
    #boolean_literal: TRUE | FALSE;
    def visitBoolean_literal(self,ctx:CSlangParser.Boolean_literalContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        return BooleanLiteral(False)
        
    #array_literal: LSB litarray_list RSB;
    def visitArray_literal(self,ctx:CSlangParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.litarray_list()))
    #litarray_list: literal_array COMMA litarray_list | literal_array;
    def visitLitarray_list(self,ctx:CSlangParser.Litarray_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.literal_array())]
        return [self.visit(ctx.literal_array())] + self.visit(ctx.litarray_list())
    #exp_list: expr COMMA exp_list | expr;
    def visitExp_list(self,ctx:CSlangParser.Exp_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exp_list())
    #index_operator:  LSB expr RSB ;
    def visitIndex_operator(self,ctx:CSlangParser.Index_operatorContext):
        return self.visit(ctx.expr())
        

    
    #identifier_name: ID | STATIC_ID;
    def visitIdentifier_name(self,ctx:CSlangParser.Identifier_nameContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return Id(ctx.STATIC_ID().getText())
        







    
