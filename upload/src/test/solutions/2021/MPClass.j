.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static pi F

.method public static circle_area(I)F
.var 0 is a I from Label0 to Label1
Label0:
	getstatic MPClass/pi F
	iload_0
	i2f
	fmul
	iload_0
	i2f
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 3.14
	putstatic MPClass/pi F
	iconst_1
	invokestatic MPClass/circle_area(I)F
	invokestatic io/putFloat(F)V
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
