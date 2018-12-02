.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static sum(I)I
.var 0 is a I from Label0 to Label1
.var 1 is sum I from Label0 to Label1
.var 2 is temp I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
.var 3 is i I from Label2 to Label3
	iconst_1
	istore_3
	iload_3
	iconst_1
	isub
	istore_3
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iload_0
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
.var 4 is n I from Label8 to Label9
	iconst_1
	istore_2
	iconst_1
	istore 4
	iload 4
	iconst_1
	isub
	istore 4
Label10:
	iload 4
	iconst_1
	iadd
	istore 4
	iload 4
	iload_3
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_2
	iload_0
	imul
	istore_2
	goto Label10
Label11:
Label9:
	iload_1
	iload_2
	iadd
	istore_1
	goto Label4
Label5:
Label3:
	iload_1
	ireturn
Label1:
.limit stack 6
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	invokestatic MPClass/sum(I)I
	invokestatic io/putInt(I)V
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
