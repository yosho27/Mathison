start:
LOADNEXT var0 TEMP
MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2}
LOADNEXT var1 TEMP
MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2, 2x0:2, 2x1:3}  
MAP {0:0x0, 1:0x1, 2:1x0, 3:1x1}
STORENEXT vard TEMP
JUMP start

oob: 
UNREAD var0
UNREAD var1
UNREAD vard
