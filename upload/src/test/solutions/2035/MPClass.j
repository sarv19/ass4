.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static power(II)F
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	i2f
	freturn
Label4:
	iload_1
	iconst_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iload_0
	iload_1
	iconst_1
	iadd
	invokestatic MPClass/power(II)F
	iconst_1
	i2f
	iload_0
	i2f
	fdiv
	fmul
	freturn
Label8:
	iload_0
	i2f
	iload_0
	iload_1
	iconst_1
	isub
	invokestatic MPClass/power(II)F
	fmul
	freturn
Label9:
Label5:
Label1:
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	iconst_2
	invokestatic MPClass/power(II)F
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
