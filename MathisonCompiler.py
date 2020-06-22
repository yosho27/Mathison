from dataclasses import dataclass
from parsita import *

@dataclass
class Instruction:
    command: str
    read: bool = None
    big: bool = None
    var0: str = None
    var1: str = None
    vard: str = None
    varr: str = None
    map_: dict = None
    labels: list = None
    next_quasis: list = None #refers to one or more indices in quasis
    imm: int = None
    temp: str = None

@dataclass
class Label:
    name: str

@dataclass
class Step:
    instruction: int #refers to an index in quasis
    is_found: bool
    variable: str #the variable name
    next_quasis: int #refers to one or more indices in quasis
    direction: bool = None

class ImmParser(TextParsers,whitespace=None):
    imm1 = reg(r'[01]') > int
    imm2d = reg(r'[0123]') > int
    imm2b = reg(r'[01]{2}') > (lambda x: int(x,2))
    imm2 = imm2d | imm2b

class MapParser(TextParsers):
    state = ImmParser.imm2 & opt('x' >> ImmParser.imm1) > (lambda x: tuple([x[0]]+x[1]))
    mapping = state & ':' >> state
    map_ = '{' >> repsep(mapping, ',') << '}' > dict

def create_args(*args):
    return (lambda x: Instruction(**dict(zip(('command',)+args,x))))

class LineParser(TextParsers,whitespace=None):
    s = reg(r'[ \t]+')
    valid = reg(r'[A-Za-z][A-Za-z0-9_]*')
    label = valid << ':' > Label
    instr = (
      (lit('LOAD','STORE') & opt('NEXT') & opt('BIG') &s>> valid &s>> lit('ACC','TEMP') > create_args('read','big','vard','temp'))
    | (lit('UNREAD','JUMP','NOTs','COMPs') &s>> valid > create_args('vard'))
    | ('MAP' &s>> MapParser.map_ > create_args('map_'))
    | ('BRANCH' &s>> pred(repsep(valid,s), lambda x: len(x)==4, 'list of four labels') > create_args('labels'))
    | ('LOADI' &s>> (ImmParser.imm2 &s>> 'ACC' | ImmParser.imm1 &s>> 'TEMP') > create_args('imm','temp'))
    | (lit('SLLs','SRLs','ZEROs') &s>> valid &s>> ImmParser.imm1 > create_args('vard','imm'))
    | (lit('SLL2s','SRL2s','ADDIs','SUBIs') &s>> valid &s>> ImmParser.imm2 > create_args('vard','imm'))
       )
    line = instr | label

def find_next_instruction(k,label):
    for j in range(k,len(quasis)):
        if label=='null':
            if type(quasis[j])==Instruction:
                return j
        else:
            if type(quasis[j])==Label and quasis[j].name==label:
                label='null'
            

def parse(text):
    global quasis
    lines = [line.strip() for line in text.split('\n')]
    quasis = [LineParser.line.parse(line).value for line in lines if line]
    for k,quasi in enumerate(quasis):
        if type(quasi)==Instruction:
            if quasi.command in ['LOAD','STORE']:
                quasi.next_quasis = [find_next_instruction(k+1,'null'),find_next_instruction(k+1,'oob')]
            elif quasi.command=='JUMP':
                quasi.next_quasis = [find_next_instruction(0,quasi.vard)]
            elif quasi.command=='BRANCH':
                quasi.next_quasis = [find_next_instruction(0,quasi.labels[j]) for j in range(4)]
            else:
                quasi.next_quasis = [find_next_instruction(k+1,'null')]
            

def instructions2steps():
    global quasis
    for k,quasi in enumerate(quasis):
        if type(quasi)==Instruction and quasi.command in ['NOTs', 'COMPs','SLLs','SRLs','SLL2s','SRL2s','ZEROs','ADDIs','SUBIs','LOAD','STORE','UNREAD']:
            indices = [len(quasis)+s for s in range(2)]   
            quasis += [
                Step(instruction=k,is_found=False,variable=quasi.vard,next_quasis=[indices[1]]),
                Step(instruction=k,is_found=True,variable=quasi.vard,next_quasis=quasi.next_quasis)
            ]
            for quasi1 in quasis:
                if type(quasi1)==Instruction:
                    for j in range(len(quasi1.next_quasis)):
                        if quasi1.next_quasis[j] == k:
                            quasi1.next_quasis[j] = indices[0]


def compile():
    quasis = []
