.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static towerOfHanoi(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
.var 0 is n I from Label0 to Label1
.var 1 is start_disk Ljava/lang/String; from Label0 to Label1
.var 2 is desination_disk Ljava/lang/String; from Label0 to Label1
.var 3 is auxiliary_disk Ljava/lang/String; from Label0 to Label1
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
	ldc "Move 1 disk from "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
	ldc " to "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	invokestatic io/putStringLn(Ljava/lang/String;)V
	return
	goto Label5
Label4:
Label5:
	iload_0
	iconst_1
	isub
	aload_1
	aload_3
	aload_2
	invokestatic MPClass/towerOfHanoi(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
	ldc "Move 1 disk from "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
	ldc " to "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_0
	iconst_1
	isub
	aload_3
	aload_2
	aload_1
	invokestatic MPClass/towerOfHanoi(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	ldc "A"
	ldc "C"
	ldc "B"
	invokestatic MPClass/towerOfHanoi(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
