.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static square(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static addBy1(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static minusBy1(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	isub
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static diff(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fsub
	invokestatic MPClass/isPositive(F)Z
	ifle Label2
	fload_0
	fload_1
	fsub
	freturn
	goto Label3
Label2:
	fload_1
	fload_0
	fsub
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static isPositive(F)Z
.var 0 is n F from Label0 to Label1
Label0:
	fload_0
	iconst_0
	i2f
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is difference F from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iload_1
	invokestatic MPClass/addBy1(I)I
	invokestatic MPClass/square(I)I
	i2f
	iload_1
	invokestatic MPClass/minusBy1(I)I
	invokestatic MPClass/square(I)I
	i2f
	invokestatic MPClass/diff(FF)F
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
	fload_2
	invokestatic MPClass/isPositive(F)Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 2
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
