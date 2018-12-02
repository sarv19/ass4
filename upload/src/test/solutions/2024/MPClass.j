.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is i Z from Label0 to Label1
.var 3 is n Z from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_1
	istore_2
	iload_2
	iconst_1
	isub
	istore_2
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	bipush 20
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_1
	istore_3
	iload_3
	iconst_1
	isub
	istore_3
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	bipush 10
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_1
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	istore_1
	goto Label6
Label7:
	iload_1
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	istore_1
	goto Label2
Label3:
	iload_1
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 12
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
