.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static foo()V
Label0:
	getstatic MPClass/a I
	iconst_1
	iadd
	putstatic MPClass/a I
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass/a I
Label2:
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
	invokestatic MPClass/foo()V
	iload_1
	invokestatic io/putIntLn(I)V
Label3:
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
