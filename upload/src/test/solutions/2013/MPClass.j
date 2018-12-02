.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static percent(II)F
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
.var 3 is d F from Label0 to Label1
Label0:
	iload_0
	i2f
	fstore_2
	iload_1
	i2f
	fstore_3
	fload_2
	fload_3
	fdiv
	bipush 100
	i2f
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	bipush 8
	invokestatic MPClass/percent(II)F
	invokestatic io/putFloat(F)V
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
