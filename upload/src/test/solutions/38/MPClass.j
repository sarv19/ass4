.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static toHexadecimal(I)V
.var 0 is n I from Label0 to Label1
.var 1 is quotient I from Label0 to Label1
.var 2 is remainder I from Label0 to Label1
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
	return
	goto Label5
Label4:
Label5:
	iload_0
	bipush 16
	idiv
	istore_1
	iload_0
	bipush 16
	irem
	istore_2
	iload_1
	invokestatic MPClass/toHexadecimal(I)V
	iload_2
	iconst_0
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_2
	bipush 9
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	ifle Label10
	iload_2
	invokestatic io/putInt(I)V
	goto Label11
Label10:
	iload_2
	bipush 10
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	ldc "A"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label15
Label14:
Label15:
	iload_2
	bipush 11
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	ldc "B"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label19
Label18:
Label19:
	iload_2
	bipush 12
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label22
	ldc "C"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label23
Label22:
Label23:
	iload_2
	bipush 13
	if_icmpne Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label26
	ldc "D"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label27
Label26:
Label27:
	iload_2
	bipush 14
	if_icmpne Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label30
	ldc "E"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label31
Label30:
Label31:
	iload_2
	bipush 15
	if_icmpne Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifle Label34
	ldc "F"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label35
Label34:
Label35:
Label11:
Label1:
	return
.limit stack 19
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 1000
	invokestatic MPClass/toHexadecimal(I)V
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
