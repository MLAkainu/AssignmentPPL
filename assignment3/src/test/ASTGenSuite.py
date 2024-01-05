import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_1(self):
        input = """
            class A {
                
                func fooo(b:int) : void {
                    var a: int = 1;
                    {
                        var a: int = 1;
                        const c: float = 10.0;
                        /* {
                            var c: int = 1;
                        } */
                        // var c: int = 1;

                    }
                }

                func main() : void {}
                
            }


        """

        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(fooo),[VarDecl(Id(b),IntType)],VoidType,Block([VarDecl(Id(a),IntType,IntLiteral(1)),Block([VarDecl(Id(a),IntType,IntLiteral(1)),ConstDecl(Id(c),FloatType,FloatLiteral(10.0))]))])),MethodDecl(Id(main),[],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,3001))
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))


    def test_class_with_one_decl_program(self):
        input = """
            class a {
                func main() : void {}
                var c:int;
                var c:int;
            }
        
        
        """
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(main),[],VoidType,Block([])),AttributeDecl(VarDecl(Id(c),IntType)),AttributeDecl(VarDecl(Id(c),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,301))
    # def test_simple_program(self):
    #     """Simple program: class main {} """
    #     input = """class main {}"""
    #     expect = str(Program([ClassDecl(Id("main"),[])]))
    #     self.assertTrue(TestAST.test(input,expect,300))

    # def test_class_with_one_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         var a:int;
    #         var b:int;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),
    #         [AttributeDecl(VarDecl(Id("a"),IntType())),
    #          AttributeDecl(VarDecl(Id("b"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,302))
   