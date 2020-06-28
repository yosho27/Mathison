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
ADDIs A 3
END