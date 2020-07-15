FUNC ADD vard var0 var1
LOADI 0 ACC
start:
LOADNEXT var0 TEMP
MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2}
LOADNEXT var1 TEMP
MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2, 2x0:2, 2x1:3}  
MAP {0:0x0, 1:0x1, 2:1x0, 3:1x1}
STORENEXT vard TEMP
JUMP start
oob: 
MAP {0:0, 1:1, 2:1, 3:1}
UNREAD var0
UNREAD var1
UNREAD vard
END


FUNC SUB vard var0 var1
LOADI 0 ACC
start:
LOADNEXT var0 TEMP
MAP {0x0:0, 0x1:1, 3x0:3, 3x1:0}
LOADNEXT var1 TEMP
MAP {0x0:0, 0x1:3, 1x0:1, 1x1:0, 3x0:3, 3x1:2}
MAP {0:0x0, 1:0x1, 2:3x0, 3:3x1}
STORENEXT vard TEMP
JUMP start
oob: 
MAP {0:0, 1:1, 2:1, 3:1}
UNREAD var0
UNREAD var1
UNREAD vard
END


FUNC BOL vard var0 var1 map
LOADI 0 ACC
start:
LOADNEXT var0 ACC
LOADNEXT var1 TEMP
MAP map
STORENEXT vard ACC
JUMP start
oob: 
UNREAD var0
UNREAD var1
UNREAD vard
END


FUNC ADDs vard var0
LOADI 0 ACC
start:
LOADNEXT var0 TEMP
MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2}
LOAD vard TEMP
MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2, 2x0:2, 2x1:3}
MAP {0:0x0, 1:0x1, 2:1x0, 3:1x1}
STORENEXT vard TEMP
JUMP start
oob: 
MAP {0:0, 1:1, 2:1, 3:1}
UNREAD var0
UNREAD vard
END


FUNC SUBs vard var0
LOADI 0 ACC
start:
LOADNEXT var0 TEMP
MAP {0x0:0, 0x1:3, 3x0:3, 3x1:2}
LOAD vard TEMP
MAP {0x0:0, 0x1:1, 2x0:2, 2x1:3, 3x0:3, 3x1:0}
MAP {0:0x0, 1:0x1, 2:3x0, 3:3x1}
STORENEXT vard TEMP
JUMP start
oob: 
MAP {0:0, 1:1, 2:1, 3:1}
UNREAD var0
UNREAD vard
END


FUNC BOLs vard var0 map
LOADI 0 ACC
start:
LOADNEXT var0 ACC
LOAD vard TEMP
MAP map
STORENEXT vard ACC
JUMP start
oob: 
UNREAD var0
UNREAD vard
END


FUNC SLL vard var0 imm
LOADI 0 ACC
LOADNEXTBIG var0 TEMP
start:
LOADNEXTBIG var0 ACC
STORENEXTBIG vard ACC
JUMP start
oob:
LOADI imm TEMP
STORENEXTBIG vard TEMP
UNREAD var0
UNREAD vard
END


FUNC SRL vard var0 imm
LOADI 0 ACC
LOADNEXT var0 TEMP
start:
LOADNEXT var0 ACC
STORENEXT vard ACC
JUMP start
oob:
LOADI imm TEMP
STORENEXT vard TEMP
UNREAD var0
UNREAD vard
END


FUNC SLT var0 var1
LOADI 0 ACC
start:
LOADNEXTBIG var0 ACC
LOADNEXTBIG var1 TEMP
MAP {0x0:0, 0x1:1, 1x0:3, 1x1:0}
BRANCH start oob null oob
oob:
UNREAD var0
UNREAD var1
END


FUNC MULT vard var0 var1
LOADI 0 ACC
start:
LOADNEXT var0 ACC
BRANCH shift add null null
add:
ADDs vard var1
shift:
SLLs var1 0
JUMP start
oob:
UNREAD var0
END


FUNC MULTo vard var0 var1
LOADI 0 ACC
start:
LOADNEXT var0 ACC
BRANCH shift add null null
add:
ADDs vard var1
BRANCH shift oob null null
shift:
SLLs var1 0
BRANCH start flow null null
flow:
LOADI 0 ACC
LOADNEXT var0 ACC
BRANCH flow oob null null
oob:
UNREAD var0
END


FUNC DIV vard varr var0 var1
LOADI 0 ACC
ZEROs varr 0
start:
SLLs varr 0
LOADNEXTBIG var0 ACC
STORE varr ACC
SLT varr var1
MAP {0:0x1, 1:1x0, 3:0x1}
STORENEXTBIG vard TEMP
BRANCH sub start null null
sub:
SUBs varr var1
JUMP start
oob:
UNREAD var0
UNREAD vard
END


FUNC MOD varr var0 var1
LOADI 0 ACC
ZEROs varr 0
start:
SLLs varr 0
LOADNEXTBIG var0 ACC
STORE varr ACC
SLT varr var1
BRANCH sub start null null
sub:
SUBs varr var1
JUMP start
oob:
UNREAD var0
END


FUNC RECP vard varr var0
LOADI 0 ACC
ZEROs varr 0
start:
SLLs varr 1
SLT varr var0
MAP {0:0x1, 1:1x0, 3:0x1}
STORENEXTBIG vard TEMP
BRANCH sub start null null
sub:
SUBs varr var0
JUMP start
oob:
UNREAD vard
END