.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static fooT()Z
Label0:
	iconst_1
	invokestatic io/putIntLn(I)V
	iconst_0
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static fooF()Z
Label0:
	iconst_2
	invokestatic io/putIntLn(I)V
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	dup
	ifeq Label9
	goto Label8
Label8:
	iand
Label9:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 6
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