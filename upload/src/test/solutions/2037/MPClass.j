.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static power(FF)F
.var 0 is x F from Label0 to Label1
.var 1 is n F from Label0 to Label1
Label0:
	fload_1
	iconst_1
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_0
	freturn
	goto Label5
Label4:
Label5:
	fload_0
	fload_1
	iconst_1
	i2f
	fsub
	invokestatic MPClass/power(FF)F
	fload_0
	fmul
	freturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static algo(F)F
.var 0 is n F from Label0 to Label1
Label0:
	fload_0
	iconst_1
	i2f
	fcmpl
	ifne Label2
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
	fload_0
	iconst_1
	i2f
	fsub
	invokestatic MPClass/algo(F)F
	fload_0
	fmul
	freturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static power_algo(FF)F
.var 0 is x F from Label0 to Label1
.var 1 is n F from Label0 to Label1
Label0:
	fload_1
	iconst_1
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_0
	freturn
	goto Label5
Label4:
Label5:
	fload_0
	fload_1
	iconst_1
	i2f
	fsub
	invokestatic MPClass/power_algo(FF)F
	fload_0
	fload_1
	iconst_1
	i2f
	fsub
	invokestatic MPClass/power(FF)F
	fload_0
	fmul
	fload_1
	iconst_1
	i2f
	fsub
	invokestatic MPClass/algo(F)F
	fload_1
	fmul
	fdiv
	fadd
	freturn
Label1:
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	i2f
	bipush 10
	i2f
	invokestatic MPClass/power_algo(FF)F
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
