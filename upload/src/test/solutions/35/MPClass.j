.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static swap(FF)V
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is temp F from Label0 to Label1
Label0:
	fload_0
	fstore_2
	fload_1
	fstore_0
	fload_2
	fstore_1
	ldc "Swap successful"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "a = "
	invokestatic io/putString(Ljava/lang/String;)V
	fload_0
	invokestatic io/putFloatLn(F)V
	ldc "b = "
	invokestatic io/putString(Ljava/lang/String;)V
	fload_1
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	bipush 10
	istore_2
	ldc "a = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	i2f
	invokestatic io/putFloatLn(F)V
	ldc "b = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	i2f
	invokestatic io/putFloatLn(F)V
	iload_1
	i2f
	iload_2
	i2f
	invokestatic MPClass/swap(FF)V
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
