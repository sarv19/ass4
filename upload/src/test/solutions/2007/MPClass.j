.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static min(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_1
	ireturn
Label4:
	iload_0
	ireturn
Label5:
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static mausochung(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is x I from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
	iload_0
	iload_1
	invokestatic MPClass/min(II)I
	istore_2
	iconst_2
	istore_3
	iload_3
	iconst_1
	isub
	istore_3
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iload_2
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_0
	iload_3
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_1
	iload_3
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	ifle Label10
	goto Label3
	goto Label11
Label10:
Label11:
	goto Label2
Label3:
	iload_3
	ireturn
Label1:
.limit stack 8
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 121
	bipush 66
	invokestatic MPClass/mausochung(II)I
	invokestatic io/putInt(I)V
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
