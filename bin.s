FUNC BIN0

SUB NK N K

factA:
SEZ N
BRANCH null returnA null null
BOLs f FA {0x0:0, 0x1:0, 1x0:1, 1x1:1}
ZEROs FA 0
MULT FA N f
SUBIs N 1
JUMP factA
returnA:

factB:
SEZ K
BRANCH null returnB null null
BOLs f FA {0x0:0, 0x1:0, 1x0:1, 1x1:1}
DIV FA varr f K
SUBIs K 1
JUMP factB
returnB:

factC:
SEZ NK
BRANCH null returnC null null
BOLs f FA {0x0:0, 0x1:0, 1x0:1, 1x1:1}
DIV FA varr f NK
SUBIs NK 1
JUMP factC
returnC:

END
