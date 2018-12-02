.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static logarit(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ineg
	ireturn
	goto Label5
Label4:
Label5:
	iload_0
	iconst_2
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_1
	iload_0
	iconst_2
	idiv
	invokestatic MPClass/logarit(I)I
	iadd
	ireturn
Label8:
	iconst_0
	ireturn
Label9:
Label1:
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 16
	invokestatic MPClass/logarit(I)I
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
