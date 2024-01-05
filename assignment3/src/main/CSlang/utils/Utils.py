from AST import Type
from typing import List
from dataclasses import dataclass

@dataclass
class MType(Type):
    partype : List[Type]
    rettype : Type
    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

@dataclass
class Symbol:
    name:str
    cstype:Type
    mutable:bool

    def __str__(self):
        return "Symbol(" + self.name + "," + self.cstype + "," + str(self.mutable) + ")"


class Utils:
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

