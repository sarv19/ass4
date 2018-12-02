.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static power(II)I
.var 0 is x I from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_3
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
	iload_1
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_3
	iload_0
	imul
	istore_3
	goto Label2
Label3:
	iload_3
	ireturn
Label1:
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_4
	invokestatic MPClass/power(II)I
	invokestatic io/putInt(I)V
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
