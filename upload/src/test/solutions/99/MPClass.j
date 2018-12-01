.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label2
	iconst_1
	ifle Label4
	iconst_1
	iconst_0
	ior
	ifle Label6
	iconst_1
	invokestatic io/putInt(I)V
	goto Label7
Label6:
	iconst_2
	invokestatic io/putInt(I)V
Label7:
	goto Label5
Label4:
	iconst_3
	invokestatic io/putInt(I)V
Label5:
	goto Label3
Label2:
	iconst_1
	iconst_0
	iand
	ifle Label8
	iconst_4
	invokestatic io/putInt(I)V
	goto Label9
Label8:
	iconst_5
	invokestatic io/putInt(I)V
Label9:
Label3:
Label1:
	return
.limit stack 8
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
