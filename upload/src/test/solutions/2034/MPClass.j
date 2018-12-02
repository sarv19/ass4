.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static algo(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
	goto Label5
Label4:
Label5:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/algo(I)I
	iload_0
	imul
	ireturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static sum(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
	goto Label5
Label4:
Label5:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/sum(I)I
	iload_0
	iconst_1
	isub
	invokestatic MPClass/algo(I)I
	iload_0
	imul
	iadd
	ireturn
Label1:
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	invokestatic MPClass/sum(I)I
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
