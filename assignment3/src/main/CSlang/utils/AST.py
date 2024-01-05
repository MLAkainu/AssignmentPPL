from abc import ABC, abstractmethod, ABCMeta
#from Visitor import Visitor
from dataclasses import dataclass
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self,param)

class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class MemDecl(AST):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Id(LHS):
    name:str
    def __str__(self):
        return "Id(" + self.name + ")"
        

# used for binary expression
@dataclass
class BinaryOp(Expr):
    op:str
    left:Expr
    right:Expr
    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

#used for unary expression with orerand like !,+,-
@dataclass
class UnaryOp(Expr):
    op:str
    body:Expr
    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

@dataclass
class CallExpr(Expr):
    obj: Expr # None if there is no obj
    method:Id
    param:List[Expr]
    def __str__(self):
        return "CallExpr(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class NewExpr(Expr):
    classname:Id
    param:List[Expr]
    def __str__(self):
        return "NewExpr(" + str(self.classname) + ",[" +  ','.join(str(i) for i in self.param) + "])"

@dataclass
class ArrayCell(LHS):
    arr:Expr
    idx:Expr
    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

@dataclass
class FieldAccess(LHS):
    obj:Expr # None if there is no obj
    fieldname:Id
    def __str__(self):
        return "FieldAccess(" + ((str(self.obj) + ",") if self.obj else "") + str(self.fieldname) + ")"

class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class IntLiteral(Literal):
    value:int
    def __str__(self):
        return "IntLit(" + str(self.value) + ")"

@dataclass
class FloatLiteral(Literal):
    value:float
    def __str__(self):
        return "FloatLit(" + str(self.value) + ")"

@dataclass
class StringLiteral(Literal):
    value:str
    def __str__(self):
        return "StringLit(" + self.value + ")"

@dataclass
class BooleanLiteral(Literal):
    value:bool
    def __str__(self):
        return "BooleanLit(" + str(self.value) + ")"

class NullLiteral(Literal):
    def __str__(self):
        return "NullLiteral()"

class SelfLiteral(Literal):
    def __str__(self):
        return "Self()"
@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]
    def __str__(self):
        return '[' + ','.join(str(i) for i in self.value)+ ']'
class Decl(AST):
    __metaclass__ = ABCMeta
    pass
class StoreDecl(Stmt):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Block(Stmt):
    stmt:List[Stmt] # empty list if there is no statement in block
    def __str__(self):
        return "Block([" + ','.join(str(i) for i in self.stmt) + "])"

@dataclass
class Assign(Stmt):
    lhs:Expr
    exp:Expr
    def __str__(self):
        return "AssignStmt(" + str(self.lhs) + "," +  str(self.exp) + ")"

@dataclass
class If(Stmt):
    expr:Expr
    thenStmt:Block
    preStmt:Block = None # None if there is no pre-statement
    elseStmt:Block = None # None if there is no else branch
    def __str__(self):
        return "If(" + ((str(self.preStmt) + ",") if self.preStmt else "") + str(self.expr) + "," + str(self.thenStmt) + (("," +  str(self.elseStmt)) if self.elseStmt else "")  + ")"

@dataclass
class For(Stmt):
    initStmt:Assign
    expr:Expr
    postStmt:Assign
    loop:Block  
    def __str__(self):
        return "For(" + str(self.initStmt) + "," + str(self.expr) + "," + str(self.postStmt) + ',' + str(self.loop)  + "])"

class Break(Stmt):
    def __str__(self):
        return "Break"

class Continue(Stmt):
    def __str__(self):
        return "Continue"

@dataclass
class Return(Stmt):
    expr:Expr = None # None if there is no expression after return
    def __str__(self):
        return "Return(" + (str(self.expr)  if  self.expr else "") + ")"

@dataclass
class CallStmt(Stmt):
    obj: Expr  # None if there is no obj 
    method:Id
    param:List[Expr]
    def __str__(self):
        return "Call(" + ((str(self.obj) + ",") if self.obj else "") + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

# used for local variable or parameter declaration 
@dataclass
class VarDecl(StoreDecl):
    variable : Id
    varType : Type
    varInit : Expr = None # None if there is no initial
    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + (","+ str(self.varInit) if self.varInit else "") + ")"
    def toParam(self):
        return "Param(" + str(self.variable) + "," + str(self.varType) + ")"


# used for local constant declaration
@dataclass
class ConstDecl(StoreDecl):
    constant : Id
    constType : Type
    value : Expr
    def __str__(self):
        return "ConstDecl(" + str(self.constant) + "," + str(self.constType) + "," + str(self.value) + ")"

 
#used for a class declaration
@dataclass
class ClassDecl(Decl):
    classname : Id
    memlist : List[MemDecl]
    parentname : Id = None # None if there is no parent
    def __str__(self):
        return "ClassDecl(" + str(self.classname) + (("," + str(self.parentname)) if self.parentname else "") + ",[" + ','.join(str(i) for i in self.memlist) + "])"



# used for a normal or special method declaration. 
# In the case of special method declaration, the return type is VoidType()
@dataclass
class MethodDecl(MemDecl):
    name: Id
    param: List[VarDecl]
    returnType: Type  # VoidType for constructor
    body: Block
    def __str__(self):
        return "MethodDecl(" + str(self.name) +  ",[" +  ','.join(i.toParam() for i in self.param) + "]," + ((str(self.returnType) ) if self.returnType else str(VoidType())) + "," + str(self.body) + ")"

@dataclass
class AttributeDecl(MemDecl):
    decl: StoreDecl #VarDecl or ConstDecl
    def __str__(self):
        return "AttributeDecl(" +  str(self.decl) + ")"


class IntType(Type):
    def __str__(self):
        return "IntType"

class FloatType(Type):
    def __str__(self):
        return "FloatType"

class BoolType(Type):
    def __str__(self):
        return "BoolType"

class StringType(Type):
    def __str__(self):
        return "StringType"

@dataclass
class ArrayType(Type):
    size : int
    eleType:Type
    def __str__(self):
        return "ArrayType(" + str(self.size) +  "," + str(self.eleType) + ")"

@dataclass
class ClassType(Type):
    classname:Id
    def __str__(self):
        return "ClassType(" + str(self.classname)  + ")"


class VoidType(Type):
    def __str__(self):
        return "VoidType"


# used for whole program
@dataclass
class Program(AST):
    decl : List[ClassDecl]
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
