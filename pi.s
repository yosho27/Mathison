FUNC PI
start:
RECP V varr N
LOAD S ACC
BRANCH add null null null
COMPs V
add:
ADDs P V
ADDIs N 2
BRANCH null end null null
NOTs S
JUMP start
end:
END

FUNC TEST
MULTo D A B
STORE S ACC
END

FUNC EULER
next:
BOLs n N {0x0:0, 0x1:0, 1x0:1, 1x1:1}
ZEROs F 0
LOAD F 1
start:
BOLs f F {0x0:0, 0x1:0, 1x0:1, 1x1:1}
ZEROs F 0
MULT F n f
SUBIs n 1
SEZ n
BRANCH start recip null null
recip:
RECP Q varr F
ADDs E Q
ADDIs N 1
BRANCH next end null null
end:
END