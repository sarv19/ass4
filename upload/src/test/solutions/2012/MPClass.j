.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static loop(III)V
.var 0 is step I from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
Label2:
	iload_1
	iload_2
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	invokestatic io/putIntLn(I)V
	iload_1
	iload_0
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	bipush 10
	bipush 20
	invokestatic MPClass/loop(III)V
Label1:
	return
.limit stack 3
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
