#update: 6/04/2019
from abc import ABC
from dataclasses import dataclass
from AST import *

class Kind(ABC):
    pass

class Class(Kind):
    def __str__(self):
        return "Class"

class Method(Kind):
    def __str__(self):
        return "Method"

class Attribute(Kind):
    def __str__(self):
        return "Attribute"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Constant(Kind):
    def __str__(self):
        return "Constant"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass
@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str # name of identifier
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n
@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier

    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n
@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)
@dataclass
class TypeMismatchInStatement(StaticError):
    stmt:Stmt

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)
@dataclass
class CannotAssignToConstant(StaticError):
    stmt:Stmt
    def __str__(self):
        return "Cannot Assign To Constant: "+ str(self.stmt)
@dataclass
class TypeMismatchInDeclaration(StaticError):
    decl:StoreDecl
    def __str__(self):
        return "Type Mismatch In Declaration: "+ str(self.decl)
@dataclass
class MustInLoop(StaticError):
    stmt:Stmt
    def __str__(self):
        return str(self.stmt) + " Not In Loop"
@dataclass
class IllegalMemberAccess(StaticError):
    expr:Expr
    def __str__(self):
        return "Illegal Member Access: "+ str(self.expr)

@dataclass
class IllegalArrayLiteral(StaticError):
    arr:ArrayLiteral
    def __str__(self):
        return "Illegal Array Literal: "+ str(self.arr)

@dataclass
class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"

