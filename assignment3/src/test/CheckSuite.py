import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):

    
    
    def test_redeclared_class(self):
        input = """class a {} class b {} class a {}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    def test_redeclared_attribute(self):
        input = """class a {var a:int;var c:int;var c:int;}"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_redeclared_class_with_ast(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[])])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,402))


    def test_redeclared_attribute_with_ast2(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[])])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_attribute_with_ast(self):
        input = Program([ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,404))    

    def test_5(self):

        input =  """
            class a {
                func main() : void {}
                var c : int;
                var c : int;
            }
        
        
        """
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        input =  Program([ClassDecl(Id("a"),[MethodDecl(Id("main"),[],VoidType(),Block([])),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,406))


    def test_7(self):
        input = """
            class A{}
            class B {}
            class A{}
            class Program{
                func main() : void {}
            }
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        input = """
            class a{}
            class b{}
            class Program {
                func main() : void {}
            }
            class Program {}
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input,expect,408))


    def test_9(self):
        input = """
            class A {
                const a: int = 1;
                var @a: int = 2;
                const a: float = 3.0;
            }
            class program {
                func main() : void {}
            }
        
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        input = Program([ClassDecl(Id("Program"),[MethodDecl(Id("main"),[],VoidType(),Block([])),AttributeDecl(VarDecl(Id("c"),IntType())),MethodDecl(Id("c"),[],IntType(),Block([]))])])
        expect = "Redeclared Method: c"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        input = """
            class A {
                func main() : void {}
                func main() : void {}
            }
            class Program {
                func main() : void {}
            }
        
        """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        input = """
            class Program {
                var d : int;
                const @d : int = 1;
                const @d : float;
            
            }"""
        expect = "Redeclared Attribute: @d"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        input = """
            class Program {
                var d : int;
                const @a : float = 9.0;
                func foo() : void {
                    var a : int;
                    
                }
                var @a : int;

            }"""
        expect = "Redeclared Attribute: @a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        input = """
            class Program {
                func a() : void {}
                func a() : int {}

            }"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        input = """
            class Program {
                func @a(c: int ) : void {}
                func @a(e,f,g:float, k:int) : int {}
                func main() : void {}
            }"""
        expect = "Redeclared Method: @a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        input = """
            class A {
                func constructor() {
                    var a : int;
                }
                func main() : void {}
                func constructor() {
                    var b : int;
                }

            }


        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        input = """
            class A {
                var a: int = 1;
                func fooo(a:int) : void {
                    const a : int = 1;
                }

                func main() : void {}
                
            }


        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,417))


    def test_18(self):
        input = """
            class A {
                
                func fooo(b:int) : void {
                    var a: int = 1;
                    {
                        var a: int = 1;
                        const c: float = 10.0;
                        {
                            var c: int = 1;
                        }
                        var c: int = 1;

                    }
                }

                func main() : void {}
                
            }


        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_19(self):
        input = """
             class A {
                func foo(a: int, a, b : float) : void {}

             }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,419))


    def test_20(self):
        input = """
             class A {
                func foo(a: int, b : float) : void {}
                func foo2(a: int, b : float) : void {}

             }
             class Program {
                 func main() : void {}
             }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,420))

    
    def test_21(self):
        input = """
             class A {
                func constructor() {}
                func constructor() {}

             }
             class Program {
                 func @main() : void {}
             }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_22(self):
        input = """
            class A {}
            class C <- B {}
            class Program {
                func @main() : void {}
            }
        """

        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        input = """
            class A {}
            class A <- B {}
            class D <- Program {
                func @main() : void {}
            }
        """

        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        input = """
            class A {}
            class B {}
            class Program {
                func @main() : void {
                    var d : D;
                }
            }
        """
        expectt = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input,expectt,424))

    def test_25(self):
        input = """
            class E <- E{}
            class Program {
                func @main() : void {}
            }
        """
        expect = "Undeclared Class: E"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input = """
            class Program {
                func @main() : void {
                    var B : int;
                    var c : int = B.@a;

                }
            }
        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        input = """
            class ABC {
                var b : int = 3;
                var x : int;
            }
            class Program {
                func @main() : void {
                    ABC.d := 1;
                }
            }
        """
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        input = """
            class ABC {
                var b : int = 3;
                var x : int;
            }
            class Program {
                func @main() : void {
                    var a : ABC;
                    a.n := 1;
                }
            }
        """
        expect = "Undeclared Attribute: n"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        input = """
            class ABC {
                var b : int = 3;
                var x : int;
            }
            class Program {
                func @main() : void {
                    var b: int;
                    var a: ABC;
                    b := a.z;
                }
            }


        """
        expect = "Undeclared Attribute: z"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input = """
            class A{
                const a: int = 1;
            }
            class A <- B {
                var b : int;
            }
            class Program {
                func @main() : void {
                    var x : B;
                    const c: float = x.a;
                }
            }
            
            
            
            """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input = """
            class AB {
                const @a: int = 1;
                var x : int = 0;
            }
            class Program {
                func @main() : void {
                    var y : int;
                    y := AB.@a;
                    var z : int;
                    z := AB.@x;
                }
            }
        """
        expect = "Undeclared Attribute: @x"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        input = """
            class AB {
                const @a: int = 1;
                var x : int = 0;
            }
            class Program {
                func @main() : void {
                    var y : int = AB.@a;
                    var z : int = AB.@x;
                }
            }
        """
        expect = "Undeclared Attribute: @x"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        input = """
            class AB {
                var a : int = 1;
                var x : float;
            }
            class Program {
                func @main() : void {
                    var z : AB;
                    z.a := 3;
                    z.m := 3;
                }
            }
        """
        expect = "Undeclared Attribute: m"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        input = """
            class AB {
                var @a : int = 1;
                const x : float = 3.0;
            }
            class Program {
                func @main() : void {
                    AB.@a := 3;
                    AB.@z := 9;
                }
            }
        """
        expect = "Undeclared Attribute: @z"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        input = """
            class AB {
                var a: int = 1;
                var x: int = 2;
                func foo(a, x : int) : int {
                    const c : int = 1;
                    var b : int;
                    return a;
                    
                }
            }
            class B {
                func foo2() : void {    
                }
            }
            class Program {
                func @main() : void {
                    var z : AB;
                    var b : int = z.foo(1,2);
                    var d : int = z.foo2();
                }
            }
        """
        expect = "Undeclared Method: foo2"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        input = """
            class AB {
                var a : int = 1;
                var b : int = 2;
                func foo(_a, _b : int) : void {
                    self.a := _a;
                    self.b := _b;
                }
            }
            class Program {
                func @main() : void {
                    var z : AB;
                    z.foo(1,2);
                    AB.@foo();
                }
            }

        """
        expect = "Undeclared Method: @foo"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        input = """
            class AB {
                var a : int = 1;
                var b : int = 3;
                func constructor(_a, _b : int) {
                    self.a := _a;
                    self.b := _b;
                }
                func foo(_a, _b : int) : int {
                    self.a := _a;
                    self.b := _b;
                    return 1;
                }
                func foo2() : int {
                    return 1;
                }
            }
            class Program {
                func @main() : void {
                    var a : AB; 
                    var b : int = a.foo(1,2);
                    var c : int = a.foo3();

                }
            }

        """
        expect = "Undeclared Method: foo3"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        input = """
            class AB {
                var a: int = 1;
                var x: int = 2;
                func foo(a, x : int) : int {
                    const c : int = 1;
                    var b : int;
                    return a + x + b;
                    
                }
            }
            class B {
                func foo2() : void {    
                }
            }
            class Program {
                func @main() : void {
                    var z : AB = new AB();
                    var b : int = z.foo(1,2);
                    var d : int = z.foo2();
                }
            }
        """
        expect = "Undeclared Method: foo2"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        input = """
            class A {
                var a : int = 1;
                var @a : int = 2;
            }
            class Program {
                func @main() : void {
                    var z : A = new A();
                    var x : int = A.@a;
                    var y : int = z.a;
                    var t : int = A.foo();
                }
            }


        """
        expect = "Undeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        input = """
            class Program {
                func @main() : void {
                    var a : int;
                    var b : int = c;
                }
            }"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        input = """
            class B {
                func foo() : void {}
            }
            class Program {
                func @main() : void {
                    a.foo();
                }
            }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        input = """
            class B {
                var b : int = 1;
            }
            class Program {
                func @main() : void {
                    x.b := 1;
                }
            }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        input = """
            class B {
                func foo() : void {}
            }
            class Program {
            
                func @main() : void {
                    var a : int = 1;
                    var b : int ;
                    b := a + x.foo();
                }
            }
            """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        input = """
            class Program {
                func @main() : void {
                    var a : int = 1;
                    for i := 1; i < 10; i := i + 1 {
                        a := a + i;
                    }
                }   
                
            }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_45(self):
        input = """
            class Program {
                func @main() : void {
                    var a : int = 1;
                    if {a := 2;} a > 1 {a := 3;}
                    else {a := b;}
                }   
                
            }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        input = """
            class B {
                func foo() : int {
                    return x;
                
                }
            }  
            class Program {
                func @main() : void {
                    var a : A;
                    var b : int = a.foo();
                }
            }
                
            """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        input = """
            class A {
                func foo() : int {
                    return 1;
                }
            }
            class Program {
                func @main() : void {
                    var a : A;
                    var b : int = a.foo();
                    d := b * 2;
                }
            }
                

        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        input = """
            class A {
                func @foo() : int {
                    return 7;
                }
            }
            class Program {
                func @main() : void {
                    var x : int = 1;
                    var y : int = A.@foo();
                    var z : int;
                    z := x + y * t;
                }
            }
            
            """
        
        expect = "Undeclared Identifier: t"
        self.assertTrue(TestChecker.test(input,expect,448))


    def test_49(self):
        input = """
            class A {
                func foo() : int {
                    return 1;
                }
            }
            class Program {
                func @main() : void {
                    var a : A;
                    var b : int = a.foo();
                    var c : int = a.foo2();
                }
            }
        """
        expect = "Undeclared Method: foo2"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input ="""
        class Program {
        
            func @main() : void {
                var a : int;
                var i : int;
                for i := 1; i < 10; i := i + 1 {
                    if i > 5 {
                        break;
                    }
                    else {
                        i := b;
                    }
                }
            }
        
        }

        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,450))


    def test_51(self):
        input = """
            class Program {
                func @main() : void {
                    const a : int = 1;
                    a := 2;
                }
                
            }


        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        input = """
            class AB {
                const a : int = 1;
            }
            class Program {
                func @main() : void {
                    var m : AB;
                    m.a := 2;
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(m),Id(a)),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        input = """
            class A{
                const @a : int = 1;
            }
            class Program {
                func @main() : void {
                    A.@a := 2;
                }
            }

        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(A),Id(@a)),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,453))


    def test_54(self):
        input = """
            class Program {
               func @main() : void {
                   const a : int = 1;
                   var i : int;
                   for i := 1; i < 10; i := i + 1 {
                       a := i;
                   }
               }

            }

        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_55(self):
        input = """
            class Program {
                func @main() : void {
                    var a : int;
                    const b : int = 1;
                    for a := 1; a < 10; b := b + 1 {
                        a := b;
                    }
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))"
        self.assertTrue(TestChecker.test(input,expect,455)) 

    def test_56(self):
        input = """
            class Program {
                func @main() : void {
                    var a : int;
                    const b : int = 1;
                    for b := 1; a < 10; a := a + 1 {
                        b := a;
                    }
                }
            }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(b),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_57(self):
        input = """
            class Program {
                func @main() : void {
                    var i : int;
                    for i := 1; i < 10; i := i + 1 {
                        if i + 4  {
                           break;
                        }

                    }
                }
            }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(i),IntLit(4)),Block([Break]))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_58(self):
        input = """
            class Program {
                func @main() : void {
                    var i : float = 1.0;
                    var a : float;
                    for i := true; i < 10; i := i + 1 {
                        a := i;
                    }
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_59(self):
        input = """
            class Program {
                func @main() : void {
                    var i : int;
                    var a : float;
                    for i := 6.9; i < 10; i := i + 1 {
                        a := i;
                    }
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),FloatLit(6.9))"
        self.assertTrue(TestChecker.test(input,expect,459))


    def test_60(self):
        input = """
            class Program {
                func @main() : void {
                    var i : int;
                    var a : float;
                    for i := 1; i < 10; i := i + 2.5 {
                        a := i;
                    }
                    
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),BinaryOp(+,Id(i),FloatLit(2.5)))"
        self.assertTrue(TestChecker.test(input,expect,460))


    def test_61(self):
        input = """
            class Program {
                func @main() : void {
                    var a : float;
                    var b : int;
                    a := 9;
                    b := 9.8;
                }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),FloatLit(9.8))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_62(self):
        input = """
            class Program {
                func @main() : void {
                   var c : bool;
                    c := 1;
                }
            }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_63(self):
        input = """
            class A {
                func foo(_x, _y : float) : float {
                    return _x + _y;
                }
            }
            class Program {
                func @main() : void {
                    var x : A;
                    x.foo(1.8, 4.9);
                }
            }
        """
        expect = "Type Mismatch In Statement: Call(Id(x),Id(foo),[FloatLit(1.8),FloatLit(4.9)])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_64(self):
        input = """
            class A {
                func foo(_x, _y : float) : void {
                    return;
                }
            }
            class Program {
                func @main() : void {
                    var x : A;
                    x.foo(1.8, 4.9);
                    x.foo(1.8, false);
                }
            }
            
            """
        expect = "Type Mismatch In Statement: Call(Id(x),Id(foo),[FloatLit(1.8),BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_65(self):
        input = """
            class A {
                func foo(a: float, b : int) : float {
                    return a + b;
                }
            }
            class Program {
                func @main() : void {
                    var x : A;
                    var a : int;
                    a := x.foo(1.8, 4);
                }
            }
            
            
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),CallExpr(Id(x),Id(foo),[FloatLit(1.8),IntLit(4)]))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_66(self):
        input = """
            class Program {
                func constructor() {
                    return 1;
                }
                func @main() : void {
                
                }
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_67(self):
        input = """
            class A {
                var length : float = 1.0;
                var width : int = 2;

            }
            class B {
                var a : A = new A();

            }
            class Program {
            
                func @main() : void {
                    var a : B;
                    a.a.length := 6;
                    a.a.width := 7.0;
                }
            }
        
        
        """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(FieldAccess(Id(a),Id(a)),Id(width)),FloatLit(7.0))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_68(self):
        input = """
            class Program {
                var a : [3]int;
                
                func @main() : void {
                    a[1] := "a";
                }

            }"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLit(1)),StringLit(a))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_69(self):
        input = """
            class Program {
                var a : [3]int;
                
                func @main() : void {
                    a[1] := 5.0;
                }

            }"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLit(1)),FloatLit(5.0))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_70(self):
        input = """
            class Program {
                var a : [3]int;
                
                func @main() : void {
                    a[1] := true;
                }

            }"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLit(1)),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input = """
            class Program {
                func @main() : void {
                    var b : [5]int;
                    b[1.8] := 5;
                }

            }

        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),FloatLit(1.8))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    var x : [6]int;
                    const y : int = 1;
                    var z : float = 1.6;
                    var t : int;
                    x[5] := 3;
                    t := (y + z) % (y - 1);
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,BinaryOp(+,Id(y),Id(z)),BinaryOp(-,Id(y),IntLit(1)))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    
                    const y : int = 1;
                    var z : float = 1.6;
                    var t : bool;
                    
                    t := (y + z) == !(y - 1);
                }
            }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,BinaryOp(-,Id(y),IntLit(1)))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        input = """
            class A {
                var c: int = 1;

            }
            class Program {
                func main() : void {
                    var x : int;
                    var y : int;
                    y := x.c;
                }
            }
        """
        expect = "Type Mismatch In Expression: FieldAccess(Id(x),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input = """
            
            class Program {
                func @main() : void {
                    var x : int = 2;
                    var y : int;
                    y := x % 2.5;
                }
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(x),FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    
                    const x : [3]int = [1.4, 3.5, 6.8];
                }
            }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(x),ArrayType(3,IntType),[FloatLit(1.4),FloatLit(3.5),FloatLit(6.8)])"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    
                    var x : [3]int = [1.4, 3.5, 6.8];
                }
            }
        """
        
        expect = "Type Mismatch In Statement: VarDecl(Id(x),ArrayType(3,IntType),[FloatLit(1.4),FloatLit(3.5),FloatLit(6.8)])"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_78(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    
                    const x : [3]int = [1.4, 3.5];
                }
            }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(x),ArrayType(3,IntType),[FloatLit(1.4),FloatLit(3.5)])"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    
                    const x : int = 8.9;
                }
            }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(x),IntType,FloatLit(8.9))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        input = """ 
            class Program {
            
                func @main() : void {
                    
                    const a : [3]float = ["a", "b", "c"];
                }
            }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),ArrayType(3,FloatType),[StringLit(a),StringLit(b),StringLit(c)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input = """
            class Program {
                func @main() : void {
                    var i : int;
                    for i := 1; i < 10; i := i + 1 {
                        if i > 5  {
                           break;
                        }
                        else {
                            continue;
                        }
                        i := 3;

                    }
                    continue;
                }
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input = """
            class A {
                var x : int = 4;
                const y : int;
            }
            class Program {
                func @main() : void {
                
                }
            }
        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(y),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        input = """
            class A {
                var x : int = 4;
                const y : int = 4;
                func foo(a, b : int) : int {
                    const z : float = self.x + self.y;
                }
            }
            class Program {
                func @main() : void {
                
                }
            }
        """
        expect = "Type Mismatch In Declaration: BinaryOp(+,FieldAccess(Self(),Id(x)),FieldAccess(Self(),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        input = """
            class A {
                var x : int = 4;
                const y : int = self.x + 7;
            }
            class Program {
                func @main() : void {
                
                }
            }
        """
        expect = "Type Mismatch In Declaration: BinaryOp(+,FieldAccess(Self(),Id(x)),IntLit(7))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
        input = """
            class Program {
                var x: int = 2;
                func @main() : void {
                    var a: [3]int = [1,2,3];
                    const y : int = self.x + 4;
                
                }
            }
            """
        expect = "Type Mismatch In Declaration: BinaryOp(+,FieldAccess(Self(),Id(x)),IntLit(4))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input = """
            class Program {
                var a : [2]int = [1, 3.5];
                func @main() : void {}
            }"""
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(3.5)]"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        input = """
            class Program {
                var a : [2]int = [1, 3];
                func @main() : void {
                    const b : [2]int = [1, 3.5];
                }
            }
        """
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(3.5)]"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        input = """
            class Program {
                var a : [2]int = [1, 3];
                func @main() : void {
                    var b : [2]int = [1, "a"];
                }
            }
        """
        expect = "Illegal Array Literal: [IntLit(1),StringLit(a)]"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        input = """
            class Program {
                var a : [2]int = [1, 3];
                func @main() : void {
                    var b : [2]int = [1, 3];
                    b[1.5] := 3;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_90(self):
        input = """
            class Program {
                var a : [2]int = [1, 3];
                func @main() : void {
                    var b : [2]string = ["b", 3];
                }
            }
        """
        expect = "Illegal Array Literal: [StringLit(b),IntLit(3)]"

        self.assertTrue(TestChecker.test(input,expect,490))


    def test_91(self):
        input = """
            class A {}
            class B {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        input = """
            class A {}
            class B {}
            class Program {}

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
        input = """
            class A {}
            class C {}
            class Program{
                func main() : void {}
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
        input = """
            class A {}
            class C {}
            class Program{
                func @main() : void {}
            }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
        input = """
            class Program{
                func @main() : void {
                    continue;
                }
            }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_96(self):
        input = """
        class Program{
                func @main() : void {
                    var x : string ;
                    x := 1;
                }
            }

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
        input = """
        class Program{
                func @main() : void {
                    const a : int = 1;
                    a := 3;
                }
            }

        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input,expect,497))


    def test_98(self):
        input = """
        class Program{
                func @main() : void {
                    const a : int;
                }
            }

        """
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input = """
        class Program{
                func @main() : void {
                     b := 9;
                }
            }

        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,499))
        








