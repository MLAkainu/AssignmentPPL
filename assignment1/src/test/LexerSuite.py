import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    
    def test_identifier_1(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    
    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("BDC","BDC,<EOF>",102))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("aCBbdc ads","aCBbdc,ads,<EOF>",103))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.test("aCBbdc234","aCBbdc234,<EOF>",104))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("aCBbdc_234","aCBbdc_234,<EOF>",105))

    def test_identifier_6(self):
        self.assertTrue(TestLexer.test("_aCBbdc_234","_aCBbdc_234,<EOF>",106))

    def test_identifier_7(self):
        self.assertTrue(TestLexer.test("@aCBbdc_234","@aCBbdc_234,<EOF>",107))
    
    def test_identifier_8(self):
        self.assertTrue(TestLexer.test("@" ,"Error Token @",108))
    
    def test_identifier_9(self):
        self.assertTrue(TestLexer.test("@___" ,"@___,<EOF>",109))

    def test_identifier_10(self):
        self.assertTrue(TestLexer.test("_ minhloc _minhloc" , "_,minhloc,_minhloc,<EOF>",110))

    def test_identifier_11(self):
        self.assertTrue(TestLexer.test("_Kmh hjk@","_Kmh,hjk,Error Token @",111))

    def test_identifier_12(self):
        self.assertTrue(TestLexer.test(",Hdn",",,Hdn,<EOF>",112))
    
    def test_identifier_13(self):
        self.assertTrue(TestLexer.test(".Khg?",".,Khg,Error Token ?",113))

    def test_identifier_14(self):
        self.assertTrue(TestLexer.test("123a345 123 123a","123,a345,123,123,a,<EOF>",114))

    def test_identifier_15(self):
        input = "123a123 0 687 99aa9aaa"
        expect = "123,a123,0,687,99,aa9aaa,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,115))

    def test_keywords(self):
        input = """break continue if else for true false int float bool string 
        return null class constructor var self new void const func"""

        self.assertTrue(TestLexer.test(input,"break,continue,if,else,for,true,false,int,float,bool,string,return,null,class,constructor,var,self,new,void,const,func,<EOF>",116))

    def test_separators(self):
        input = """()[].,;:{}"""
        self.assertTrue(TestLexer.test(input,"(,),[,],.,,,;,:,{,},<EOF>",117))

    def test_operators(self):
        input = """+ - * / \ ! && || == = != < <= > >= := ^ new %"""
        self.assertTrue(TestLexer.test(input,"+,-,*,/,\,!,&&,||,==,=,!=,<,<=,>,>=,:=,^,new,%,<EOF>",118))

    def test_intlit(self):
        input = "123 0 123456789 000"
        self.assertTrue(TestLexer.test(input,"123,0,123456789,0,0,0,<EOF>",119))

    def test_floatlit(self):
        input = "9.0"
        self.assertTrue(TestLexer.test(input,"9.0,<EOF>",120))

    def test_floatlit_1(self):
        input = "0.0"
        self.assertTrue(TestLexer.test(input,"0.0,<EOF>",121))

    def test_floatlit_2(self):
        input = "12e8"
        self.assertTrue(TestLexer.test(input,"12e8,<EOF>",122))

    def test_floatlit_3(self):
        input = "1."
        self.assertTrue(TestLexer.test(input,"1.,<EOF>",123))

    def test_floatlit_4(self):
        input = ".1"
        self.assertTrue(TestLexer.test(input,".,1,<EOF>",124))
    
    def test_floatlit_5(self):
        input = "0.33E-3"
        self.assertTrue(TestLexer.test(input,"0.33E-3,<EOF>",125))

    def test_floatlit_6(self):
        input = "0.33E"
        self.assertTrue(TestLexer.test(input,"0.33,E,<EOF>",126))

    def test_floatlit_7(self):
        input = "0.33E-"
        self.assertTrue(TestLexer.test(input,"0.33,E,-,<EOF>",127))

    def test_floatlit_8(self):
        input = "0.33E-3.3"
        self.assertTrue(TestLexer.test(input,"0.33E-3,.,3,<EOF>",128))

    def test_floatlit_9(self):
        input = "0.33E-3.3E-3"
        self.assertTrue(TestLexer.test(input,"0.33E-3,.,3E-3,<EOF>",129))

    def test_bool(self):
        input = "true false"
        self.assertTrue(TestLexer.test(input,"true,false,<EOF>",130))

    def test_boolit2 (self):
        input = "TrueFalse" 
        self.assertTrue(TestLexer.test(input,"TrueFalse,<EOF>",131))

    def test_boolit3 (self):
        input = "truefalse"
        self.assertTrue(TestLexer.test(input,"truefalse,<EOF>",132))

    def test_array(self):
        input = "[1,2,3]"
        self.assertTrue(TestLexer.test(input,"[,1,,,2,,,3,],<EOF>",133))

    def test_stringlit (self):
        input = """ "abc" """
        self.assertTrue(TestLexer.test(input,"abc,<EOF>",134))

    def test_stringlit2 (self):
        input = """ "A string literal has a type of string." """
        self.assertTrue(TestLexer.test(input,"A string literal has a type of string.,<EOF>",135))

    def test_stringlit3 (self):
        input = """ "He asked me: \\"Where is John?\\"" """
        expect = """He asked me: \\"Where is John?\\",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,136))

    def test_stringlit4 (self):
        input = """ "This is a string containing tab \t" """
        expect = """This is a string containing tab \t,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,137))

    def test_unclose_string (self):
        self.assertTrue(TestLexer.test("""\"This is an unclosed string""", "Unclosed String: This is an unclosed string", 138))

    def test_illgal_escape (self):
        self.assertTrue(TestLexer.test(""" "This is an illegal escape \k" """, "Illegal Escape In String: This is an illegal escape \k", 139))

    def test_illgal_escape2 (self):
        self.assertTrue(TestLexer.test(""" "This is an illegal escape \\'" """, "Illegal Escape In String: This is an illegal escape \\'", 140))

    def test_stringlit5 (self):
        input = """ "abc\\n def" """
        expect = """abc\\n def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_stringlit6 (self):
        input = """ "abc\\b def" """
        expect = """abc\\b def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_stringlit7 (self):
        input = """ "abc\\r def" """
        expect = """abc\\r def,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_illgal_escape3 (self):
        self.assertTrue(TestLexer.test(""" "abc\\~ def" """, "Illegal Escape In String: abc\\~", 144))

    def test_stringlit8 (self):
        self.assertTrue(TestLexer.test(""" "abc\t" """, """abc\t,<EOF>""", 145))

    def test_stringlit9 (self):
        self.assertTrue(TestLexer.test(""" "abc\b" """, """abc\b,<EOF>""", 146))

    def test_unclose_string2 (self):
        input = """ "hjhasdfasdk\n" """
        expect = """Unclosed String: hjhasdfasdk"""
        self.assertTrue(TestLexer.test(input,expect,147))

    def test_unclose_string3 (self):
        input = """ "hjhasdfasdk\r" """
        expect = """Unclosed String: hjhasdfasdk"""
        self.assertTrue(TestLexer.test(input,expect,148))

    def test_comment1 (self):
        input = """//This is a comment\n"""
        self.assertTrue(TestLexer.test(input,"<EOF>",149))

    def test_comment2 (self):
        input = "//This is a comment\n"
        self.assertTrue(TestLexer.test(input,"<EOF>",150))

    def test_comment3 (self):
        input = "//This is a comment\n//This is a comment"
        self.assertTrue(TestLexer.test(input,"<EOF>",151))

    def test_comment4 (self):
        input = "/*This is a comment*/"
        self.assertTrue(TestLexer.test(input,"<EOF>",152))

    def test_comment5 (self):
        input = "/*This is a comment*/\n"
        self.assertTrue(TestLexer.test(input,"<EOF>",153))

    def test_comment6 (self):
        input = "/*This is a comment*/12ban/*This is a comment*/"
        self.assertTrue(TestLexer.test(input,"12,ban,<EOF>",154))

    def test_comment7 (self):
        input = "/*This is a block comment so // has no meaning here*/"
        self.assertTrue(TestLexer.test(input,"<EOF>",155))

    def test_comment8 (self):
        input = "// This is a line comment /*This is a block comment"
        self.assertTrue(TestLexer.test(input,"<EOF>",156))

    def test_stringlit10 (self):
        self.assertTrue(TestLexer.test(""" "abvc\bcd" """, """abvc\bcd,<EOF>""", 157)) 

    def test_statement1 (self):
        input = """if {i := 1;} j > i {j := j - 1;} else {j := j + 1;}"""
        self.assertTrue(TestLexer.test(input,"if,{,i,:=,1,;,},j,>,i,{,j,:=,j,-,1,;,},else,{,j,:=,j,+,1,;,},<EOF>",158))

    def test_statement2 (self):
        input = """for i := 0; i < 10; i := i + 1 {io.@writeInt(i);}"""
        self.assertTrue(TestLexer.test(input,"for,i,:=,0,;,i,<,10,;,i,:=,i,+,1,{,io,.,@writeInt,(,i,),;,},<EOF>",159))

    def test_statement3 (self):
        input = "self.aPi := 3.14;"
        self.assertTrue(TestLexer.test(input,"self,.,aPi,:=,3.14,;,<EOF>",160))

    def test_statement4 (self):
        input = "value := x.foo(5);"
        self.assertTrue(TestLexer.test(input,"value,:=,x,.,foo,(,5,),;,<EOF>",161))

    def test_statement (self):
        input = "i<3u"
        self.assertTrue(TestLexer.test(input,"i,<,3,u,<EOF>",162))

    def test_statement5 (self):
        input = "#adjadajasdj"
        self.assertTrue(TestLexer.test(input,"Error Token #",163))

    def test_floatlit10 (self):
        input = "12e-10"
        self.assertTrue(TestLexer.test(input,"12e-10,<EOF>",164))

    def test_floatlit11 (self):
        input = "12e10"
        self.assertTrue(TestLexer.test(input,"12e10,<EOF>",165))
    def test_illgal_escape4 (self):
        self.assertTrue(TestLexer.test(""" ",cxvbcvb\\12" """, """Illegal Escape In String: ,cxvbcvb\\1""", 166))

    def test_statement6 (self):
        input = "const MyPi = 3.14;"
        self.assertTrue(TestLexer.test(input,"const,MyPi,=,3.14,;,<EOF>",167))

    def test_statement7 (self):
        input = "class A { }"
        self.assertTrue(TestLexer.test(input,"class,A,{,},<EOF>",168))

    def test_statement8 (self):
        input = """class A { }
                    class B <- A { }"""
        self.assertTrue(TestLexer.test(input,"class,A,{,},class,B,<-,A,{,},<EOF>",169))

    def test_statement9 (self):
        input = """class A {
                    func constructor()
         }
                    class B <- A { }"""
        self.assertTrue(TestLexer.test(input,"class,A,{,func,constructor,(,),},class,B,<-,A,{,},<EOF>",170))

    def test_stringlit11 (self):
        input = """ "hehe \f " """
        self.assertTrue(TestLexer.test(input,"hehe \f ,<EOF>",171))

    def test_illgal_escape5 (self):
        input =  """ \"\\!asdgqwetrew\" """
        self.assertTrue(TestLexer.test(input,"Illegal Escape In String: \\!",172))

    def test_illgal_escape6 (self):
        input =  """ \'kjajasdkj\" """
        self.assertTrue(TestLexer.test(input,"Error Token '",173))

    def test_illgal_escape7 (self):
        input = """ adasdas \"**aasd2244+\\^ def\" """
        self.assertTrue(TestLexer.test(input,"adasdas,Illegal Escape In String: **aasd2244+\\^",174))

    def test_unclose_string4 (self):
        input = """ abc \" def """
        self.assertTrue(TestLexer.test(input,"abc,Unclosed String:  def ",175))

    def test_unclose_string5 (self):
        input = """aa = "Hello \n world !";"""
        self.assertTrue(TestLexer.test(input,"aa,=,Unclosed String: Hello ",176))

    def test_unclose_string6 (self):
        input = """a= "No one said: " Hello " \n ";"""
        expect = """a,=,No one said: ,Hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input,expect,177))

    def test_unclose_string7 (self):
        input = """<">"""
        expect = """<,Unclosed String: >"""
        self.assertTrue(TestLexer.test(input,expect,178))

    def test_unclose_string8 (self):
        input = """ {/*"*/*"}*/*"""
        expect = """{,*,Unclosed String: }*/*"""
        self.assertTrue(TestLexer.test(input,expect,179))

    def test_unclose_string9 (self):
        input = """aasdas"-a)
                    " """
        expect = """aasdas,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(input,expect,180))
    

    def test_illgal_escape8 (self):
        input = """ "abc\\x" """
        expect = """Illegal Escape In String: abc\\x"""
        self.assertTrue(TestLexer.test(input,expect,181))

    def test_illgal_escape9 (self):
        input = """ "\\b\\ " """
        expect = """Illegal Escape In String: \\b\\ """
        self.assertTrue(TestLexer.test(input,expect,182))

    def test_illgal_escape10 (self):
        input = """ "\\n\\ " """
        expect = """Illegal Escape In String: \\n\\ """
        self.assertTrue(TestLexer.test(input,expect,183))

    def test_illgal_escape11 (self):
        input = """ "abc\\m" """
        expect = """Illegal Escape In String: abc\\m"""
        self.assertTrue(TestLexer.test(input,expect,184))


    def test_bool_type (self):
        input = "!&&||==!="
        expect = "!,&&,||,==,!=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,185))

    def test_integer (self):
        input = "0.0000000000000000"
        expect = "0.0000000000000000,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,186))

    def test_void_type (self):
        input = "void"
        expect = "void,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,187))

    def test_identifier_16 (self):
        input = "a[1] := 1;"
        expect = "a,[,1,],:=,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,188))

    def test_identifier_17 (self):
        input = ":=:ada:adad=="
        expect = ":=,:,ada,:,adad,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,189))

    def test_identifier_18 (self):
        input = "[;]sdfghsdfgwaDSFGHEWdsfg\t"
        expect = "[,;,],sdfghsdfgwaDSFGHEWdsfg,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,190))

    def test_int (self):
        input = "0x123"
        expect = "0,x123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,191))

    def test_illgal_escape12 (self):
        input = """ "dasd\\a" """
        expect = """Illegal Escape In String: dasd\\a"""
        self.assertTrue(TestLexer.test(input,expect,192))

    def test_int2 (self):
        input = "1....2...3"
        expect = "1.,.,.,.,2.,.,.,3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,193))

    def test_int3 (self):
        input = "1.2.3"
        expect = "1.2,.,3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,194))

    def test_comment9 (self):
        input = """/*This is a comment
               adajkd
                asdasdsad
                asdasdasda */ """


        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,195))

    def test_comment10 (self):
        input = """/*This is a comment
               adajkd
                asdasdsad
                asdasdasda */ 
                456e asdjasjda *
                //This is a comment
                """
        expect = "456,e,asdjasjda,*,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,196))

    def test_identifier_20 (self):
        input = "@$$$"
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input,expect,197))

    def test_identifier_21 (self):
        input = "@_______"
        expect = "@_______,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,198))

    def test_identifier_22 (self):
        input = "@_______ @123 _______"
        expect = "@_______,@123,_______,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,199))

    def test_identifier_end (self):
        input = "123@123"
        expect = "123,@123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,200))
    