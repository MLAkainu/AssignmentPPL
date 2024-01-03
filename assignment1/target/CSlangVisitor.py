# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_declarelist.
    def visitClass_declarelist(self, ctx:CSlangParser.Class_declarelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_declare.
    def visitClass_declare(self, ctx:CSlangParser.Class_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#name_class.
    def visitName_class(self, ctx:CSlangParser.Name_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#name_superclass.
    def visitName_superclass(self, ctx:CSlangParser.Name_superclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#body_class_list.
    def visitBody_class_list(self, ctx:CSlangParser.Body_class_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#body_class_prime.
    def visitBody_class_prime(self, ctx:CSlangParser.Body_class_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#body_class.
    def visitBody_class(self, ctx:CSlangParser.Body_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_declare.
    def visitAttribute_declare(self, ctx:CSlangParser.Attribute_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attdecl_.
    def visitAttdecl_(self, ctx:CSlangParser.Attdecl_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#indenlist.
    def visitIndenlist(self, ctx:CSlangParser.IndenlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attdecl.
    def visitAttdecl(self, ctx:CSlangParser.AttdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#varlist.
    def visitVarlist(self, ctx:CSlangParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#type_att.
    def visitType_att(self, ctx:CSlangParser.Type_attContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primitive_type.
    def visitPrimitive_type(self, ctx:CSlangParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primitive_type_.
    def visitPrimitive_type_(self, ctx:CSlangParser.Primitive_type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_type.
    def visitArray_type(self, ctx:CSlangParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#element_type.
    def visitElement_type(self, ctx:CSlangParser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_type.
    def visitClass_type(self, ctx:CSlangParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_declare.
    def visitMethod_declare(self, ctx:CSlangParser.Method_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramlist.
    def visitParamlist(self, ctx:CSlangParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramprime.
    def visitParamprime(self, ctx:CSlangParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#idlist.
    def visitIdlist(self, ctx:CSlangParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#type_return.
    def visitType_return(self, ctx:CSlangParser.Type_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructor_declare.
    def visitConstructor_declare(self, ctx:CSlangParser.Constructor_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#blockstmt.
    def visitBlockstmt(self, ctx:CSlangParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmtlist.
    def visitStmtlist(self, ctx:CSlangParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmtprime.
    def visitStmtprime(self, ctx:CSlangParser.StmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#var_and_const_declstmt.
    def visitVar_and_const_declstmt(self, ctx:CSlangParser.Var_and_const_declstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#varstmt_decl.
    def visitVarstmt_decl(self, ctx:CSlangParser.Varstmt_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#variable_namelist.
    def visitVariable_namelist(self, ctx:CSlangParser.Variable_namelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#varstmt_declass.
    def visitVarstmt_declass(self, ctx:CSlangParser.Varstmt_declassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:CSlangParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_lhs.
    def visitAssign_lhs(self, ctx:CSlangParser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#index_exp_for_scalar_variable.
    def visitIndex_exp_for_scalar_variable(self, ctx:CSlangParser.Index_exp_for_scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_stmt.
    def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignstmt.
    def visitAssignstmt(self, ctx:CSlangParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_stmt.
    def visitFor_stmt(self, ctx:CSlangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSlangParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSlangParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSlangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_invocation_stmt.
    def visitMethod_invocation_stmt(self, ctx:CSlangParser.Method_invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_invocation.
    def visitMethod_invocation(self, ctx:CSlangParser.Method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_method_invocation.
    def visitStatic_method_invocation(self, ctx:CSlangParser.Static_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#name_class_access.
    def visitName_class_access(self, ctx:CSlangParser.Name_class_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instance_method_invocation.
    def visitInstance_method_invocation(self, ctx:CSlangParser.Instance_method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#pre_exp.
    def visitPre_exp(self, ctx:CSlangParser.Pre_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#funcall.
    def visitFuncall(self, ctx:CSlangParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#static_funcall.
    def visitStatic_funcall(self, ctx:CSlangParser.Static_funcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operands.
    def visitOperands(self, ctx:CSlangParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literals.
    def visitLiterals(self, ctx:CSlangParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal_array.
    def visitLiteral_array(self, ctx:CSlangParser.Literal_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#boolean_literal.
    def visitBoolean_literal(self, ctx:CSlangParser.Boolean_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_literal.
    def visitArray_literal(self, ctx:CSlangParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#litarray_list.
    def visitLitarray_list(self, ctx:CSlangParser.Litarray_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp_list.
    def visitExp_list(self, ctx:CSlangParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#index_operator.
    def visitIndex_operator(self, ctx:CSlangParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attribute_name.
    def visitAttribute_name(self, ctx:CSlangParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#identifier_name.
    def visitIdentifier_name(self, ctx:CSlangParser.Identifier_nameContext):
        return self.visitChildren(ctx)



del CSlangParser