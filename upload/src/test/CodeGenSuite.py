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
    #
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
    #
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
    #
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
    #
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
    #
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
    # def test_assign3(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), FloatType()),
    #                      VarDecl(Id('c'), StringType()),
    # 		FuncDecl(Id("main"),[],[],[
    #             Assign(Id('b'),IntLiteral(5)),
    # 			CallStmt(Id("putFloat"),[Id('b')])])])
    # 	expect = "5.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,603))
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
    #
    # def test_while1(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), FloatType()),
    #                      VarDecl(Id('c'), StringType()),
    #                      VarDecl(Id('d'), BoolType()),
    # 		FuncDecl(Id("main"),[],[],[Assign(Id('a'),IntLiteral(4)),
    #                     While(BinaryOp('>',Id('a'), IntLiteral(3)),[Assign(Id('a'), IntLiteral(1))])
    #         ])])
    # 	expect = ""
    # 	self.assertTrue(TestCodeGen.test(input,expect,701))
    #
    # def test_while2(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), IntType()),
    #                      VarDecl(Id('c'), StringType()),
    #                      VarDecl(Id('d'), BoolType()),
    # 		FuncDecl(Id("main"),[],[],[Assign(Id('a'),IntLiteral(4)),
    #                                    Assign(Id('b'), IntLiteral(5)),
    #                     While(BinaryOp('>',Id('a'), IntLiteral(3)),[Assign(Id('a'), IntLiteral(1)),
    #                                                                 While(BinaryOp('>',Id('b'),IntLiteral(2)),
    #                                                                 [Assign(Id('b'), IntLiteral(1))])])
    #         ])])
    # 	expect = ""
    # 	self.assertTrue(TestCodeGen.test(input,expect,702))
    #
    # def test_while2(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), IntType()),
    #                      VarDecl(Id('c'), StringType()),
    #                      VarDecl(Id('d'), BoolType()),
    # 		FuncDecl(Id("main"),[],[],[Assign(Id('a'),IntLiteral(4)),
    #                                    Assign(Id('b'), IntLiteral(5)),
    #                     While(BinaryOp('>',Id('a'), IntLiteral(3)),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))])
    #         ])])
    # 	expect = ""
    # 	self.assertTrue(TestCodeGen.test(input,expect,702))
    #
    # def test_if2(self):
    # 	input = Program([VarDecl(Id('a'), IntType()),
    #                      VarDecl(Id('b'), IntType()),
    #                      VarDecl(Id('c'), StringType()),
    #                      VarDecl(Id('d'), BoolType()),
    # 		FuncDecl(Id("main"),[],[],[
    #                     If(BinaryOp('>',IntLiteral(2),IntLiteral(1)),[CallStmt(Id("putInt"),[IntLiteral(5)]),
    #                                                                   CallStmt(Id("putInt"),[IntLiteral(6)])],[])
    #         ])])
    # 	expect = "56"
    # 	self.assertTrue(TestCodeGen.test(input,expect,802))
    #
    # def test_if2(self):
    # 	input = """
    #         procedure main();
    #         var a: integer;
    #         begin
    #             a:=6;
    #             if a>=5 then
    #                 a:=a+1;
    #             putInt(a);
    #         end
    #     """
    # 	expect = "7"
    # 	self.assertTrue(TestCodeGen.test(input,expect,802))
    #
    # def test_if3(self):
    # 	input = """
    #         procedure main();
    #         var a: integer;
    #         begin
    #             a:=6;
    #             if (a>=5) and (a<10) then
    #                 begin
    #                     a:=a+1;
    #                     putInt(a);
    #                 end
    #             else
    #                 putInt(a-1);
    #         end
    #     """
    # 	expect = "7"
    # 	self.assertTrue(TestCodeGen.test(input,expect,803))
    #
    # def test_if4(self):
    # 	input = """
    #         procedure main();
    #         var a: integer;
    #         begin
    #             a:=6;
    #             if (a <> 0) or (a>=-1) then
    #                 begin
    #                     a:=a+1;
    #                     putFloat(a);
    #                 end
    #             else
    #                 putInt(a-1);
    #         end
    #     """
    # 	expect = "7.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,804))
    #
    # def test_if5(self):
    # 	input = """
    #         procedure checkEven(a:integer);
    #             begin
    #                 if a mod 2 = 0 then
    #                     putString("oh yeah");
    #                 else
    #                     putString("no no no");
    #             end
    #
    #         procedure main();
    #         var a: integer;
    #         begin
    #             checkEven(5);
    #             putLn();
    #             checkEven(4);
    #             putLn();
    #             checkEven(100);
    #         end
    #     """
    # 	expect = "no no no\noh yeah\noh yeah"
    # 	self.assertTrue(TestCodeGen.test(input,expect,805))
    #
    # def test_if6(self):
    # 	input = """
    #         var a: integer;
    #
    #         function checkEven(i:integer): boolean;
    #             begin
    #                 if i mod 2 = 0 then
    #                     begin
    #                         a:=a+2;
    #                         return True;
    #                     end
    #                 else
    #                     begin
    #                         a:=a*2;
    #                         return False;
    #                     end
    #             end
    #
    #         procedure main();
    #
    #         begin
    #             a:=1;
    #             putBoolLn(checkEven(a));
    #             putIntLn(a);
    #             a:=2;
    #             putBoolLn(checkEven(a));
    #             putInt(a);
    #         end
    #     """
    # 	expect = "false\n2\ntrue\n4"
    # 	self.assertTrue(TestCodeGen.test(input,expect,806))
    # #
    # def test_for1(self):
    # 	input = """
    #         procedure main();
    #
    #             var a: integer;
    #         begin
    #             for a:= 1 to 5 do
    #                 putFloatLn(7);
    #         end
    #     """
    # 	expect = "7.0\n7.0\n7.0\n7.0\n7.0\n"
    # 	self.assertTrue(TestCodeGen.test(input,expect,901))
    #
    # def test_call_expr1(self):
    # 	input = """
    #         function foo(b:integer):integer;
    #         BEGIN
    #             return b+1;
    #         end
    #
    #         procedure main();
    #             var a: integer;
    #         begin
    #             a:=1;
    #             putInt(foo(1));
    #         end
    #     """
    # 	expect = "2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,1001))

    # def test_call_expr2(self):
    # 	input = """
    #         function increase1(b:integer):integer;
    #         BEGIN
    #             return b+1;
    #         end
    #
    #         function double(b:integer):integer;
    #         BEGIN
    #             return b*2;
    #         end
    #
    #         function half(b:integer):integer;
    #         BEGIN
    #             return b div 2;
    #         end
    #
    #         procedure main();
    #         begin
    #             putInt(increase1(half(increase1(double(5)))));
    #         end
    #     """
    # 	expect = "6"
    # 	self.assertTrue(TestCodeGen.test(input,expect,1002))
    #
    # def test_return1(self):
    # 	input = """
    #         function foo(n:integer):boolean;
    #         begin
    #             if (n = 1) or (n = 0 )then
    #                 return false;
    #             return true;
    #         end
    #
    #         procedure main();
    #         BEGIN
    #             putBool(foo(5));
    #         end
    #     """
    # 	expect = "true"
    # 	self.assertTrue(TestCodeGen.test(input,expect,1101))
    #
    # def test_mixstyle_1(self):
    #     input="""
    #         function power(x:integer;a:integer):integer;
    #                 var i,b: integer;
    #                  begin
    #
    #                      b:=1;
    #                      for i:=1 to a do
    #                         b:=b*x;
    #                      return b;
    #                  end
    #         procedure main();
    #         begin
    #             putInt(power(2,4));
    #         end
    #     """
    #     expect = "16"
    #     self.assertTrue(TestCodeGen.test(input,expect,2001))
    #
    # def test_mixstyle_2(self):
    #     input="""
    #         function log(a:integer;b:integer):integer;
    #             var i:integer;
    #                  begin
    #
    #                     i:=0;
    #                     while (a>1) do
    #                      BEGIN
    #                         if (a mod b <> 0 ) then
    #                             break;
    #                         a:=a+1;
    #                      end
    #                      return a;
    #                  end
    #         procedure main();
    #         begin
    #             putInt(log(27,3));
    #         end
    #     """
    #     expect = "28"
    #     self.assertTrue(TestCodeGen.test(input,expect,2002))
    #
    #
    # def test_mixstyle_3(self):
    #     input="""
    #         procedure square(a:integer);
    #                 var x,y:integer;
    #                  begin
    #
    #                     for x:=1 to a do
    #                         begin
    #                             for y:=1 to a do
    #                                 putString("*");
    #                             putLn();
    #                         end
    #                  end
    #         procedure main();
    #         begin
    #             square(2);
    #         end
    #     """
    #     expect = "**\n**\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2003))
    #
    # def test_mixstyle_4(self):
    #     input="""
    #         procedure answer(a:integer);
    #                  begin
    #                     if (a=0) then
    #                         putString("No");
    #                     else
    #                         putString("Yes");
    #                     putLn();
    #                  end
    #         procedure main();
    #         begin
    #             answer(0);
    #             answer(1);
    #         end
    #     """
    #     expect = "No\nYes\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2004))
    #
    # def test_mixstyle_5(self):
    #     input="""
    #         function dectohex(a:integer):string;
    #                  begin
    #                     if (a=0) then
    #                         return "0";
    #                     else if (a=1) then
    #                         return "1";
    #                     else if (a=2) then
    #                         return "2";
    #                     else if (a=3) then
    #                         return "3";
    #                     else if (a=4) then
    #                         return "4";
    #                     else if (a=5) then
    #                         return "5";
    #                     else if (a=6) then
    #                         return "6";
    #                     else if (a=7) then
    #                         return "7";
    #                     else if (a=8) then
    #                         return "8";
    #                     else if (a=9) then
    #                         return "9";
    #                     else if (a=10) then
    #                         return "A";
    #                     else if (a=11) then
    #                         return "B";
    #                     else if (a=12) then
    #                         return "C";
    #                     else if (a=13) then
    #                         return "D";
    #                     else if (a=14) then
    #                         return "E";
    #                     else return "F";
    #                  end
    #         procedure main();
    #         begin
    #             putString(dectohex(10));
    #         end
    #     """
    #     expect = "A"
    #     self.assertTrue(TestCodeGen.test(input,expect,2005))
    #
    # def test_mixstyle_7(self):
    #     input="""
    #         function min(a:integer;b:integer): integer;
    #         begin
    #             if (a>b) then return b;
    #             else return a;
    #         end
    #
    #         function mausochung(a:integer;b:integer):integer;
    #                 var x,i: integer;
    #                  begin
    #
    #                     x:=min(a,b);
    #                     for i:=2 to x do
    #                         begin
    #                         if (a mod i =0) and (b mod i =0) then break;
    #                         end
    #                     return i;
    #                  end
    #         procedure main();
    #         begin
    #             putInt(mausochung(121,66));
    #         end
    #     """
    #     expect = "11"
    #     self.assertTrue(TestCodeGen.test(input,expect,2007))
    #
    # def test_mixstyle_8(self):
    #     input="""
    #         function round(a:real): integer;
    #         var i: integer;
    #             BEGIN
    #
    #                 i:=0;
    #                 while (i+1<a) do i:=i+1;
    #                 return i;
    #              end
    #         procedure main();
    #         begin
    #             putInt(round(9.5));
    #         end
    #     """
    #     expect = "9"
    #     self.assertTrue(TestCodeGen.test(input,expect,2008))
    #
    # def test_mixstyle_9(self):
    #     input="""
    #         function divide(a:integer;b:integer): real;
    #         begin
    #             return a / b;
    #         end
    #         procedure main();
    #         begin
    #             putFloat(divide(5,2));
    #         end
    #     """
    #     expect = "2.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,2009))
    #
    # def test_mixstyle_10(self):
    #     input="""
    #         function isPrime(n:integer):boolean;
    #                  var flag:boolean;
    #                  i:integer;
    #                  begin
    #                      if (n = 1) or (n = 0 )then
    #                          return False;
    #                      if (n = 2) or (n = 3)  then
    #                          return true;
    #                      flag := true;
    #
    #                      for i:= 2 to (n div 2) do
    #                      begin
    #                          if n - (n div i) * i = 0 then
    #                          begin
    #                              flag := false;
    #                              break;
    #                          end
    #                      end
    #                      return flag;
    #                  end
    #         procedure prime(a:integer);
    #                 var i: integer;
    #                  begin
    #
    #                     for i:=1 to a do
    #                         if isPrime(i) then putIntLn(i);
    #                  end
    #         procedure main();
    #         begin
    #             prime(20);
    #         end
    #     """
    #     expect = "2\n3\n5\n7\n11\n13\n17\n19\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2010))
    #
    # def test_mixstyle_11(self):
    #     input="""
    #         function gtokg(a:integer): real;
    #         var b:real;
    #         begin
    #
    #             b:=a;
    #             return b/1000;
    #         end
    #         procedure main();
    #         begin
    #             putFloat(gtokg(5190));
    #         end
    #     """
    #     expect = "5.19"
    #     self.assertTrue(TestCodeGen.test(input,expect,2011))
    #
    # def test_mixstyle_12(self):
    #     input="""
    #         procedure loop(step:integer;a:integer;b:integer);
    #             BEGIN
    #                 while (a<=b) do
    #                 BEGIN
    #                     putIntLn(a);
    #                     a:=a+step;
    #                 end
    #             end
    #
    #         procedure main();
    #         begin
    #             loop(3,10,20);
    #         end
    #     """
    #     expect = "10\n13\n16\n19\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2012))
    #
    # def test_mixstyle_13(self):
    #     input="""
    #         function percent(a:integer;b:integer): real;
    #             var c,d:real;
    #             begin
    #                 c:=a;
    #                 d:=b;
    #                 return c / d*100;
    #             end
    #
    #         procedure main();
    #         begin
    #             putFloat(percent(3,8));
    #         end
    #     """
    #     expect = "37.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,2013))
    #
    # def test_mixstyle_14(self):
    #     input="""
    #         function xor(a:boolean;b:boolean): boolean;
    #             begin
    #                 return (a and  (not b)) or ((not a) and b);
    #             end
    #
    #         procedure main();
    #         begin
    #             putBoolLn(xor(true,false));
    #             putBoolLn(xor(false,false));
    #         end
    #     """
    #     expect = "true\nfalse\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2014))
    #
    # def test_mixstyle_15(self):
    #     input="""
    #         procedure letterL(a:integer);
    #         var i:integer;
    #         BEGIN
    #             if (a<2) then
    #             begin
    #                 putString("fail");
    #                 return;
    #             end
    #
    #             for i:=1 to a do
    #                 begin
    #                     putString("*");
    #                     putLn();
    #                 end
    #             for i:=1 to a do
    #                 putString("*");
    #         end
    #
    #         procedure main();
    #         begin
    #             letterL(3);
    #         end
    #     """
    #     expect = "*\n*\n*\n***"
    #     self.assertTrue(TestCodeGen.test(input,expect,2015))
    #
    # def test_mixstyle_16(self):
    #     input="""
    #         function distance(xa:integer;ya:integer;x0:integer;y0:integer): real;
    #             begin
    #                 return (xa-x0)*(xa-x0) + (ya-y0)*(ya-y0);
    #             end
    #         function isCircle(xa:integer;ya:integer;x0:integer;y0:integer;r:real): boolean;
    #             BEGIN
    #                 return distance(xa,ya,x0,y0)<= r*r;
    #             end
    #
    #         procedure main();
    #         begin
    #             putBool(isCircle(3,2,0,0,4.5));
    #         end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,2016))
    #
    # def test_mixstyle_17(self):
    #     input="""
    #         procedure letterC(a:integer);
    #         var i:integer;
    #         BEGIN
    #             if (a<3) then
    #             begin
    #                 putString("fail");
    #                 return;
    #             end
    #
    #             for i:=1 to a do
    #                 putString("*");
    #             putLn();
    #             for i:=1 to a do
    #                 begin
    #                     putString("*");
    #                     putLn();
    #                 end
    #             for i:=1 to a do
    #                 putString("*");
    #         end
    #
    #         procedure main();
    #         begin
    #             letterC(2);
    #         end
    #     """
    #     expect = "fail"
    #     self.assertTrue(TestCodeGen.test(input,expect,2017))
    #
    # def test_mixstyle_18(self):
    #     input="""
    #         procedure letterI(a:integer);
    #         var i:integer;
    #         BEGIN
    #
    #             for i:=1 to a do
    #                 begin
    #                     putString("*");
    #                     putLn();
    #                 end
    #         end
    #
    #         procedure main();
    #         begin
    #             letterI(2);
    #         end
    #     """
    #     expect = "*\n*\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2018))
    #
    # def test_mixstyle_19(self):
    #     input="""
    #         procedure square(a:integer);
    #         var i,n:integer;
    #         BEGIN
    #             if (a<2) then
    #             begin
    #                 putString("fail");
    #                 return;
    #             end
    #
    #             for i:=1 to a do
    #                 putString("*");
    #             putLn();
    #             for i:=1 to a-2 do
    #                 begin
    #                     putString("*");
    #                     for n:=1 to a-2 do
    #                         putString(" ");
    #                     putString("*");
    #                     putLn();
    #                 end
    #             for i:=1 to a do
    #                 putString("*");
    #         end
    #
    #         procedure main();
    #         begin
    #             square(3);
    #         end
    #     """
    #     expect = "***\n* *\n***"
    #     self.assertTrue(TestCodeGen.test(input,expect,2019))
    #
    # def test_mixstyle_20(self):
    #     input="""
    #         procedure rec(a:integer;b:integer);
    #         var i,n:integer;
    #         BEGIN
    #             if (a<3) then
    #             begin
    #                 putString("fail");
    #                 return;
    #             end
    #
    #             for i:=1 to a do
    #             begin
    #                 for n:=1 to b do
    #                     putString("*");
    #                 putLn();
    #             end
    #         end
    #
    #         procedure main();
    #         begin
    #             rec(2,3);
    #         end
    #     """
    #     expect = "fail"
    #     self.assertTrue(TestCodeGen.test(input,expect,2020))
    #
    # def test_mixstyle_21(self):
    #     input="""
    #         var pi:real;
    #         function circle_area(a:integer):real;
    #         BEGIN
    #             return pi*a*a;
    #         end
    #
    #         procedure main();
    #         begin
    #             pi:=3.14;
    #             putFloat(circle_area(1));
    #         end
    #     """
    #     expect = "3.14"
    #     self.assertTrue(TestCodeGen.test(input,expect,2021))
    #
    # def test_mixstyle_22(self):
    #     input="""
    #         var pi:real;
    #         function sum(a:integer):integer;
    #         var i,sum: integer;
    #         BEGIN
    #
    #             sum:=0;
    #             for i:=1 to a do
    #                 sum:=sum+i;
    #             return sum;
    #         end
    #
    #         procedure main();
    #         begin
    #             putInt(sum(100));
    #         end
    #     """
    #     expect = "5050"
    #     self.assertTrue(TestCodeGen.test(input,expect,2022))
    #
    # def test_mixstyle_23(self):
    #     input="""
    #         function sum(a:integer):integer;
    #         var sum,temp: integer;
    #         BEGIN
    #
    #             sum:=0;
    #             with i: integer; do
    #                 for i:=1 to a do
    #                     begin
    #                         with n: integer; do
    #                             begin
    #                                 temp:=1;
    #                                 for n:=1 to i do
    #                                     temp:=temp*a;
    #                             end
    #                         sum:=sum+temp;
    #                     end
    #             return sum;
    #         end
    #
    #         procedure main();
    #         begin
    #             putInt(sum(2));
    #         end
    #     """
    #     expect = "6"
    #     self.assertTrue(TestCodeGen.test(input,expect,2023))
    #
    # def test_mixstyle_24(self):
    #     input="""
    #         procedure main();
    #         var a: boolean;
    #          i,n : boolean;
    #         begin
    #
    #             a:=false;
    #
    #             for i:=1 to 20 do
    #             BEGIN
    #                 for n:=1 to 10 do
    #                     a:= not a;
    #                 a:= not a;
    #             end
    #             putBool(a);
    #         end
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,2024))
    #
    # def test_mixstyle_25(self):
    #     input="""
    #         procedure main();
    #         var a:integer;
    #         begin
    #
    #             a:=0;
    #             while (a>=0) do
    #             BEGIN
    #                 a:=a+5;
    #                 with b:real; do
    #                     BEGIN
    #                         b:=a/1.5;
    #                         b:=b*3.3;
    #                         a:=a-6;
    #                     end
    #                 with c:boolean; do
    #                     c:= not false;
    #             end
    #             putInt(a);
    #         end
    #     """
    #     expect = "-1"
    #     self.assertTrue(TestCodeGen.test(input,expect,2025))
    #
    # def test_mixstyle_26(self):
    #     input="""
    #         procedure main();
    #         Var a:integer;
    #         begin
    #
    #             for a:=1 to 1000 do
    #                 BEGIN
    #                     if a<10 then continue;
    #                     if a<15 then putIntLn(a);
    #                     else break;
    #                 end
    #         end
    #     """
    #     expect = "10\n11\n12\n13\n14\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2026))
    #
    # def test_mixstyle_27(self):
    #     input="""
    #         function foo(a: integer): integer;
    #         begin
    #             if a>1 then
    #                 return a+foo(a-1);
    #             else return 1;
    #         end
    #         procedure main();
    #         begin
    #             putInt(foo(5));
    #         end
    #     """
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input,expect,2027))
    #
    # def test_mixstyle_28(self):
    #     input="""
    #         function foo(a: integer): integer;
    #         begin
    #             if a>1 then
    #                 return a*foo(a-1);
    #             else return 0;
    #         end
    #         procedure main();
    #
    #         begin
    #             putInt(foo(101));
    #         end
    #     """
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,2028))
    #
    # def test_mixstyle_29(self):
    #     input="""
    #         function foo(a: integer): real;
    #         begin
    #             if a>1 then
    #                 return a/foo(a-1);
    #             else return 0.5;
    #         end
    #         procedure main();
    #         begin
    #             putfloat(foo(3));
    #         end
    #     """
    #     expect = "0.75"
    #     self.assertTrue(TestCodeGen.test(input,expect,2029))
    #
    # def test_mixstyle_30(self):
    #     input="""
    #         function xor(a:boolean;b:boolean): boolean;
    #         begin
    #             return (a and  (not b)) or ((not a) and b);
    #         end
    #         function foo(a: boolean; i: integer): boolean;
    #         begin
    #             if i>1 then
    #                 return xor(a, foo(a,i-1));
    #             else return false;
    #         end
    #                 procedure main();
    #         begin
    #             putbool(foo(True,3));
    #         end
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,2030))
    #
    # def test_mixstyle_31(self):
    #     input="""
    #         procedure reverse(n: integer);
    #         begin
    #             if n <> 0 then
    #                 begin
    #                     putInt(n mod 10);
    #                     reverse(n div 10);
    #                 end
    #         end
    #
    #         procedure main();
    #         begin
    #             reverse(15);
    #         end
    #     """
    #     expect = "51"
    #     self.assertTrue(TestCodeGen.test(input,expect,2031))
    #
    # def test_mixstyle_32(self):
    #     input="""
    #         function     count(n: integer):integer;
    #         begin
    #             if n = 0 then
    #                 return 0;
    #             return 1+count(n div 10);
    #         end
    #
    #         procedure main();
    #         begin
    #             putInt(count(15112));
    #         end
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,2032))
    #
    # def test_mixstyle_33(self):
    #     input="""
    #         function logarit(n: integer):integer;
    #         begin
    #             if n < 0 then
    #                 return -1;
    #             if n>=2 then
    #                 return 1+logarit(n div 2);
    #             else return 0;
    #         end
    #
    #         procedure main();
    #         begin
    #             putInt(logarit(16));
    #         end
    #     """
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input,expect,2033))
    #
    # def test_mixstyle_34(self):
    #     input="""
    #         function algo(n:integer):integer;
    #         BEGIN
    #             if n=1 then return 1;
    #             return algo(n-1)*n;
    #         end
    #
    #         function sum(n:integer):integer;
    #         begin
    #             if n=1 then return 1;
    #             return sum(n-1) + algo(n-1)*n;
    #         end
    #
    #         procedure main();
    #         begin
    #             putInt(sum(5));
    #         end
    #     """
    #     expect = "153"
    #     self.assertTrue(TestCodeGen.test(input,expect,2034))
    #
    # def test_mixstyle_35(self):
    #     input="""
    #         function power(x,y:integer):real;
    #         BEGIN
    #             if y=0 then return 1;
    #             else
    #                 BEGIN
    #                     if y<0 then return power(x,y+1)*(1/x);
    #                     else
    #                         return x*power(x, y-1);
    #                 end
    #         end
    #
    #
    #         procedure main();
    #         begin
    #             putFloat(power(5,2));
    #         end
    #     """
    #     expect = "25.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,2035))
    #
    # def test_mixstyle_36(self):
    #     input="""
    #         function T(n:integer):real;
    #         BEGIN
    #             if n=0 then return 1;
    #             return T(n-1)*2*n;
    #         end
    #         function sum(n:integer):real;
    #         begin
    #             if n=0 then return 1;
    #             return T(n-1)+1/T(n);
    #         end
    #
    #
    #         procedure main();
    #         begin
    #             putFloat(sum(5));
    #         end
    #     """
    #     expect = "384.00027"
    #     self.assertTrue(TestCodeGen.test(input,expect,2036))

    # def test_mixstyle_37(self):
    #     input="""
    #         function power(x,n:real):real;
    #         BEGIN
    #             if n=1 then return x;
    #             return power(x,n-1)*x;
    #         end
    #
    #         function algo(n:real):real;
    #         begin
    #             if n=1 then return 1;
    #             return algo(n-1)*n;
    #         end
    #
    #         function power_algo(x,n:real):real;
    #         begin
    #             if n=1 then return x;
    #             return power_algo(x, n-1)+((power(x,n-1)*x)/(algo(n-1)*n));
    #         end
    #
    #
    #         procedure main();
    #         begin
    #             putFloat(power_algo(3,10));
    #         end
    #     """
    #     expect = "19.079666"
    #     self.assertTrue(TestCodeGen.test(input,expect,2037))

    # def test_mixstyle_38(self):
    #     input="""
    #         procedure main();
    #         var i,j:integer;
    #         begin
    #             i:=7;
    #             j:=7;
    #             for i:=1 to 7 do
    #                 begin
    #                     for j:=7-i downto 1 do
    #                         putString("*");
    #                         putLn();
    #                 end
    #         end
    #     """
    #     expect = "******\n*****\n****\n***\n**\n*\n\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2038))

    # def test_mixstyle_39(self):
    #     input="""
    #         procedure main();
    #         var i,j, k:integer;
    #         begin
    #             for i:=1 to 7 do
    #                 begin
    #                     for j:=1 to i do
    #                         putInt(j);
    #                     for k:=7-i downto 1 do
    #                         putString("*");
    #                     putLn();
    #                 end
    #         end
    #     """
    #     expect = "1******\n12*****\n123****\n1234***\n12345**\n123456*\n1234567\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,2039))

    def test_mixstyle_40(self):
        input="""
            procedure main();
            var i,j:integer;
            begin
                for i:=1 to 9 do
                    begin
                        i:=i+2;
                        for j:=1 to i do
                            begin
                                putString("*");

                            end
                            putLn();
                    end
                for i:=9 downto 1 do
                    begin
                        for j:=i downto 1 do
                            begin
                                putString("*");
                                putLn();
                            end
                    end
            end
        """
        expect = "1******\n12*****\n123****\n1234***\n12345**\n123456*\n1234567\n"
        self.assertTrue(TestCodeGen.test(input,expect,2040))
