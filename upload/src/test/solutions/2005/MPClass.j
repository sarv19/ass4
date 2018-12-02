.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static dectohex(I)Ljava/lang/String;
.var 0 is a I from Label0 to Label1
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
	ldc "0"
	areturn
Label4:
	iload_0
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "1"
	areturn
Label8:
	iload_0
	iconst_2
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	ldc "2"
	areturn
Label12:
	iload_0
	iconst_3
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	ldc "3"
	areturn
Label16:
	iload_0
	iconst_4
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	ldc "4"
	areturn
Label20:
	iload_0
	iconst_5
	if_icmpne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label24
	ldc "5"
	areturn
Label24:
	iload_0
	bipush 6
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label28
	ldc "6"
	areturn
Label28:
	iload_0
	bipush 7
	if_icmpne Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifle Label32
	ldc "7"
	areturn
Label32:
	iload_0
	bipush 8
	if_icmpne Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	ifle Label36
	ldc "8"
	areturn
Label36:
	iload_0
	bipush 9
	if_icmpne Label38
	iconst_1
	goto Label39
Label38:
	iconst_0
Label39:
	ifle Label40
	ldc "9"
	areturn
Label40:
	iload_0
	bipush 10
	if_icmpne Label42
	iconst_1
	goto Label43
Label42:
	iconst_0
Label43:
	ifle Label44
	ldc "A"
	areturn
Label44:
	iload_0
	bipush 11
	if_icmpne Label46
	iconst_1
	goto Label47
Label46:
	iconst_0
Label47:
	ifle Label48
	ldc "B"
	areturn
Label48:
	iload_0
	bipush 12
	if_icmpne Label50
	iconst_1
	goto Label51
Label50:
	iconst_0
Label51:
	ifle Label52
	ldc "C"
	areturn
Label52:
	iload_0
	bipush 13
	if_icmpne Label54
	iconst_1
	goto Label55
Label54:
	iconst_0
Label55:
	ifle Label56
	ldc "D"
	areturn
Label56:
	iload_0
	bipush 14
	if_icmpne Label58
	iconst_1
	goto Label59
Label58:
	iconst_0
Label59:
	ifle Label60
	ldc "E"
	areturn
Label60:
	ldc "F"
	areturn
Label61:
Label57:
Label53:
Label49:
Label45:
Label41:
Label37:
Label33:
Label29:
Label25:
Label21:
Label17:
Label13:
Label9:
Label5:
Label1:
.limit stack 31
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MPClass/dectohex(I)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
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
