FUNC HOFSTADER_G

g:
LEQZ G
BRANCH null base null null

PUSH G

SUBIs G 1
JAL g
JAL g

NSUBs G $POP
JUMP return
base:

return:
JR g

oob:
END



FUNC HOFSTADER_Q

q:
IS1OR2 N
BRANCH null base null null

PUSH N

SUBIs N 1
JAL q
ADDIs N 1
SUBs N Q
JAL q

BOLs N $TOP {}
PUSH Q

SUBIs N 2
JAL q
ADDIs N 2
SUBs N Q
JAL q

ADDs Q $POP
BOLs N $POP {}
JUMP return

base:
STORE1 Q

return:
JR q

oob:
END


PRIM IS1OR2 N
LOADI 0 ACC
LOADNEXT N ACC
LOADNEXT N TEMP
MAP {0x0:1, 0x1:0, 1x0:0, 1x1:1}
BRANCH null oob null null
next:
LOADNEXT N ACC
BRANCH null oob null null
JUMP next
oob:
MAP {0:1,1:0}
END


PRIM STORE1 N
LOADI 1 TEMP
STORENEXT N TEMP
next:
LOADI 0 TEMP
STORENEXT N TEMP
JUMP next
oob:
END
