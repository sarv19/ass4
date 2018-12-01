.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	i2f
	putstatic MPClass/a F
Label2:
.var 2 is a F from Label2 to Label3
	iload_1
	i2f
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
Label3:
	getstatic MPClass/a F
	iload_1
	i2f
	fadd
	invokestatic io/putFloat(F)V
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
