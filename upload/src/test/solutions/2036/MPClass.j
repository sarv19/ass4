.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static T(I)F
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
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
	goto Label5
Label4:
Label5:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/T(I)F
	iconst_2
	i2f
	fmul
	iload_0
	i2f
	fmul
	freturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static sum(I)F
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
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
	goto Label5
Label4:
Label5:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/T(I)F
	iconst_1
	i2f
	iload_0
	invokestatic MPClass/T(I)F
	fdiv
	fadd
	freturn
Label1:
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	invokestatic MPClass/sum(I)F
	invokestatic io/putFloat(F)V
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
