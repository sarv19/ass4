.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static reverse(I)V
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	bipush 10
	irem
	invokestatic io/putInt(I)V
	iload_0
	bipush 10
	idiv
	invokestatic MPClass/reverse(I)V
	goto Label5
Label4:
Label5:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 15
	invokestatic MPClass/reverse(I)V
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
