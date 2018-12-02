.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static square(I)V
.var 0 is a I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "fail"
	invokestatic io/putString(Ljava/lang/String;)V
	return
	goto Label5
Label4:
Label5:
	iconst_1
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
	iload_0
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
	iconst_1
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iload_0
	iconst_2
	isub
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_1
	istore_2
	iload_2
	iconst_1
	isub
	istore_2
Label14:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iload_0
	iconst_2
	isub
	if_icmpgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label14
Label15:
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
	invokestatic io/putLn()V
	goto Label10
Label11:
	iconst_1
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
Label18:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iload_0
	if_icmpgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label19
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label18
Label19:
Label1:
	return
.limit stack 11
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	invokestatic MPClass/square(I)V
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
