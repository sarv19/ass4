'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType(list(), VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class SubBody():  #stmt
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():   #expr
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            if type(x) is VarDecl:
                e = self.visit(x, e)
        for x in ast.decl:
            if type(x) is FuncDecl:
                e=self.visit(x,e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name.lower() == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list(map(lambda x: x.varType,consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        decl = list()
        for x in consdecl.param + consdecl.local:
            a = frame.getNewIndex()
            decl.append(Symbol(x.variable.name, x.varType, Index(a)))
            self.emit.printout(self.emit.emitVAR(a, x.variable.name, x.varType, frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, decl + glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitVarDecl(self, ast, o):
        subctxt = o
        self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, None))
        return SubBody(None, [Symbol(ast.variable.name, ast.varType, CName(self.className))]+subctxt.sym)

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        # print(ast.returnType)
        return SubBody(None, [Symbol(ast.name.name,MType(list(map(lambda x: x.varType,ast.param)),ast.returnType),CName(self.className))]+o.sym)

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        n=0
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[n]) is FloatType:
                # in_ = (in_[0] + str1, in_[1].append(typ1))
                in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1] + [typ1])
            else:
                in_ = (in_[0] + str1, in_[1] + [typ1])
            n+=1


        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        n = 0
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[n]) is FloatType:
                # in_ = (in_[0] + str1, in_[1].append(typ1))
                in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1] + [typ1])
            else:
                in_ = (in_[0] + str1, in_[1] + [typ1])
            n+=1


        # self.emit.printout(in_[0])
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), ctype.rettype
        #maybe need fix???!!!


    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitStringLiteral(self, ast, o):
        #ast: StringLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST('"'+str(ast.value)+'"', StringType(),frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        #ast: BooleanLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        if ast.value == True:
            in_ = 'true'
        else:
            in_ = 'false'
        return self.emit.emitPUSHICONST(str(in_.lower()), frame), BoolType()

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        left, lefttype = self.visit(ast.left, Access(frame,nenv,False, True))

        right, righttype = self.visit(ast.right, Access(frame,nenv,False, True))
        # return left + right + self.emit.emitADDOP(str(ast.op), IntType(), frame), IntType()
        if type(lefttype) is BoolType and type(righttype) is BoolType:
            if ast.op.lower() == 'and':
                return left + right + self.emit.emitANDOP(frame), BoolType()
            elif ast.op.lower() == 'or':
                return left + right + self.emit.emitOROP(frame), BoolType()
            elif ast.op.lower() == 'andthen':
                # return left + right + self.emit.emitREOP(str(ast.op), BoolType(), frame), BoolType()
                result = list()
                labelF = frame.getNewLabel()
                labelO = frame.getNewLabel()
                frame.pop()
                result.append(self.emit.jvm.emitDUP())
                result.append(self.emit.jvm.emitIFEQ(labelO))
                result.append(self.emit.emitGOTO(labelF,frame))
                result.append(self.emit.emitLABEL(labelF,frame))
                frame.pop()
                result.append(self.emit.emitANDOP(frame))
                result.append(self.emit.emitLABEL(labelO,frame))
                return ''.join(result), BoolType()
            elif ast.op.lower() == 'orelse':
                # return left + right + self.emit.emitREOP(str(ast.op), BoolType(), frame), BoolType()
                result = list()
                labelF = frame.getNewLabel()
                labelO = frame.getNewLabel()
                result.append(left)
                result.append(self.emit.jvm.emitDUP())
                result.append(self.emit.jvm.emitIFEQ(labelF))
                result.append(self.emit.emitGOTO(labelO,frame))
                result.append(self.emit.emitLABEL(labelF,frame))
                result.append(right)
                result.append(self.emit.emitOROP(frame))
                result.append(self.emit.emitLABEL(labelO,frame))
                return ''.join(result), BoolType()
        elif ast.op in ['>','<','<>','=','<=','>=']:
            if type(lefttype) is type(righttype):
                return left + right + self.emit.emitREOP(str(ast.op), lefttype, frame), BoolType()
            elif type(righttype) is FloatType:
                return left + self.emit.emitI2F(frame) + right + self.emit.emitREOP(str(ast.op), FloatType(), frame), BoolType()
            else:
                return left + right + self.emit.emitI2F(frame) + self.emit.emitREOP(str(ast.op), FloatType(), frame), BoolType()
        elif ast.op in ['-','+']:
            # if (type(lefttype) is IntType) and (type(righttype) is IntType):
            if type(lefttype) is type(righttype):
                return left + right + self.emit.emitADDOP(str(ast.op), lefttype, frame), lefttype
            elif type(righttype) is FloatType:
                return left + self.emit.emitI2F(frame) + right + self.emit.emitADDOP(str(ast.op), FloatType(), frame), FloatType()
            elif type(lefttype) is FloatType:
                return left + right + self.emit.emitI2F(frame) + self.emit.emitADDOP(str(ast.op), FloatType(), frame), FloatType()
        elif ast.op.lower() in ['mod','div']:
             if ast.op.lower() == 'mod':
                 return left + right + self.emit.emitMOD(frame), IntType()
             else:
                return left + right + self.emit.emitDIV(frame), IntType()
        elif ast.op in ['/','*']:
            if ast.op is '*':
                if type(lefttype) is type(righttype):
                    return left + right + self.emit.emitMULOP(str(ast.op), lefttype, frame), lefttype
                elif type(righttype) is FloatType:
                    return left + self.emit.emitI2F(frame) + right + self.emit.emitMULOP(str(ast.op), FloatType(), frame), FloatType()
                elif type(lefttype) is FloatType:
                    return left + right + self.emit.emitI2F(frame) + self.emit.emitMULOP(str(ast.op), FloatType(), frame), FloatType()
            else:
                if type(lefttype) is type(righttype):
                    if type(lefttype) is IntType:
                        return left + self.emit.emitI2F(frame) + right + self.emit.emitI2F(frame) + self.emit.emitMULOP(str(ast.op), FloatType(), frame), FloatType()
                    else:
                        return left + right + self.emit.emitMULOP(str(ast.op), lefttype, frame), FloatType()
                elif type(righttype) is FloatType:
                    return left + self.emit.emitI2F(frame) + right + self.emit.emitMULOP(str(ast.op), FloatType(), frame), FloatType()
                elif type(lefttype) is FloatType:
                    return left + right + self.emit.emitI2F(frame) + self.emit.emitMULOP(str(ast.op), FloatType(), frame), FloatType()

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        left, lefttype = self.visit(ast.body, Access(frame,nenv,True, True))
        if ast.op == '-':
            return left + self.emit.emitNEGOP(lefttype, frame), lefttype
        else:
            return left + self.emit.emitNOT(BoolType(), frame), BoolType()

    def visitAssign(self, ast, o):
        rc, rt = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
        if type(rt) is type(lt):
            self.emit.printout(rc+lc)
        elif type(rt) is IntType and type(lt) is FloatType:
            self.emit.printout(rc + self.emit.emitI2F(o.frame) + lc)

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())

        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame), sym.mtype
            else:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name, sym.mtype,sym.value.value, frame), sym.mtype

    def visitWhile(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        # result = list()

        frame.enterLoop()

        exp, expty = self.visit(ast.exp, o)

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        [self.visit(x, SubBody(frame, o.sym)) for x in ast.sl]

        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        # self.emit.printout(''.join(result))

        frame.exitLoop()

    def visitIf(self, ast, o):  ##need to left out GOTO when there is no else
        ctxt = o
        frame = ctxt.frame
        # result = list()
        exp, typee = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
        self.emit.printout(exp)
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label1,frame))
        [self.visit(x,SubBody(frame, o.sym)) for x in ast.thenStmt]
        self.emit.printout(self.emit.emitGOTO(label2,frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        [self.visit(x, SubBody(frame, o.sym)) for x in ast.elseStmt]
        self.emit.printout(self.emit.emitLABEL(label2, frame))

    def visitFor(self, ast, o):
        ctxt = o
        frame = ctxt.frame

        frame.enterLoop()

        exp1, exp1type = self.visit(ast.expr1,Access(o.frame, o.sym, False, True))  #1sr expr
        condi,conditype = self.visit(ast.id, Access(o.frame, o.sym, True, True))    #getID
        condi2,conditype2 = self.visit(ast.id, Access(o.frame, o.sym, False, True))
        self.emit.printout(exp1)
        self.emit.printout(condi)

        condi_index = self.lookup(ast.id.name.lower(), o.sym, lambda x: x.name.lower())
        # self.emit.printout(self.emit.emitWRITEVAR(ast.id.name, IntType(),condi_index.value.value,frame))
        #if up -1, if downto +1
        self.emit.printout(self.emit.emitREADVAR(ast.id.name, IntType(), condi_index.value.value, frame) + self.emit.emitPUSHICONST(1,frame))
        if ast.up is True:
            self.emit.printout(self.emit.emitADDOP('-',IntType(), frame) +self.emit.emitWRITEVAR(ast.id.name, IntType(), condi_index.value.value, frame))
        else:
            self.emit.printout(self.emit.emitADDOP('+',IntType(), frame) +self.emit.emitWRITEVAR(ast.id.name, IntType(), condi_index.value.value, frame))

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))  # co

        exp2, exp2type = self.visit(ast.expr2, Access(o.frame, o.sym, False, True))

        if ast.up is True: ##increase loop
            self.emit.printout(condi2 + self.emit.emitPUSHICONST(1,frame) + self.emit.emitADDOP('+', IntType(), frame))
            self.emit.printout(condi)
        else:
            self.emit.printout(condi2 + self.emit.emitPUSHICONST(1,frame) + self.emit.emitADDOP('-', IntType(), frame))
            self.emit.printout(condi)


        if ast.up is True: #check condition
            self.emit.printout(condi2 + exp2 + self.emit.emitREOP('<=', IntType(),frame))
        else:
            self.emit.printout(condi2 + exp2 + self.emit.emitREOP('>=', IntType(), frame))

        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        [self.visit(x, SubBody(frame, o.sym)) for x in ast.loop]
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()

    def visitReturn(self, ast, o):
        if ast.expr:
            exp, typexp = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            if type(typexp) == IntType and type(o.frame.returnType) == FloatType:
                self.emit.printout(exp + self.emit.emitI2F(o.frame) + self.emit.emitRETURN(FloatType(), o.frame))
            else:
                self.emit.printout(exp + self.emit.emitRETURN(typexp, o.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(str(o.frame.getBreakLabel()),o.frame))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(str(o.frame.getContinueLabel()),o.frame))

    def visitWith(self, ast, o):
        ctxt = o
        frame = ctxt.frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        varde = list()

        self.emit.printout(self.emit.emitLABEL(label1, frame))
        for x in ast.decl:
            sym = Symbol(x.variable.name, x.varType, Index(frame.getNewIndex()))
            varde.append(sym)
            self.emit.printout(self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, label1, label2, frame))

        for x in ast.stmt:
            stmt = self.visit(x, SubBody(frame, varde +  ctxt.sym))

        self.emit.printout(self.emit.emitLABEL(label2, frame))
