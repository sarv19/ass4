.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static isPrime(I)Z
.var 0 is n I from Label0 to Label1
.var 1 is flag Z from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_0
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifle Label6
	iconst_0
	ireturn
	goto Label7
Label6:
Label7:
	iload_0
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iload_0
	iconst_3
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	ifle Label12
	iconst_1
	ireturn
	goto Label13
Label12:
Label13:
	iconst_1
	istore_1
	iconst_2
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
	idiv
	if_icmpgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
	iload_0
	iload_0
	iload_2
	idiv
	iload_2
	imul
	isub
	iconst_0
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	iconst_0
	istore_1
	goto Label15
	goto Label21
Label20:
Label21:
	goto Label14
Label15:
	iload_1
	ireturn
Label1:
.limit stack 17
.limit locals 3
.end method

.method public static prime(I)V
.var 0 is a I from Label0 to Label1
.var 1 is i I from Label0 to Label1
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
	iload_0
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	invokestatic MPClass/isPrime(I)Z
	ifle Label6
	iload_1
	invokestatic io/putIntLn(I)V
	goto Label7
Label6:
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 20
	invokestatic MPClass/prime(I)V
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
