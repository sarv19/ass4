.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_5
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	bipush 6
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 10
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	goto Label6
Label7:
	goto Label2
	goto Label2
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
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
