from dataclasses import dataclass

@dataclass
class Instruction:
    command: str
    var0: str
    var1: str
    vard: str
    varr: str
    mapp: dict
    next_quasis: list #refers to one or more indices in quasis
    imm: int
    use_temp: bool

@dataclass
class Step:
    instruction: int #refers to an index in quasis
    is_found: bool
    variable: str #the variable name
    next_quasis: int #refers to one or more indices in quasis
    direction: bool


def instructions2steps():
    for k in range(0):
        if quasis[k].command in ['NOTs', 'COMPs','SLLs','SRLs','SLL2s','SRL2s','ZEROs','ADDIs','SUBIs',
                                 'LOAD','LOADBIG','LOADNEXT','LOADNEXTBIG','STORE','STOREBIG','STORENEXT','STORENEXTBIG',
                                 'UNREAD']:
            indices = [len(quasis)+s for s in range(2)]   
            quasis += [
                Step(instruction=k,is_found=False,variable=instr.vard,next_quasis=[indices[1]]),
                Step(instruction=k,is_found=True,variable=instr.vard,next_quasis=quasis[k].next_quasis)
            ]
            for quasi in quasis:
                for j in range(len(quasi.next_quasis)):
                    if quasi.next_quasis[j] == k:
                        quasi.next_quasis[j] = indices[0]


def compile():
    quasis = []
