import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    #def test_simple_program(self):
       # """Simple program"""
        #input = """program"""
        #expect = "successful"
        #self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_simple_program(self):
        """Simple program"""
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program1(self):
        """Simple program"""
        input = """class A {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program2(self):
        input = """func(){}"""
        expect = "Error on line 1 col 0: func"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program3(self):
        input = """class A {var a: int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program4(self):
        input = """class A {var a, b: int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_simple_program5(self):
        input = """class A {var a, @b, c: int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_simple_program6(self):
        input = """class _A1 {var a, b, c: int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_simple_program7(self):
        input = """class const {var a, b, c: int;}"""
        expect = "Error on line 1 col 6: const"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_simple_program8(self):
        input = """class A {var a: int;
                            func main() : void {} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_simple_program9(self):
        input = """class A {var a: [9]void;}"""
        expect = "Error on line 1 col 19: void"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_simple_program10(self):
        input = """class A {var a: [0]int;}"""
        expect = "Error on line 1 col 17: 0"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_simple_program11(self):
        input = """class A {var a: [9]real;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_simple_program12(self):
        input = """class real {var a: [2]real;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_simple_program13(self):
        input = """class A {var a: [2]float = [1.0, 2.0];}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_simple_program14(self):
        input = """class Shape {
            var @num: [2]int = [1,2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_simple_program15(self):
        input = """class Shape {
            var @num: [2]int = [1,2];
            func main() : void {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_simple_program16(self):
        input = """class Shape {
            var @num: [2]int = [1,2];
            func main() : void {
                return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_simple_program17(self):
        input = """class Shape {
            var @num: [2]int = [56+96, 2];
            func main() : void {
                return;
            }
        }"""
        expect = "Error on line 2 col 34: +"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_simple_program18(self):
        input = """class Shape {
            var num1, num2: int = 5, 6;
            func foo(a,b: int, c: float): int {
                var x, y: int = b, c;
                return a + b;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_simple_program19(self):
        input = """class Shape {
            var num1, num2: int = 5, 6;
            func foo(a,b: int, c: float): int {
                var x, y: int = b, c;
                var @b : int = 5;
                return a + b;
            }
            }"""
        expect = "Error on line 5 col 20: @b"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_simple_program20(self):
        input = """class Shape {
            var num1, num2: int = 5;
            func foo(a,b: int, c: float): int {
                var x, y: int = b, c;
                var b : int = 5;
                return a + b;
            }
            }"""
        expect = "Error on line 2 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_simple_program21(self):
        input = """class Shape {
            var num1: int = 5;
            const @num2: boolean = true;
            func main() : void {
                var num3 : [2]int = ["abc", 2];
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_simple_program22(self):
        input = """class Shape {
            var num1: int = 5;
            const @num2: boolean = true;
            func main() : void {
                var res : int = 5;
                io.write(res);
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    
    def test_simple_program23(self):
        input = """class Shape {
            var num1: int = 5;
            const @num2: boolean = true;
            func main() : void {
                var res : int = 5;
                var @abc : float = 5.0;
                io.write(res);
                return;
            }
            }"""
        expect = "Error on line 6 col 20: @abc"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_simple_program24(self):
        input = """class Shape {
            var ab: string = "abc";
            const @num2: string = "";
            func main() : void {
                var abc : string = "abcdf";

            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))


    def test_simple_program25(self):
        input = """class Shape {
             func constructor() {
                return;

             }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_simple_program26(self):
        input = """class Shape {
             func constructor() {}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_simple_program27(self):
        input = """class Shape {
             func constructor(length, width: int, name: string) {
                sefl.length := length;
                self.width := width;
                self.name := name;
                return;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_simple_program28(self):
        input = """class Shape {
            func main () : void {
                self.length();
                return;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    
    def test_simple_program29(self):
        input = """class Shape {
            func main () : void {
                const num : [0]int ;
            }
            }"""
        expect = "Error on line 3 col 29: 0"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_simple_program30(self):
        input = """class Shape {
            func main () : void {
                const num : [2]int = [[1,2],[3,4]];
            }
            }"""
        expect = "Error on line 3 col 38: ["
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_simple_program31(self):
        input = """class Shape {
            func getName() : string {
                return self.name;
            }

            func main() : void {
                if j > 0 {j := j + 1;}
                else {j := j - 1;}

            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_simple_program32(self):
        input = """class Shape {
            func getName() : string {
                return self.name;
            }

            func main() : void {
                if j > 0 {j := j + 1;}
                else {j := j - 1;}

                sefl.getName();

            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_simple_program33(self):
        input = """class Shape {
            func getName() : string {
                return self.name;
            }

            func main() : void {
                if j > 0 {j := j + 1;}
                else {j := j - 1;}

                getName();

            }

            }"""
        expect = "Error on line 10 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_simple_program34(self):
        input = """class Shape {
            func getName() : string {
                return self.name;
            }

            func main() : void {
                Shape.width := 5;
                x := Shape.@height;

            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_simple_program35(self):
        input = """class Shape {
            func getName() : string {
                return self.name;
            }

            func main() : void {
                Shape.width := 5;
                x := Shape.@height;
                Shape.@height := 6;
                Shape.@width := 6;
                @name := "abc";

            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_simple_program36(self):
        input = """class Shape {
            func getName() : string {
                return self.name;
            }

            func main() : void {
                Shape.width := 5;
                x := Shape.@height;
                Shape.@height := 6;
                Shape.@width := 6;
                name := "abc";
                (a+b).@name := "abc";

            }

            }"""
        expect = "Error on line 12 col 22: @name"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_simple_program37(self):
        input = """class Shape {
            
            func main() : void {
                Shape.width := self.width;
                Shape.@height := self.height;
                Shape.@length := self.length;

                Shape.volume := Shape.width * Shape.@height * Shape.@length;

                var d : int = Shape.volume;
            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_simple_program38(self):
        input = """class Shape {
            
            func main() : void {
                io.@readStr();
                io.@readInt();
            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_simple_program39(self):
        input = """class Shape {
            
            func main() : void {
                a := (b+c).name;
            }

            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_simple_program40(self):
        input = """class Shape {
            
            func main(@a, @b: int) : void {
                return;
            }"""
        expect = "Error on line 3 col 22: @a"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_simple_program41(self):
        input = """class Shape {
            
            func main(a, b: int) : void {
                a := Shape.@height ;
                Shape.@width(@length);
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test_simple_program42(self):
        input = """class Shape {
            
            func main(a, b: int) : void {
                a := Shape.@height ;
                b := Shape.@width(a,b);
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_simple_program43(self):

        input = """class Shape {
            
            func main(a, b: int) : void {
                a := (Shape.@height).name() ;
                b := Shape.@width(a,b);
                Shape.@length(a,b,c);
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_simple_program44(self):
        input = """class Shape {
            
            func main(a, b: int) : void {
                a := (Shape.@height).@name ;
                b := Shape.@width(a,b);
                Shape.@length(a,b,c);
                Shape.@height := 5;
            }
            }"""
        expect = "Error on line 4 col 37: @name"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_simple_program45(self):
        input = """class Shape {
            
            func main(a, b: int) : void {
                Shape.area := Shape.@width * Shape.@length;
                a := Shape.area;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_simple_program45(self):
        input = """class Shape {
            
            func main(a, b: int) : void {
                Shape.area := Shape.@width * Shape.@length;
                a := Shape.area;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    
    def test_simple_program46(self):
        input = """class Shape {
            
            func @A(a, b: int) : void {
                a := new Shape();
                return;
            }

            }"""


        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))


    def test_simple_program47(self):
        input = """class Shape {
            
            func @A(a, b: int) : void {
                new Shape().x();
                return;
            }

            }"""


        
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))


    def test_simple_program48(self):
        input = """class Example {
            var @a: int = 0;
            const b: int = 1;
            func @getA() : int {
                return new Example().a;
                /* Return @a; */
            }
        }
        class Program {
            func main() : void {
                var res1: int = Example.@getA() + Example.b;
                var res2: int = Example.b + Example.@getA();
                io.println(res1 + res2);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_simple_program49(self):
        input = """class Program {
            var @a: string = "Hello World";
            func main() : void {
                var b: int = 100000000;
                bcd := Program.@abc().dex()+ 1;

                
                return (b - self.@a + self.what - Program.@abc(Program.@ab).dex());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_simple_program50(self):
        input = """class Program {
            func main() : void {
                a := g != ((b * c / d % e) > f);
                b := ((abc ^ def) ^ ghi).upper();
                c := 1 || true && false;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_simple_program51(self):
        input = """class Program {
            func main() : void {
                d := -1 + -2 + -30;
                g := str1 ^ str2.str3;
                c := !true + -!2;
            }
        }"""
        expect = "Error on line 5 col 30: !"
        
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_simple_program52(self):
        input = """class Program {
            func main() : void {
                d := -1 + -2 + -30;
                g := str1 ^ str2.str3;
                c := !true + -2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_simple_program53(self):
        input = """class Program {
            func main() : void{
                a := a[a.b] + c[a.@b];
                f := true && false && true || false ^ e;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_simple_program54(self):
        input = """class Program {
             var a: int = a.b().c.@d;
        }"""
        expect = "Error on line 2 col 34: @d"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_simple_program55(self):
        input = """class Program {
            var @a: string = a.@b.c();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_simple_program56(self):
        input = """class Program {
            func main() : void {
                new X().@abc();
            }
        }"""
        expect = "Error on line 3 col 24: @abc"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_simple_program57(self):

        input = """class Program {
            func main() : void {
                new X().abc();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_simple_program58(self):
        input = """class Program {
            func main() : void {
                a := b.(new C());
            }
        }"""

        expect = "Error on line 3 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 259))
    
    def test_simple_program59(self):
        input = """class Program {
            func main() : void {
                a := b.(new C()).d();
            }
        }"""

        expect = "Error on line 3 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_simple_program60(self):
        input = """class Shape {
            var length, width: int;
            func constructor(_length, _width: int){
                self.length := _length;
                self.width := _width;
            }
        }
        class Program {
            func main() : void {
                var obj: Shape = new Shape(1, 4);
            }
        }"""
         
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_simple_program61(self):
        input = """class Program {
            var @a: [3]int = [1, 2, 3];
            func main() : void {
                a[1] := 4;
                var b: int = 10;
                const c: float = 2.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_simple_program62(self):
        input = """class Program {
            func main() : void {
                _123.@_456 := 1 + 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_simple_program63(self):
        input = """class Program {
            func main() : void {
                a.@b.c(e: int).f = a.@b.c() - a.b().c;
            }
        }"""
        expect = "Error on line 3 col 24: :"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_simple_program64(self):
        input = """class Shape {
            func @methodA() : int {
                return self.@A;
            }
        }
        class Program {
            func main() : void {
                var a: int = Shape.@methodA();
                io.writeln(a);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_simple_program65(self):
        input = """class _program {
            var @a: int = 1000;
            func @methodA() : int {
                return self.@a;
            }
        }
        class Program {
            func main() : void {
                var b: int;
                b := _program.@methodA();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_simple_program66(self):
        input = """class _Program {
            func @getMethodA() : int {
                return self.@A;
            }
            func @setMethodA(_a: [2]int) : void {
               sefl.@A := _a;
            }
        }
        class Program {
            func main() : void {
                _Program.@setMethodA(arr);
                io.writeln(_Program.@getMethodA());
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_simple_program67(self):
        input = """class Program {
            func main() : void {
                a := _1a2b3c.@d();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_simple_program68(self):
        input = """class Program1 {
            const a: int = self.function(1, str1 ^ str2,);
        }"""
        expect = "Error on line 2 col 56: )"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_simple_program69(self):
        input = """class Program {
            var a, b: int;
            if {i := 1;} j := 2 {
             // do something
            }
        }"""
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_simple_program70(self):
        input = """class Program {
            func main() : void {
                var a, b: int = 1, 2;
                if {a := -b;} b > a {
                    io.@writeStr("a is smaller than b");
                }
                else {
                    io.@writeStr("a is not smaller than b");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_simple_program71(self):
        input = """class Program {
            func main() : void {
                var a: int = 1;
                var b: float = 2.0;
                if a < b {
                    io.@writeStr("a is smaller than b");
                }
                else  {
                    io.@writeStr("a is equal to b");
                }
                
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_simple_program72(self):
        input = """class Program {
            func main() : void {
                if a > b > c {
                    io.@writeStr("1");
                }
                if a > b < c {
                    io.@writeStr("2");
                }
                if a < b > c {
                    io.@writeStr("3");
                }
                if a < b < c {
                    io.@writeStr("4");
                }
                else {
                    io.@writeStr("5");
                }
            }
        }"""
        expect = "Error on line 3 col 25: >"
        self.assertTrue(TestParser.test(input, expect, 273))


    def test_simple_program73(self):
        input = """class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    io.@writeInt(i);
                    if i % 2 == 0 {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                for i := 5; i > 2; i := i - 1 {
                    io.@writeInt(arr[i]);
                    if x % 5 == 0 {
                        return self.@a;
                    }
                }
            }
        }"""
        expect = "successful";
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_simple_program74(self):
        input = """class Program {
            func main() : void {
                for self.i := n-100; self.i < n+100; self.i := self.i + 1 {
                    io.@writeInt(self.i);
                }
            }
        }"""
        expect = "successful";
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_simple_program75(self):
        input = """class Program {
            func main() : void {
                for i := true; i < 10; i := i + 1 {
                    a[i] := i;
                    io.@writeInt(a[i]);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    def test_simple_program76(self):
        input = """class Program {
            func main() : void {
                break;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_simple_program77(self):
        input = """class Program {
            func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    if i == 5 {
                        break a;
                    }
                }
            }
        }"""
        expect = "Error on line 5 col 30: a"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_simple_program78(self):
        input = """class Program {
            func main() : void {
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_simple_program79(self):
        input = """class Program {
           func main() : void {
                for i := 0; i < 10; i := i + 1 {
                    if i == 5 {
                        continue a;
                    }
                }
            }
        }"""
        expect = "Error on line 5 col 33: a"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_simple_program80(self):
        input = """class Program {
            Shape.@getNumOfShape();
        }"""
        expect =  "Error on line 2 col 12: Shape"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_simple_program81(self):
        input = """class Program {
            func main() : void {
            
                for self.fun := 0; self.fun < 10; self.fun := self.fun + 1 {
                    io.@writeInt(self.fun);
                }
                for a._var := 0; a._var < 10; a._var := a._var + 1 {
                    io.@writeInt(a._var);
                }
                for self.a._var := 0; self.a._var < 10; self.a._var := self.a._var + 1 {
                    io.@writeInt(self.a._var);
                }
                for sefl.fun().b := 0; sefl.fun().b < 10; sefl.fun().b := sefl.fun().b + 1 {    
                    io.@writeInt(sefl.fun().b);
                }
                for a.@b := 0; a.@b < 10; a.@b := a.@b + 1 {
                    io.@writeInt(a.@b);
                }
                for self.@a.b.c := 0; self.@a.b.c < 10; self.@a.b.c := self.@a.b.c + 1 {
                    io.@writeInt(self.@a.b.c);
                }
                for self.@a().b.c := 0; self.@a().b.c < 10; self.@a().b.c := self.@a().b.c + 1 {
                    io.@writeInt(self.@a().b.c);
                }

            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_simple_program82(self):
        input = """class Program {
            func main() : void {
                for Program.@a[9]._val := 0; Program.@a[9]._val < 10; Program.@a[9]._val := Program.@a[9]._val + 1 {
                    io.@writeInt(Program.@a[9]._val);
                }
            }
        }"""
        expect = "Error on line 3 col 58: ."
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test_simple_program83(self):
        input = """class Program {
            func main() : void {
                for Program.a.@b := 0; Program.a.@b < 10; Program.a.@b := Program.a.@b + 1 {
                    io.@writeInt(Program.a.@b);
                }
            }
        }"""
        expect = "Error on line 3 col 30: @b"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_simple_program84(self):
        input = """class IOString {
            func __init__() : void {
                self.s := "";
            }
            func getString() : void {
                self.s := io.@readStr();
            }
            func printString() : void {
                io.@writeStr(s.upper());
            }
        }
        class Program {
            func main() : void {
                var strObj: string = new IOString();
                strObj.getString();
                strObj.printString();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_simple_program85(self):
        input = """class Program {
            func main() : void {
                var c, h: int = 50, 30;
                var d: int = Math.hh(io.@readStr("Enter D: "));
                var Q: int = Math.hh(2 * c * d / h);
                io.@writeStr(Math.round(Math.sqrt(Q)));
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_simple_program86(self):
        input = """class Program {
        }
        class Shape {
        }
        class Circle <- Shape {
        }
        class Rectangle <- Shape {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_simple_program87(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
               a[3+x.foo(2)] := a[b[2]] + 3;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_simple_program88(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
               x.b[2] := x.m()[3];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    
    def test_simple_program89(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
            var r, s :int; 
            r := 2;
            var a, b: [5]int;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test_simple_program90(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
            var r, s :int; 
            r := 2;
            var a, b: [5]int;
            a := b;
            a[0] := s;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_simple_program91(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
                self.aPi := 3.14;
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_simple_program92(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
                self.aPi := 3.14;
                value := x.foo(5);
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_simple_program93(self):
        input = """class Program {
        }
        class Shape {
            func main() : void {
                self.aPi := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_simple_program94(self):
        input = """class Program {
        }
        class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 1;
            var length, width: int; 
            func @getNumOfShape() : int {
                return @numOfShape;
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_simple_program95(self):
        input = """class Program {
        }
        class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 1;
            var length, width: int; 
            func @getNumOfShape() : int {
                return @numOfShape;
            }
            func @setNumOfShape(_numOfShape: int) : void {
                @numOfShape := _numOfShape;
            }
        }
        class Shape <- Rectangle {
            func @getArea() : int {
                return self.length * self.width;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_simple_program96(self):
        input = """class Program {
            func main() : void {
                io.@writeInt(Shape.@getNumOfShape());
            }
        }
        class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 1;
            var length, width: int; 
            func @getNumOfShape() : int {
                return @numOfShape;
            }
            func @setNumOfShape(_numOfShape: int) : void {
                @numOfShape := _numOfShape;
            }
        }
        class Shape <- Rectangle {
            func @getArea() : int {
                return self.length * self.width;
            }
        }
        class Rectangle <- Shape {
            func @getArea() : int {
                return self.length * self.width;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_simple_program97(self):
        input = """class Program{var  a, b, c, d: int = 3, 4, 6;}"""
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_simple_program98(self):
        input = """class Program {func @main():int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_simple_program99(self):
        input = 	"""class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_simple_program100(self):
        input = """class Program {
            func @main():int {
                Number[9].name := "Nine";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))




















    

    








    


    





