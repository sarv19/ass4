.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
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
	bipush 9
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_2
	iadd
	istore_1
	iconst_1
	istore_2
	iload_2
	iconst_1
	isub
	istore_2
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iload_1
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label6
Label7:
	invokestatic io/putLn()V
	goto Label2
Label3:
	bipush 9
	istore_1
	iload_1
	iconst_1
	iadd
	istore_1
Label10:
	iload_1
	iconst_1
	isub
	istore_1
	iload_1
	iconst_1
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_1
	istore_2
	iload_2
	iconst_1
	iadd
	istore_2
Label14:
	iload_2
	iconst_1
	isub
	istore_2
	iload_2
	iconst_1
	if_icmplt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
	goto Label14
Label15:
	goto Label10
Label11:
Label1:
	return
.limit stack 9
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
