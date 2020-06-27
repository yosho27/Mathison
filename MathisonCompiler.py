from dataclasses import dataclass
from parsita import *
from parsita.util import constant,splat
import os

more_transitions = {
    'COMPs':{
        0:{'0':['1',0],'1':['0',0]},
        1:{'0':['0',1],'1':['1',0]}
    },
    'SLLs':{
        0:{'0':['0',0],'1':['0',1]},
        1:{'0':['1',0],'1':['1',1]}
    },
    'SRLs':{
        0:{'0':['0',0],'1':['0',1]},
        1:{'0':['1',0],'1':['1',1]}
    },
    'SLL2s':{
        0b00:{'0':['0',0b00],'1':['0',0b10]},
        0b01:{'0':['1',0b00],'1':['1',0b10]},
        0b10:{'0':['0',0b01],'1':['0',0b11]},
        0b11:{'0':['1',0b01],'1':['1',0b11]}
    },
    'SRL2s':{
        0b00:{'0':['0',0b00],'1':['0',0b01]},
        0b10:{'0':['1',0b00],'1':['1',0b01]},
        0b01:{'0':['0',0b10],'1':['0',0b11]},
        0b11:{'0':['1',0b10],'1':['1',0b11]}
    },
    'ADDIs':{
        0:{'0':['0',0],'1':['1',0]},
        1:{'0':['1',0],'1':['0',1]},
        2:{'0':['0',1],'1':['1',1]},
        3:{'0':['1',1],'1':['0',2]}
    },
    'SUBIs':{
        0:{'0':['0',0],'1':['1',0]},
        1:{'0':['1',1],'1':['0',0]},
        2:{'0':['0',1],'1':['1',1]},
        3:{'0':['1',2],'1':['0',1]}
    }
}

functions = []
quasis = []

@dataclass
class FunctionHeader:
    command: str
    params: list #the type of argument is defined by the first letter,
    #           'v' for variable, 'i' for immediate, 'm' for map
    lines: list = None

@dataclass
class FunctionCall:
    command: str
    args: list
    next_quasis: list = None

    def apply(self,index,argsdict):
        return FunctionCall(
            command=self.command,
            args=[(argsdict[arg] if (type(arg)==str and arg in argsdict) else arg) for arg in self.args],
            next_quasis=[index+next_quasi for next_quasi in self.next_quasis])

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
    def __init__(self,command,read=None,big=None,vard=None,map_=None,
                 labels=None,next_quasis=None,imm=None,loadto=None):
        self.command = command
        self.read = bool(read)
        self.big = bool(big)
        self.vard = vard
        self.map_ = map_
        self.labels = labels
        self.next_quasis = next_quasis
        self.imm = imm
        self.loadto = loadto

    def __str__(self):
        result = 'Instruction(' + self.command
        if self.read:
            result+='NEXT'
        if self.big:
            result+='BIG'
        if self.vard:
            result+=', vard=' + self.vard
        if self.map_:
            result+=', map=' + str(self.map_)
        if self.imm:
            result+=', imm=' + str(self.imm)
        result += ', next_quasis=' + str(self.next_quasis) + ')'
        return result

@dataclass
class Label:
    name: str

@dataclass
class Step:
    instruction: int #refers to an index in quasis
    is_found: bool
    variable: str #the variable name
    next_quasis: list #refers to one or more indices in quasis
    direction: bool = None

@dataclass
class End:
    is_start: bool
    next_quasis: list

    def apply(self,index):
        return End(
            is_start=self.is_start,
            next_quasis=[index+next_quasi for next_quasi in self.next_quasis])

@dataclass
class State:
    step: int #refers to an index in quasis
    acc: int
    transitions: dict #{symbol:[symbol,acc,step)}
    direction: int #+1 or -1

def get_none_transition(state,symbol,k):
    if symbol in state.transitions:
        transition = state.transitions[symbol]
        if transition[0]==None:
            transition[0] = symbol
    else:
        transition = [symbol,0,k]
    return transition
    

def equal_states(k,j):
    state1,state2 = quasis[k],quasis[j]
    if type(state1)!=State or type(state2)!=State:
        return False
    for symbol in state1.transitions.keys()|state2.transitions.keys():
        transition1 = get_none_transition(state1,symbol,k)
        transition2 = get_none_transition(state2,symbol,j)
        if not (transition1[0]==transition2[0] and
                (transition1[2]==transition2[2] or transition1[2]==k and transition2[2]==j)):
            return False
    return True
            
        
@dataclass(frozen=True,eq=True)
class Symbol:
    symbol: str
    offset: int = 0

    def __repr__(self):
        return 'Sym(\''+self.symbol+'\'+'+str(self.offset)+')'

class ImmParser(TextParsers,whitespace=None):
    imm1 = reg(r'[01]') > int
    imm2d = reg(r'[0123]') > int
    imm2b = reg(r'[01]{2}') > (lambda x: int(x,2))
    imm2 = imm2b | imm2d

class MapParser(TextParsers):
    state = ImmParser.imm2 & opt('x' >> ImmParser.imm1) > (lambda x: tuple([x[0]]+x[1]))
    mapping = state & ':' >> state
    map_ = '{' >> repsep(mapping, ',') << '}' > dict

def create_args(*args):
    return (lambda x: Instruction(x[0],**dict(zip(args,x[1:]))))

def functioncall2instruction(function_call):
    command = function_call.command
    memory_command = is_memory_command(command)
    args = function_call.args
    instr = None
    if memory_command:
        instr = Instruction(memory_command[0],read=memory_command[1],big=memory_command[2],vard=args[0],loadto=args[1])
    elif command in ['UNREAD','NOTs','COMPs','SEZ']:
        instr = Instruction(command,vard=args[0])
    elif command=='JUMP':
        instr = Instruction(command,labels=[args[0]])
    elif command=='BRANCH':
        instr = Instruction(command,labels=[args[k] for k in range(4)])
    elif command=='LOADI':
        instr = Instruction(command,imm=args[0],loadto=args[1])
    elif command=='MAP':
        instr = Instruction(command,map_=args[0])
    elif command in ['SLLs','SRLs','ZEROs','SLL2s','SRL2s','ADDIs','SUBIs']:
        instr = Instruction(command,vard=args[0],imm=args[1])
    if instr:
        instr.next_quasis = function_call.next_quasis[:]
        return instr
    else:
        return function_call
    

class LineParser(TextParsers,whitespace=None):
    s = reg(r'[ \t]+')
    valid = reg(r'[A-Za-z][A-Za-z0-9_]*')
    label = valid << ':' > Label
    arg = reg(r'[vimVIM][A-Za-z0-9_]*')
    function_header = 'FUNC' >>s>> valid & rep(s >> arg) > splat(FunctionHeader)
    function_call = valid & rep(s >> (MapParser.map_ | ImmParser.imm2 | valid)) > splat(FunctionCall)
    memory_command = lit('LOAD','STORE') & opt('NEXT') & opt('BIG')
    end = lit('END') > constant(End(False,[]))
    instr = (
      (memory_command &s>> valid &s>> lit('ACC','TEMP') > create_args('read','big','vard','loadto'))
    | (lit('UNREAD','JUMP','NOTs','COMPs','SEZ') &s>> valid > create_args('vard'))
    | ('MAP' &s>> MapParser.map_ > create_args('map_'))
    | ('BRANCH' &s>> pred(repsep(valid,s), lambda x: len(x)==4, 'list of four labels') > create_args('labels'))
    | ('LOADI' &s>> (ImmParser.imm2 &s>> 'ACC' | ImmParser.imm1 &s>> 'TEMP') > create_args('imm','loadto'))
    | (lit('SLLs','SRLs','ZEROs') &s>> valid &s>> ImmParser.imm1 > create_args('vard','imm'))
    | (lit('SLL2s','SRL2s','ADDIs','SUBIs') &s>> valid &s>> ImmParser.imm2 > create_args('vard','imm'))
       )
    line = end | label | function_header | function_call

def find_next_instruction(k,label):
    for j in range(k,len(quasis)):
        if label=='null':
            if type(quasis[j])==Instruction or type(quasis[j])==End and not quasis[j].is_start:
                return j
        else:
            if type(quasis[j])==Label and quasis[j].name==label:
                label='null'

def find_next_function(lines,k,label):
    for j in range(k,len(lines)):
        if label=='null':
            if type(lines[j])==FunctionCall or type(lines[j])==End and not lines[j].is_start:
                return j
        else:
            if type(lines[j])==Label and lines[j].name==label:
                label='null'
    return find_next_function(lines,k+1,'null')

def parse_files():
    global functions
    for filename in os.listdir():
        if filename.endswith('.s'):
            text = open(filename,'r').read()
            lines = [line.strip() for line in text.split('\n')]
            function = None
            for line in lines:
                if line:
                    parsed_line = LineParser.line.parse(line).value
                    if function:
                        if type(parsed_line)==FunctionHeader:
                            raise Exception
                        elif type(parsed_line)==End:
                            function.lines.append(parsed_line)
                            functions.append(function)
                            function = None
                        else:
                            function.lines.append(parsed_line)
                    else:                        
                        if type(parsed_line)==FunctionHeader:
                            function = parsed_line
                            function.lines = [End(True,[])]

def is_memory_command(command):
    memory_command = LineParser.memory_command.parse(command)
    if type(memory_command)==Success:
        return memory_command.value
    else:
        return None

def link_lines():
    global functions
    for function in functions:
        lines = function.lines
        for k,quasi in enumerate(lines):
            if type(quasi)==FunctionCall:
                if is_memory_command(quasi.command):
                    quasi.next_quasis = [find_next_function(lines,k+1,'null'),find_next_function(lines,k+1,'oob')]
                elif quasi.command=='JUMP':
                    quasi.next_quasis = [find_next_function(lines,0,quasi.args[0])]
                elif quasi.command=='BRANCH':
                    quasi.next_quasis = [find_next_function(lines,k+1 if quasi.args[j]=='null' else 0,quasi.args[j]) for j in range(4)]
                else:
                    quasi.next_quasis = [find_next_function(lines,k+1,'null')]
            elif type(quasi)==End and quasi.is_start:
                quasi.next_quasis = [find_next_function(lines,0,'null')]

def evaluate_function_call(function_call):
    global functions, quasis
    for function in functions:
        if function.command==function_call.command:
            assert len(function.params)==len(function_call.args)
            index = len(quasis)
            argsdict = dict(zip(function.params,function_call.args))
            quasis += [None]*len(function.lines)
            for k,line in enumerate(function.lines):
                if type(line)==FunctionCall:
                    new_function = functioncall2instruction(line.apply(index,argsdict))
                    quasis[index+k] = new_function
                    if type(new_function)==FunctionCall:
                        replace_links(index+k,len(quasis))
                        evaluate_function_call(new_function)
                elif type(line)==End:
                    if line.is_start:
                        quasis[index+k] = line.apply(index)
                    else:
                        quasis[index+k] = End(False,function_call.next_quasis)

def parse(text):
    global quasis
    lines = [line.strip() for line in text.split('\n')]
    quasis = [End(True,[])]+[LineParser.line.parse(line).value for line in lines if line]+[End(False,[])]
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
        elif type(quasi)==End and quasi.is_start:
            quasi.next_quasis = [find_next_instruction(0,'null')]

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
    elif command in ['NOTs','ZEROs','LOAD','STORE','SEZ','UNREAD']:
        init_state = acc
    elif command in ['SLLs','SRLs','SLL2s','SRL2s','ADDIs','SUBIs']:
        init_state = imm
    if command in ['SRLs','SRL2s'] or command in ['LOAD','STORE'] and instruction.big:
        direction = 1
    else:
        direction = 0
    return {Symbol(step.variable,direction):[None,init_state,step.next_quasis[0]]},None
    

def get_found_transitions(n_step,acc):
    global quasis
    step = quasis[n_step]
    instruction = quasis[step.instruction]
    command = instruction.command
    transitions = None
    #ACC preserving commands
    if command=='NOTs':
        transitions={'0':['1',acc],'1':['0',acc]}
    elif command=='ZEROs':
        imm = str(instruction.imm)
        transitions={'0':[imm,acc],'1':[imm,acc]}
    #"Other primitive commands" except SEZ and ACC-preserving
    elif command in more_transitions.keys():
        if acc in more_transitions[command].keys():
            transitions = more_transitions[command][acc]
        else:
            return None,None
    #"Other primitive commands" except SEZ
    if command in ['SRLs','SRL2s']:
        direction = 0
    else:
        direction = +1
    if transitions:
        for symbol in transitions:
            transitions[symbol] += [n_step]
        transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
        transitions[Symbol(step.variable,direction)] = [None,acc,step.next_quasis[0]]
        return transitions,2*direction-1
    #SEZ
    if command=='SEZ':
        return {'0':['0',acc,n_step],'1':['1',0,step.next_quasis[0]],
                     Symbol(step.variable,+1):[None,1,step.next_quasis[0]]},+1
    #All LOAD and STORE commands
    use_temp = instruction.loadto=='TEMP'
    if command=='LOAD':
        transitions={'0':['0', acc if use_temp else 0],'1':['1', acc if use_temp else 1]}
    elif command=='STORE':        
        transitions={'0':['0' if use_temp else str(acc), acc],'1':['1' if use_temp else str(acc), acc]}
    if transitions:
        for symbol in transitions:
            if instruction.read:
                transitions[symbol][0] += '\''
            transitions[symbol] += [step.next_quasis[0]]
        transitions.update(
            {'0\'':['0\'',acc,n_step],'1\'':['1\'',acc,n_step],
            Symbol(step.variable,1-instruction.big):[None,acc,step.next_quasis[1]]})
        return transitions,1-2*instruction.big
    #UNREAD
    if command=='UNREAD':
        return {'0':['0',acc,n_step],'1':['1',acc,n_step],
                '0\'':['0',acc,n_step],'1\'':['1',acc,n_step],
                     Symbol(step.variable,+1):[None,acc,step.next_quasis[0]]},+1

def steps2states():
    global quasis
    for k,quasi in enumerate(quasis):
        if type(quasi)==Step:
            for acc in range(4):
                if quasi.is_found:
                    transitions,direction = get_found_transitions(k,acc)
                else:
                    transitions,direction = get_search_transitions(k,acc)
                if transitions:
                    quasis.append(State(step=k,acc=acc,transitions=transitions,direction=direction))
        

def replace_links(a,b):
    global quasis
    for quasi in quasis:
        if type(quasi) in [Instruction,Step,End] and quasi.next_quasis:
            for k in range(len(quasi.next_quasis)):
                if quasi.next_quasis[k] == a:
                    quasi.next_quasis[k] = b
        elif type(quasi)==State:
            for symbol in quasi.transitions:
                if quasi.transitions[symbol][2] == a:
                    quasi.transitions[symbol][2] = b

def instructions2steps():
    global quasis
    for k,quasi in enumerate(quasis):
        if type(quasi)==Instruction and quasi.command in [
                'NOTs', 'COMPs','SLLs','SRLs','SLL2s','SRL2s','ZEROs','ADDIs','SUBIs','LOAD','STORE','SEZ','UNREAD']:
            indices = [len(quasis)+s for s in range(2)]   
            quasis += [
                Step(instruction=k,is_found=False,variable=quasi.vard,next_quasis=[indices[1]]),
                Step(instruction=k,is_found=True,variable=quasi.vard,next_quasis=quasi.next_quasis)
            ]
            replace_links(k,indices[0])

def validate_maps(map_):
    sizes = {(len(key),len(map_[key])) for key in map_}    
    assert len(sizes)==1
    return sizes.pop()

def apply_posts():
    global quasis
    altered = False
    for quasi in quasis:
        if type(quasi)==State:
            instruction = quasis[quasis[quasi.step].instruction]
            for symbol in quasi.transitions:
                transition = quasi.transitions[symbol]
                quasi2 = quasis[transition[2]]
                if type(quasi2)==Instruction:
                    if quasi2.command=='JUMP':
                        transition[2] = quasi2.next_quasis[0]
                        altered = True
                    elif quasi2.command=='BRANCH':
                        transition[2] = quasi2.next_quasis[transition[1]]
                        altered = True
                    elif quasi2.command=='LOADI' and quasi2.loadto=='ACC':
                        transition[1] = quasi2.imm
                        transition[2] = quasi2.next_quasis[0]
                        altered = True
                    elif quasi2.command=='MAP':
                        size = validate_maps(quasi2.map_)
                        if size==(2,1):
                            assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                            if (transition[1],int(symbol)) in quasi2.map_:
                                transition[1] = quasi2.map_[(transition[1],int(symbol))][0]
                            transition[2] = quasi2.next_quasis[0]
                            altered = True
                        elif size==(1,1):
                            if (transition[1],) in quasi2.map_:
                                transition[1] = quasi2.map_[(transition[1],)][0]
                            transition[2] = quasi2.next_quasis[0]                            
                            altered = True
                elif type(quasi2)==End and quasi2.next_quasis:
                    transition[2] = quasi2.next_quasis[0]
                    altered = True
    return altered

def apply_pres():
    global quasis
    altered = False
    for k,quasi in enumerate(quasis):
        if type(quasi)==Instruction:
            if quasi.command=='MAP' or quasi.command=='LOADI' and quasi.loadto=='TEMP':
                if quasi.command=='MAP':
                    size = validate_maps(quasi.map_)
                if quasi.command=='LOADI' or size==(1,2):
                    for quasi2 in quasis:
                        if (type(quasi2)==State and quasis[quasi2.step].is_found and
                                quasis[quasi.next_quasis[0]].next_quasis[0]==quasi2.step):
                            for symbol in ['0','1']:
                                transition = quasi2.transitions[symbol]
                                if quasi.command=='MAP':
                                    if (quasi2.acc,) in quasi.map_:
                                        mapping = quasi.map_[(quasi2.acc,)]
                                        transition[0] = str(mapping[0]) + transition[0][1:]
                                        transition[1] = mapping[1]
                                else:
                                    transition[0] = str(quasi.imm) + transition[0][1:]
                            altered = True
                    replace_links(k,quasi.next_quasis[0])
                    quasi.next_quasis[0] = 0
    return altered

def skip_searches():
    global quasis
    altered = False
    for quasi in quasis:
        if type(quasi)==State:
            step = quasis[quasi.step]
            instruction = quasis[step.instruction]
            command = instruction.command
            if step.is_found and command in ['LOAD','STORE']:
                for symbol in quasi.transitions:
                    quasi2 = quasis[quasi.transitions[symbol][2]]
                    if type(quasi2)==State:
                        step2 = quasis[quasi2.step]
                        if not step2.is_found and step.variable==step2.variable:
                            instruction2 = quasis[step2.instruction]
                            command2 = instruction2.command
                            if command2 in ['LOAD','STORE'] and instruction.big==instruction2.big:
                                if instruction.read:
                                    quasi.transitions[symbol][2] = quasi2.transitions[0][2]
                                else:
                                    quasi3 = quasis[list(quasi2.transitions.values())[0][2]]
                                    quasi.transitions[symbol] = quasi3.transitions[symbol]
                                altered = True
    return altered
                        
                        
                    


def find_state(acc,step):
    global quasis
    if type(quasis[step])==Step:
        for k,quasi in enumerate(quasis):
            if type(quasi)==State and quasi.acc==acc and quasi.step==step:
                return k
    else:
        return step

def stitch_acc():
    global quasis
    for quasi in quasis:
        if type(quasi)==End and quasi.is_start:
            quasi.next_quasis[0] = find_state(0,quasi.next_quasis[0])
        if type(quasi)==State:
            for symbol in quasi.transitions:
                transition = quasi.transitions[symbol]
                transition[2] = find_state(transition[1],transition[2])

def find_successors(k):
    global quasis,used_states
    if type(quasis[k])==End and quasis[k].next_quasis:
        for j in quasis[k].next_quasis:
            if not j in used_states:
                used_states.add(j)
                find_successors(j)
    if type(quasis[k])==State:
        for symbol in quasis[k].transitions:
            j = quasis[k].transitions[symbol][2]
            if not j in used_states:
                used_states.add(j)
                find_successors(j)

def merge_links():
    for k,state1 in enumerate(quasis):
        if type(state1)==State:
            for j,state2 in enumerate(quasis):
                if j>k:
                    if type(state2)==State:
                        if equal_states(k,j):
                            quasis[j]=None
                            replace_links(j,k)
                            return True
    return False
					

def compile_function(function_call):
    global quasis, used_states
    function = LineParser.line.parse(function_call).value
    evaluate_function_call(function)
    instructions2steps()
    steps2states()
    more_posts,more_pres = True,True
    while (more_posts or more_pres):
        if more_posts:
            more_posts = apply_posts()
        if more_pres:
            more_pres = apply_pres()
    stitch_acc()
    skip_searches()
    more_merges = True
    while more_merges:
        more_merges = merge_links()
    used_states = {0}
    find_successors(0)
    for k,quasi in enumerate(quasis):
        if k in used_states:
            print(k,quasi)

parse_files()
link_lines()
