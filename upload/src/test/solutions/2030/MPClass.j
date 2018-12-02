.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static xor(ZZ)Z
.var 0 is a Z from Label0 to Label1
.var 1 is b Z from Label0 to Label1
Label0:
	iload_0
	iload_1
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iand
	iload_0
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_1
	iand
	ior
	ireturn
Label1:
.limit stack 9
.limit locals 2
.end method

.method public static foo(ZI)Z
.var 0 is a Z from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iload_1
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_0
	iload_0
	iload_1
	iconst_1
	isub
	invokestatic MPClass/foo(ZI)Z
	invokestatic MPClass/xor(ZZ)Z
	ireturn
Label4:
	iconst_0
	ireturn
Label5:
Label1:
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_3
	invokestatic MPClass/foo(ZI)Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
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
