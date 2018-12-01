.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	putstatic MPClass/a I
Label2:
.var 2 is a I from Label2 to Label3
	iload_1
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
	getstatic MPClass/a I
	iload_1
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
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
