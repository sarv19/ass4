.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static round(F)I
.var 0 is a F from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_1
	iadd
	i2f
	fload_0
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	iload_1
	ireturn
Label1:
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 9.5
	invokestatic MPClass/round(F)I
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
