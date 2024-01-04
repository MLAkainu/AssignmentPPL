import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_303_program(self):
        input = """class main {
            var x, y, t:int = 1, 2, 3;
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(x),IntType,IntLit(1))),AttributeDecl(VarDecl(Id(y),IntType,IntLit(2))),AttributeDecl(VarDecl(Id(t),IntType,IntLit(3)))])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_304_program(self):
        input ="""class object<-main{ const x, y, z: int = 1, 2, 3;
        var a, b: float;}"""
        expect = "Program([ClassDecl(Id(main),Id(object),[AttributeDecl(ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(ConstDecl(Id(y),IntType,IntLit(2))),AttributeDecl(ConstDecl(Id(z),IntType,IntLit(3))),AttributeDecl(VarDecl(Id(a),FloatType)),AttributeDecl(VarDecl(Id(b),FloatType))])])"
        self.assertTrue(TestAST.test(input,expect,304))


    def test_305_program(self):
        input = """class main{ func a(): void {}}"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(a),[],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_306_program(self):
        input = """class main{
            func foo  (a: int, b: float):void {}

            func @main():void{
                io.printInt(4);
        }}"""
        expect="Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[Param(Id(a),IntType),Param(Id(b),FloatType)],VoidType,Block([])),MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(printInt),[IntLit(4)])]))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_307_program(self):
        input = """class main{}
        class foo<-main{}"""
        expect = "Program([ClassDecl(Id(main),[]),ClassDecl(Id(main),Id(foo),[])])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_308_program(self):
        input = """class main{
            var a: int;
            func foo():void{
                a:=1;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(a),IntType)),MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(Id(a),IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_309_program(self):
        input = """class main{
            func foo():void{
                if j > i {j := j + 1;} else {j := j - 1;}
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[],VoidType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))]),Block([AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1)))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,309))
    
    def test_310_program(self):
        input = """class _program123{}"""
        expect = "Program([ClassDecl(Id(_program123),[])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_311_program(self):
        input = """class Program{
            func main():void{}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,311))
    def test_312_program(self):
        input = """class Program{
            func main(a:int):void{}
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[Param(Id(a),IntType)],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_313_program(self):
        input = """class Program{
            func main(a:int):void{
                {}
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[Param(Id(a),IntType)],VoidType,Block([Block([])]))])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_314_program(self):
        input = """class _HelloWorld{
            func main(a:int):void{
                //var a: int = 1;
                //const b: float = 1.0;
                {
                return a-b;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[MethodDecl(Id(main),[Param(Id(a),IntType)],VoidType,Block([Block([Return(BinaryOp(-,Id(a),Id(b)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_315_program(self):
        input = """class _HelloWorld{
            func main(a:int):void{
                var a: int;
                //const b: float = 1.0;
                {
                return a-b;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[MethodDecl(Id(main),[Param(Id(a),IntType)],VoidType,Block([VarDecl(Id(a),IntType),Block([Return(BinaryOp(-,Id(a),Id(b)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,315))
    
    def test_316_program(self):
        input = """class _HelloWorld{
            func main(a:int):void{
                var a: int;
                const b: float = 1.0;
                {
                return a-b;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[MethodDecl(Id(main),[Param(Id(a),IntType)],VoidType,Block([VarDecl(Id(a),IntType),ConstDecl(Id(b),FloatType,FloatLit(1.0)),Block([Return(BinaryOp(-,Id(a),Id(b)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_317_program(self):
        input = """class _HelloWorld{
            func main(a:int):void{
                var a, b, c: int;
                const x, y, z: float = 1.0, 2.0, 3.0;
                {
                return a-b;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[MethodDecl(Id(main),[Param(Id(a),IntType)],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(x),FloatType,FloatLit(1.0)),ConstDecl(Id(y),FloatType,FloatLit(2.0)),ConstDecl(Id(z),FloatType,FloatLit(3.0)),Block([Return(BinaryOp(-,Id(a),Id(b)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_318_program(self):
        input = """class _HelloWorld{
            func constructor(a:int) {}
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[MethodDecl(Id(constructor),[Param(Id(a),IntType)],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_319_program(self):
        input = """class _HelloWorld{
            var a: int;
            const b, c, d: float = 1.0, 2.0, 3.0;
            func constructor(a:int) {}
            func @abc (a,b,c:float, d:int):float{}
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[AttributeDecl(VarDecl(Id(a),IntType)),AttributeDecl(ConstDecl(Id(b),FloatType,FloatLit(1.0))),AttributeDecl(ConstDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(ConstDecl(Id(d),FloatType,FloatLit(3.0))),MethodDecl(Id(constructor),[Param(Id(a),IntType)],VoidType,Block([])),MethodDecl(Id(@abc),[Param(Id(a),FloatType),Param(Id(b),FloatType),Param(Id(c),FloatType),Param(Id(d),IntType)],FloatType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test_320_program(self):
        input = """class _HelloWorld{
            func main():void{
                var a: [5]int;
            }
        }"""
        expect = "Program([ClassDecl(Id(_HelloWorld),[MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),ArrayType(5,IntType))]))])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_321_program(self):
        input = """class Rectangle{
            var w: [3]int = [1,2,3];
            const h: int = 4;
            var area: int = new Shape();
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(VarDecl(Id(w),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(ConstDecl(Id(h),IntType,IntLit(4))),AttributeDecl(VarDecl(Id(area),IntType,NewExpr(Id(Shape),[])))])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_322_program(self):
        input = """class Rectangle{
            var @wight, h, c: int;
            const h: int = 4;
            var @area: int = new Shape(a,b,c);
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(VarDecl(Id(@wight),IntType)),AttributeDecl(VarDecl(Id(h),IntType)),AttributeDecl(VarDecl(Id(c),IntType)),AttributeDecl(ConstDecl(Id(h),IntType,IntLit(4))),AttributeDecl(VarDecl(Id(@area),IntType,NewExpr(Id(Shape),[Id(a),Id(b),Id(c)])))])])"
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_323_program(self):
        input="""class Shape{
            const PI: float = 3.14;
            func area():Shape{
                self.area(a,b,c*PI);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(ConstDecl(Id(PI),FloatType,FloatLit(3.14))),MethodDecl(Id(area),[],ClassType(Id(Shape)),Block([Call(Self(),Id(area),[Id(a),Id(b),BinaryOp(*,Id(c),Id(PI))])]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_324_program(self):
        input="""class Shape{
            const PI: ABC = 3.14;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(ConstDecl(Id(PI),ClassType(Id(ABC)),FloatLit(3.14)))])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test_325_program(self):
        input="""class Shape{
            var PI: ABC = 3.14;
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(PI),ClassType(Id(ABC)),FloatLit(3.14)))])])"
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test_326_program(self):
        input="""class Shape{
            var PI: ABC;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(PI),ClassType(Id(ABC)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input,expect,326))

    def test_327_program(self):
        input="""class Shape{
            var PI: ABC;
            const PI: ABC;
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(PI),ClassType(Id(ABC)),NullLiteral())),AttributeDecl(ConstDecl(Id(PI),ClassType(Id(ABC)),None))])])"
        self.assertTrue(TestAST.test(input,expect,327))

    def test_328_program(self):
        input="""class Shape{
            var PI: ABC;
            const PI: ABC = true;
            func main():void{
                var a: int;
                var b: float;
                var c: bool;
                var d: string;
                io.@writeInt(res);
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(PI),ClassType(Id(ABC)),NullLiteral())),AttributeDecl(ConstDecl(Id(PI),ClassType(Id(ABC)),BooleanLit(True))),MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),BoolType),VarDecl(Id(d),StringType),Call(Id(io),Id(@writeInt),[Id(res)])]))])])"
        self.assertTrue(TestAST.test(input,expect,328))

    def test_329_program(self):
        input="""class Shape{
            var abc: string = "Hello World";
            const PI: ABC = true;
            func main():void{
                var chj : string = "Hello World";
                const PI: ABC = false;
            }    
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(abc),StringType,StringLit(Hello World))),AttributeDecl(ConstDecl(Id(PI),ClassType(Id(ABC)),BooleanLit(True))),MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(chj),StringType,StringLit(Hello World)),ConstDecl(Id(PI),ClassType(Id(ABC)),BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test_330_program(self):
        input = """class Program {
            const a : int = self.foo(1, abc ^ 2);
            const b : float = ABC.@main(1,2,3);
            const c : Shape = _abc.@foo().bar;
            
        }"""
        expect="Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(a),IntType,CallExpr(Self(),Id(foo),[IntLit(1),BinaryOp(^,Id(abc),IntLit(2))]))),AttributeDecl(ConstDecl(Id(b),FloatType,CallExpr(Id(ABC),Id(@main),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(ConstDecl(Id(c),ClassType(Id(Shape)),FieldAccess(CallExpr(Id(_abc),Id(@foo),[]),Id(bar))))])])"
        self.assertTrue(TestAST.test(input,expect,330))


    def test_331_program(self):
        input = """class Program {
        func main():void{
                const k : Rectangle = null;
                var a : int = abc.Instance().vnm;
                var b : float = abc.@Saticfunc().vnm;
                const mn : string = __.@main();
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([ConstDecl(Id(k),ClassType(Id(Rectangle)),NullLiteral()),VarDecl(Id(a),IntType,FieldAccess(CallExpr(Id(abc),Id(Instance),[]),Id(vnm))),VarDecl(Id(b),FloatType,FieldAccess(CallExpr(Id(abc),Id(@Saticfunc),[]),Id(vnm))),ConstDecl(Id(mn),StringType,CallExpr(Id(__),Id(@main),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,331))
    def test_332_program(self):
        input = """class Program {
            const a,x,y : int = self.foo(1, abc ^ 2), 1, 2;
            const b : float = ABC.@main(1,2,3);
            const c : Shape = _abc.@foo().bar;
            
        }"""
        expect="Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(a),IntType,CallExpr(Self(),Id(foo),[IntLit(1),BinaryOp(^,Id(abc),IntLit(2))]))),AttributeDecl(ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(ConstDecl(Id(y),IntType,IntLit(2))),AttributeDecl(ConstDecl(Id(b),FloatType,CallExpr(Id(ABC),Id(@main),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(ConstDecl(Id(c),ClassType(Id(Shape)),FieldAccess(CallExpr(Id(_abc),Id(@foo),[]),Id(bar))))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_333_program(self):
        input="""class Shape{
            func constructor() {
                return;
            }
            }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(constructor),[],VoidType,Block([Return()]))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    def test_334_program(self):
        input="""class Rectangle{
            func constructor() {
                self.width := 1;
                self.height := 4;
                return self.width * self.height;
            }
            }"""
        expect = "Program([ClassDecl(Id(Rectangle),[MethodDecl(Id(constructor),[],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(width)),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(height)),IntLit(4)),Return(BinaryOp(*,FieldAccess(Self(),Id(width)),FieldAccess(Self(),Id(height))))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test_335_program(self):
        input="""class Rectangle{
            func constructor(width:int, height:int) {
                self.width := 1;
                self.height := 4;
                return self.width * self.height;
            }
            }"""
        expect = "Program([ClassDecl(Id(Rectangle),[MethodDecl(Id(constructor),[Param(Id(width),IntType),Param(Id(height),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(width)),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(height)),IntLit(4)),Return(BinaryOp(*,FieldAccess(Self(),Id(width)),FieldAccess(Self(),Id(height))))]))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_336_program(self):
        input="""class Rectangle{
            func constructor(width:int, height:int) {
                var area : int;
                {
                    area := width * height;
                    return area;
                }
                return area;
            }
            }"""
        expect = "Program([ClassDecl(Id(Rectangle),[MethodDecl(Id(constructor),[Param(Id(width),IntType),Param(Id(height),IntType)],VoidType,Block([VarDecl(Id(area),IntType),Block([AssignStmt(Id(area),BinaryOp(*,Id(width),Id(height))),Return(Id(area))]),Return(Id(area))]))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_337_program(self):
        input="""class Main{
            var abc : [9]Shape;
            const op : [3]float = [1.0, 2.0, 3.0];
            func main():void{
                var name : string = "Hello World";
            }
        }"""
        expect = "Program([ClassDecl(Id(Main),[AttributeDecl(VarDecl(Id(abc),ArrayType(9,ClassType(Id(Shape))))),AttributeDecl(ConstDecl(Id(op),ArrayType(3,FloatType),[FloatLit(1.0),FloatLit(2.0),FloatLit(3.0)])),MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(name),StringType,StringLit(Hello World))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_338_program(self):
        input="""class Arr{
            const a : [3]int = [1,true,"3"];
            func main():void{
                var name : [3]string = [1,9., "Hello World"];
            }
        }"""
        expect = "Program([ClassDecl(Id(Arr),[AttributeDecl(ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1),BooleanLit(True),StringLit(3)])),MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(name),ArrayType(3,StringType),[IntLit(1),FloatLit(9.0),StringLit(Hello World)])]))])])"
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test_339_program(self):
        input="""class x{
            const abc, xyz : [3]int = [1e2, 2e-3, 3e-4], [1.e2, 2.e-3, 3.e-4];
        }"""
        expect = "Program([ClassDecl(Id(x),[AttributeDecl(ConstDecl(Id(abc),ArrayType(3,IntType),[FloatLit(100.0),FloatLit(0.002),FloatLit(0.0003)])),AttributeDecl(ConstDecl(Id(xyz),ArrayType(3,IntType),[FloatLit(100.0),FloatLit(0.002),FloatLit(0.0003)]))])])"
        self.assertTrue(TestAST.test(input,expect,339))

    def test_340_program(self):
        input="""class y{
            func main():void{
                var a: int = true * false;
                var b: float = 1e2 * 2e-3;
                var c: [3]int = Program.getArray().getValue().abc;
            }
        }"""
        expect = "Program([ClassDecl(Id(y),[MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType,BinaryOp(*,BooleanLit(True),BooleanLit(False))),VarDecl(Id(b),FloatType,BinaryOp(*,FloatLit(100.0),FloatLit(0.002))),VarDecl(Id(c),ArrayType(3,IntType),FieldAccess(CallExpr(CallExpr(Id(Program),Id(getArray),[]),Id(getValue),[]),Id(abc)))]))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test_341_program(self):
        input="""class y{
            func dbs():void{
                a := 1;
                c := true;
                b := !c;
                const a: float = -1e2;
            }
        }"""
        expect = "Program([ClassDecl(Id(y),[MethodDecl(Id(dbs),[],VoidType,Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(c),BooleanLit(True)),AssignStmt(Id(b),UnaryOp(!,Id(c))),ConstDecl(Id(a),FloatType,UnaryOp(-,FloatLit(100.0)))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test_342_program(self):
        input="""class y{
            func main():void{
                X.shape.getArea := 1;
                a := a.@c;
                a := X.shape.getArea;

            }
        }"""
        expect = "Program([ClassDecl(Id(y),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(FieldAccess(FieldAccess(Id(X),Id(shape)),Id(getArea)),IntLit(1)),AssignStmt(Id(a),FieldAccess(Id(a),Id(@c))),AssignStmt(Id(a),FieldAccess(FieldAccess(Id(X),Id(shape)),Id(getArea)))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test_343_program(self):
        input = """class Program {
            func main():void{
                a := (1+2).b;
                d := (true * (1.2 - 5.6 \\ 5) + 1e2) * 3e-4;
                f := (false / 5).f;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(Id(a),FieldAccess(BinaryOp(+,IntLit(1),IntLit(2)),Id(b))),AssignStmt(Id(d),BinaryOp(*,BinaryOp(+,BinaryOp(*,BooleanLit(True),BinaryOp(-,FloatLit(1.2),BinaryOp(\,FloatLit(5.6),IntLit(5)))),FloatLit(100.0)),FloatLit(0.0003))),AssignStmt(Id(f),FieldAccess(BinaryOp(/,BooleanLit(False),IntLit(5)),Id(f)))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test_344_program(self):
        input=input = """class Program {
            func main():void {
                Shape.width := 10;
                a := Shape.@length;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(FieldAccess(Id(Shape),Id(width)),IntLit(10)),AssignStmt(Id(a),FieldAccess(Id(Shape),Id(@length)))]))])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test_355_program(self):
        input = """class Program {
            func foo() : int {
                Program.x.y.z();
                (x.y[1][2]).foo();
                Shape.@area.calculate();
                (Shape.@w.s[1]).eval();
            }
            func main() : void {
                Shape.@width := 10;
                a := Shape.@area;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),[],IntType,Block([Call(FieldAccess(FieldAccess(Id(Program),Id(x)),Id(y)),Id(z),[]),Call(ArrayCell(ArrayCell(FieldAccess(Id(x),Id(y)),IntLit(1)),IntLit(2)),Id(foo),[]),Call(FieldAccess(Id(Shape),Id(@area)),Id(calculate),[]),Call(ArrayCell(FieldAccess(FieldAccess(Id(Shape),Id(@w)),Id(s)),IntLit(1)),Id(eval),[])])),MethodDecl(Id(main),[],VoidType,Block([AssignStmt(FieldAccess(Id(Shape),Id(@width)),IntLit(10)),AssignStmt(Id(a),FieldAccess(Id(Shape),Id(@area)))]))])])"
        
        self.assertTrue(TestAST.test(input,expect,345))
    
    def test_346_program(self):
        input="""class Shape{
            var PI: ABC;
            const PI: ABC;
            const @b, c, d: float = 1.0, 2.0, 3.0;
            func main():void{
                return new x().y();
            }
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(PI),ClassType(Id(ABC)),NullLiteral())),AttributeDecl(ConstDecl(Id(PI),ClassType(Id(ABC)),None)),AttributeDecl(ConstDecl(Id(@b),FloatType,FloatLit(1.0))),AttributeDecl(ConstDecl(Id(c),FloatType,FloatLit(2.0))),AttributeDecl(ConstDecl(Id(d),FloatType,FloatLit(3.0))),MethodDecl(Id(main),[],VoidType,Block([Return(CallExpr(NewExpr(Id(x),[]),Id(y),[]))]))])])"
        self.assertTrue(TestAST.test(input,expect,346))

    def test_347_program(self):
        input="""class Shape{
            const @a: int = 0;
            const b: float = 1.0;
            func @getA():int{
                return @a;
            }
            }
        class Rectangle{
            const @a: int = 0;
            const b: float = 1.0;
    
        }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(ConstDecl(Id(@a),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(b),FloatType,FloatLit(1.0))),MethodDecl(Id(@getA),[],IntType,Block([Return(FieldAccess(Id(@a)))]))]),ClassDecl(Id(Rectangle),[AttributeDecl(ConstDecl(Id(@a),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(b),FloatType,FloatLit(1.0)))])])"
        self.assertTrue(TestAST.test(input,expect,347))

    def test_348_program(self):
        input="""class Program {
            func main() : void {
                const res1 : int = Example.@getA() + Example.b;
                const res2 : int = Example.b + Example.@getA();
                io.printInt(res1 + res2);
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([ConstDecl(Id(res1),IntType,BinaryOp(+,CallExpr(Id(Example),Id(@getA),[]),FieldAccess(Id(Example),Id(b)))),ConstDecl(Id(res2),IntType,BinaryOp(+,FieldAccess(Id(Example),Id(b)),CallExpr(Id(Example),Id(@getA),[]))),Call(Id(io),Id(printInt),[BinaryOp(+,Id(res1),Id(res2))])]))])])"
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_349_program(self):
        input="""class Program {
            const @a: string = "Hello World";
            func main(): void {
                const b: int = 100000000;
                b.c.d := Program.@a() + 1;
                return (b - Program.@a + Self.@what - Program.@a());
            }
        }"""
        
        expect="Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(@a),StringType,StringLit(Hello World))),MethodDecl(Id(main),[],VoidType,Block([ConstDecl(Id(b),IntType,IntLit(100000000)),AssignStmt(FieldAccess(FieldAccess(Id(b),Id(c)),Id(d)),BinaryOp(+,CallExpr(Id(Program),Id(@a),[]),IntLit(1))),Return(BinaryOp(-,BinaryOp(+,BinaryOp(-,Id(b),FieldAccess(Id(Program),Id(@a))),FieldAccess(Id(Self),Id(@what))),CallExpr(Id(Program),Id(@a),[])))]))])])"
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_350_program(self):
        input = """class Program {
            func foo() : void {
                a := g != ((b * c / d % e) > f);
                b := ((abc ^ def) ^ ghi).upper();
                c := 1 || true && false;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(Id(a),BinaryOp(!=,Id(g),BinaryOp(>,BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(b),Id(c)),Id(d)),Id(e)),Id(f)))),AssignStmt(Id(b),CallExpr(BinaryOp(^,BinaryOp(^,Id(abc),Id(def)),Id(ghi)),Id(upper),[])),AssignStmt(Id(c),BinaryOp(&&,BinaryOp(||,IntLit(1),BooleanLit(True)),BooleanLit(False)))]))])])"

        
        self.assertTrue(TestAST.test(input,expect,350))

    def test_350_program(self):
        input = """class Sub {
            func main() : void {
                a := -1 + -2 + -3;
                b := str1 ^ st4.st6;
                c := !true;
                d := _class1.getString() ^ _.getString(); 
            }
        }"""

        expect="Program([ClassDecl(Id(Sub),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2))),UnaryOp(-,IntLit(3)))),AssignStmt(Id(b),BinaryOp(^,Id(str1),FieldAccess(Id(st4),Id(st6)))),AssignStmt(Id(c),UnaryOp(!,BooleanLit(True))),AssignStmt(Id(d),BinaryOp(^,CallExpr(Id(_class1),Id(getString),[]),CallExpr(Id(_),Id(getString),[])))]))])])"
        self.assertTrue(TestAST.test(input,expect,350))

    def test_351_program(self):
        input = """class Program {
            func main() : string {
                a := a[a.b] + c[a.@b];
                d := true && false && true || false ^ e;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],StringType,Block([AssignStmt(Id(a),BinaryOp(+,ArrayCell(Id(a),FieldAccess(Id(a),Id(b))),ArrayCell(Id(c),FieldAccess(Id(a),Id(@b))))),AssignStmt(Id(d),BinaryOp(^,BinaryOp(||,BinaryOp(&&,BinaryOp(&&,BooleanLit(True),BooleanLit(False)),BooleanLit(True)),BooleanLit(False)),Id(e)))]))])])"
        
        self.assertTrue(TestAST.test(input,expect,351))

    def test_352_program(self):
        input = """class XYZ {
            var a: float = a.b().c;
        }"""
        expect="Program([ClassDecl(Id(XYZ),[AttributeDecl(VarDecl(Id(a),FloatType,FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c))))])])"
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test_353_program(self):
        input = """class Program {
            var @a: string = a.@b.c();
            var @b: Shape = a.@b;
        }"""
        expect="Program([ClassDecl(Id(Program),[AttributeDecl(VarDecl(Id(@a),StringType,CallExpr(FieldAccess(Id(a),Id(@b)),Id(c),[]))),AttributeDecl(VarDecl(Id(@b),ClassType(Id(Shape)),FieldAccess(Id(a),Id(@b))))])])"
        self.assertTrue(TestAST.test(input,expect,353))

    def test_354_program(self):
        input = """class Program {
            func foo() : void  {
                a := _new.@abc;
                b := a * 1.0 / 2 % 3;
                c := ("true" ^ a)[1];
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(Id(a),FieldAccess(Id(_new),Id(@abc))),AssignStmt(Id(b),BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(a),FloatLit(1.0)),IntLit(2)),IntLit(3))),AssignStmt(Id(c),ArrayCell(BinaryOp(^,StringLit(true),Id(a)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input,expect,354))

    def test_355_program(self):
        input = """class Program {
            func foo() : void {
                (abc + 9)[1] := 1.05;
                a[2][3] := self.x;
            }
            func main() : int {
                var a : int = a[1] + b[2]; 
                a := new X();
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(ArrayCell(BinaryOp(+,Id(abc),IntLit(9)),IntLit(1)),FloatLit(1.05)),AssignStmt(ArrayCell(ArrayCell(Id(a),IntLit(2)),IntLit(3)),FieldAccess(Self(),Id(x)))])),MethodDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType,BinaryOp(+,ArrayCell(Id(a),IntLit(1)),ArrayCell(Id(b),IntLit(2)))),AssignStmt(Id(a),NewExpr(Id(X),[]))]))])])"
        
        self.assertTrue(TestAST.test(input,expect,355))

    def test_356_program(self):
        input = """class Shape {
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
        }
        class Program {
            func main() : void {
                var obj1: Shape = new Shape(1, 4);
                const obj2: Shape;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(constructor),[Param(Id(_length),IntType),Param(Id(_width),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(_length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(_width))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(obj1),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(4)])),ConstDecl(Id(obj2),ClassType(Id(Shape)),None)]))])])"
        self.assertTrue(TestAST.test(input,expect,356))
    
    def test_357_program(self):
        input = """class Program {
            func main() : void {
                a[1] := 1;
                (a + b).foo := 9;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(ArrayCell(Id(a),IntLit(1)),IntLit(1)),AssignStmt(FieldAccess(BinaryOp(+,Id(a),Id(b)),Id(foo)),IntLit(9))]))])])"
        
        self.assertTrue(TestAST.test(input,expect,357))

    def test_358_program(self):
        input = """class Program {
            func main() :void{
                _kmn.@_456 := 1 + 2;
                a.@b.c()[_] := null;
                return;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(FieldAccess(Id(_kmn),Id(@_456)),BinaryOp(+,IntLit(1),IntLit(2))),AssignStmt(ArrayCell(CallExpr(FieldAccess(Id(a),Id(@b)),Id(c),[]),Id(_)),NullLiteral()),Return()]))])])"
        
        self.assertTrue(TestAST.test(input,expect,358))

    def test_359_program(self):
        input = """class Program {
            func main() : void {
                a.@b.c.d := a.@b.c() - a.b().c;
                a.@b().c := a.b.c.d().val;
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(@b)),Id(c)),Id(d)),BinaryOp(-,CallExpr(FieldAccess(Id(a),Id(@b)),Id(c),[]),FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c)))),AssignStmt(FieldAccess(CallExpr(Id(a),Id(@b),[]),Id(c)),FieldAccess(CallExpr(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d),[]),Id(val)))]))])])"
        self.assertTrue(TestAST.test(input,expect,359))

    def test_360_program(self):
        input="""class Program{
            func main() : void {
                self.aPI := 3.14;
                value := x.foo(5,6);
                l[3] := value * 2;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(aPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5),IntLit(6)])),AssignStmt(ArrayCell(Id(l),IntLit(3)),BinaryOp(*,Id(value),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input,expect,360))

    def test_361_program(self):
        input="""class Program {
            var @c: _program;
            func main() : void {
                var b: int;
                b := _program.@methodA();
                io.@printInt(b);
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[AttributeDecl(VarDecl(Id(@c),ClassType(Id(_program)),NullLiteral())),MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(b),IntType),AssignStmt(Id(b),CallExpr(Id(_program),Id(@methodA),[])),Call(Id(io),Id(@printInt),[Id(b)])]))])])"
        self.assertTrue(TestAST.test(input,expect,361))


    def test_362_program(self):
        input = """class Program {
            func main() : void {
                a := _1a2b3c.@d();
                A[1][2][true] := new x() + 2 * new Y();
                io.print("a " + i + ": " + b.d[i - 1]);
                io.print("a " + i + ": " + c.@e[i - 1]);
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([AssignStmt(Id(a),CallExpr(Id(_1a2b3c),Id(@d),[])),AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(A),IntLit(1)),IntLit(2)),BooleanLit(True)),BinaryOp(+,NewExpr(Id(x),[]),BinaryOp(*,IntLit(2),NewExpr(Id(Y),[])))),Call(Id(io),Id(print),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(a ),Id(i)),StringLit(: )),ArrayCell(FieldAccess(Id(b),Id(d)),BinaryOp(-,Id(i),IntLit(1))))]),Call(Id(io),Id(print),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(a ),Id(i)),StringLit(: )),ArrayCell(FieldAccess(Id(c),Id(@e)),BinaryOp(-,Id(i),IntLit(1))))])]))])])"
        self.assertTrue(TestAST.test(input,expect,362))

    def test_363_program(self):
        input = """class Program {
            func main() : void {
                if  j > i {io.@write(j);}
                
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([Call(Id(io),Id(@write),[Id(j)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,363))
    
    def test_364_program(self):
        input = """class Program {
            func main() : void {
                if  {i:=0;} j > i {io.@write(j);}
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([If(Block([AssignStmt(Id(i),IntLit(0))]),BinaryOp(>,Id(j),Id(i)),Block([Call(Id(io),Id(@write),[Id(j)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,364))
    
    def test_365_program(self):
        input = """class Program {
            func main() : void {
                if  j > i {io.@write(j);}
                else {io.@write(i);}
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([Call(Id(io),Id(@write),[Id(j)])]),Block([Call(Id(io),Id(@write),[Id(i)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,365))

    def test_366_program(self):
        input = """class Program {
            func main() : void {
                if {i:=0;} j > i {io.@write(j);}
                else {io.@write(i);}
                
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([If(Block([AssignStmt(Id(i),IntLit(0))]),BinaryOp(>,Id(j),Id(i)),Block([Call(Id(io),Id(@write),[Id(j)])]),Block([Call(Id(io),Id(@write),[Id(i)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,366))

    def test_367_program(self):
        input = """class Program {
            func main() : void {
                if  j > i {io.@write(j);}
                if i > j {io.@write(i);}
                else {io.@write(i+j);}
                
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([Call(Id(io),Id(@write),[Id(j)])])),If(BinaryOp(>,Id(i),Id(j)),Block([Call(Id(io),Id(@write),[Id(i)])]),Block([Call(Id(io),Id(@write),[BinaryOp(+,Id(i),Id(j))])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,367))

    def test_368_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                }
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,368))

    def test_369_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                    if i == 5 {break;}
                }
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)]),If(BinaryOp(==,Id(i),IntLit(5)),Block([Break]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,369))

    def test_370_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                    if i == 5 {continue;}
                }
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)]),If(BinaryOp(==,Id(i),IntLit(5)),Block([Continue]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,370))

    def test_371_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                    if i == 5 {return;}
                }
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)]),If(BinaryOp(==,Id(i),IntLit(5)),Block([Return()]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,371))

    def test_372_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                    if i == 5 {return 1;}
                }
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)]),If(BinaryOp(==,Id(i),IntLit(5)),Block([Return(IntLit(1))]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,372))
    
    def test_373_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                    if i == 5 {return 1;}
                    else {return 0;}
                }
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)]),If(BinaryOp(==,Id(i),IntLit(5)),Block([Return(IntLit(1))]),Block([Return(IntLit(0))]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,373))

    def test_374_program(self):
        input="""class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@write(i);
                    if i == 5 {return 1;}
                    if i == 6 {return 2;}
                    if i == 7 {return 3;}
                    if {c := 1;} i == 8 {return 4;}
                    else {return 0;}
                }
                return 2;
        }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@write),[Id(i)]),If(BinaryOp(==,Id(i),IntLit(5)),Block([Return(IntLit(1))])),If(BinaryOp(==,Id(i),IntLit(6)),Block([Return(IntLit(2))])),If(BinaryOp(==,Id(i),IntLit(7)),Block([Return(IntLit(3))])),If(Block([AssignStmt(Id(c),IntLit(1))]),BinaryOp(==,Id(i),IntLit(8)),Block([Return(IntLit(4))]),Block([Return(IntLit(0))]))])]),Return(IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input,expect,374))

    def test_375_program(self):
        input="""class Program {
            func main() : int {
                if i == 5 {for i := 0; i < 10; i := i + 1 {return 1;}}
                else {return 0;}
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],IntType,Block([If(BinaryOp(==,Id(i),IntLit(5)),Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Return(IntLit(1))])])]),Block([Return(IntLit(0))]))]))])])"
        self.assertTrue(TestAST.test(input,expect,375))

    def test_376_program(self):
        input = """class Program {
            func main() : void{
                Shape.@getNumOfShape();
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([Call(Id(Shape),Id(@getNumOfShape),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,376))

    def test_377_program(self):
        input = """class Program {
            func main() : void{
                Shape.@getNumOfShape();
                Shape.@getNumOfShape();
            }
        }"""

        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([Call(Id(Shape),Id(@getNumOfShape),[]),Call(Id(Shape),Id(@getNumOfShape),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,377))

    def test_378_program(self):
        input = """class Program {
            func main() : void {
                for self.a := 1; self.a < 11; self.a := self.a + 1  {
                    io.@write(self.a);
                }
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1)),BinaryOp(<,FieldAccess(Self(),Id(a)),IntLit(11)),AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(+,FieldAccess(Self(),Id(a)),IntLit(1))),Block([Call(Id(io),Id(@write),[FieldAccess(Self(),Id(a))])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,378))

    def test_379_program(self):
        input = """class Program {
            func main() : void {
                for a.bc := 1; a.bc < 11; a.bc := a.bc + 1  {
                    io.@write(a.bc);
                    if a.bc == 5 {break;}
                }
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(FieldAccess(Id(a),Id(bc)),IntLit(1)),BinaryOp(<,FieldAccess(Id(a),Id(bc)),IntLit(11)),AssignStmt(FieldAccess(Id(a),Id(bc)),BinaryOp(+,FieldAccess(Id(a),Id(bc)),IntLit(1))),Block([Call(Id(io),Id(@write),[FieldAccess(Id(a),Id(bc))]),If(BinaryOp(==,FieldAccess(Id(a),Id(bc)),IntLit(5)),Block([Break]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test_380_program(self):
        input = """class Program {
            func main() : void {
                for self.a.b := 1; self.a.b < 11; self.a.b := self.a.b + 1  {
                    io.@write(self.a.b);
                    if self.a.b == 5 {break;}
                }
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),IntLit(1)),BinaryOp(<,FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),IntLit(11)),AssignStmt(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),BinaryOp(+,FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),IntLit(1))),Block([Call(Id(io),Id(@write),[FieldAccess(FieldAccess(Self(),Id(a)),Id(b))]),If(BinaryOp(==,FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),IntLit(5)),Block([Break]))])])]))])])"
        self.assertTrue(TestAST.test(input,expect,380))

    def test_381_program(self):
        input = """class Program {
            func main() : void {
                for a.@b := 1; a.@b < 11; a.@b := a.@b + 1  {
                    io.@write(a.@b);
                }
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(FieldAccess(Id(a),Id(@b)),IntLit(1)),BinaryOp(<,FieldAccess(Id(a),Id(@b)),IntLit(11)),AssignStmt(FieldAccess(Id(a),Id(@b)),BinaryOp(+,FieldAccess(Id(a),Id(@b)),IntLit(1))),Block([Call(Id(io),Id(@write),[FieldAccess(Id(a),Id(@b))])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,381))

    def test_382_program(self):
        input = """class Program {
            func main() : void {
                for Program.@b.mn.c := 1; Program.@b.mn.c < 11; Program.@b.mn.c := Program.@b.mn.c + 1  {
                    io.@write(Program.@b.mn.c);
                }
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(Program),Id(@b)),Id(mn)),Id(c)),IntLit(1)),BinaryOp(<,FieldAccess(FieldAccess(FieldAccess(Id(Program),Id(@b)),Id(mn)),Id(c)),IntLit(11)),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(Program),Id(@b)),Id(mn)),Id(c)),BinaryOp(+,FieldAccess(FieldAccess(FieldAccess(Id(Program),Id(@b)),Id(mn)),Id(c)),IntLit(1))),Block([Call(Id(io),Id(@write),[FieldAccess(FieldAccess(FieldAccess(Id(Program),Id(@b)),Id(mn)),Id(c))])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,382))

    def test_383_program(self):
        input = """class Program {
            func main() : void {
                for a.@b.c := 1; a.@b.c < 11; a.@b.c := a.@b.c + 1  {
                    io.@write(a.@b.c);
                }
            }
        }"""
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([For(AssignStmt(FieldAccess(FieldAccess(Id(a),Id(@b)),Id(c)),IntLit(1)),BinaryOp(<,FieldAccess(FieldAccess(Id(a),Id(@b)),Id(c)),IntLit(11)),AssignStmt(FieldAccess(FieldAccess(Id(a),Id(@b)),Id(c)),BinaryOp(+,FieldAccess(FieldAccess(Id(a),Id(@b)),Id(c)),IntLit(1))),Block([Call(Id(io),Id(@write),[FieldAccess(FieldAccess(Id(a),Id(@b)),Id(c))])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,383))

    def test_384_program(self):
        input = """class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
            func @getNumOfShape() : int {
                return @numOfShape;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(constructor),[Param(Id(_length),IntType),Param(Id(_width),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(_length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(_width))])),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(FieldAccess(Id(@numOfShape)))]))])])"
        self.assertTrue(TestAST.test(input,expect,384))

    def test_385_program(self):
        input = """class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
            func @getNumOfShape() : int {
                return @numOfShape;
            }
        }
        class Shape <- Retangle {
            func getArea() : int {
                return self.length * self.width;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(constructor),[Param(Id(_length),IntType),Param(Id(_width),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(_length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(_width))])),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(FieldAccess(Id(@numOfShape)))]))]),ClassDecl(Id(Retangle),Id(Shape),[MethodDecl(Id(getArea),[],IntType,Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,385))

    def test_386_program(self):
        input="""class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
            func @getNumOfShape() : int {
                return @numOfShape;
            }
        }
        class Shape <- Retangle {
            func getArea() : int {
                return self.length * self.width;
            }
        }
        class Program {
            func main() : void {
                var obj1: Shape = new Shape(1, 4);
                const obj2: Shape;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(constructor),[Param(Id(_length),IntType),Param(Id(_width),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(_length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(_width))])),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(FieldAccess(Id(@numOfShape)))]))]),ClassDecl(Id(Retangle),Id(Shape),[MethodDecl(Id(getArea),[],IntType,Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(obj1),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(4)])),ConstDecl(Id(obj2),ClassType(Id(Shape)),None)]))])])"
        self.assertTrue(TestAST.test(input,expect,386))

    def test_387_program(self):
        input="""class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
            func @getNumOfShape() : int {
                return @numOfShape;
            }
        }
        class Shape <- Retangle {
            func getArea() : int {
                return self.length * self.width;
            }
        }
        class Program {
            func main() : void {
                var obj1: Shape = new Shape(1, 4);
                const obj2: Shape;
                obj2 := obj1;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(constructor),[Param(Id(_length),IntType),Param(Id(_width),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(_length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(_width))])),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(FieldAccess(Id(@numOfShape)))]))]),ClassDecl(Id(Retangle),Id(Shape),[MethodDecl(Id(getArea),[],IntType,Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(obj1),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(4)])),ConstDecl(Id(obj2),ClassType(Id(Shape)),None),AssignStmt(Id(obj2),Id(obj1))]))])])"
        self.assertTrue(TestAST.test(input,expect,387))

    def test_388_program(self):
        input="""class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
            func @getNumOfShape() : int {
                return @numOfShape;
            }
        }
        class Shape <- Retangle {
            func getArea() : int {
                return self.length * self.width;
            }
        }
        class Program {
            func main() : void {
                var obj1: Shape = new Shape(1, 4);
                const obj2: Shape;
                obj2 := obj1;
                obj2.length := 2;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[AttributeDecl(VarDecl(Id(@numOfShape),IntType,IntLit(0))),AttributeDecl(ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(VarDecl(Id(length),IntType)),AttributeDecl(VarDecl(Id(width),IntType)),MethodDecl(Id(constructor),[Param(Id(_length),IntType),Param(Id(_width),IntType)],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(length)),Id(_length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(_width))])),MethodDecl(Id(@getNumOfShape),[],IntType,Block([Return(FieldAccess(Id(@numOfShape)))]))]),ClassDecl(Id(Retangle),Id(Shape),[MethodDecl(Id(getArea),[],IntType,Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(obj1),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(4)])),ConstDecl(Id(obj2),ClassType(Id(Shape)),None),AssignStmt(Id(obj2),Id(obj1)),AssignStmt(FieldAccess(Id(obj2),Id(length)),IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input,expect,388))


    def test_389_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  abc ^ bvc;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(^,Id(abc),Id(bvc)))]))])])"
        self.assertTrue(TestAST.test(input,expect,389))

    def test_390_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  abc ^ bvc >= 1;
                y := x * 2;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(^,Id(abc),BinaryOp(>=,Id(bvc),IntLit(1)))),AssignStmt(Id(y),BinaryOp(*,Id(x),IntLit(2)))]))])])"
        
        self.assertTrue(TestAST.test(input,expect,390))

    def test_391_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  abc ^ bvc >= 1 * 2 ;
                y := x * 2 + 5;
                z := y / 3;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(^,Id(abc),BinaryOp(>=,Id(bvc),BinaryOp(*,IntLit(1),IntLit(2))))),AssignStmt(Id(y),BinaryOp(+,BinaryOp(*,Id(x),IntLit(2)),IntLit(5))),AssignStmt(Id(z),BinaryOp(/,Id(y),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,391))

    def test_392_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  abc ^ bvc >= 1 * 2  + 9 - 5;
                y := x * 2 + 5;
                z := y / 3;
                t := z % 2;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(^,Id(abc),BinaryOp(>=,Id(bvc),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(9)),IntLit(5))))),AssignStmt(Id(y),BinaryOp(+,BinaryOp(*,Id(x),IntLit(2)),IntLit(5))),AssignStmt(Id(z),BinaryOp(/,Id(y),IntLit(3))),AssignStmt(Id(t),BinaryOp(%,Id(z),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input,expect,392))

    def test_393_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  abc ^ bvc >= 1 * 2  + 9 - 5;
                y := x * 2 + 5;
                z := y / 3;
                t := z % 2;
                u := t == 1;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(^,Id(abc),BinaryOp(>=,Id(bvc),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(9)),IntLit(5))))),AssignStmt(Id(y),BinaryOp(+,BinaryOp(*,Id(x),IntLit(2)),IntLit(5))),AssignStmt(Id(z),BinaryOp(/,Id(y),IntLit(3))),AssignStmt(Id(t),BinaryOp(%,Id(z),IntLit(2))),AssignStmt(Id(u),BinaryOp(==,Id(t),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input,expect,393))
    
    def test_394_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  abc ^ bvc >= 1 * 2  + 9 - !5 ;
                y := !x * 2 + 5;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(^,Id(abc),BinaryOp(>=,Id(bvc),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(9)),UnaryOp(!,IntLit(5)))))),AssignStmt(Id(y),BinaryOp(+,BinaryOp(*,UnaryOp(!,Id(x)),IntLit(2)),IntLit(5)))]))])])"
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_395_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  -y;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),UnaryOp(-,Id(y)))]))])])"
        self.assertTrue(TestAST.test(input,expect,395))

    def test_396_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  -y;
                y := -b - c;
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),UnaryOp(-,Id(y))),AssignStmt(Id(y),BinaryOp(-,UnaryOp(-,Id(b)),Id(c)))]))])])"
        self.assertTrue(TestAST.test(input,expect,396))

    def test_397_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  a[1];
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),ArrayCell(Id(a),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input,expect,397))

    def test_398_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  a[1] + b[2];
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(+,ArrayCell(Id(a),IntLit(1)),ArrayCell(Id(b),IntLit(2))))]))])])"
        self.assertTrue(TestAST.test(input,expect,398))
    
    def test_399_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  a[1] + b[2] - c[3];
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(-,BinaryOp(+,ArrayCell(Id(a),IntLit(1)),ArrayCell(Id(b),IntLit(2))),ArrayCell(Id(c),IntLit(3))))]))])])"
        self.assertTrue(TestAST.test(input,expect,399))

    def test_400_program(self):
        input="""class Shape {
            func @getNumOfShape() : int {
                x :=  a[1] + b[2] - c[3] * d[4];
            }
        }"""
        expect="Program([ClassDecl(Id(Shape),[MethodDecl(Id(@getNumOfShape),[],IntType,Block([AssignStmt(Id(x),BinaryOp(-,BinaryOp(+,ArrayCell(Id(a),IntLit(1)),ArrayCell(Id(b),IntLit(2))),BinaryOp(*,ArrayCell(Id(c),IntLit(3)),ArrayCell(Id(d),IntLit(4)))))]))])])"
        self.assertTrue(TestAST.test(input,expect,400))
    






        
        
        
        

        
        
        
        
        
        
    
        

        
        
        
        
        

        
        
            
        
    
       
        
        
        
        
   