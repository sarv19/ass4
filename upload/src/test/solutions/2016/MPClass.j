.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static distance(IIII)F
.var 0 is xa I from Label0 to Label1
.var 1 is ya I from Label0 to Label1
.var 2 is x0 I from Label0 to Label1
.var 3 is y0 I from Label0 to Label1
Label0:
	iload_0
	iload_2
	isub
	iload_0
	iload_2
	isub
	imul
	iload_1
	iload_3
	isub
	iload_1
	iload_3
	isub
	imul
	iadd
	i2f
	freturn
Label1:
.limit stack 4
.limit locals 4
.end method

.method public static isCircle(IIIIF)Z
.var 0 is xa I from Label0 to Label1
.var 1 is ya I from Label0 to Label1
.var 2 is x0 I from Label0 to Label1
.var 3 is y0 I from Label0 to Label1
.var 4 is r F from Label0 to Label1
Label0:
	iload_0
	iload_1
	iload_2
	iload_3
	invokestatic MPClass/distance(IIII)F
	fload 4
	fload 4
	fmul
	fcmpl
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 4
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	iconst_2
	iconst_0
	iconst_0
	ldc 4.5
	invokestatic MPClass/isCircle(IIIIF)Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 5
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
