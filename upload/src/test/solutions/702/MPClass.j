.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c Ljava/lang/String;
.field static d Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	putstatic MPClass/a I
	iconst_5
	putstatic MPClass/b I
	iconst_1
	putstatic MPClass/a I
	iconst_1
	putstatic MPClass/b I
Label6:
	getstatic MPClass/b I
	iconst_2
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	goto Label6
Label7:
Label2:
	getstatic MPClass/a I
	iconst_3
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	goto Label2
Label3:
Label1:
	return
.limit stack 5
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
