.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static checkEven(I)V
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "oh yeah"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label5
Label4:
	ldc "no no no"
	invokestatic io/putString(Ljava/lang/String;)V
Label5:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_5
	invokestatic MPClass/checkEven(I)V
	invokestatic io/putLn()V
	iconst_4
	invokestatic MPClass/checkEven(I)V
	invokestatic io/putLn()V
	bipush 100
	invokestatic MPClass/checkEven(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
