FUNC BIN0

SUB NK N K

factA:
LEQZ N
BRANCH null returnA null null
BOLs f FA {}
ZEROs FA 0
MULT FA N f
SUBIs N 1
JUMP factA
returnA:

factB:
LEQZ K
BRANCH null returnB null null
BOLs f FA {}
DIV FA varr f K
SUBIs K 1
JUMP factB
returnB:

factC:
LEQZ NK
BRANCH null returnC null null
BOLs f FA {}
DIV FA varr f NK
SUBIs NK 1
JUMP factC
returnC:

END



FUNC BIN1
bin:
LEQZ K
BRANCH null base null null
SLT K N
BRANCH base null null null

SUBIs N 1
JAL bin

SUBIs K 1
JAL bin

ADDIs N 1
ADDIs K 1
JR bin

base:
ADDIs C 1
JR bin

oob:
END




FUNC TRIN1

trin:
LEQZ K
BRANCH null baseK null null
LEQZ J
BRANCH notbase baseKorJ null null
baseK:
LEQZ J
BRANCH null base null null
baseKorJ:
LEQZ I
BRANCH null base null null
notbase:

SUBIs N 1

LEQZ I
BRANCH null skipI null null
SUBIs I 1
JAL trin
ADDIs I 1
skipI:

LEQZ K
BRANCH null skipK null null
SUBIs K 1
JAL trin
ADDIs K 1
skipK:

LEQZ J
BRANCH null skipJ null null
SUBIs J 1
JAL trin
ADDIs J 1
skipJ:

ADDIs N 1
JR trin

base:
ADDIs C 1
JR trin

oob:
END