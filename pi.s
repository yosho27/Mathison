FUNC PI
start:
RECP V varr N
LOAD S ACC
BRANCH add null null null
COMPs V
add:
ADDs P V
ADDIs N 2
BRANCH null oob null null
NOTs S
JUMP start
oob:
END

FUNC TEST
IS1OR2 N
STORE S ACC
END

FUNC EULER
start:
BOLs f F {}
ZEROs F 0
MULTo F N f
BRANCH null end null null
RECP Q varr F
ADDs E Q
ADDIs N 1
BRANCH start end null null
end:
END

FUNC PRIME
prime:
SUBIs C 1
BRANCH null end null null
notprime:
ADDIs N 1
STORE2 D
next:
MOD R N D
LEQZ R
BRANCH null notprime null null
ADDIs D 1
SLT D N
BRANCH prime next null prime
end:
END

PRIM STORE2 N
LOADI 0 TEMP
STORENEXT N TEMP
LOADI 1 TEMP
STORENEXT N TEMP
next:
LOADI 0 TEMP
STORENEXT N TEMP
JUMP next
oob:
END