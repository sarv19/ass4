.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_0
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_5
	iadd
	istore_1
Label6:
.var 2 is b F from Label6 to Label7
	iload_1
	i2f
	ldc 1.5
	fdiv
	fstore_2
	fload_2
	ldc 3.3
	fmul
	fstore_2
	iload_1
	bipush 6
	isub
	istore_1
Label7:
Label8:
.var 3 is c Z from Label8 to Label9
	iconst_0
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	istore_3
Label9:
	goto Label2
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
.limit locals 4
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
