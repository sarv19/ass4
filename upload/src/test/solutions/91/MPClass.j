.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static MaiN([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	dup
	ifeq Label11
	goto Label10
Label10:
	iand
Label11:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 16
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
