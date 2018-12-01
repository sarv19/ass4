.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static toBinary(I)V
.var 0 is n I from Label0 to Label1
.var 1 is quotient I from Label0 to Label1
.var 2 is remainder I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	return
	goto Label5
Label4:
Label5:
	iload_0
	iconst_2
	idiv
	istore_1
	iload_0
	iconst_2
	irem
	istore_2
	iload_1
	invokestatic MPClass/toBinary(I)V
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MPClass/toBinary(I)V
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
