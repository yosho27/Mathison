from dataclasses import dataclass
from parsita import *


class Instruction:
    '''command: str
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
    loadto: str = None #'ACC' or 'TEMP'
    '''
    def __init__(self,command,read=None,big=None,var0=None,var1=None,vard=None,varr=None,
                 map_=None,labels=None,next_quasis=None,imm=None,loadto=None):
        self.command = command
        self.read = bool(read)
        self.big = bool(big)
        self.var0 = var0
        self.var1 = var1
        self.vard = vard
        self.varr = varr
        self.map_ = map_
        self.labels = labels
        self.next_quasis = next_quasis
        self.imm = imm
        self.loadto = loadto

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

@dataclass
class State:
    step: int #refers to an index in quasis
    acc: int
    transitions: dict #{symbol:(step,acc)}
    direction: int #+1 or -1

@dataclass(frozen=True,eq=True)
class Symbol:
    symbol: str
    offset: int = 0

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
    return (lambda x: Instruction(x[0],**dict(zip(args,x[1:]))))

class LineParser(TextParsers,whitespace=None):
    s = reg(r'[ \t]+')
    valid = reg(r'[A-Za-z][A-Za-z0-9_]*')
    label = valid << ':' > Label
    instr = (
      (lit('LOAD','STORE') & opt('NEXT') & opt('BIG') &s>> valid &s>> lit('ACC','TEMP') > create_args('read','big','vard','loadto'))
    | (lit('UNREAD','JUMP','NOTs','COMPs','SEZ') &s>> valid > create_args('vard'))
    | ('MAP' &s>> MapParser.map_ > create_args('map_'))
    | ('BRANCH' &s>> pred(repsep(valid,s), lambda x: len(x)==4, 'list of four labels') > create_args('labels'))
    | ('LOADI' &s>> (ImmParser.imm2 &s>> 'ACC' | ImmParser.imm1 &s>> 'TEMP') > create_args('imm','loadto'))
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

def group_unreads():
    global quasis

def get_search_transitions(n_step,acc):
    global quasis
    step = quasis[n_step]
    instruction = quasis[step.instruction]
    command = instruction.command
    transitions = None
    imm = instruction.imm
    if command=='COMPs':
        init_state = 1
    elif command in ['NOTs','ZEROs','LOAD','STORE','SEZ']:
        init_state = acc
    elif command in ['SLLs','SRLs','SLL2s','SRL2s','ADDIs','SUBIs']:
        init_state = imm
    if command in ['SRLs','SRL2s'] or command in ['LOAD','STORE'] and instruction.big:
        direction = 1
    else:
        direction = 0
    return {Symbol(step.variable,direction):(None,init_state,step.next_quasis[0])},None
    

def get_found_transitions(n_step,acc):
    global quasis
    step = quasis[n_step]
    instruction = quasis[step.instruction]
    command = instruction.command
    #If 0' and 1' aren't specified, assume that they're the same as 0 and 1
    transitions = None
    #"other primitive commands" except SEZ
    if command=='NOTs':
        transitions={'0':('1',acc),'1':('0',acc)}
    elif command=='ZEROs':
        imm = str(instruction.imm)
        transitions={'0':(imm,acc),'1':(imm,acc)}
    elif command=='COMPs':
        if acc==0:
            transitions={'0':('1',0),'1':('0',0)}
        elif acc==1:
            transitions={'0':('0',1),'1':('1',0)}
    elif command in ['SLLs','SRLs']:
        if acc==0:
            transitions={'0':('0',0),'1':('0',1)}
        elif acc==1:
            transitions={'0':('1',0),'1':('1',1)}
    elif command=='SLL2s':
        if acc==0b00:
            transitions={'0':('0',0b00),'1':('0',0b10)}
        elif acc==0b01:
            transitions={'0':('1',0b00),'1':('1',0b10)}
        elif acc==0b10:
            transitions={'0':('0',0b01),'1':('0',0b11)}
        elif acc==0b11:
            transitions={'0':('1',0b01),'1':('1',0b11)}
    elif command=='SRL2s':
        if acc==0b00:
            transitions={'0':('0',0b00),'1':('0',0b01)}
        elif acc==0b10:
            transitions={'0':('1',0b00),'1':('1',0b01)}
        elif acc==0b01:
            transitions={'0':('0',0b10),'1':('0',0b11)}
        elif acc==0b11:
            transitions={'0':('1',0b10),'1':('1',0b11)}
    elif command=='ADDIs':
        if acc==0:
            transitions={'0':('0',0),'1':('1',0)}
        elif acc==1:
            transitions={'0':('1',0),'1':('0',1)}
        elif acc==2:
            transitions={'0':('0',1),'1':('1',1)}
        elif acc==3:
            transitions={'0':('1',1),'1':('0',2)}
    elif command=='SUBIs':
        if acc==0:
            transitions={'0':('0',0),'1':('1',0)}
        elif acc==1:
            transitions={'0':('1',1),'1':('0',0)}
        elif acc==2:
            transitions={'0':('0',1),'1':('1',1)}
        elif acc==3:
            transitions={'0':('1',2),'1':('0',1)}
    if command in ['SRLs','SRL2s']:
        direction = -1
    else:
        direction = +1
    if transitions:
        for symbol in transitions:
            transitions[symbol] += (n_step,)
            transitions[symbol+'\''] = transitions[symbol]
        transitions[Symbol(step.variable,direction)] = (None,acc,step.next_quasis[0])
        return transitions,direction
    #SEZ
    if command=='SEZ':
        return {'0':('0',acc,n_step),'1':('1',0,step.next_quasis[0]),
                     Symbol(step.variable,+1):(None,1,step.next_quasis[0])},+1
    #All LOAD and STORE commands
    mark_read = '\'' if instruction.read else ''
    use_temp = instruction.loadto=='TEMP'
    direction = 1-2*instruction.big
    if command=='LOAD':
        transitions={'0':('0'+mark_read, acc if use_temp else 0),
                '1':('1'+mark_read, acc if use_temp else 1)}
    elif command=='STORE':        
        transitions={'0':(('0' if use_temp else str(acc))+mark_read, acc),
                '1':(('1' if use_temp else str(acc))+mark_read, acc)}
    if transitions:
        for symbol in transitions:
            transitions[symbol] += (step.next_quasis[0],)
        transitions.update(
            {'0\'':('0\'',acc,n_step),'1\'':('1\'',acc,n_step),
            Symbol(step.variable,direction):(None,acc,step.next_quasis[1])})
        return transitions,direction
    

def steps2states():
    global quasis
    for k,quasi in enumerate(quasis):
        if type(quasi)==Step:
            for acc in range(4):
                if quasi.is_found:
                    transitions,direction = get_found_transitions(k,acc)
                else:
                    transitions,direction = get_search_transitions(k,acc)
                quasis.append(State(step=k,acc=acc,transitions=transitions,direction=direction))
        

def instructions2steps():
    global quasis
    for k,quasi in enumerate(quasis):
        if type(quasi)==Instruction and quasi.command in [
                'NOTs', 'COMPs','SLLs','SRLs','SLL2s','SRL2s','ZEROs','ADDIs','SUBIs','LOAD','STORE','SEZ']:
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
