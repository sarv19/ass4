.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static checkEven(I)Z
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	getstatic MPClass/a I
	iconst_2
	iadd
	putstatic MPClass/a I
	iconst_1
	ireturn
Label4:
	getstatic MPClass/a I
	iconst_2
	imul
	putstatic MPClass/a I
	iconst_0
	ireturn
Label5:
Label1:
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass/a I
	getstatic MPClass/a I
	invokestatic MPClass/checkEven(I)Z
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass/a I
	invokestatic io/putIntLn(I)V
	iconst_2
	putstatic MPClass/a I
	getstatic MPClass/a I
	invokestatic MPClass/checkEven(I)Z
	invokestatic io/putBoolLn(Z)V
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
