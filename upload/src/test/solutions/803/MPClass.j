.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 6
	istore_1
	iload_1
	iconst_5
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_1
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	ifle Label6
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	goto Label7
Label6:
	iload_1
	iconst_1
	isub
	invokestatic io/putInt(I)V
Label7:
Label1:
	return
.limit stack 6
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
