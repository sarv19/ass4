.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo(I)I
	imul
	ireturn
Label4:
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
	bipush 101
	invokestatic MPClass/foo(I)I
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
