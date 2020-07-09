from dataclasses import dataclass
from parsita import *
from parsita.util import constant,splat
import os
from random import shuffle

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

#### CLASSES ####

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

    def __repr__(self):
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
class End:
    is_start: bool
    next_quasis: list

@dataclass
class State:
    instruction: int #refers to an index in quasis
    acc: int
    transitions: dict #{symbol:[symbol,acc,step)}
    direction: int #+1 or -1

@dataclass(frozen=True,eq=True)
class Symbol:
    symbol: str
    offset: int = 0

    def __repr__(self):
        return 'Sym(\''+self.symbol+'\'+'+str(self.offset)+')'

#### STATE-EQUALITY FUNCTIONS ####

def get_none_transition(state,symbol,k):
    if symbol in state.transitions:
        transition = state.transitions[symbol]
        if transition[0]==None:
            return [symbol] + transition[1:]
        else:
            return transition
    else:
        return [symbol,0,k,False]
    

def equal_states(k,j):
    state1,state2 = quasis[k],quasis[j]
    if type(state1)!=State or type(state2)!=State:
        return False
    for symbol in state1.transitions.keys()|state2.transitions.keys():
        transition1 = get_none_transition(state1,symbol,k)
        transition2 = get_none_transition(state2,symbol,j)
        if not (transition1[0]==transition2[0] and transition1[3]==transition2[3] and
                (transition1[2]==transition2[2] or transition1[2]==k and transition2[2]==j)):
            return False
    return True

#### PARSERS ####

class ImmParser(TextParsers,whitespace=None):
    imm1 = reg(r'[01]') > int
    imm2d = reg(r'[0123]') > int
    imm2b = reg(r'[01]{2}') > (lambda x: int(x,2))
    imm2 = imm2b | imm2d

class MapParser(TextParsers):
    state = ImmParser.imm2 & opt('x' >> ImmParser.imm1) > (lambda x: tuple([x[0]]+x[1]))
    mapping = state & ':' >> state
    map_ = '{' >> repsep(mapping, ',') << '}' > dict

class LineParser(TextParsers,whitespace=None):
    s = reg(r'[ \t]+')
    valid = reg(r'[A-Za-z][A-Za-z0-9_]*')
    label = valid << ':' > Label
    arg = reg(r'[vimVIM][A-Za-z0-9_]*')
    function_header = 'FUNC' >>s>> valid & rep(s >> arg) > splat(FunctionHeader)
    function_call = valid & rep(s >> (MapParser.map_ | ImmParser.imm2 | valid)) > splat(FunctionCall)
    memory_command = lit('LOAD','STORE') & opt('NEXT') & opt('BIG')
    end = lit('END') > constant(End(False,[]))
    line = end | label | function_header | function_call

#### PRE-COMPILATION FUNCTIONS ####

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

def find_next_function(lines,k,label):
    for j in range(k,len(lines)):
        if label=='null':
            if type(lines[j])==FunctionCall or type(lines[j])==End and not lines[j].is_start:
                return j
        else:
            if type(lines[j])==Label and lines[j].name==label:
                label='null'
    return find_next_function(lines,k,'null')

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

#### GENERATORS ####

def get_quasis(types=[FunctionCall,Instruction,State,End]):
    global quasis
    for k,quasi in enumerate(quasis):
        if type(quasi) in types:
            yield k,quasi

def get_quasis_from(quasi,types=[FunctionCall,Instruction,State,End]):
    global quasis
    if type(quasi)==State and quasi.transitions:
        for symbol,transition in quasi.transitions.items():
            if type(quasis[transition[2]]) in types:
                yield symbol,transition,quasis[transition[2]]
            elif State in types:
                yield from get_states_of(transition[2])
    elif type(quasi) in [FunctionCall,Instruction,End] and quasi.next_quasis:
        for k,next_quasi in enumerate(quasi.next_quasis):
            if next_quasi:
                if type(quasis[next_quasi]) in types:
                    yield k,next_quasi,quasis[next_quasi]
                elif State in types:
                    yield from get_states_of(next_quasi)

def get_states_of(n_step):
    for k,state in get_quasis([State]):
        if state.instruction == n_step:
            yield k,state

#### COMPILATION FUNCTIONS ####
            
def evaluate_function_call(function_call):
    global functions, quasis
    for function in functions:
        if function.command==function_call.command:
            assert len(function.params)==len(function_call.args)
            index = len(quasis)
            argsdict = dict(zip(function.params,function_call.args))
            quasis += [None]*len(function.lines)
            replacements = []
            for k,line in enumerate(function.lines):
                if type(line)==FunctionCall:
                    new_function = functioncall2instruction(line.apply(index,argsdict))
                    quasis[index+k] = new_function
                    if type(new_function)==FunctionCall:
                        new_index = len(quasis)
                        evaluate_function_call(new_function)
                        new_function.next_quasis = [new_index]
                elif type(line)==End:
                    if line.is_start:
                        quasis[index+k] = End(True,[index+line.next_quasis[0]])                        
                    else:
                        quasis[index+k] = End(False,function_call.next_quasis)

def remove_ends():
    global quasis
    altered = False
    for _,quasi in get_quasis():
        for k,_,next_quasi in get_quasis_from(quasi,[FunctionCall,End]):
            try:
                _,quasi.next_quasis[k],_ = next(get_quasis_from(next_quasi))
                altered = True
            except StopIteration:
                pass                
    return altered    

def get_found_transitions(n_step,acc):
    global quasis
    instruction = quasis[n_step]
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
            transitions = {symbol:transitions[symbol][:] for symbol in transitions}
        else:
            return {},None
    #"Other primitive commands" except SEZ
    if command in ['SRLs','SRL2s','ZEROs']:
        direction = 0
    else:
        direction = +1
    if transitions:
        for symbol in transitions:
            transitions[symbol] += [n_step,False]
        transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
        transitions[Symbol(instruction.vard,direction)] = [None,acc,instruction.next_quasis[0],True]
        return transitions,2*direction-1
    #SEZ
    if command=='SEZ':
        return {'0':['0',1,n_step,False],'1':['1',0,instruction.next_quasis[0],True],
                     Symbol(instruction.vard,+1):[None,1,instruction.next_quasis[0],True]},+1
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
            transitions[symbol] += [instruction.next_quasis[0],True]
        transitions.update(
            {'0\'':['0\'',acc,n_step,False],'1\'':['1\'',acc,n_step,False],
            Symbol(instruction.vard,1-instruction.big):[None,acc,instruction.next_quasis[1],True]})
        return transitions,1-2*instruction.big
    #UNREAD
    if command=='UNREAD':
        return {'0':['0',acc,n_step,False],'1':['1',acc,n_step,False],
                '0\'':['0',acc,n_step,False],'1\'':['1',acc,n_step,False],
                     Symbol(instruction.vard,0):[None,acc,instruction.next_quasis[0],True]},-1

def replace_links(a,b):
    global quasis
    for _,quasi in get_quasis([Instruction,End]):
        for k in range(len(quasi.next_quasis)):
            if quasi.next_quasis[k] == a:
                quasi.next_quasis[k] = b
    for _,quasi in get_quasis([State]):
        for symbol in quasi.transitions:
            if quasi.transitions[symbol][2] == a:
                quasi.transitions[symbol][2] = b

def instructions2states():
    global quasis
    quasis[0] = State(instruction=0,acc=0,
                      transitions={0:[None,0,quasis[0].next_quasis[0],True]},direction=None)
    for k,instr in get_quasis([Instruction]):
        if instr.command in [
                'NOTs', 'COMPs','SLLs','SRLs','SLL2s','SRL2s','ZEROs','ADDIs','SUBIs','LOAD','STORE','SEZ','UNREAD']:
            for acc in range(4):
                transitions,direction = get_found_transitions(k,acc)
                quasis.append(State(instruction=k,acc=acc,transitions=transitions,direction=direction))
                

def validate_maps(map_):
    sizes = {(len(key),len(map_[key])) for key in map_}    
    assert len(sizes)==1
    return sizes.pop()

def apply_posts():
    global quasis
    altered = False
    for _,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        for symbol,transition,next_instr in get_quasis_from(state,[Instruction]):
            state_change = -1
            if next_instr.command=='JUMP':
                state_change = 0
            elif next_instr.command=='BRANCH':
                state_change = transition[1]
            elif next_instr.command=='LOADI' and next_instr.loadto=='ACC':
                transition[1] = next_instr.imm
                state_change = 0
            elif next_instr.command=='MAP':
                size = validate_maps(next_instr.map_)
                if size==(2,1):
                    assert instruction.command=='LOAD' and instruction.loadto=='TEMP'
                    if (transition[1],int(symbol)) in next_instr.map_:
                        transition[1] = next_instr.map_[(transition[1],int(symbol))][0]
                    state_change = 0
                elif size==(1,1):
                    if (transition[1],) in next_instr.map_:
                        transition[1] = next_instr.map_[(transition[1],)][0]             
                    state_change = 0
            if state_change>=0:
                transition[2] = next_instr.next_quasis[state_change]
                altered = True
    return altered

def apply_pres():
    global quasis
    altered = False
    for k,instr in get_quasis([Instruction]):
        if (instr.command=='MAP' and validate_maps(instr.map_)==(1,2) or
                instr.command=='LOADI' and instr.loadto=='TEMP'):
            for _,state in get_quasis_from(instr,[State]):
                for symbol in ['0','1']:
                    transition = state.transitions[symbol]
                    if instr.command=='MAP' and (state.acc,) in instr.map_:
                        mapping = instr.map_[(state.acc,)]
                        transition[0] = str(mapping[1]) + transition[0][1:]
                        transition[1] = mapping[0]
                    else:
                        transition[0] = str(instr.imm) + transition[0][1:]
                altered = True
            replace_links(k,instr.next_quasis[0])
            quasis[k] = None
    return altered

def adjacent_bits(instruction,next_instruction):
    return (type(instruction)==Instruction and
            type(next_instruction)==Instruction and
            instruction.command in ['LOAD','STORE'] and
            next_instruction.command in ['LOAD','STORE'] and
            instruction.vard==next_instruction.vard and
            instruction.big==next_instruction.big)

def skip_searches():
    global quasis
    altered = False
    for k,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        command = instruction.command if state.instruction else None
        if command in ['LOAD','STORE'] and not instruction.read:
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if k!=transition[2] and adjacent_bits(instruction,next_instruction):
                    next_symbol = transition[0] if transition[0] else symbol
                    state.transitions[symbol] = next_state.transitions[next_symbol]
                    altered = True
    return altered                        
                    


def find_state(acc,n_step):
    global quasis
    if type(quasis[n_step])==Instruction:
        for k,state in get_states_of(n_step):
            if state.acc==acc:
                return k
    else:
        return step

def get_init_acc(acc,n_step):
    instruction = quasis[n_step]
    command,imm = instruction.command,instruction.imm
    if command in ['COMPs','SEZ']:
        return 1
    elif command in ['NOTs','ZEROs','LOAD','STORE','UNREAD']:
        return acc
    elif command in ['SLLs','SRLs','SLL2s','SRL2s','ADDIs','SUBIs']:
        return imm

def stitch_acc():
    global quasis
    for _,state in get_quasis([State]):
        for _,transition,_ in get_quasis_from(state,[Instruction]):
            transition[2] = find_state(
                get_init_acc(transition[1],transition[2]) if transition[3] else transition[1],
                transition[2])

def find_successors(k):
    global quasis,used_states
    for _,j,_ in get_quasis_from(quasis[k],[End,State]):
        if type(j)==list:
            j = j[2]
        if not j in used_states:
                used_states.add(j)
                find_successors(j)

def merge_links():
    altered = False
    for k,state1 in get_quasis([State]):
        for j,state2 in get_quasis([State]):
            if j>k and equal_states(k,j):
                quasis[j]=None
                replace_links(j,k)
                altered = True
    return altered

#### OTHER OPTIMIZATIONS ####

def skip_unreads():
    global explored_states
    for k,state in get_quasis([State]):
        instruction = quasis[state.instruction]
        if state.instruction and instruction.command=='UNREAD':
            for _,transition,_ in get_quasis_from(state,[State,End]):
                explored_states = set()
                if transition[3] and  will_unread(transition[2],instruction.vard):
                    replace_links(k,transition[2])

def will_unread(k,var):
    global explored_states
    explored_states.add(k)
    state = quasis[k]
    if type(state)==State:
        instruction = quasis[state.instruction]
        if instruction.vard==var:
            if instruction.command in ['LOAD','STORE']:
                return False
            elif instruction.command in ['NOTs', 'COMPs','SLLs','SRLs','SLL2s','SRL2s','ZEROs','ADDIs','SUBIs','UNREAD']:
                return True
    else:
        return True
    for _,transition,_ in get_quasis_from(state,[State,End]):
        if not transition[2] in explored_states:
            if not will_unread(transition[2],var):
                return False
    return True
		
#### MAIN FUNCTION ####

def compile_function(function_call,order=None):
    global quasis, used_states, rules, best_order
    quasis = []
    function = LineParser.line.parse(function_call).value
    function.next_quasis = [None]
    evaluate_function_call(function)
    more_ends = True
    while more_ends:
        more_ends = remove_ends()
    instructions2states()
    more_posts = True
    while more_posts:
        more_posts = apply_posts() or apply_pres()
    stitch_acc()
    skip_searches()
    more_merges = True
    while more_merges:
        more_merges = merge_links()
    skip_unreads()
    used_states = {0}
    find_successors(0)
    directions = {}
    states2searches()
    if not order:
        order = list({instruction.vard for _,instruction in
                      get_quasis([Instruction]) if instruction.vard})
    best_order,best_score = order,score(order)
    for _ in range(len(order)*2):
        shuffle(order)
        new_order,new_score = find_optimal_order(order)
        if new_score<best_score:
            best_order,best_score = new_order,new_score
    states2rules(best_order)
    searches2rules(best_order)

#### SYMBOL CONVERSIONS ####

def sign2char(sign):
    if sign<0:
        return 'L'
    elif sign>0:
        return 'R'
    else:
        return ''

def symbol2string(symbol,order):
    if type(symbol)==Symbol:
        return order[(order.index(symbol.symbol)+symbol.offset)%len(order)]
    elif symbol==None:
        return None
    else:
        return str(symbol)

def symbol2int(symbol,order):
    if type(symbol)==Symbol:
        return order.index(symbol.symbol)+symbol.offset
    else:
        return int(symbol)

#### TAPE OPTIMIZATION ####

def states2searches():
    global to_symbols, from_symbols, transition_symbols
    to_symbols = {}
    transition_symbols = {}
    for k,state in get_quasis([State]):
        if k in used_states:
            instruction = quasis[state.instruction]
            if state.instruction:
                to_symbols[k] = Symbol(instruction.vard,int(state.direction<0)) 
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if transition[3] and not adjacent_bits(instruction,next_instruction):
                    if not transition[2] in transition_symbols:
                        transition_symbols[transition[2]] = {}
                    transition_symbols[transition[2]][k] = (
                        symbol if type(symbol) in [Symbol,int] else Symbol(instruction.vard,1/2) )
    from_symbols = {key:set(value.values()) for key,value in transition_symbols.items()}

def find_optimal_order(order):
    best_order = order
    original_score = score(order)
    best_score = original_score
    for a in range(len(order)):
        for b in range(len(order)+1):
            new_order = move_element(order,a,b)
            if new_order:
                new_score = score(new_order)
                if new_score<best_score:
                    best_score = new_score
                    best_order = new_order		    
    if best_score<original_score:
        return find_optimal_order(best_order)
    else:
        return best_order,best_score
    
def move_element(A,a,b):
    if b>a+1:
        return A[:a]+A[a+1:b]+A[a:a+1]+A[b:]
    elif b<a:
        return A[:b]+A[a:a+1]+A[b:a]+A[a+1:]

def score(order):
    total = 0
    for k in from_symbols:
        to_symbol = to_symbols[k]
        left = False
        right = False
        for from_symbol in from_symbols[k]:
            offset = symbol2int(to_symbol,order) - symbol2int(from_symbol,order)
            if offset<0:
                left = True
            if offset>0:
                right = True
        total += (left+right)
    return total         

#### RULE CREATION ####

def states2rules(order):
    global rules
    rules = {}
    for k,state in get_quasis([State]):
        if k in used_states:
            instruction = quasis[state.instruction]
            for symbol,transition,next_state in get_quasis_from(state,[State]):
                next_instruction = quasis[next_state.instruction]
                if transition[2] in transition_symbols and k in transition_symbols[transition[2]]:
                    current_var = symbol2int(transition_symbols[transition[2]][k],order)
                    next_var = symbol2int(to_symbols[transition[2]],order)
                    direction = sign2char(next_var-current_var)
                    rules[(str(k),symbol2string(symbol,order))] = (
                             str(transition[2])+direction,
                             symbol2string(transition[0],order),
                             direction if direction else sign2char(next_state.direction))
                else:
                    rules[(str(k),symbol2string(symbol,order))] = (
                            str(transition[2]),
                            symbol2string(transition[0],order),
                            sign2char(state.direction))
            for symbol,transition,end in get_quasis_from(state,[End]):
                rules[(str(k),symbol2string(symbol,order))] = (
                    None,
                    symbol2string(transition[0],order),
                    '')

def searches2rules(order):
    for k in {value[0] for value in rules.values() if value[0] and value[0][-1] in ['L','R']}:
        rules[(k,None)] = (k,None,k[-1])
        rules[(k,symbol2string(to_symbols[int(k[:-1])],order))] = (k[:-1],None,sign2char(quasis[int(k[:-1])].direction))

#### OUTPUT ####

def morphett_output():
    replacements = {'0':'0','1':'1','0\'':'2','1\'':'3'}
    k = 97
    for var in best_order:
        if len(var)>1:
            while chr(k) in best_order:
                k+=1
            replacements[var]=chr(k)
        else:
            replacements[var]=var
    result = ''
    for key,value in rules.items():
        if key[0]!='0':
            result += ' '.join([
                key[0],
                replacements[key[1]] if key[1] else '*',
                replacements[value[1]] if value[1] else '*',
                value[2].lower() if value[2] else '*',
                value[0] if value[0] else 'halt'
            ]) + '\n'
        else:
            result += 'Initial state: ' + value[0] + '\n'
    return result

#### TURING SIMULATOR

#Have all programs start on the second space on the tape
#The initial state is found in quasis[0], with either an R or nothing
def simulate(tape,position=1,state=None):
    if not state:
        state = rules[('0','0')][0]
    steps = 0
    while True:
        try:
            rule = rules[(state,tape[position])]
        except KeyError:
            rule = rules[(state,None)]
        if rule[1]:
            tape[position] = rule[1]
        if rule[0]:
            state = rule[0]
        else:
            break
        if rule[2]=='L':
            position-=1
        elif rule[2]=='R':
            position+=1
        steps+=1
        if steps%100000==0:
            print(steps)

def create_tape(default_size,sizes={},values={}):
    tape = []
    for var in best_order:
        tape.append(var)
        size = sizes[var] if var in sizes else default_size
        value = bin(values[var]%(2**size) if var in values else 0)[2:]
        for k in range(1,size+1):
            tape.append(value[-k] if k<=len(value) else '0')
    tape.append(best_order[0])
    return tape

def get_tape_values(tape):
    values = {}
    var = None
    for c in tape:
        if c[0] in ['0','1']:
            res += c[0]
        else:
            if var:
                values[var] = int(res[::-1],2)
            var = c
            res = ''
    return values
            
            

#### PRE-COMPILATION ####

parse_files()
link_lines()
