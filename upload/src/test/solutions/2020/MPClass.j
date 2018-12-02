.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static rec(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_3
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
	iload_0
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iconst_1
	istore_3
	iload_3
	iconst_1
	isub
	istore_3
Label10:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iload_1
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label10
Label11:
	invokestatic io/putLn()V
	goto Label6
Label7:
Label1:
	return
.limit stack 7
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_3
	invokestatic MPClass/rec(II)V
Label1:
	return
.limit stack 2
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
