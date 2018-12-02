.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static log(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_2
Label2:
	iload_0
	iconst_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label3
	goto Label9
Label8:
Label9:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label2
Label3:
	iload_0
	ireturn
Label1:
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 27
	iconst_3
	invokestatic MPClass/log(II)I
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
