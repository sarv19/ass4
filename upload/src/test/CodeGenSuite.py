import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):


    # def test_with_1(self):
    #     """Simple program: int main() {} """
    #     input = """ procedure main();
    #                 begin
    #                     with a:integer; do
    #                         begin
    #                             a := 1;
    #                             putInt(a);
    #                         end
    #                 end"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,22))
    #
    # def test_if_1(self):
    #     """Simple program: int main() {} """
    #     input = """ procedure main();
    #                 var a:integer;
    #                 begin
    #                     a := 2;
    #                     if (a > 1) then
    #                         begin
    #                             a := a + 1;
    #                             putInt(a);
    #
    #                         end
    #                     else
    #                         putInt(a - 1);
    #                 end"""
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,23))
    #
    # def test_int2float_1(self):
    #     """Simple program: int main() {} """
    #     input = """ procedure main();
    #
    #                 begin
    #                     putFloat(1);
    #                 end"""
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,24))
    #
    # def test_while_1(self):
    #     """Simple program: int main() {} """
    #     input = """ procedure main();
    #                 var a:integer;
    #                 begin
    #                     a := 0;
    #                     while (a < 10) do
    #                         a := a + 1;
    #
    #                     putInt(a);
    #                 end"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,25))
    #
    # def test_while_2(self):
    #     """Simple program: int main() {} """
    #     input = """ procedure main();
    #                 var a:integer;
    #                 begin
    #                     a := 0;
    #                     while (a < 10) do
    #                         begin
    #                             if (a = 5) then break;
    #                             a := a + 1;
    #                         end
    #
    #                     putInt(a);
    #                 end"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,26))
    #
    # def test_for_1(self):
    #     """Simple program: int main() {} """
    #     input = """ procedure main();
    #                 var a,b:integer;
    #                 begin
    #                     for a := 0 to 5 do
    #                         b := 1;
    #                     putInt(a);
    #                 end"""
    #     expect = "6"
    #     self.assertTrue(TestCodeGen.test(input,expect,27))
    #
    #
    # def test_call_expr_1(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                 procedure main();
    #                 begin
    #                     foo(1);
    #                 end
    #
    #                 procedure foo(b:integer);
    #                 begin
    #                     return;
    #                 end"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,28))

    def test_and_1(self):
        """Simple program: int main() {} """
        input = """
                    procedure main();
                    begin
                        putBool(true and then false and then foo());
                    end

                    function foo():boolean;
                    begin
                        putInt(1);
                        return true;
                    end
                    """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,29))

    # def test_float_3(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                 procedure main();
    #                 var a:integer; b:real;
    #                 begin
    #                     b := 2.2;
    #                     putFloat(b);
    #                 end
    #                 """
    #     expect = "2.2"
    #     self.assertTrue(TestCodeGen.test(input,expect,30))

#     def test_fibonacci(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     begin
#                         putInt(fibonacci(5));
#                     end
#
#                     function fibonacci(n:integer):integer;
#                     begin
#                         if ((n = 0) or (n = 1)) then return 1;
#
#                         return n + fibonacci(n - 1);
#                     end
#                     """
#         expect = "15"
#         self.assertTrue(TestCodeGen.test(input,expect,31))
#
#     def test_hanoiTower(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure towerOfHanoi(n : integer; start_disk : string; desination_disk : string; auxiliary_disk : string);
#                     begin
#                         if (n = 1) (* If only has 1 disk left *)
#                             then
#                                 begin
#                                     putString("Move 1 disk from ");
#                                     putString(start_disk);
#                                     putString(" to ");
#                                     putStringLn(desination_disk);
#                                     return;
#                                 end
#
#                         towerOfHanoi(n - 1, start_disk, auxiliary_disk, desination_disk);
#
#                         putString("Move 1 disk from ");
#                         putString(start_disk);
#                         putString(" to ");
#                         putStringLn(desination_disk);
#
#                         towerOfHanoi(n - 1, auxiliary_disk, desination_disk, start_disk);
#                     end
#
#
#                     procedure main();
#                     begin
#                         towerOfHanoi(3, "A", "C", "B");
#                     end
#                     """
#         expect = """Move 1 disk from A to C
# Move 1 disk from A to B
# Move 1 disk from C to B
# Move 1 disk from A to C
# Move 1 disk from B to A
# Move 1 disk from B to C
# Move 1 disk from A to C
# """
#         self.assertTrue(TestCodeGen.test(input,expect,32))
#
#     def test_factorial(self):
#         """Simple program: int main() {} """
#         input = """ function getFactorial(n : integer):integer;
#                     begin
#                         if (n = 1) then return 1;
#
#                         return n * getFactorial(n - 1);
#                     end
#
#                     procedure main();
#                     begin
#                         putInt(getFactorial(5));
#                     end
#                     """
#         expect = "120"
#         self.assertTrue(TestCodeGen.test(input,expect,33))
#
#     def test_random_1(self):
#         """Simple program: int main() {} """
#         input = """ function square(n : integer):integer;
#                     begin return n*n; end
#
#                     function addBy1(n : integer):integer;
#                     begin return n + 1; end
#
#                     function minusBy1(n : integer):integer;
#                     begin return n - 1; end
#
#                     function diff(a: real; b: real ):real;
#                     begin
#                         if isPositive(a - b) then return a - b;
#                         else return b - a;
#                     end
#
#                     function isPositive(n : real):boolean;
#                     begin return n >= 0; end
#
#                     procedure main();
#                     var n:integer; difference:real;
#                     begin
#                         n := 5;
#                         difference := diff(square(addBy1(n)) , square(minusBy1(n)));
#                         putFloatLn(difference);
#                         putBoolLn(isPositive(difference));
#                     end
#                     """
#         expect = """20.0
# true
# """
#         self.assertTrue(TestCodeGen.test(input,expect,34))
#
#     def test_random_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure swap(a,b:real);
#                     var temp:real;
#                     begin
#                         temp := a;
#                         a := b;
#                         b := temp;
#                         putStringLn("Swap successful");
#                         putString("a = "); putFloatLn(a);
#                         putString("b = "); putFloatLn(b);
#                     end
#
#                     procedure main();
#                     var a,b:integer;
#                     begin
#                         a := 5;
#                         b := 10;
#                         putString("a = "); putFloatLn(a);
#                         putString("b = "); putFloatLn(b);
#
#                         swap(a,b);
#                     end
#                     """
#         expect = "a = 5.0\nb = 10.0\nSwap successful\na = 10.0\nb = 5.0\n"
#         self.assertTrue(TestCodeGen.test(input,expect,35))
#
#     def test_with_2(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     begin
#                         putInt(foo());
#                     end
#
#                     function foo():integer;
#                     begin
#                         with a:integer; do
#                             if (2 < 1) then return 1;
#                             else return 2;
#                     end
#                     """
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,36))
#
#     def test_example(self):
#         """Simple program: int main() {} """
#         input = """
#                     var i:integer;
#                     function f():integer;
#                     begin
#                         return 200;
#                     end
#
#                     procedure main();
#                     var main:integer;
#                     begin
#                         main := g := f();
#                         putIntLn(main);
#                         with i:integer; main:integer; f:integer; do
#                             begin
#                                 main := f := i := 100;
#                                 putIntLn(i);
#                                 putIntLn(main);
#                                 putIntLn(f);
#                                 putIntLn(g);
#                             end
#                         putIntLn(main);
#
#                     end
#                     var g:integer;
#                     """
#         expect = "200\n100\n100\n100\n200\n200\n"
#         self.assertTrue(TestCodeGen.test(input,expect,37))
#
#     def test_toHexa(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure toHexadecimal(n : integer);
#                     var quotient, remainder:integer;
#                     begin
#
#                         if (n = 0) then return;
#
#                         quotient := n div 16;
#                         remainder := n mod 16;
#
#                         toHexadecimal(quotient);
#
#                         if (remainder >= 0) and (remainder <= 9) then putInt(remainder);
#                         else
#                             begin
#                                 if remainder = 10 then putString("A");
#                                 if remainder = 11 then putString("B");
#                                 if remainder = 12 then putString("C");
#                                 if remainder = 13 then putString("D");
#                                 if remainder = 14 then putString("E");
#                                 if remainder = 15 then putString("F");
#                             end
#
#                     end
#
#                     procedure main();
#                     begin
#                         toHexadecimal(1000);
#                     end
#                     """
#         expect = "3E8"
#         self.assertTrue(TestCodeGen.test(input,expect,38))
#
#     def test_procedure_recursion(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure print2console(n : integer);
#                     begin
#                         if n = -1 then return;
#                         putInt(n);
#                         print2console(n - 1);
#                         putInt(n);
#                     end
#                     procedure main();
#                     begin
#                         print2console(5);
#                     end
#                     """
#         expect = "543210012345"
#         self.assertTrue(TestCodeGen.test(input,expect,39))
#
#     def test_toBinary(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure toBinary(n : integer);
#                     var quotient, remainder: integer;
#                     begin
#                         if n = 0 then return;
#
#                         quotient := n div 2;
#                         remainder := n mod 2;
#
#                         toBinary(quotient);
#
#                         putInt(remainder);
#                     end
#
#                     procedure main();
#                     begin
#                         toBinary(10);
#                     end
#                     """
#         expect = "1010"
#         self.assertTrue(TestCodeGen.test(input,expect,40))
#
#     def test_var_5(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#
#                     procedure foo();
#                     begin
#                         a := a + 1;
#                     end
#
#                     procedure main();
#                     begin
#                         a := 0;
#                         with a:integer; do
#                             begin
#                                 a := 5;
#                                 foo();
#                                 putIntLn(a);
#                             end
#                         putInt(a);
#                     end
#                     """
#         expect = "5\n1"
#         self.assertTrue(TestCodeGen.test(input,expect,41))
#
#     def test_var_6(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#                     procedure main();
#                     var b:integer;
#                     begin
#                         a := b := 1;
#                         with a:integer; do
#                             begin
#                                 a := b;
#                                 putIntLn(a);
#                             end
#                         putInt(a + b);
#                     end
#                     """
#         expect = "1\n2"
#         self.assertTrue(TestCodeGen.test(input,expect,42))
#
#     def test_var_7(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     var b:integer;
#                     begin
#                         a := b := 1;
#                         with a:integer; do
#                             begin
#                                 a := b;
#                                 putIntLn(a);
#                             end
#                         putInt(a + b);
#                     end
#
#                     var a:integer;
#                     """
#         expect = "1\n2"
#         self.assertTrue(TestCodeGen.test(input,expect,43))
#
#     def test_var_8(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     var b:integer;
#                     begin
#                         a := b := 1;
#                         with a:integer; do
#                             begin
#                                 a := b;
#                                 putIntLn(a);
#                             end
#                         putFloat(a + b);
#                     end
#
#                     var a:real;
#                     """
#         expect = "1\n2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,44))
#
#     def test_var_9(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     var b:integer;
#                     begin
#                         a := b := 1;
#                         with a:real; do
#                             begin
#                                 a := b;
#                                 putFloatLn(a);
#                             end
#                         putInt(a + b);
#                     end
#
#                     var a:integer;
#                     """
#         expect = "1.0\n2"
#         self.assertTrue(TestCodeGen.test(input,expect,45))
#
#     def test_var_10(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     var b:integer;
#                     begin
#                         a := b := 1;
#                         with a:real; do
#                             begin
#                                 a := b;
#                                 putFloatLn(a);
#                             end
#                         putFloat(a + b);
#                     end
#
#                     var a:real;
#                     """
#         expect = "1.0\n2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,46))
#
#     def test_var_11(self):
#         """Simple program: int main() {} """
#         input = """
#                     procedure main();
#                     var b:integer;
#                     begin
#                         a := b := 1;
#                         with a:real; b:integer; c:boolean; do
#                             begin
#                                 b := 2;
#                                 a := b;
#                                 putFloatLn(a + b);
#                             end
#                         putFloat(a + b);
#                     end
#
#                     var a:real;
#                     """
#         expect = "4.0\n2.0"
#         self.assertTrue(TestCodeGen.test(input,expect,47))
#
#     def test_case_insensitive_1(self):
#         """Simple program: int main() {} """
#         input = """ procedure Main();
#                     var a:integer;
#                     begin
#                         foo2();
#                     end
#                     function foo():integer;
#                     begin
#                         return 1;
#                     end
#
#                     procedure foo2();
#                     begin
#                         putInt(1);
#                     end
#                     """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,48))
#
#     def test_random_3(self):
#         """Simple program: int main() {} """
#         input = """ function foo(a :integer): integer;
#                     var b : integer;
#                     begin
#                         return a;
#                     end
#                     procedure main();
#                     var a, b: real;
#                         c: integer;
#                     begin
#                         c := foo(1);
#                         putInt(c);
#                     end
#                     """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,49))
#
#     def test_case_insensitive_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var A:integer;
#                     begin
#                         a := 1;
#                         foo2();
#                     end
#                     function foo():integer;
#                     begin
#                         return 1;
#                     end
#
#                     procedure foo2();
#                     begin
#                         putInt(1);
#                     end
#                     """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,50))
#
#     def test_case_insensitive_3(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var A:integer;
#                     begin
#
#                         foo2(FOO());
#                     end
#                     function foo():integer;
#                     begin
#                         return 1;
#                     end
#
#                     procedure foo2(a : integer);
#                     begin
#                         putInt(1);
#                     end
#                     """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,51))
#
#     def test_orelse_1(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#                     function fooT():boolean;
#                     begin
#                         putIntLn(1);
#                         return false;
#                     end
#
#                     function fooF():boolean;
#                     begin
#                         putIntLn(2);
#                         return true;
#                     end
#
#                     procedure main();
#                     begin
#                         putBool(false or else fooF() or else fooT());
#                     end
#                     """
#         expect = "2\ntrue"
#         self.assertTrue(TestCodeGen.test(input,expect,52))
#
#     def test_orelse_2(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#                     function fooT():boolean;
#                     begin
#                         putIntLn(1);
#                         return false;
#                     end
#
#                     function fooF():boolean;
#                     begin
#                         putIntLn(2);
#                         return true;
#                     end
#
#                     procedure main();
#                     begin
#                         putBool((1 > 0) or else fooT());
#                     end
#                     """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,53))
#
#     def test_and_then_1(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#                     function fooT():boolean;
#                     begin
#                         putIntLn(1);
#                         return false;
#                     end
#
#                     function fooF():boolean;
#                     begin
#                         putIntLn(2);
#                         return true;
#                     end
#
#                     procedure main();
#                     begin
#                         putBool((1 > 0) and then fooT());
#                     end
#                     """
#         expect = "1\nfalse"
#         self.assertTrue(TestCodeGen.test(input,expect,54))
#
#     def test_and_then_2(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#                     function fooT():boolean;
#                     begin
#                         putIntLn(1);
#                         return false;
#                     end
#
#                     function fooF():boolean;
#                     begin
#                         putIntLn(2);
#                         return true;
#                     end
#
#                     procedure main();
#                     begin
#                         putBool((-1 > 0) and then fooF());
#                     end
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,55))
#
#     def test_and_then_3(self):
#         """Simple program: int main() {} """
#         input = """ var a:integer;
#                     function fooT():boolean;
#                     begin
#                         putIntLn(1);
#                         return false;
#                     end
#
#                     function fooF():boolean;
#                     begin
#                         putIntLn(2);
#                         return true;
#                     end
#
#                     procedure main();
#                     begin
#                         putBool((1 > 0 and then 0 >= 1) and then fooF());
#                     end
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,56))
#
#     def test_float_4(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putFLoat(2e3);
#                     end
#                     """
#         expect = "2000.0"
#         self.assertTrue(TestCodeGen.test(input,expect,57))
#
#     def test_float_5(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putFLoat(2e-3);
#                     end
#                     """
#         expect = "0.002"
#         self.assertTrue(TestCodeGen.test(input,expect,58))
#
#     def test_float_6(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putFLoat(2.2e-3);
#                     end
#                     """
#         expect = "0.0022"
#         self.assertTrue(TestCodeGen.test(input,expect,59))
#
#     def test_float_7(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putFLoat(2.122e-3);
#                     end
#                     """
#         expect = "0.002122"
#         self.assertTrue(TestCodeGen.test(input,expect,60))
#
#     def test_float_8(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putFLoat(2.122e3);
#                     end
#                     """
#         expect = "2122.0"
#         self.assertTrue(TestCodeGen.test(input,expect,61))
#
#     def test_integer_1(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putInt(2147483647);
#                     end
#                     """
#         expect = "2147483647"
#         self.assertTrue(TestCodeGen.test(input,expect,62))
#
#     def test_integer_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putInt(-2147483648);
#                     end
#                     """
#         expect = "-2147483648"
#         self.assertTrue(TestCodeGen.test(input,expect,63))
#
#     def test_print_triangle_1(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printTriangle(5);
#                     end
#
#                     procedure printTriangle(height : integer);
#                     var iCounter, jCounter : integer;
#                     begin
#                         for iCounter := 1 to height do
#                             begin
#                                 for jCounter := 1 to iCounter do
#                                 begin
#                                     printStar();
#                                 end
#                                 putLn(); (* print new line *)
#                             end
#
#                     end
#
#                     procedure printStar();
#                     begin
#                         putString("*");
#                     end
#                     """
#         expect = "*\n**\n***\n****\n*****\n"
#         self.assertTrue(TestCodeGen.test(input,expect,64))
#
#     def test_print_triangle_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printTriangle(5);
#                     end
#
#                     procedure printTriangle(height : integer);
#                     var iCounter, jCounter, kCounter : integer;
#                     begin
#                         for iCounter := 1 to height do
#                             begin
#                                 for kCounter := iCounter + 1 to height do printSpace();
#                                 for jCounter := 1 to iCounter do printStar();
#                                 putLn();
#                             end
#
#                     end
#
#                     procedure printStar();
#                     begin
#                         putString("*");
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#                     """
#         expect = "    *\n   **\n  ***\n ****\n*****\n"
#
#         #    *
#         #   **
#         #  ***
#         # ****
#         #*****
#         self.assertTrue(TestCodeGen.test(input,expect,65))
#
#     def test_print_triangle_3(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printTriangle(5);
#                     end
#
#                     procedure printTriangle(height : integer);
#                     var iCounter, jCounter, kCounter : integer;
#                     begin
#                         for iCounter := 1 to height do
#                             begin
#                                 for kCounter := iCounter + 1 to height do printSpace();
#                                 for jCounter := 1 to 2 * iCounter - 1 do printStar();
#                                 putLn();
#                             end
#
#                     end
#
#                     procedure printStar();
#                     begin
#                         putString("*");
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#                     """
#         expect = "    *\n   ***\n  *****\n *******\n*********\n"
#
#         #    *
#         #   ***
#         #  *****
#         # *******
#         #*********
#         self.assertTrue(TestCodeGen.test(input,expect,66))
#
#     def test_print_triangle_4(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printTriangle(5);
#                     end
#
#                     procedure printTriangle(height : integer);
#                     var iCounter, jCounter, kCounter : integer;
#                     begin
#                         for iCounter := 1 to height do
#                             begin
#                                 for kCounter := iCounter + 1 to height do printSpace();
#                                 putInt(getNumberOfHeight(iCounter));
#                                 putLn();
#                             end
#
#                     end
#
#                     function getNumberOfHeight(height : integer):integer;
#                     var sum, iCounter: integer;
#                     begin
#                         sum := 0;
#
#                         for iCounter := height downto 1 do
#                             begin
#                                 sum := sum * 10 + iCounter;
#                             end
#
#                         for iCounter := 2 to height do
#                             begin
#                                 sum := sum * 10 + iCounter;
#                             end
#
#                         return sum;
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#                     """
#         expect = "    1\n   212\n  32123\n 4321234\n543212345\n"
#
#         #    1
#         #   212
#         #  32123
#         # 4321234
#         #543212345
#         self.assertTrue(TestCodeGen.test(input,expect,67))
#
#     def test_print_triangle_5(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printTriangle(5);
#                     end
#
#                     procedure printTriangle(height : integer);
#                     var iCounter, jCounter, kCounter : integer;
#                     begin
#                         for iCounter := 1 to height do
#                             begin
#                                 for kCounter := iCounter + 1 to height do printSpace();
#                                 if (iCounter = 1) or (iCounter = height) then
#                                     begin
#                                         if iCounter = 1 then printStar();
#                                         if iCounter = height then
#                                             for jCounter := 1 to 2*iCounter - 1 do printStar();
#                                         putLn();
#                                     end
#                                 else
#                                     begin
#                                         printStar();
#                                         for jCounter := 1 to 2 * (iCounter - 1) - 1 do printSpace();
#                                         printStar();
#                                         putLn();
#                                     end
#                             end
#
#                     end
#
#                     procedure printStar();
#                     begin
#                         putString("*");
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#                     """
#         expect = "    *\n   * *\n  *   *\n *     *\n*********\n"
#
#         #    *
#         #   * *
#         #  *   *
#         # *     *
#         #*********
#         self.assertTrue(TestCodeGen.test(input,expect,68))
#
#     def test_print_diamond(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printDiamond(7);
#                     end
#
#                     procedure printDiamond(row : integer);
#                     var height, iCounter, jCounter, kCounter : integer;
#                     begin
#                         height := row div 2 + 1;
#
#                         for iCounter := 1 to height do
#                             begin
#                                 for kCounter := iCounter + 1 to height do printSpace();
#                                 for jCounter := 1 to 2 * iCounter - 1 do printStar();
#                                 putLn();
#                             end
#
#                         for iCounter := height - 1 downto 1 do
#                             begin
#                                 for kCounter := iCounter + 1 to height do printSpace();
#                                 for jCounter := 1 to 2 * iCounter - 1 do printStar();
#                                 putLn();
#                             end
#
#                     end
#
#                     procedure printStar();
#                     begin
#                         putString("*");
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#                     """
#         expect = "   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n"
#
#         #    *
#         #   ***
#         #  *****
#         # *******
#         #  *****
#         #   ***
#         #    *
#         self.assertTrue(TestCodeGen.test(input,expect,69))
#
#     def test_print_triangle_6(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         printTriangle(5);
#                     end
#
#                     procedure printTriangle(height : integer);
#                     var iCounter, jCounter, kCounter : integer;
#                     begin
#                         for iCounter := 1 to height do
#                             begin
#                                 for jCounter := height downto iCounter do printStar();
#                                 for kCounter := 1 to 2 * iCounter - 1 do printSpace();
#                                 for jCounter := height downto iCounter do printStar();
#                                 putLn();
#                             end
#
#                     end
#
#                     procedure printStar();
#                     begin
#                         putString("*");
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#                     """
#         expect = "***** *****\n****   ****\n***     ***\n**       **\n*         *\n"
#
#         #***** *****
#         #****   ****
#         #***     ***
#         #**       **
#         #*         *
#
#         self.assertTrue(TestCodeGen.test(input,expect,70))
#
#     def test_pi(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putFLoat(getPi(1000000));
#                     end
#
#                     function getPi(n : integer):real;
#                     var counter:integer; pi : real; sign : integer;
#                     begin
#                         pi := 0;
#                         sign := 1;
#                         for counter := 1 to n do
#                             begin
#                                 pi := pi + (sign*4)/(2*counter - 1);
#                                 sign := sign * (-1);
#                             end
#                         return pi;
#                     end
#                     """
#         expect = "3.1415954"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,71))
#
#
#     def test_toDecimal(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                   begin
#                       putInt(toDecimal(1010));
#                   end
#
#                   function toDecimal(n : integer):integer;
#                   var decimal:integer; remainder : integer; temp: integer; iCounter: integer;
#                   begin
#                       temp := n;
#                       decimal := 0;
#                       iCounter := 0;
#
#                       while (temp <> 0) do
#                           begin
#                               remainder := temp mod 10;
#                               temp := temp div 10;
#                               decimal := decimal + remainder * getPower(2, iCounter);
#                               iCounter := iCounter + 1;
#                           end
#                       return decimal;
#
#                   end
#
#                   function getPower(n : integer; power:integer):integer;
#                   var iCounter: integer; result:integer;
#                   begin
#                       result := 1;
#                       for iCOUNTER := 1 to power do
#                           result := result*n;
#                       return result;
#                   end
#                     """
#         expect = "10"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,72))
#
#     def test_if_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                   begin
#                       putInt(foo());
#                   end
#
#                   function foo():integer;
#                   begin
#                       if (0 > 1 and then 2 > 1) then
#                           return 1;
#                       else return 2;
#                   end
#
#                     """
#         expect = "2"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,73))
#
#     def test_if_3(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                   begin
#                       putInt(foo());
#                   end
#
#                   function foo():integer;
#                   begin
#                       if (1 > 0 or else 1 > 1) then
#                           return 1;
#                       else return 2;
#                   end
#
#                     """
#         expect = "1"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,74))
#
#     def test_if_4(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                   begin
#                       putInt(foo());
#                   end
#
#                   function foo():integer;
#                   begin
#                       if (1 > 0 and then 1 > 1) then
#                           return 1;
#                       else
#                           if (1 > 2 and then 3 > 2) then return 2;
#                           else return 3;
#                   end
#
#                     """
#         expect = "3"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,75))
#
#     def test_add_float_1(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                   begin
#                       putFloat(2.2 - 1.1);
#                   end
#
#                     """
#         expect = "1.1"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,76))
#
#     def test_string_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure mAin();
#                   begin
#                       putString(getString("F"));
#                   end
#
#                   function getString(str : string):string;
#                   begin
#                       return str;
#                   end
#                     """
#         expect = "F"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,77))
#
#     def test_hourglass(self):
#         """Simple program: int main() {} """
#         input = """ procedure mAin();
#                     begin
#                         printDiamond(3);
#                     end
#
#                     procedure printDiamond(height : integer);
#                     var iCounter, jCounter, kCounter : integer;
#                     begin
#                         for iCounter := height downto 1 do
#                             begin
#                                 for kCounter := 1 to height - iCounter do printSpace();
#                                 for jCounter := 1 to 2 * iCOUNTER - 1 do printStar();
#                                 putLn();
#                             end
#                         for iCOunter := 2 to height do
#                             begin
#                                 for kCounter := iCOUNTER + 1 to height do printSpace();
#                                 for jCounter := 1 to 2 * iCounter - 1 do printStar();
#                                 putLn();
#                             end
#                     end
#
#
#                     procedure printStar();
#                     begin
#                         PutString("*");
#                     end
#
#                     procedure printSpace();
#                     begin
#                         putString(" ");
#                     end
#
#                     """
#         expect = "*****\n ***\n  *\n ***\n*****\n"
#
#         #*****
#         # ***
#         #  *
#         # ***
#         #*****
#
#         self.assertTrue(TestCodeGen.test(input,expect,78))
#
#     def test_for_2(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var a:integer;
#                     begin
#                         for a:= 1 to 5 do
#                         begin
#                             continue;
#                         end
#                         putInt(a);
#                     end
#
#                     """
#         expect = "6"
#
#
#         self.assertTrue(TestCodeGen.test(input,expect,79))
#
#     def test_for_3(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var a:integer;
#                     begin
#                         for a:= 1 to 5 do
#                         begin
#                             for a:= 6 to 10 do begin end
#                             continue;
#                         end
#                         putInt(a);
#                     end
#
#                     """
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input,expect,80))
#
#     def test_while_3(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var a:integer;
#                     begin
#                         a:= 1;
#
#                         while a <= 10 do
#                             begin
#                                 a := a + 1;
#                                 continue;
#                             end
#                         putInt(a);
#                     end
#
#                     """
#         expect = "11"
#         self.assertTrue(TestCodeGen.test(input,expect,81))
#
#     def test_while_4(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var a:integer;
#                     begin
#                         a:= 1;
#
#                         while a <= 10 do
#                             begin
#                                 a := a + 1;
#                                 for a := 5 to 12 do continue;
#                                 break;
#                             end
#                         putInt(a);
#                     end
#
#                     """
#         expect = "13"
#         self.assertTrue(TestCodeGen.test(input,expect,82))
#
#     def test_int_8(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putInt(------1);
#                     end
#
#                     """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,83))
#
#     def test_float_9(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putFloat(--------7.8);
#                     end
#
#                     """
#         expect = "7.8"
#         self.assertTrue(TestCodeGen.test(input,expect,84))
#
#     def test_float_10(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putFloat(--1.1---2.2);
#                     end
#
#                     """
#         expect = "-1.1"
#         self.assertTrue(TestCodeGen.test(input,expect,85))
#
#     def test_float_11(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putFloat(--1.1--2.2);
#                     end
#
#                     """
#         expect = "3.3000002"
#         self.assertTrue(TestCodeGen.test(input,expect,86))
#
#     def test_bool_8(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(not not not not not not true);
#                     end
#
#                     """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,87))
#
#     def test_bool_9(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(not not not not not  true);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,88))
#
#     def test_bool_10(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(not not not not false);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,89))
#
#     def test_bool_11(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(not not not not false and true);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,90))
#
#     def test_bool_12(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(not not not not false and THEN true);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,91))
#
#     def test_bool_12(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(not not not not false and THEN true);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,91))
#
#     def test_string_3(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putString("NaNI!? Omae Wa Mou Shindeiru");
#                     end
#
#                     """
#         expect = "NaNI!? Omae Wa Mou Shindeiru"
#         self.assertTrue(TestCodeGen.test(input,expect,92))
#
#     def test_string_3(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putString("NaNI!? Omae Wa Mou Shindeiru");
#                     end
#
#                     """
#         expect = "NaNI!? Omae Wa Mou Shindeiru"
#         self.assertTrue(TestCodeGen.test(input,expect,92))
#
#     def test_printIpv4_address(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putString("IPv4 192.168.1.1 is ");
#                         toIpv4(192,168,1,1);
#                     end
#
#                     procedure toIpv4(addr1, addr2, addr3, addr4:integer);
#                     begin
#                         toBinary(addr1);
#                         putString(".");
#                         toBinary(addr2);
#                         putString(".");
#                         toBinary(addr3);
#                         putString(".");
#                         toBinary(addr4);
#                     end
#
#                     procedure toBinary(n : integer);
#                     var quotient, remainder: integer;
#                     begin
#                         if n = 0 then return;
#
#                         quotient := n div 2;
#                         remainder := n mod 2;
#
#                         toBinary(quotient);
#
#                         putInt(remainder);
#                     end
#
#                     """
#         expect = "IPv4 192.168.1.1 is 11000000.10101000.1.1"
#         self.assertTrue(TestCodeGen.test(input,expect,93))
#
#     def test_float_12(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(1.1 >= 0);
#                     end
#
#                     """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,94))
#
#     def test_float_13(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(1.1 >= 1.1);
#                     end
#
#                     """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,95))
#
#     def test_float_14(self):
#         """Simple program: int main() {} """
#         input = """ pRoceDure MaiN();
#                     begin
#                         putBool(1.1 >= 1.12);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,96))
#
#     def test_float_15(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putBool(1.1 + 2.2 > 3.3);
#                     end
#
#                     """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,97))
#
#     def test_float_16(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         putBool((3.3 - (1.1 + 2.2)) >= 0);
#                     end
#
#                     """
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,98))
#
#     def test_if_5(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     begin
#                         if true then
#                             if true then
#                                 if true or false then
#                                     putInt(1);
#                                 else
#                                     putInt(2);
#                             else
#                                 putInt(3);
#                         else
#                             if true and false then
#                                 putInt(4);
#                             else putInt(5);
#                     end
#
#                     """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,99))
#
#     def test_with_3(self):
#         """Simple program: int main() {} """
#         input = """ procedure main();
#                     var a:integer;
#                     begin
#                         for a := 1 to 10 do
#                             with a : integer; do
#                                 a := 1;
#
#                         putInt(a);
#                     end
#
#                     """
#         expect = "11"
#         self.assertTrue(TestCodeGen.test(input,expect,100))
