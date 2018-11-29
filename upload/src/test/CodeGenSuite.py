import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin putInt(100); end"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    #
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
    #
    # def test_float_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[FloatLiteral(5.5)])])])
    # 	expect = "5.5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,502))
    #
    # def test_string_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putString"),[StringLiteral("oh wao")])])])
    # 	expect = "oh wao"
    # 	self.assertTrue(TestCodeGen.test(input,expect,503))
    #
    # def test_bool_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BooleanLiteral('True')])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,504))
    #
    # def test_biop_int(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp('+',IntLiteral(1),IntLiteral(2))])])])
    # 	expect = "3"
    # 	self.assertTrue(TestCodeGen.test(input,expect,505))
    #
    # def test_biop_2(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('+',FloatLiteral(1.2),FloatLiteral(1.2))])])])
    # 	expect = "2.4"
    # 	self.assertTrue(TestCodeGen.test(input,expect,506))
    #
    # def test_biop_3(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp('-',IntLiteral(5),IntLiteral(2))])])])
    # 	expect = "3"
    # 	self.assertTrue(TestCodeGen.test(input,expect,507))
    #
    # def test_biop_4(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('-',FloatLiteral(1.2),FloatLiteral(0.2))])])])
    # 	expect = "1.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,508))
    #
    # def test_biop_5(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('+',IntLiteral(1),FloatLiteral(0.2))])])])
    # 	expect = "1.2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,509))
    #
    # def test_biop_6(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('+',FloatLiteral(1.2),IntLiteral(1))])])])
    # 	expect = "2.2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,510))
    #
    # def test_biop_7(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp('*',IntLiteral(2),IntLiteral(1))])])])
    # 	expect = "2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,511))
    #
    # def test_biop_8(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('*',FloatLiteral(1.2),FloatLiteral(1.1))])])])
    # 	expect = "1.32"
    # 	self.assertTrue(TestCodeGen.test(input,expect,512))
    #
    # def test_biop_9(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('*',IntLiteral(1),FloatLiteral(1.1))])])])
    # 	expect = "1.1"
    # 	self.assertTrue(TestCodeGen.test(input,expect,513))
    #
    # def test_biop_10(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('+',FloatLiteral(1.1),IntLiteral(1))])])])
    # 	expect = "2.1"
    # 	self.assertTrue(TestCodeGen.test(input,expect,514))
    #
    # def test_biop_11(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('/',IntLiteral(5),IntLiteral(1))])])])
    # 	expect = "5.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,515))

    # def test_biop_12(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('/',FloatLiteral(5.0),IntLiteral(1))])])])
    # 	expect = "5.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,516))
    #
    # def test_biop_13(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp('/',FloatLiteral(5.0),FloatLiteral(1.0))])])])
    # 	expect = "5.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,517))
    #
    # def test_biop_14(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('and',BooleanLiteral('true'), BooleanLiteral('true'))])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,518))
    #
    # def test_biop_15(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('or',BooleanLiteral('false'), BooleanLiteral('true'))])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,520))
    #
    # def test_biop_16(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('and',BooleanLiteral('false'), BooleanLiteral('true'))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,521))
    #
    # def test_biop_17(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp('mod',IntLiteral(5), IntLiteral(2))])])])
    # 	expect = "1"
    # 	self.assertTrue(TestCodeGen.test(input,expect,522))

    # def test_biop_18(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp('div',IntLiteral(5), IntLiteral(2))])])])
    # 	expect = "2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,523))
    #
    # def test_biop_19(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('>',IntLiteral(5), IntLiteral(2))])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,524))

    # def test_biop_20(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('<>',IntLiteral(5), IntLiteral(5))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,525))
    #
    # def test_biop_21(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('>',FloatLiteral(5.5), IntLiteral(5))])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,526))
    #
    # def test_biop_22(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('<',FloatLiteral(6.5), FloatLiteral(5.5))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,527))
    #
    # def test_biop_23(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('>=',FloatLiteral(4.5), FloatLiteral(5.5))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,528))
    #
    # def test_biop_24(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('<=',FloatLiteral(6.5), FloatLiteral(5.5))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,529))
    #
    # def test_biop_25(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[BinaryOp('=',FloatLiteral(6.5), FloatLiteral(5.5))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,530))

    # def test_unaryop_1(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[UnaryOp('not', BooleanLiteral('true'))])])])
    # 	expect = "false"
    # 	self.assertTrue(TestCodeGen.test(input,expect,551))
    #
    # def test_unaryop_2(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[UnaryOp('-', IntLiteral(6))])])])
    # 	expect = "-6"
    # 	self.assertTrue(TestCodeGen.test(input,expect,552))
    #
    # def test_unaryop_3(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[UnaryOp('-', FloatLiteral(6.6))])])])
    # 	expect = "-6.6"
    # 	self.assertTrue(TestCodeGen.test(input,expect,553))
    #
    # def test_unaryop_4(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putBool"),[UnaryOp('not', BooleanLiteral('false'))])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,554))

    # def test_assign1(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), FloatType()),
    #                      VarDecl(Id('c'), StringType()),
    # 		FuncDecl(Id("main"),[],[],[
    #             Assign(Id('a'),IntLiteral(5)),
    # 			CallStmt(Id("putInt"),[Id('a')])])])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,601))
    #
    # def test_assign1(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), FloatType()),
    #                      VarDecl(Id('c'), StringType()),
    # 		FuncDecl(Id("main"),[],[],[
    #             Assign(Id('b'),IntLiteral(5)),
    # 			CallStmt(Id("putFloat"),[Id('b')])])])
    # 	expect = "5.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,601))
    #
    # def test_assign2(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), FloatType()),
    #                      VarDecl(Id('c'), StringType()),
    #                      VarDecl(Id('d'), BoolType()),
    # 		FuncDecl(Id("main"),[],[],[
    #             Assign(Id('d'),BooleanLiteral('True')),
    # 			CallStmt(Id("putBool"),[Id('d')])])])
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,602))

    def test_while1(self):
    	input = Program([VarDecl(Id('a'), IntType()),
                         VarDecl(Id('b'), FloatType()),
                         VarDecl(Id('c'), StringType()),
                         VarDecl(Id('d'), BoolType()),
    		FuncDecl(Id("main"),[],[],[Assign(Id('a'),IntLiteral(4)),
                        While(BinaryOp('>',Id('a'), IntLiteral(3)),[Assign(Id('a'), IntLiteral(1))])
            ])])
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,701))

    def test_while2(self):
    	input = Program([VarDecl(Id('a'), IntType()),
                         VarDecl(Id('b'), IntType()),
                         VarDecl(Id('c'), StringType()),
                         VarDecl(Id('d'), BoolType()),
    		FuncDecl(Id("main"),[],[],[Assign(Id('a'),IntLiteral(4)),
                                       Assign(Id('b'), IntLiteral(5)),
                        While(BinaryOp('>',Id('a'), IntLiteral(3)),[Assign(Id('a'), IntLiteral(1)),
                                                                    While(BinaryOp('>',Id('b'),IntLiteral(2)),
                                                                    [Assign(Id('b'), IntLiteral(1))])])
            ])])
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,702))
