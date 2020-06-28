Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> import os
>>> os.listdir()
['.git', 'ACSL Turing Language.docx', 'add.s', 'Mathison Compilation.docx', 'Mathison.docx', 'MathisonCompiler.py', '~$SL Turing Language.docx', '~$thison Compilation.docx', '~$thison.docx', '~WRL2874.tmp']
>>> for filename in os.listdir():
	if filename.endswith('.s'):
		print(filename)

		
add.s
>>> raise ValueError
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    raise ValueError
ValueError
>>> raise Exception
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    raise Exception
Exception
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
Traceback (most recent call last):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 44, in <module>
    @dataclass
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 966, in dataclass
    return wrap(_cls)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 958, in wrap
    return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 809, in _process_class
    for name, type in cls_annotations.items()]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 809, in <listcomp>
    for name, type in cls_annotations.items()]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\dataclasses.py", line 702, in _get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'list'> for field lines is not allowed: use default_factory
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
		     
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 178, in parse_files
    for filename in os.listdir():
NameError: name 'os' is not defined
>>> import os
		     
>>> parse_files()
		     
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 199, in parse_files
    function.lines = [End(True)]
TypeError: __init__() missing 1 required positional argument: 'next_quasis'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> import os
		     
>>> parse_files()
		     
>>> functions
		     
[]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
		     
>>> functions
		     
[]
>>>     for filename in os.listdir():
        if filename.endswith('.s'):
            text = open(filename,'r').read()
            lines = [line.strip() for line in text.split('\n')]
		     
SyntaxError: unexpected indent
>>> for filename in os.listdir():
    if filename.endswith('.s'):
        text = open(filename,'r').read()
        lines = [line.strip() for line in text.split('\n')]

		     
>>> len(lines)
		     
16
>>> lines
		     
['FUNC ADD vard var0 var1', '', 'start:', 'LOADNEXT var0 TEMP', 'MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2}', 'LOADNEXT var1 TEMP', 'MAP {0x0:0, 0x1:1, 1x0:1, 1x1:2, 2x0:2, 2x1:3}', 'MAP {0:0x0, 1:0x1, 2:1x0, 3:1x1}', 'STORENEXT vard TEMP', 'JUMP start', '', 'oob:', 'UNREAD var0', 'UNREAD var1', 'UNREAD vard', 'END']
>>> for line in lines:
                if line:
                    parsed_line = LineParser.line.parse(line).value
		     print(parsed_line)
		     
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
		     
>>> for line in lines:
	if line:
		parsed_line = LineParser.line.parse(line).value
		print(parsed_line)

		     
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=None)
Label(name='start')
Instruction(LOAD, next_quasis=None)
Instruction(MAP, next_quasis=None)
Instruction(LOAD, next_quasis=None)
Instruction(MAP, next_quasis=None)
Instruction(MAP, next_quasis=None)
Instruction(STORE, next_quasis=None)
Instruction(JUMP, next_quasis=None)
Label(name='oob')
Instruction(UNREAD, next_quasis=None)
Instruction(UNREAD, next_quasis=None)
Instruction(UNREAD, next_quasis=None)
FunctionCall(command='END', args=[])
>>> )))
SyntaxError: invalid syntax
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> functions
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    functions
NameError: name 'functions' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> functions
[]
>>> for filename in os.listdir():
        if filename.endswith('.s'):
            text = open(filename,'r').read()
            lines = [line.strip() for line in text.split('\n')]

            
>>> for line in lines:
	if line:
		parsed_line = LineParser.line.parse(line).value
		print(parsed_line)

		
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=None)
Label(name='start')
FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}])
FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}])
FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}])
FunctionCall(command='STORENEXT', args=['vard', 'TEMP'])
FunctionCall(command='JUMP', args=['start'])
Label(name='oob')
FunctionCall(command='UNREAD', args=['var0'])
FunctionCall(command='UNREAD', args=['var1'])
FunctionCall(command='UNREAD', args=['vard'])
END
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> functions
[]
>>> functions = []
>>> function = FunctionHeader
>>> function.lines.add('hello')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    function.lines.add('hello')
AttributeError: 'NoneType' object has no attribute 'add'
>>> function.lines.apend('hello')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    function.lines.apend('hello')
AttributeError: 'NoneType' object has no attribute 'apend'
>>> function.lines.append('hello')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    function.lines.append('hello')
AttributeError: 'NoneType' object has no attribute 'append'
>>> function.lines = ['a']
>>> function.lines.append('hello')
>>> functions.append(function)
>>> function
<class '__main__.FunctionHeader'>
>>> functions
[<class '__main__.FunctionHeader'>]
>>> functions[0]
<class '__main__.FunctionHeader'>
>>> function = FunctionHeader('a',[])
>>> function.lines = ['b']
>>> function.lines.append('c')
>>> functions = []
>>> functions.append(function)
>>> functions
[FunctionHeader(command='a', params=[], lines=['b', 'c'])]
>>> function = None
>>> functions
[FunctionHeader(command='a', params=[], lines=['b', 'c'])]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> functions = []
>>> parse_files()
>>> functions
[]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start')])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP']), FunctionCall(command='JUMP', args=['start'])])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP']), FunctionCall(command='JUMP', args=['start']), Label(name='oob')])
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP']), FunctionCall(command='JUMP', args=['start']), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'])])Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 191, in parse_files
    print(function)
KeyboardInterrupt
>>> for line in lines:
	if line:
		parsed_line = LineParser.line.parse(line).value
		print(parsed_line)

		
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    for line in lines:
NameError: name 'lines' is not defined
>>> for filename in os.listdir():
        if filename.endswith('.s'):
            text = open(filename,'r').read()
            lines = [line.strip() for line in text.split('\n')]

            
>>> for line in lines:
	if line:
		parsed_line = LineParser.line.parse(line).value
		print(parsed_line)

		
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=None)
Label(name='start')
FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}])
FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}])
FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}])
FunctionCall(command='STORENEXT', args=['vard', 'TEMP'])
FunctionCall(command='JUMP', args=['start'])
Label(name='oob')
FunctionCall(command='UNREAD', args=['var0'])
FunctionCall(command='UNREAD', args=['var1'])
FunctionCall(command='UNREAD', args=['vard'])
END
>>> type(LineParser.line.parse(line).value)
<class 'str'>
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 189, in parse_files
    parsed_line = LineParser.line.parse(line).value
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\parsita\options.py", line 31, in default_parse_method
    return completely_parse_reader(self, reader)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\parsita\parsers.py", line 169, in completely_parse_reader
    result = (parser << eof).consume(reader)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\parsita\parsers.py", line 446, in consume
    status1 = self.left.consume(reader)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\parsita\parsers.py", line 378, in consume
    status = parser.consume(reader)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\parsita\parsers.py", line 667, in consume
    return Continue(status.remainder, self.converter(status.value)).merge(status)
TypeError: __init__() missing 1 required positional argument: 'next_quasis'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> functions
[FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP']), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP']), FunctionCall(command='JUMP', args=['start']), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0']), FunctionCall(command='UNREAD', args=['var1']), FunctionCall(command='UNREAD', args=['vard']), End(is_start=False, next_quasis=[])])]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 214, in parse_files
    for k,quasi in enumerate(quasis):
NameError: name 'quasis' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 225, in parse_files
    quasi.next_quasis = [find_next_instruction(0,'null')]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 173, in find_next_instruction
    for j in range(k,len(quasis)):
NameError: name 'quasis' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    parse_files()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 225, in parse_files
    quasi.next_quasis = [find_next_function(0,'null')]
TypeError: find_next_function() missing 1 required positional argument: 'label'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> functions
[FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=None), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=None), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=None), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=None), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=None), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=None), FunctionCall(command='JUMP', args=['start'], next_quasis=None), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=None), FunctionCall(command='UNREAD', args=['var1'], next_quasis=None), FunctionCall(command='UNREAD', args=['vard'], next_quasis=None), End(is_start=False, next_quasis=[])])]
>>> len(functions)
1
>>> link_lines()
>>> len(functions)
1
>>> functions
[FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13]), End(is_start=False, next_quasis=[])])]
>>> for line in functions[0].lines:
	print(line)

	
End(is_start=True, next_quasis=[2])
Label(name='start')
FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4])
FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6])
FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7])
FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8])
FunctionCall(command='JUMP', args=['start'], next_quasis=[2])
Label(name='oob')
FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11])
FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12])
FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
End(is_start=False, next_quasis=[])
>>> for k,line in enumerate(functions[0].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[2])
1 Label(name='start')
2 FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3])
3 FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4])
4 FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5])
5 FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6])
6 FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7])
7 FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8])
8 FunctionCall(command='JUMP', args=['start'], next_quasis=[2])
9 Label(name='oob')
10 FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11])
11 FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12])
12 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
13 End(is_start=False, next_quasis=[])
>>> Success
<class 'parsita.state.Success'>
>>> bool(Success)
True
>>> Failure
<class 'parsita.state.Failure'>
>>> bool(Failure)
True
>>> lit('LOAD','STORE')
'LOAD' | 'STORE'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> link_lines()
>>> for k,line in enumerate(functions[0].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[2])
1 Label(name='start')
2 FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10])
3 FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4])
4 FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5, 10])
5 FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6])
6 FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7])
7 FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10])
8 FunctionCall(command='JUMP', args=['start'], next_quasis=[2])
9 Label(name='oob')
10 FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11])
11 FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12])
12 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
13 End(is_start=False, next_quasis=[])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> link_lines()
>>> for k,line in enumerate(functions[1].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[2])
1 Label(name='start')
2 FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10])
3 FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}], next_quasis=[4])
4 FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5, 10])
5 FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}], next_quasis=[6])
6 FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7])
7 FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10])
8 FunctionCall(command='JUMP', args=['start'], next_quasis=[2])
9 Label(name='oob')
10 FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11])
11 FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12])
12 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
13 End(is_start=False, next_quasis=[])
>>> for k,line in enumerate(functions[-1].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='ZERO', args=['varr'], next_quasis=[3])
2 Label(name='start')
3 FunctionCall(command='SLLs', args=['varr', 1], next_quasis=[4])
4 FunctionCall(command='SLT', args=['varr', 'var1'], next_quasis=[5])
5 FunctionCall(command='MAP', args=[{(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}], next_quasis=[6])
6 FunctionCall(command='STORENEXTBIG', args=['vard', 'TEMP'], next_quasis=[7, 12])
7 FunctionCall(command='BRANCH', args=['sub', 'start', 'null', 'null'], next_quasis=[9, 3, 1, 1])
8 Label(name='sub')
9 FunctionCall(command='SUB', args=['varr', 'var1'], next_quasis=[10])
10 FunctionCall(command='JUMP', args=['start'], next_quasis=[3])
11 Label(name='oob')
12 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
13 End(is_start=False, next_quasis=[])
>>> for k,line in enumerate(functions[2].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[2])
1 Label(name='start')
2 FunctionCall(command='LOADNEXT', args=['var0', 'ACC'], next_quasis=[3, 7])
3 FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[4, 7])
4 FunctionCall(command='MAP', args=['map'], next_quasis=[5])
5 FunctionCall(command='STORENEXT', args=['vard', 'ACC'], next_quasis=[7, 7])
6 Label(name='oob')
7 FunctionCall(command='UNREAD', args=['var0'], next_quasis=[8])
8 FunctionCall(command='UNREAD', args=['var1'], next_quasis=[9])
9 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[10])
10 End(is_start=False, next_quasis=[])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> parse_files()
>>> link_lines()
>>> for k,line in enumerate(functions[2].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[2])
1 Label(name='start')
2 FunctionCall(command='LOADNEXT', args=['var0', 'ACC'], next_quasis=[3, 7])
3 FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[4, 7])
4 FunctionCall(command='MAP', args=['map'], next_quasis=[5])
5 FunctionCall(command='STORENEXT', args=['vard', 'ACC'], next_quasis=[7, 7])
6 Label(name='oob')
7 FunctionCall(command='UNREAD', args=['var0'], next_quasis=[8])
8 FunctionCall(command='UNREAD', args=['var1'], next_quasis=[9])
9 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[10])
10 End(is_start=False, next_quasis=[])
>>> for k,line in enumerate(functions[-1].lines):
	print(k,line)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='ZERO', args=['varr'], next_quasis=[3])
2 Label(name='start')
3 FunctionCall(command='SLLs', args=['varr', 1], next_quasis=[4])
4 FunctionCall(command='SLT', args=['varr', 'var1'], next_quasis=[5])
5 FunctionCall(command='MAP', args=[{(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}], next_quasis=[6])
6 FunctionCall(command='STORENEXTBIG', args=['vard', 'TEMP'], next_quasis=[7, 12])
7 FunctionCall(command='BRANCH', args=['sub', 'start', 'null', 'null'], next_quasis=[9, 3, 9, 9])
8 Label(name='sub')
9 FunctionCall(command='SUB', args=['varr', 'var1'], next_quasis=[10])
10 FunctionCall(command='JUMP', args=['start'], next_quasis=[3])
11 Label(name='oob')
12 FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
13 End(is_start=False, next_quasis=[])
>>> ['a','b','c'].index('c')
2
>>> ['a','b','c'].find('c')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    ['a','b','c'].find('c')
AttributeError: 'list' object has no attribute 'find'
>>> ['a','b','c'].index('d')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    ['a','b','c'].index('d')
ValueError: 'd' is not in list
>>> a=[0,1,2]
>>> a += [None]*3
>>> a
[0, 1, 2, None, None, None]
>>> a[4]=7
>>> a
[0, 1, 2, None, 7, None]
>>> a = [0,1,2]
>>> b=a
>>> b[1]=7
>>> a
[0, 7, 2]
>>> a = [0,1,2]
>>> b=a[:]
>>> b[1]=7
>>> b
[0, 7, 2]
>>> a
[0, 1, 2]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> LineParser.memory_command.parse('LOADNEXT')
Success('LOAD')
>>> LineParser.memory_command.parse('LOAD')
Success('LOAD')
>>> LineParser.memory_command.parse('LOADHI')
Failure("Expected 'NEXT' or 'BIG' or end of source but found 'HI'\nLine 1, character 5\n\nLOADHI\n    ^ ")
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> is_memory_command('LOADHI')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    is_memory_command('LOADHI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 228, in is_memory_command
    memory_command = LineParser.memory_command.parse(quasi.command)
NameError: name 'quasi' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> LineParser.memory_command.parse('LOADNEXT')
Success(['LOAD', ['NEXT'], []])
>>> is_memory_command('LOADHI')
>>> is_memory_command('LOADNEXT')
['LOAD', ['NEXT'], []]
>>> is_memory_command('LOADNEXT')[0]
'LOAD'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C D')
>>> function
Success(FunctionCall(command='RECP', args=['A', 'B', 'C', 'D'], next_quasis=None))
>>> evaluate_function_call(function)
>>> len(quasis)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    len(quasis)
NameError: name 'quasis' is not defined
>>> len(functions)
0
>>> parse_files()
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 254, in evaluate_function_call
    if function.command==function_call.command:
AttributeError: 'Success' object has no attribute 'command'
>>> function = LineParser.line.parse('RECP A B C D').value
>>> len(quasis)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    len(quasis)
NameError: name 'quasis' is not defined
>>> quasis=[]
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 255, in evaluate_function_call
    assert len(function.params)==len(function_call.args)
AssertionError
>>> function = LineParser.line.parse('RECP A B C').value
>>> quasis=[]
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 267, in evaluate_function_call
    quasis[index+k] = line.apply(index)
TypeError: apply() takes 1 positional argument but 2 were given
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> quasis=[]
>>> parse_files()
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 267, in evaluate_function_call
    quasis[index+k] = line.apply(index)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 115, in apply
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
TypeError: __init__() got an unexpected keyword argument 'is_start'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> quasis=[]
>>> parse_files()
>>> 
>>> 
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 264, in evaluate_function_call
    evaluate_function_call(new_function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 261, in evaluate_function_call
    new_function = functioncall2instruction(line.apply(index,argsdict))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 63, in apply
    args=[(argsdict[arg] if arg in argsdict else arg) for arg in self.args],
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 63, in <listcomp>
    args=[(argsdict[arg] if arg in argsdict else arg) for arg in self.args],
TypeError: unhashable type: 'dict'
>>> len(quasis)
24
>>> quasis
[End(is_start=True, next_quasis=[1]), FunctionCall(command='ZERO', args=['B'], next_quasis=[3]), None, <__main__.Instruction object at 0x038A3170>, FunctionCall(command='SLT', args=['B', 'var1'], next_quasis=[5]), None, None, None, None, None, None, None, None, None, End(is_start=True, next_quasis=[16]), None, <__main__.Instruction object at 0x0389C750>, <__main__.Instruction object at 0x0389C4B0>, None, None, None, None, None, None]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> quasis=[]
>>> parse_files()
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 264, in evaluate_function_call
    evaluate_function_call(new_function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 261, in evaluate_function_call
    new_function = functioncall2instruction(line.apply(index,argsdict))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 63, in apply
    args=[(argsdict[arg] if arg in argsdict else arg) for arg in self.args],
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 63, in <listcomp>
    args=[(argsdict[arg] if arg in argsdict else arg) for arg in self.args],
TypeError: unhashable type: 'dict'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> quasis=[]
>>> parse_files()
>>> 
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 264, in evaluate_function_call
    evaluate_function_call(new_function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 255, in evaluate_function_call
    assert len(function.params)==len(function_call.args)
AssertionError
>>> len(quasis)
24
>>> quasis
[End(is_start=True, next_quasis=[1]), FunctionCall(command='ZERO', args=['B'], next_quasis=[3]), None, <__main__.Instruction object at 0x038C3390>, FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5]), <__main__.Instruction object at 0x038C3750>, <__main__.Instruction object at 0x038BC970>, <__main__.Instruction object at 0x038BC650>, None, FunctionCall(command='SUB', args=['B', 'var1'], next_quasis=[10]), None, None, None, None, End(is_start=True, next_quasis=[16]), None, <__main__.Instruction object at 0x038BC810>, <__main__.Instruction object at 0x038BC6F0>, <__main__.Instruction object at 0x038BC7B0>, <__main__.Instruction object at 0x038BC770>, None, <__main__.Instruction object at 0x038BC730>, <__main__.Instruction object at 0x038BC6B0>, End(is_start=False, next_quasis=[5])]
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='ZERO', args=['B'], next_quasis=[3])
2 None
3 Instruction(SLLs, next_quasis=None)
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, next_quasis=None)
6 Instruction(STORE, next_quasis=None)
7 Instruction(BRANCH, next_quasis=None)
8 None
9 FunctionCall(command='SUB', args=['B', 'var1'], next_quasis=[10])
10 None
11 None
12 None
13 None
14 End(is_start=True, next_quasis=[16])
15 None
16 Instruction(LOAD, next_quasis=None)
17 Instruction(LOAD, next_quasis=None)
18 Instruction(MAP, next_quasis=None)
19 Instruction(BRANCH, next_quasis=None)
20 None
21 Instruction(UNREAD, next_quasis=None)
22 Instruction(UNREAD, next_quasis=None)
23 End(is_start=False, next_quasis=[5])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> quasis=[]
>>> parse_files()
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 268, in evaluate_function_call
    evaluate_function_call(new_function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 259, in evaluate_function_call
    assert len(function.params)==len(function_call.args)
AssertionError
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='ZERO', args=['B'], next_quasis=[3])
2 None
3 Instruction(SLLs, next_quasis=[4])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, next_quasis=[6])
6 Instruction(STORE, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[9, 3, 9, 9])
8 None
9 FunctionCall(command='SUB', args=['B', 'var1'], next_quasis=[10])
10 None
11 None
12 None
13 None
14 End(is_start=True, next_quasis=[16])
15 None
16 Instruction(LOAD, next_quasis=[17, 21])
17 Instruction(LOAD, next_quasis=[18, 21])
18 Instruction(MAP, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[16, 21, 21, 21])
20 None
21 Instruction(UNREAD, next_quasis=[22])
22 Instruction(UNREAD, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> parse_files()
>>> link_lines()
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 260, in evaluate_function_call
    index = len(quasis)
NameError: name 'quasis' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 FunctionCall(command='ZERO', args=['B'], next_quasis=[3])
2 None
3 Instruction(SLLs, next_quasis=[4])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, next_quasis=[6])
6 Instruction(STORE, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[9, 3, 9, 9])
8 None
9 FunctionCall(command='SUBs', args=['B', 'var1'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[3])
11 None
12 Instruction(UNREAD, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[16])
15 None
16 Instruction(LOAD, next_quasis=[17, 21])
17 Instruction(LOAD, next_quasis=[18, 21])
18 Instruction(MAP, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[16, 21, 21, 21])
20 None
21 Instruction(UNREAD, next_quasis=[22])
22 Instruction(UNREAD, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
24 End(is_start=True, next_quasis=[26])
25 None
26 Instruction(LOAD, next_quasis=[27, 34])
27 Instruction(MAP, next_quasis=[28])
28 Instruction(LOAD, next_quasis=[29, 34])
29 Instruction(MAP, next_quasis=[30])
30 Instruction(MAP, next_quasis=[31])
31 Instruction(STORE, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[26])
33 None
34 Instruction(UNREAD, next_quasis=[35])
35 Instruction(UNREAD, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[14])
1 FunctionCall(command='ZERO', args=['B'], next_quasis=[3])
2 None
3 Instruction(SLLs, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, next_quasis=[6])
6 Instruction(STORE, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[24, 3, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'var1'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[3])
11 None
12 Instruction(UNREAD, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[16])
15 None
16 Instruction(LOAD, next_quasis=[17, 21])
17 Instruction(LOAD, next_quasis=[18, 21])
18 Instruction(MAP, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[16, 21, 21, 21])
20 None
21 Instruction(UNREAD, next_quasis=[22])
22 Instruction(UNREAD, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
24 End(is_start=True, next_quasis=[26])
25 None
26 Instruction(LOAD, next_quasis=[27, 34])
27 Instruction(MAP, next_quasis=[28])
28 Instruction(LOAD, next_quasis=[29, 34])
29 Instruction(MAP, next_quasis=[30])
30 Instruction(MAP, next_quasis=[31])
31 Instruction(STORE, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[26])
33 None
34 Instruction(UNREAD, next_quasis=[35])
35 Instruction(UNREAD, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 266, in evaluate_function_call
    new_function = functioncall2instruction(line.apply(index,argsdict))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 162, in functioncall2instruction
    instr = Instruction(command,vard=args[0],imm=args[1])
IndexError: list index out of range
>>> len(quasis)
14
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 None
2 None
3 None
4 None
5 None
6 None
7 None
8 None
9 None
10 None
11 None
12 None
13 None
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 Instruction(ZEROs, next_quasis=[3])
2 None
3 Instruction(SLLs, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, next_quasis=[6])
6 Instruction(STORE, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[24, 3, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'var1'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[3])
11 None
12 Instruction(UNREAD, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[16])
15 None
16 Instruction(LOAD, next_quasis=[17, 21])
17 Instruction(LOAD, next_quasis=[18, 21])
18 Instruction(MAP, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[16, 21, 21, 21])
20 None
21 Instruction(UNREAD, next_quasis=[22])
22 Instruction(UNREAD, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
24 End(is_start=True, next_quasis=[26])
25 None
26 Instruction(LOAD, next_quasis=[27, 34])
27 Instruction(MAP, next_quasis=[28])
28 Instruction(LOAD, next_quasis=[29, 34])
29 Instruction(MAP, next_quasis=[30])
30 Instruction(MAP, next_quasis=[31])
31 Instruction(STORE, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[26])
33 None
34 Instruction(UNREAD, next_quasis=[35])
35 Instruction(UNREAD, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 Traceback (most recent call last):
  File "<pyshell#211>", line 2, in <module>
    print(k,quasi)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 95, in __str__
    if read:
NameError: name 'read' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 Traceback (most recent call last):
  File "<pyshell#215>", line 2, in <module>
    print(k,quasi)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 100, in __str__
    result+=', vard=' + vard
NameError: name 'vard' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[1])
1 Instruction(ZEROs, vard=B, next_quasis=[3])
2 None
3 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[6])
6 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[24, 3, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'var1'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[3])
11 None
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[16])
15 None
16 Instruction(LOADNEXTBIG, vard=B, next_quasis=[17, 21])
17 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 21])
18 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[16, 21, 21, 21])
20 None
21 Instruction(UNREAD, vard=B, next_quasis=[22])
22 Instruction(UNREAD, vard=C, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
24 End(is_start=True, next_quasis=[26])
25 None
26 Instruction(LOADNEXT, vard=var1, next_quasis=[27, 34])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[28])
28 Instruction(LOAD, vard=B, next_quasis=[29, 34])
29 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[30])
30 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[31])
31 Instruction(STORENEXT, vard=B, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[26])
33 None
34 Instruction(UNREAD, vard=var1, next_quasis=[35])
35 Instruction(UNREAD, vard=B, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
>>> used_quasis = {0}
>>> def find_successors(k):
    global quasis,used_states
    if quasis[k]:
        for j in quasis[k].next_quasis:
            if not j in used_states:
                used_states.add(j)
                find_successors(j)

                
>>> find_successors(0)
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    find_successors(0)
  File "<pyshell#222>", line 5, in find_successors
    if not j in used_states:
NameError: name 'used_states' is not defined
>>> used_states={}
>>> find_successors(0)
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    find_successors(0)
  File "<pyshell#222>", line 6, in find_successors
    used_states.add(j)
AttributeError: 'dict' object has no attribute 'add'
>>> used_states={0}
>>> find_successors(0)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    find_successors(0)
  File "<pyshell#222>", line 7, in find_successors
    find_successors(j)
  File "<pyshell#222>", line 7, in find_successors
    find_successors(j)
  File "<pyshell#222>", line 7, in find_successors
    find_successors(j)
  [Previous line repeated 11 more times]
  File "<pyshell#222>", line 4, in find_successors
    for j in quasis[k].next_quasis:
TypeError: 'NoneType' object is not iterable
>>> def find_successors(k):
    global quasis,used_states
    if quasis[k] and quasis[k].next_quasis:
        for j in quasis[k].next_quasis:
            if not j in used_states:
                used_states.add(j)
                find_successors(j)

                
>>> used_states={0}
>>> find_successors(0)
>>> used_states
{0, 1, 3, 5, 6, 7, 10, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36}
>>> len(used_states)
28
>>> for k in used_states:
	print(k,quasis[k])

	
0 End(is_start=True, next_quasis=[1])
1 Instruction(ZEROs, vard=B, next_quasis=[3])
3 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
5 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[6])
6 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[24, 3, 24, 24])
10 Instruction(JUMP, next_quasis=[3])
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[16])
16 Instruction(LOADNEXTBIG, vard=B, next_quasis=[17, 21])
17 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 21])
18 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[16, 21, 21, 21])
21 Instruction(UNREAD, vard=B, next_quasis=[22])
22 Instruction(UNREAD, vard=C, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
24 End(is_start=True, next_quasis=[26])
26 Instruction(LOADNEXT, vard=var1, next_quasis=[27, 34])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[28])
28 Instruction(LOAD, vard=B, next_quasis=[29, 34])
29 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[30])
30 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[31])
31 Instruction(STORENEXT, vard=B, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[26])
34 Instruction(UNREAD, vard=var1, next_quasis=[35])
35 Instruction(UNREAD, vard=B, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
>>> steps2states()
>>> instructions2steps()
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    instructions2steps()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 414, in instructions2steps
    replace_links(k,indices[0])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 396, in replace_links
    for k in range(len(quasi.next_quasis)):
TypeError: object of type 'NoneType' has no len()
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> instructions2steps()
>>> steps2states()
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    steps2states()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 386, in steps2states
    transitions,direction = get_found_transitions(k,acc)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 353, in get_found_transitions
    for symbol in transitions:
RuntimeError: dictionary changed size during iteration
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> instructions2steps()
>>> steps2states()
>>> len(quasis)
117
>>> used_states={0}
>>> find_successors(0)
>>> len(used_states)
2
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[37])
1 Instruction(ZEROs, vard=B, next_quasis=[39])
2 None
3 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[5])
5 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[41])
6 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[24, 39, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'var1'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[39])
11 None
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[43])
15 None
16 Instruction(LOADNEXTBIG, vard=B, next_quasis=[45, 21])
17 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 21])
18 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[43, 21, 21, 21])
20 None
21 Instruction(UNREAD, vard=B, next_quasis=[22])
22 Instruction(UNREAD, vard=C, next_quasis=[23])
23 End(is_start=False, next_quasis=[5])
24 End(is_start=True, next_quasis=[47])
25 None
26 Instruction(LOADNEXT, vard=var1, next_quasis=[27, 34])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[49])
28 Instruction(LOAD, vard=B, next_quasis=[29, 34])
29 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[30])
30 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[51])
31 Instruction(STORENEXT, vard=B, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[47])
33 None
34 Instruction(UNREAD, vard=var1, next_quasis=[35])
35 Instruction(UNREAD, vard=B, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
37 Step(instruction=1, is_found=False, variable='B', next_quasis=[38], direction=None)
38 Step(instruction=1, is_found=True, variable='B', next_quasis=[39], direction=None)
39 Step(instruction=3, is_found=False, variable='B', next_quasis=[40], direction=None)
40 Step(instruction=3, is_found=True, variable='B', next_quasis=[14], direction=None)
41 Step(instruction=6, is_found=False, variable='A', next_quasis=[42], direction=None)
42 Step(instruction=6, is_found=True, variable='A', next_quasis=[7, 12], direction=None)
43 Step(instruction=16, is_found=False, variable='B', next_quasis=[44], direction=None)
44 Step(instruction=16, is_found=True, variable='B', next_quasis=[45, 21], direction=None)
45 Step(instruction=17, is_found=False, variable='C', next_quasis=[46], direction=None)
46 Step(instruction=17, is_found=True, variable='C', next_quasis=[18, 21], direction=None)
47 Step(instruction=26, is_found=False, variable='var1', next_quasis=[48], direction=None)
48 Step(instruction=26, is_found=True, variable='var1', next_quasis=[27, 34], direction=None)
49 Step(instruction=28, is_found=False, variable='B', next_quasis=[50], direction=None)
50 Step(instruction=28, is_found=True, variable='B', next_quasis=[29, 34], direction=None)
51 Step(instruction=31, is_found=False, variable='B', next_quasis=[52], direction=None)
52 Step(instruction=31, is_found=True, variable='B', next_quasis=[32, 34], direction=None)
53 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 38]}, direction=None)
54 State(step=37, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 38]}, direction=None)
55 State(step=37, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 38]}, direction=None)
56 State(step=37, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 38]}, direction=None)
57 State(step=38, acc=0, transitions={'0': ['0', 0, 38], '1': ['0', 0, 38], "0'": ['0', 0, 38], "1'": ['0', 0, 38], Symbol(symbol='B', offset=1): [None, 0, 39]}, direction=1)
58 State(step=38, acc=1, transitions={'0': ['0', 1, 38], '1': ['0', 1, 38], "0'": ['0', 1, 38], "1'": ['0', 1, 38], Symbol(symbol='B', offset=1): [None, 1, 39]}, direction=1)
59 State(step=38, acc=2, transitions={'0': ['0', 2, 38], '1': ['0', 2, 38], "0'": ['0', 2, 38], "1'": ['0', 2, 38], Symbol(symbol='B', offset=1): [None, 2, 39]}, direction=1)
60 State(step=38, acc=3, transitions={'0': ['0', 3, 38], '1': ['0', 3, 38], "0'": ['0', 3, 38], "1'": ['0', 3, 38], Symbol(symbol='B', offset=1): [None, 3, 39]}, direction=1)
61 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
62 State(step=39, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
63 State(step=39, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
64 State(step=39, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
65 State(step=40, acc=0, transitions={'0': ['0', 0, 40], '1': ['0', 1, 40], "0'": ['0', 0, 40], "1'": ['0', 1, 40], Symbol(symbol='B', offset=1): [None, 0, 14]}, direction=1)
66 State(step=40, acc=1, transitions={'0': ['1', 0, 40], '1': ['1', 1, 40], "0'": ['1', 0, 40], "1'": ['1', 1, 40], Symbol(symbol='B', offset=1): [None, 1, 14]}, direction=1)
67 State(step=40, acc=2, transitions=None, direction=None)
68 State(step=40, acc=3, transitions=None, direction=None)
69 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 42]}, direction=None)
70 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 42]}, direction=None)
71 State(step=41, acc=2, transitions={Symbol(symbol='A', offset=1): [None, 2, 42]}, direction=None)
72 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 42]}, direction=None)
73 State(step=42, acc=0, transitions={'0': ["0'", 0, 7], '1': ["1'", 0, 7], "0'": ["0'", 0, 42], "1'": ["1'", 0, 42], Symbol(symbol='A', offset=-1): [None, 0, 12]}, direction=-1)
74 State(step=42, acc=1, transitions={'0': ["0'", 1, 7], '1': ["1'", 1, 7], "0'": ["0'", 1, 42], "1'": ["1'", 1, 42], Symbol(symbol='A', offset=-1): [None, 1, 12]}, direction=-1)
75 State(step=42, acc=2, transitions={'0': ["0'", 2, 7], '1': ["1'", 2, 7], "0'": ["0'", 2, 42], "1'": ["1'", 2, 42], Symbol(symbol='A', offset=-1): [None, 2, 12]}, direction=-1)
76 State(step=42, acc=3, transitions={'0': ["0'", 3, 7], '1': ["1'", 3, 7], "0'": ["0'", 3, 42], "1'": ["1'", 3, 42], Symbol(symbol='A', offset=-1): [None, 3, 12]}, direction=-1)
77 State(step=43, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 44]}, direction=None)
78 State(step=43, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 44]}, direction=None)
79 State(step=43, acc=2, transitions={Symbol(symbol='B', offset=1): [None, 2, 44]}, direction=None)
80 State(step=43, acc=3, transitions={Symbol(symbol='B', offset=1): [None, 3, 44]}, direction=None)
81 State(step=44, acc=0, transitions={'0': ["0'", 0, 45], '1': ["1'", 1, 45], "0'": ["0'", 0, 44], "1'": ["1'", 0, 44], Symbol(symbol='B', offset=-1): [None, 0, 21]}, direction=-1)
82 State(step=44, acc=1, transitions={'0': ["0'", 0, 45], '1': ["1'", 1, 45], "0'": ["0'", 1, 44], "1'": ["1'", 1, 44], Symbol(symbol='B', offset=-1): [None, 1, 21]}, direction=-1)
83 State(step=44, acc=2, transitions={'0': ["0'", 0, 45], '1': ["1'", 1, 45], "0'": ["0'", 2, 44], "1'": ["1'", 2, 44], Symbol(symbol='B', offset=-1): [None, 2, 21]}, direction=-1)
84 State(step=44, acc=3, transitions={'0': ["0'", 0, 45], '1': ["1'", 1, 45], "0'": ["0'", 3, 44], "1'": ["1'", 3, 44], Symbol(symbol='B', offset=-1): [None, 3, 21]}, direction=-1)
85 State(step=45, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 46]}, direction=None)
86 State(step=45, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 46]}, direction=None)
87 State(step=45, acc=2, transitions={Symbol(symbol='C', offset=1): [None, 2, 46]}, direction=None)
88 State(step=45, acc=3, transitions={Symbol(symbol='C', offset=1): [None, 3, 46]}, direction=None)
89 State(step=46, acc=0, transitions={'0': ["0'", 0, 18], '1': ["1'", 0, 18], "0'": ["0'", 0, 46], "1'": ["1'", 0, 46], Symbol(symbol='C', offset=-1): [None, 0, 21]}, direction=-1)
90 State(step=46, acc=1, transitions={'0': ["0'", 1, 18], '1': ["1'", 1, 18], "0'": ["0'", 1, 46], "1'": ["1'", 1, 46], Symbol(symbol='C', offset=-1): [None, 1, 21]}, direction=-1)
91 State(step=46, acc=2, transitions={'0': ["0'", 2, 18], '1': ["1'", 2, 18], "0'": ["0'", 2, 46], "1'": ["1'", 2, 46], Symbol(symbol='C', offset=-1): [None, 2, 21]}, direction=-1)
92 State(step=46, acc=3, transitions={'0': ["0'", 3, 18], '1': ["1'", 3, 18], "0'": ["0'", 3, 46], "1'": ["1'", 3, 46], Symbol(symbol='C', offset=-1): [None, 3, 21]}, direction=-1)
93 State(step=47, acc=0, transitions={Symbol(symbol='var1', offset=0): [None, 0, 48]}, direction=None)
94 State(step=47, acc=1, transitions={Symbol(symbol='var1', offset=0): [None, 1, 48]}, direction=None)
95 State(step=47, acc=2, transitions={Symbol(symbol='var1', offset=0): [None, 2, 48]}, direction=None)
96 State(step=47, acc=3, transitions={Symbol(symbol='var1', offset=0): [None, 3, 48]}, direction=None)
97 State(step=48, acc=0, transitions={'0': ["0'", 0, 27], '1': ["1'", 0, 27], "0'": ["0'", 0, 48], "1'": ["1'", 0, 48], Symbol(symbol='var1', offset=1): [None, 0, 34]}, direction=1)
98 State(step=48, acc=1, transitions={'0': ["0'", 1, 27], '1': ["1'", 1, 27], "0'": ["0'", 1, 48], "1'": ["1'", 1, 48], Symbol(symbol='var1', offset=1): [None, 1, 34]}, direction=1)
99 State(step=48, acc=2, transitions={'0': ["0'", 2, 27], '1': ["1'", 2, 27], "0'": ["0'", 2, 48], "1'": ["1'", 2, 48], Symbol(symbol='var1', offset=1): [None, 2, 34]}, direction=1)
100 State(step=48, acc=3, transitions={'0': ["0'", 3, 27], '1': ["1'", 3, 27], "0'": ["0'", 3, 48], "1'": ["1'", 3, 48], Symbol(symbol='var1', offset=1): [None, 3, 34]}, direction=1)
101 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 50]}, direction=None)
102 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 50]}, direction=None)
103 State(step=49, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 50]}, direction=None)
104 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 50]}, direction=None)
105 State(step=50, acc=0, transitions={'0': ['0', 0, 29], '1': ['1', 0, 29], "0'": ["0'", 0, 50], "1'": ["1'", 0, 50], Symbol(symbol='B', offset=1): [None, 0, 34]}, direction=1)
106 State(step=50, acc=1, transitions={'0': ['0', 1, 29], '1': ['1', 1, 29], "0'": ["0'", 1, 50], "1'": ["1'", 1, 50], Symbol(symbol='B', offset=1): [None, 1, 34]}, direction=1)
107 State(step=50, acc=2, transitions={'0': ['0', 2, 29], '1': ['1', 2, 29], "0'": ["0'", 2, 50], "1'": ["1'", 2, 50], Symbol(symbol='B', offset=1): [None, 2, 34]}, direction=1)
108 State(step=50, acc=3, transitions={'0': ['0', 3, 29], '1': ['1', 3, 29], "0'": ["0'", 3, 50], "1'": ["1'", 3, 50], Symbol(symbol='B', offset=1): [None, 3, 34]}, direction=1)
109 State(step=51, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 52]}, direction=None)
110 State(step=51, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 52]}, direction=None)
111 State(step=51, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 52]}, direction=None)
112 State(step=51, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 52]}, direction=None)
113 State(step=52, acc=0, transitions={'0': ["0'", 0, 32], '1': ["1'", 0, 32], "0'": ["0'", 0, 52], "1'": ["1'", 0, 52], Symbol(symbol='B', offset=1): [None, 0, 34]}, direction=1)
114 State(step=52, acc=1, transitions={'0': ["0'", 1, 32], '1': ["1'", 1, 32], "0'": ["0'", 1, 52], "1'": ["1'", 1, 52], Symbol(symbol='B', offset=1): [None, 1, 34]}, direction=1)
115 State(step=52, acc=2, transitions={'0': ["0'", 2, 32], '1': ["1'", 2, 32], "0'": ["0'", 2, 52], "1'": ["1'", 2, 52], Symbol(symbol='B', offset=1): [None, 2, 34]}, direction=1)
116 State(step=52, acc=3, transitions={'0': ["0'", 3, 32], '1': ["1'", 3, 32], "0'": ["0'", 3, 52], "1'": ["1'", 3, 52], Symbol(symbol='B', offset=1): [None, 3, 34]}, direction=1)
>>> more_posts,more_pres = True,True
>>> while (more_posts or more_pres):
        if more_posts:
            more_posts = apply_posts()
        if more_pres:
            more_pres = apply_pres()

            
Traceback (most recent call last):
  File "<pyshell#255>", line 3, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 427, in apply_posts
    for symbol in quasi.transitions:
TypeError: 'NoneType' object is not iterable
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> instructions2steps()
>>> steps2states()
>>> len(quasis)
115
>>> more_posts,more_pres = True,True
>>> while (more_posts or more_pres):
        if more_posts:
            more_posts = apply_posts()
        if more_pres:
            more_pres = apply_pres()

            
>>> stitch_acc()
>>> used_states = {0}
>>> find_successors(0)
>>> len(used_states)
15
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[53])
1 Instruction(ZEROs, vard=B, next_quasis=[39])
2 None
3 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[41])
5 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[0])
6 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 12])
7 Instruction(BRANCH, next_quasis=[24, 39, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'var1'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[39])
11 None
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[75])
15 None
16 Instruction(LOADNEXTBIG, vard=B, next_quasis=[45, 21])
17 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 21])
18 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[43, 21, 21, 21])
20 None
21 Instruction(UNREAD, vard=B, next_quasis=[22])
22 Instruction(UNREAD, vard=C, next_quasis=[23])
23 End(is_start=False, next_quasis=[41])
24 End(is_start=True, next_quasis=[91])
25 None
26 Instruction(LOADNEXT, vard=var1, next_quasis=[27, 34])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[49])
28 Instruction(LOAD, vard=B, next_quasis=[29, 34])
29 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[51])
30 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
31 Instruction(STORENEXT, vard=B, next_quasis=[32, 34])
32 Instruction(JUMP, next_quasis=[47])
33 None
34 Instruction(UNREAD, vard=var1, next_quasis=[35])
35 Instruction(UNREAD, vard=B, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
37 Step(instruction=1, is_found=False, variable='B', next_quasis=[38], direction=None)
38 Step(instruction=1, is_found=True, variable='B', next_quasis=[39], direction=None)
39 Step(instruction=3, is_found=False, variable='B', next_quasis=[40], direction=None)
40 Step(instruction=3, is_found=True, variable='B', next_quasis=[14], direction=None)
41 Step(instruction=6, is_found=False, variable='A', next_quasis=[42], direction=None)
42 Step(instruction=6, is_found=True, variable='A', next_quasis=[7, 12], direction=None)
43 Step(instruction=16, is_found=False, variable='B', next_quasis=[44], direction=None)
44 Step(instruction=16, is_found=True, variable='B', next_quasis=[45, 21], direction=None)
45 Step(instruction=17, is_found=False, variable='C', next_quasis=[46], direction=None)
46 Step(instruction=17, is_found=True, variable='C', next_quasis=[18, 21], direction=None)
47 Step(instruction=26, is_found=False, variable='var1', next_quasis=[48], direction=None)
48 Step(instruction=26, is_found=True, variable='var1', next_quasis=[27, 34], direction=None)
49 Step(instruction=28, is_found=False, variable='B', next_quasis=[50], direction=None)
50 Step(instruction=28, is_found=True, variable='B', next_quasis=[29, 34], direction=None)
51 Step(instruction=31, is_found=False, variable='B', next_quasis=[52], direction=None)
52 Step(instruction=31, is_found=True, variable='B', next_quasis=[32, 34], direction=None)
53 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 57]}, direction=None)
54 State(step=37, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 58]}, direction=None)
55 State(step=37, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 59]}, direction=None)
56 State(step=37, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 60]}, direction=None)
57 State(step=38, acc=0, transitions={'0': ['0', 0, 57], '1': ['0', 0, 57], "0'": ['0', 0, 57], "1'": ['0', 0, 57], Symbol(symbol='B', offset=1): [None, 0, 61]}, direction=1)
58 State(step=38, acc=1, transitions={'0': ['0', 1, 58], '1': ['0', 1, 58], "0'": ['0', 1, 58], "1'": ['0', 1, 58], Symbol(symbol='B', offset=1): [None, 1, 62]}, direction=1)
59 State(step=38, acc=2, transitions={'0': ['0', 2, 59], '1': ['0', 2, 59], "0'": ['0', 2, 59], "1'": ['0', 2, 59], Symbol(symbol='B', offset=1): [None, 2, 63]}, direction=1)
60 State(step=38, acc=3, transitions={'0': ['0', 3, 60], '1': ['0', 3, 60], "0'": ['0', 3, 60], "1'": ['0', 3, 60], Symbol(symbol='B', offset=1): [None, 3, 64]}, direction=1)
61 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 66]}, direction=None)
62 State(step=39, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 66]}, direction=None)
63 State(step=39, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 1, 66]}, direction=None)
64 State(step=39, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 1, 66]}, direction=None)
65 State(step=40, acc=0, transitions={'0': ['0', 0, 65], '1': ['0', 1, 66], "0'": ['0', 0, 65], "1'": ['0', 1, 66], Symbol(symbol='B', offset=1): [None, 0, 75]}, direction=1)
66 State(step=40, acc=1, transitions={'0': ['1', 0, 65], '1': ['1', 1, 66], "0'": ['1', 0, 65], "1'": ['1', 1, 66], Symbol(symbol='B', offset=1): [None, 1, 76]}, direction=1)
67 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 71]}, direction=None)
68 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 72]}, direction=None)
69 State(step=41, acc=2, transitions={Symbol(symbol='A', offset=1): [None, 2, 73]}, direction=None)
70 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 74]}, direction=None)
71 State(step=42, acc=0, transitions={'0': ["0'", 1, 92], '1': ["0'", 1, 92], "0'": ["0'", 0, 71], "1'": ["1'", 0, 71], Symbol(symbol='A', offset=-1): [None, 0, 12]}, direction=-1)
72 State(step=42, acc=1, transitions={'0': ["1'", 0, 61], '1': ["1'", 0, 61], "0'": ["0'", 1, 72], "1'": ["1'", 1, 72], Symbol(symbol='A', offset=-1): [None, 1, 12]}, direction=-1)
73 State(step=42, acc=2, transitions={'0': ["0'", 2, 93], '1': ["1'", 2, 93], "0'": ["0'", 2, 73], "1'": ["1'", 2, 73], Symbol(symbol='A', offset=-1): [None, 2, 12]}, direction=-1)
74 State(step=42, acc=3, transitions={'0': ["0'", 1, 92], '1': ["0'", 1, 92], "0'": ["0'", 3, 74], "1'": ["1'", 3, 74], Symbol(symbol='A', offset=-1): [None, 3, 12]}, direction=-1)
75 State(step=43, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 79]}, direction=None)
76 State(step=43, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 80]}, direction=None)
77 State(step=43, acc=2, transitions={Symbol(symbol='B', offset=1): [None, 2, 81]}, direction=None)
78 State(step=43, acc=3, transitions={Symbol(symbol='B', offset=1): [None, 3, 82]}, direction=None)
79 State(step=44, acc=0, transitions={'0': ["0'", 0, 83], '1': ["1'", 1, 84], "0'": ["0'", 0, 79], "1'": ["1'", 0, 79], Symbol(symbol='B', offset=-1): [None, 0, 21]}, direction=-1)
80 State(step=44, acc=1, transitions={'0': ["0'", 0, 83], '1': ["1'", 1, 84], "0'": ["0'", 1, 80], "1'": ["1'", 1, 80], Symbol(symbol='B', offset=-1): [None, 1, 21]}, direction=-1)
81 State(step=44, acc=2, transitions={'0': ["0'", 0, 83], '1': ["1'", 1, 84], "0'": ["0'", 2, 81], "1'": ["1'", 2, 81], Symbol(symbol='B', offset=-1): [None, 2, 21]}, direction=-1)
82 State(step=44, acc=3, transitions={'0': ["0'", 0, 83], '1': ["1'", 1, 84], "0'": ["0'", 3, 82], "1'": ["1'", 3, 82], Symbol(symbol='B', offset=-1): [None, 3, 21]}, direction=-1)
83 State(step=45, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 87]}, direction=None)
84 State(step=45, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 88]}, direction=None)
85 State(step=45, acc=2, transitions={Symbol(symbol='C', offset=1): [None, 2, 89]}, direction=None)
86 State(step=45, acc=3, transitions={Symbol(symbol='C', offset=1): [None, 3, 90]}, direction=None)
87 State(step=46, acc=0, transitions={'0': ["0'", 0, 75], '1': ["1'", 1, 21], "0'": ["0'", 0, 87], "1'": ["1'", 0, 87], Symbol(symbol='C', offset=-1): [None, 0, 21]}, direction=-1)
88 State(step=46, acc=1, transitions={'0': ["0'", 3, 21], '1': ["1'", 0, 75], "0'": ["0'", 1, 88], "1'": ["1'", 1, 88], Symbol(symbol='C', offset=-1): [None, 1, 21]}, direction=-1)
89 State(step=46, acc=2, transitions={'0': ["0'", 2, 21], '1': ["1'", 2, 21], "0'": ["0'", 2, 89], "1'": ["1'", 2, 89], Symbol(symbol='C', offset=-1): [None, 2, 21]}, direction=-1)
90 State(step=46, acc=3, transitions={'0': ["0'", 3, 21], '1': ["1'", 3, 21], "0'": ["0'", 3, 90], "1'": ["1'", 3, 90], Symbol(symbol='C', offset=-1): [None, 3, 21]}, direction=-1)
91 State(step=47, acc=0, transitions={Symbol(symbol='var1', offset=0): [None, 0, 95]}, direction=None)
92 State(step=47, acc=1, transitions={Symbol(symbol='var1', offset=0): [None, 1, 96]}, direction=None)
93 State(step=47, acc=2, transitions={Symbol(symbol='var1', offset=0): [None, 2, 97]}, direction=None)
94 State(step=47, acc=3, transitions={Symbol(symbol='var1', offset=0): [None, 3, 98]}, direction=None)
95 State(step=48, acc=0, transitions={'0': ["0'", 0, 99], '1': ["1'", 1, 100], "0'": ["0'", 0, 95], "1'": ["1'", 0, 95], Symbol(symbol='var1', offset=1): [None, 0, 34]}, direction=1)
96 State(step=48, acc=1, transitions={'0': ["0'", 1, 100], '1': ["1'", 1, 100], "0'": ["0'", 1, 96], "1'": ["1'", 1, 96], Symbol(symbol='var1', offset=1): [None, 1, 34]}, direction=1)
97 State(step=48, acc=2, transitions={'0': ["0'", 2, 101], '1': ["1'", 2, 101], "0'": ["0'", 2, 97], "1'": ["1'", 2, 97], Symbol(symbol='var1', offset=1): [None, 2, 34]}, direction=1)
98 State(step=48, acc=3, transitions={'0': ["0'", 3, 102], '1': ["1'", 0, 99], "0'": ["0'", 3, 98], "1'": ["1'", 3, 98], Symbol(symbol='var1', offset=1): [None, 3, 34]}, direction=1)
99 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 103]}, direction=None)
100 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 104]}, direction=None)
101 State(step=49, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 105]}, direction=None)
102 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 106]}, direction=None)
103 State(step=50, acc=0, transitions={'0': ['0', 0, 107], '1': ['1', 3, 110], "0'": ["0'", 0, 103], "1'": ["1'", 0, 103], Symbol(symbol='B', offset=1): [None, 0, 34]}, direction=1)
104 State(step=50, acc=1, transitions={'0': ['0', 1, 108], '1': ['1', 0, 107], "0'": ["0'", 1, 104], "1'": ["1'", 1, 104], Symbol(symbol='B', offset=1): [None, 1, 34]}, direction=1)
105 State(step=50, acc=2, transitions={'0': ['0', 2, 109], '1': ['1', 2, 109], "0'": ["0'", 2, 105], "1'": ["1'", 2, 105], Symbol(symbol='B', offset=1): [None, 2, 34]}, direction=1)
106 State(step=50, acc=3, transitions={'0': ['0', 3, 110], '1': ['1', 2, 109], "0'": ["0'", 3, 106], "1'": ["1'", 3, 106], Symbol(symbol='B', offset=1): [None, 3, 34]}, direction=1)
107 State(step=51, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 111]}, direction=None)
108 State(step=51, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 112]}, direction=None)
109 State(step=51, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 113]}, direction=None)
110 State(step=51, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 114]}, direction=None)
111 State(step=52, acc=0, transitions={'0': ["0'", 0, 91], '1': ["0'", 0, 91], "0'": ["0'", 0, 111], "1'": ["1'", 0, 111], Symbol(symbol='B', offset=1): [None, 0, 34]}, direction=1)
112 State(step=52, acc=1, transitions={'0': ["0'", 1, 92], '1': ["0'", 1, 92], "0'": ["0'", 1, 112], "1'": ["1'", 1, 112], Symbol(symbol='B', offset=1): [None, 1, 34]}, direction=1)
113 State(step=52, acc=2, transitions={'0': ["1'", 0, 91], '1': ["1'", 0, 91], "0'": ["0'", 2, 113], "1'": ["1'", 2, 113], Symbol(symbol='B', offset=1): [None, 2, 34]}, direction=1)
114 State(step=52, acc=3, transitions={'0': ["1'", 1, 92], '1': ["1'", 1, 92], "0'": ["0'", 3, 114], "1'": ["1'", 3, 114], Symbol(symbol='B', offset=1): [None, 3, 34]}, direction=1)
>>> def find_successors(k):
    global quasis,used_states
    if type(quasis[k]) in [End,Instruction]:
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

                
>>> used_states={}
>>> used_states={0}
>>> find_successors(0)
>>> len(used_states)
18
>>> used_states
{0, 65, 66, 41, 75, 76, 79, 80, 83, 23, 53, 21, 87, 22, 57, 84, 88, 61}
>>> sorted(used_states)
[0, 21, 22, 23, 41, 53, 57, 61, 65, 66, 75, 76, 79, 80, 83, 84, 87, 88]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> instructions2steps()
>>> steps2states()
>>> len(quasis)
165
>>> more_posts,more_pres = True,True
>>> while (more_posts or more_pres):
        if more_posts:
            more_posts = apply_posts()
        if more_pres:
            more_pres = apply_pres()

            
Traceback (most recent call last):
  File "<pyshell#286>", line 3, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 460, in apply_posts
    transition[2] = quasi2.next_quasis[0]
TypeError: 'NoneType' object is not subscriptable
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('RECP A B C').value
>>> evaluate_function_call(function)
>>> instructions2steps()
>>> steps2states()
>>> more_posts,more_pres = True,True
>>> while (more_posts or more_pres):
        if more_posts:
            more_posts = apply_posts()
        if more_pres:
            more_pres = apply_pres()

            
>>> used_states = {0}
>>> find_successors(0)
>>> len(used_states)
2
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[37])
1 Instruction(ZEROs, vard=B, next_quasis=[39])
2 None
3 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[41])
5 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[0])
6 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 43])
7 Instruction(BRANCH, next_quasis=[24, 39, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'C'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[39])
11 None
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[45])
15 None
16 Instruction(LOADNEXTBIG, vard=B, next_quasis=[47, 49])
17 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 49])
18 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[45, 49, 49, 49])
20 None
21 Instruction(UNREAD, vard=B, next_quasis=[51])
22 Instruction(UNREAD, vard=C, next_quasis=[23])
23 End(is_start=False, next_quasis=[41])
24 End(is_start=True, next_quasis=[53])
25 None
26 Instruction(LOADNEXT, vard=C, next_quasis=[27, 59])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[55])
28 Instruction(LOAD, vard=B, next_quasis=[29, 59])
29 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[57])
30 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
31 Instruction(STORENEXT, vard=B, next_quasis=[32, 59])
32 Instruction(JUMP, next_quasis=[53])
33 None
34 Instruction(UNREAD, vard=C, next_quasis=[61])
35 Instruction(UNREAD, vard=B, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
37 Step(instruction=1, is_found=False, variable='B', next_quasis=[38], direction=None)
38 Step(instruction=1, is_found=True, variable='B', next_quasis=[39], direction=None)
39 Step(instruction=3, is_found=False, variable='B', next_quasis=[40], direction=None)
40 Step(instruction=3, is_found=True, variable='B', next_quasis=[14], direction=None)
41 Step(instruction=6, is_found=False, variable='A', next_quasis=[42], direction=None)
42 Step(instruction=6, is_found=True, variable='A', next_quasis=[7, 43], direction=None)
43 Step(instruction=12, is_found=False, variable='A', next_quasis=[44], direction=None)
44 Step(instruction=12, is_found=True, variable='A', next_quasis=[13], direction=None)
45 Step(instruction=16, is_found=False, variable='B', next_quasis=[46], direction=None)
46 Step(instruction=16, is_found=True, variable='B', next_quasis=[47, 49], direction=None)
47 Step(instruction=17, is_found=False, variable='C', next_quasis=[48], direction=None)
48 Step(instruction=17, is_found=True, variable='C', next_quasis=[18, 49], direction=None)
49 Step(instruction=21, is_found=False, variable='B', next_quasis=[50], direction=None)
50 Step(instruction=21, is_found=True, variable='B', next_quasis=[51], direction=None)
51 Step(instruction=22, is_found=False, variable='C', next_quasis=[52], direction=None)
52 Step(instruction=22, is_found=True, variable='C', next_quasis=[23], direction=None)
53 Step(instruction=26, is_found=False, variable='C', next_quasis=[54], direction=None)
54 Step(instruction=26, is_found=True, variable='C', next_quasis=[27, 59], direction=None)
55 Step(instruction=28, is_found=False, variable='B', next_quasis=[56], direction=None)
56 Step(instruction=28, is_found=True, variable='B', next_quasis=[29, 59], direction=None)
57 Step(instruction=31, is_found=False, variable='B', next_quasis=[58], direction=None)
58 Step(instruction=31, is_found=True, variable='B', next_quasis=[32, 59], direction=None)
59 Step(instruction=34, is_found=False, variable='C', next_quasis=[60], direction=None)
60 Step(instruction=34, is_found=True, variable='C', next_quasis=[61], direction=None)
61 Step(instruction=35, is_found=False, variable='B', next_quasis=[62], direction=None)
62 Step(instruction=35, is_found=True, variable='B', next_quasis=[36], direction=None)
63 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 38]}, direction=None)
64 State(step=37, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 38]}, direction=None)
65 State(step=37, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 38]}, direction=None)
66 State(step=37, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 38]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 38], '1': ['0', 0, 38], "0'": ['0', 0, 38], "1'": ['0', 0, 38], Symbol(symbol='B', offset=1): [None, 0, 39]}, direction=1)
68 State(step=38, acc=1, transitions={'0': ['0', 1, 38], '1': ['0', 1, 38], "0'": ['0', 1, 38], "1'": ['0', 1, 38], Symbol(symbol='B', offset=1): [None, 1, 39]}, direction=1)
69 State(step=38, acc=2, transitions={'0': ['0', 2, 38], '1': ['0', 2, 38], "0'": ['0', 2, 38], "1'": ['0', 2, 38], Symbol(symbol='B', offset=1): [None, 2, 39]}, direction=1)
70 State(step=38, acc=3, transitions={'0': ['0', 3, 38], '1': ['0', 3, 38], "0'": ['0', 3, 38], "1'": ['0', 3, 38], Symbol(symbol='B', offset=1): [None, 3, 39]}, direction=1)
71 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
72 State(step=39, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
73 State(step=39, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
74 State(step=39, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 1, 40]}, direction=None)
75 State(step=40, acc=0, transitions={'0': ['0', 0, 40], '1': ['0', 1, 40], "0'": ['0', 0, 40], "1'": ['0', 1, 40], Symbol(symbol='B', offset=1): [None, 0, 45]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 40], '1': ['1', 1, 40], "0'": ['1', 0, 40], "1'": ['1', 1, 40], Symbol(symbol='B', offset=1): [None, 1, 45]}, direction=1)
77 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 42]}, direction=None)
78 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 42]}, direction=None)
79 State(step=41, acc=2, transitions={Symbol(symbol='A', offset=1): [None, 2, 42]}, direction=None)
80 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 42]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 53], '1': ["0'", 1, 53], "0'": ["0'", 0, 42], "1'": ["1'", 0, 42], Symbol(symbol='A', offset=-1): [None, 0, 43]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 39], '1': ["1'", 0, 39], "0'": ["0'", 1, 42], "1'": ["1'", 1, 42], Symbol(symbol='A', offset=-1): [None, 1, 43]}, direction=-1)
83 State(step=42, acc=2, transitions={'0': ["0'", 2, 53], '1': ["1'", 2, 53], "0'": ["0'", 2, 42], "1'": ["1'", 2, 42], Symbol(symbol='A', offset=-1): [None, 2, 43]}, direction=-1)
84 State(step=42, acc=3, transitions={'0': ["0'", 1, 53], '1': ["0'", 1, 53], "0'": ["0'", 3, 42], "1'": ["1'", 3, 42], Symbol(symbol='A', offset=-1): [None, 3, 43]}, direction=-1)
85 State(step=43, acc=0, transitions={Symbol(symbol='A', offset=0): [None, 0, 44]}, direction=None)
86 State(step=43, acc=1, transitions={Symbol(symbol='A', offset=0): [None, 1, 44]}, direction=None)
87 State(step=43, acc=2, transitions={Symbol(symbol='A', offset=0): [None, 2, 44]}, direction=None)
88 State(step=43, acc=3, transitions={Symbol(symbol='A', offset=0): [None, 3, 44]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 44], '1': ['1', 0, 44], "0'": ['0', 0, 44], "1'": ['1', 0, 44], Symbol(symbol='A', offset=1): [None, 0, 13]}, direction=1)
90 State(step=44, acc=1, transitions={'0': ['0', 1, 44], '1': ['1', 1, 44], "0'": ['0', 1, 44], "1'": ['1', 1, 44], Symbol(symbol='A', offset=1): [None, 1, 13]}, direction=1)
91 State(step=44, acc=2, transitions={'0': ['0', 2, 44], '1': ['1', 2, 44], "0'": ['0', 2, 44], "1'": ['1', 2, 44], Symbol(symbol='A', offset=1): [None, 2, 13]}, direction=1)
92 State(step=44, acc=3, transitions={'0': ['0', 3, 44], '1': ['1', 3, 44], "0'": ['0', 3, 44], "1'": ['1', 3, 44], Symbol(symbol='A', offset=1): [None, 3, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 46]}, direction=None)
94 State(step=45, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 46]}, direction=None)
95 State(step=45, acc=2, transitions={Symbol(symbol='B', offset=1): [None, 2, 46]}, direction=None)
96 State(step=45, acc=3, transitions={Symbol(symbol='B', offset=1): [None, 3, 46]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 47], "0'": ["0'", 0, 46], "1'": ["1'", 0, 46], Symbol(symbol='B', offset=-1): [None, 0, 49]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 47], "0'": ["0'", 1, 46], "1'": ["1'", 1, 46], Symbol(symbol='B', offset=-1): [None, 1, 49]}, direction=-1)
99 State(step=46, acc=2, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 47], "0'": ["0'", 2, 46], "1'": ["1'", 2, 46], Symbol(symbol='B', offset=-1): [None, 2, 49]}, direction=-1)
100 State(step=46, acc=3, transitions={'0': ["0'", 0, 47], '1': ["1'", 1, 47], "0'": ["0'", 3, 46], "1'": ["1'", 3, 46], Symbol(symbol='B', offset=-1): [None, 3, 49]}, direction=-1)
101 State(step=47, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 48]}, direction=None)
102 State(step=47, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 48]}, direction=None)
103 State(step=47, acc=2, transitions={Symbol(symbol='C', offset=1): [None, 2, 48]}, direction=None)
104 State(step=47, acc=3, transitions={Symbol(symbol='C', offset=1): [None, 3, 48]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 45], '1': ["1'", 1, 49], "0'": ["0'", 0, 48], "1'": ["1'", 0, 48], Symbol(symbol='C', offset=-1): [None, 0, 49]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 49], '1': ["1'", 0, 45], "0'": ["0'", 1, 48], "1'": ["1'", 1, 48], Symbol(symbol='C', offset=-1): [None, 1, 49]}, direction=-1)
107 State(step=48, acc=2, transitions={'0': ["0'", 2, 49], '1': ["1'", 2, 49], "0'": ["0'", 2, 48], "1'": ["1'", 2, 48], Symbol(symbol='C', offset=-1): [None, 2, 49]}, direction=-1)
108 State(step=48, acc=3, transitions={'0': ["0'", 3, 49], '1': ["1'", 3, 49], "0'": ["0'", 3, 48], "1'": ["1'", 3, 48], Symbol(symbol='C', offset=-1): [None, 3, 49]}, direction=-1)
109 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 50]}, direction=None)
110 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 50]}, direction=None)
111 State(step=49, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 50]}, direction=None)
112 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 50]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 50], '1': ['1', 0, 50], "0'": ['0', 0, 50], "1'": ['1', 0, 50], Symbol(symbol='B', offset=1): [None, 0, 51]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 50], '1': ['1', 1, 50], "0'": ['0', 1, 50], "1'": ['1', 1, 50], Symbol(symbol='B', offset=1): [None, 1, 51]}, direction=1)
115 State(step=50, acc=2, transitions={'0': ['0', 2, 50], '1': ['1', 2, 50], "0'": ['0', 2, 50], "1'": ['1', 2, 50], Symbol(symbol='B', offset=1): [None, 2, 51]}, direction=1)
116 State(step=50, acc=3, transitions={'0': ['0', 3, 50], '1': ['1', 3, 50], "0'": ['0', 3, 50], "1'": ['1', 3, 50], Symbol(symbol='B', offset=1): [None, 3, 51]}, direction=1)
117 State(step=51, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 52]}, direction=None)
118 State(step=51, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 52]}, direction=None)
119 State(step=51, acc=2, transitions={Symbol(symbol='C', offset=0): [None, 2, 52]}, direction=None)
120 State(step=51, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 52]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 52], '1': ['1', 0, 52], "0'": ['0', 0, 52], "1'": ['1', 0, 52], Symbol(symbol='C', offset=1): [None, 0, 41]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 52], '1': ['1', 1, 52], "0'": ['0', 1, 52], "1'": ['1', 1, 52], Symbol(symbol='C', offset=1): [None, 1, 41]}, direction=1)
123 State(step=52, acc=2, transitions={'0': ['0', 2, 52], '1': ['1', 2, 52], "0'": ['0', 2, 52], "1'": ['1', 2, 52], Symbol(symbol='C', offset=1): [None, 2, 41]}, direction=1)
124 State(step=52, acc=3, transitions={'0': ['0', 3, 52], '1': ['1', 3, 52], "0'": ['0', 3, 52], "1'": ['1', 3, 52], Symbol(symbol='C', offset=1): [None, 3, 41]}, direction=1)
125 State(step=53, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 54]}, direction=None)
126 State(step=53, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 54]}, direction=None)
127 State(step=53, acc=2, transitions={Symbol(symbol='C', offset=0): [None, 2, 54]}, direction=None)
128 State(step=53, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 54]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 55], '1': ["1'", 1, 55], "0'": ["0'", 0, 54], "1'": ["1'", 0, 54], Symbol(symbol='C', offset=1): [None, 0, 59]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 55], '1': ["1'", 1, 55], "0'": ["0'", 1, 54], "1'": ["1'", 1, 54], Symbol(symbol='C', offset=1): [None, 1, 59]}, direction=1)
131 State(step=54, acc=2, transitions={'0': ["0'", 2, 55], '1': ["1'", 2, 55], "0'": ["0'", 2, 54], "1'": ["1'", 2, 54], Symbol(symbol='C', offset=1): [None, 2, 59]}, direction=1)
132 State(step=54, acc=3, transitions={'0': ["0'", 3, 55], '1': ["1'", 0, 55], "0'": ["0'", 3, 54], "1'": ["1'", 3, 54], Symbol(symbol='C', offset=1): [None, 3, 59]}, direction=1)
133 State(step=55, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 56]}, direction=None)
134 State(step=55, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 56]}, direction=None)
135 State(step=55, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 56]}, direction=None)
136 State(step=55, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 56]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ['0', 0, 57], '1': ['1', 3, 57], "0'": ["0'", 0, 56], "1'": ["1'", 0, 56], Symbol(symbol='B', offset=1): [None, 0, 59]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ['0', 1, 57], '1': ['1', 0, 57], "0'": ["0'", 1, 56], "1'": ["1'", 1, 56], Symbol(symbol='B', offset=1): [None, 1, 59]}, direction=1)
139 State(step=56, acc=2, transitions={'0': ['0', 2, 57], '1': ['1', 2, 57], "0'": ["0'", 2, 56], "1'": ["1'", 2, 56], Symbol(symbol='B', offset=1): [None, 2, 59]}, direction=1)
140 State(step=56, acc=3, transitions={'0': ['0', 3, 57], '1': ['1', 2, 57], "0'": ["0'", 3, 56], "1'": ["1'", 3, 56], Symbol(symbol='B', offset=1): [None, 3, 59]}, direction=1)
141 State(step=57, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 58]}, direction=None)
142 State(step=57, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 58]}, direction=None)
143 State(step=57, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 58]}, direction=None)
144 State(step=57, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 58]}, direction=None)
145 State(step=58, acc=0, transitions={'0': ["0'", 0, 53], '1': ["0'", 0, 53], "0'": ["0'", 0, 58], "1'": ["1'", 0, 58], Symbol(symbol='B', offset=1): [None, 0, 59]}, direction=1)
146 State(step=58, acc=1, transitions={'0': ["0'", 1, 53], '1': ["0'", 1, 53], "0'": ["0'", 1, 58], "1'": ["1'", 1, 58], Symbol(symbol='B', offset=1): [None, 1, 59]}, direction=1)
147 State(step=58, acc=2, transitions={'0': ["1'", 0, 53], '1': ["1'", 0, 53], "0'": ["0'", 2, 58], "1'": ["1'", 2, 58], Symbol(symbol='B', offset=1): [None, 2, 59]}, direction=1)
148 State(step=58, acc=3, transitions={'0': ["1'", 1, 53], '1': ["1'", 1, 53], "0'": ["0'", 3, 58], "1'": ["1'", 3, 58], Symbol(symbol='B', offset=1): [None, 3, 59]}, direction=1)
149 State(step=59, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 60]}, direction=None)
150 State(step=59, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 60]}, direction=None)
151 State(step=59, acc=2, transitions={Symbol(symbol='C', offset=0): [None, 2, 60]}, direction=None)
152 State(step=59, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 60]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 60], '1': ['1', 0, 60], "0'": ['0', 0, 60], "1'": ['1', 0, 60], Symbol(symbol='C', offset=1): [None, 0, 61]}, direction=1)
154 State(step=60, acc=1, transitions={'0': ['0', 1, 60], '1': ['1', 1, 60], "0'": ['0', 1, 60], "1'": ['1', 1, 60], Symbol(symbol='C', offset=1): [None, 1, 61]}, direction=1)
155 State(step=60, acc=2, transitions={'0': ['0', 2, 60], '1': ['1', 2, 60], "0'": ['0', 2, 60], "1'": ['1', 2, 60], Symbol(symbol='C', offset=1): [None, 2, 61]}, direction=1)
156 State(step=60, acc=3, transitions={'0': ['0', 3, 60], '1': ['1', 3, 60], "0'": ['0', 3, 60], "1'": ['1', 3, 60], Symbol(symbol='C', offset=1): [None, 3, 61]}, direction=1)
157 State(step=61, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 62]}, direction=None)
158 State(step=61, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 62]}, direction=None)
159 State(step=61, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 62]}, direction=None)
160 State(step=61, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 62]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 62], '1': ['1', 0, 62], "0'": ['0', 0, 62], "1'": ['1', 0, 62], Symbol(symbol='B', offset=1): [None, 0, 39]}, direction=1)
162 State(step=62, acc=1, transitions={'0': ['0', 1, 62], '1': ['1', 1, 62], "0'": ['0', 1, 62], "1'": ['1', 1, 62], Symbol(symbol='B', offset=1): [None, 1, 39]}, direction=1)
163 State(step=62, acc=2, transitions={'0': ['0', 2, 62], '1': ['1', 2, 62], "0'": ['0', 2, 62], "1'": ['1', 2, 62], Symbol(symbol='B', offset=1): [None, 2, 39]}, direction=1)
164 State(step=62, acc=3, transitions={'0': ['0', 3, 62], '1': ['1', 3, 62], "0'": ['0', 3, 62], "1'": ['1', 3, 62], Symbol(symbol='B', offset=1): [None, 3, 39]}, direction=1)
>>> used_states
{0, 37}
>>> stitch_acc()
>>> used_states = {0}
>>> find_successors(0)
Traceback (most recent call last):
  File "<pyshell#302>", line 1, in <module>
    find_successors(0)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 515, in find_successors
    find_successors(j)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 521, in find_successors
    find_successors(j)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 521, in find_successors
    find_successors(j)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 521, in find_successors
    find_successors(j)
  [Previous line repeated 14 more times]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 512, in find_successors
    for j in quasis[k].next_quasis:
TypeError: 'NoneType' object is not iterable
>>> len(used_states)
19
>>> def find_successors(k):
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

                
>>> used_states = {0}
>>> find_successors(0)
>>> len(used_states)
67
>>> for k,quasi in enumerate(quasis):
        if k in used_states:
            print(k,quasi)

            
0 End(is_start=True, next_quasis=[63])
13 End(is_start=False, next_quasis=None)
63 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 67]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 67], '1': ['0', 0, 67], "0'": ['0', 0, 67], "1'": ['0', 0, 67], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
71 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
72 State(step=39, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
74 State(step=39, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
75 State(step=40, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 76], "0'": ['0', 0, 75], "1'": ['0', 1, 76], Symbol(symbol='B', offset=1): [None, 0, 93]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 76], "0'": ['1', 0, 75], "1'": ['1', 1, 76], Symbol(symbol='B', offset=1): [None, 1, 94]}, direction=1)
77 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 81]}, direction=None)
78 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 82]}, direction=None)
80 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 84]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Symbol(symbol='A', offset=-1): [None, 0, 85]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Symbol(symbol='A', offset=-1): [None, 1, 86]}, direction=-1)
84 State(step=42, acc=3, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 3, 84], "1'": ["1'", 3, 84], Symbol(symbol='A', offset=-1): [None, 3, 88]}, direction=-1)
85 State(step=43, acc=0, transitions={Symbol(symbol='A', offset=0): [None, 0, 89]}, direction=None)
86 State(step=43, acc=1, transitions={Symbol(symbol='A', offset=0): [None, 1, 90]}, direction=None)
88 State(step=43, acc=3, transitions={Symbol(symbol='A', offset=0): [None, 3, 92]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 89], '1': ['1', 0, 89], "0'": ['0', 0, 89], "1'": ['1', 0, 89], Symbol(symbol='A', offset=1): [None, 0, 13]}, direction=1)
90 State(step=44, acc=1, transitions={'0': ['0', 1, 90], '1': ['1', 1, 90], "0'": ['0', 1, 90], "1'": ['1', 1, 90], Symbol(symbol='A', offset=1): [None, 1, 13]}, direction=1)
92 State(step=44, acc=3, transitions={'0': ['0', 3, 92], '1': ['1', 3, 92], "0'": ['0', 3, 92], "1'": ['1', 3, 92], Symbol(symbol='A', offset=1): [None, 3, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 97]}, direction=None)
94 State(step=45, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 98]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 0, 97], "1'": ["1'", 0, 97], Symbol(symbol='B', offset=-1): [None, 0, 109]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 1, 98], "1'": ["1'", 1, 98], Symbol(symbol='B', offset=-1): [None, 1, 110]}, direction=-1)
101 State(step=47, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 105]}, direction=None)
102 State(step=47, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 106]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 93], '1': ["1'", 1, 110], "0'": ["0'", 0, 105], "1'": ["1'", 0, 105], Symbol(symbol='C', offset=-1): [None, 0, 109]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 112], '1': ["1'", 0, 93], "0'": ["0'", 1, 106], "1'": ["1'", 1, 106], Symbol(symbol='C', offset=-1): [None, 1, 110]}, direction=-1)
109 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 113]}, direction=None)
110 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 114]}, direction=None)
112 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 116]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 113], '1': ['1', 0, 113], "0'": ['0', 0, 113], "1'": ['1', 0, 113], Symbol(symbol='B', offset=1): [None, 0, 117]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 114], '1': ['1', 1, 114], "0'": ['0', 1, 114], "1'": ['1', 1, 114], Symbol(symbol='B', offset=1): [None, 1, 118]}, direction=1)
116 State(step=50, acc=3, transitions={'0': ['0', 3, 116], '1': ['1', 3, 116], "0'": ['0', 3, 116], "1'": ['1', 3, 116], Symbol(symbol='B', offset=1): [None, 3, 120]}, direction=1)
117 State(step=51, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 121]}, direction=None)
118 State(step=51, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 122]}, direction=None)
120 State(step=51, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 124]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 121], '1': ['1', 0, 121], "0'": ['0', 0, 121], "1'": ['1', 0, 121], Symbol(symbol='C', offset=1): [None, 0, 77]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 122], '1': ['1', 1, 122], "0'": ['0', 1, 122], "1'": ['1', 1, 122], Symbol(symbol='C', offset=1): [None, 1, 78]}, direction=1)
124 State(step=52, acc=3, transitions={'0': ['0', 3, 124], '1': ['1', 3, 124], "0'": ['0', 3, 124], "1'": ['1', 3, 124], Symbol(symbol='C', offset=1): [None, 3, 80]}, direction=1)
125 State(step=53, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 129]}, direction=None)
126 State(step=53, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 130]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 133], '1': ["1'", 1, 134], "0'": ["0'", 0, 129], "1'": ["1'", 0, 129], Symbol(symbol='C', offset=1): [None, 0, 149]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 134], '1': ["1'", 1, 134], "0'": ["0'", 1, 130], "1'": ["1'", 1, 130], Symbol(symbol='C', offset=1): [None, 1, 150]}, direction=1)
133 State(step=55, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 137]}, direction=None)
134 State(step=55, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 138]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ['0', 0, 141], '1': ['1', 3, 144], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ['0', 1, 142], '1': ['1', 0, 141], "0'": ["0'", 1, 138], "1'": ["1'", 1, 138], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
141 State(step=57, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 145]}, direction=None)
142 State(step=57, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 146]}, direction=None)
144 State(step=57, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 148]}, direction=None)
145 State(step=58, acc=0, transitions={'0': ["0'", 0, 125], '1': ["0'", 0, 125], "0'": ["0'", 0, 145], "1'": ["1'", 0, 145], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
146 State(step=58, acc=1, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 1, 146], "1'": ["1'", 1, 146], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
148 State(step=58, acc=3, transitions={'0': ["1'", 1, 126], '1': ["1'", 1, 126], "0'": ["0'", 3, 148], "1'": ["1'", 3, 148], Symbol(symbol='B', offset=1): [None, 3, 152]}, direction=1)
149 State(step=59, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 153]}, direction=None)
150 State(step=59, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 154]}, direction=None)
152 State(step=59, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 156]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 153], '1': ['1', 0, 153], "0'": ['0', 0, 153], "1'": ['1', 0, 153], Symbol(symbol='C', offset=1): [None, 0, 157]}, direction=1)
154 State(step=60, acc=1, transitions={'0': ['0', 1, 154], '1': ['1', 1, 154], "0'": ['0', 1, 154], "1'": ['1', 1, 154], Symbol(symbol='C', offset=1): [None, 1, 158]}, direction=1)
156 State(step=60, acc=3, transitions={'0': ['0', 3, 156], '1': ['1', 3, 156], "0'": ['0', 3, 156], "1'": ['1', 3, 156], Symbol(symbol='C', offset=1): [None, 3, 160]}, direction=1)
157 State(step=61, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 161]}, direction=None)
158 State(step=61, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 162]}, direction=None)
160 State(step=61, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 164]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 161], '1': ['1', 0, 161], "0'": ['0', 0, 161], "1'": ['1', 0, 161], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
162 State(step=62, acc=1, transitions={'0': ['0', 1, 162], '1': ['1', 1, 162], "0'": ['0', 1, 162], "1'": ['1', 1, 162], Symbol(symbol='B', offset=1): [None, 1, 72]}, direction=1)
164 State(step=62, acc=3, transitions={'0': ['0', 3, 164], '1': ['1', 3, 164], "0'": ['0', 3, 164], "1'": ['1', 3, 164], Symbol(symbol='B', offset=1): [None, 3, 74]}, direction=1)
>>> for state1 in quasis:
	if type(state1)==State:
		for state2 in quasis:
			if type(state2)==State:
				if state1.transitions==state2.transitions:
					print('yay')

					
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
Traceback (most recent call last):
  File "<pyshell#319>", line 6, in <module>
    print('yay')
KeyboardInterrupt
>>> for k,state1 in enumerate(quasis):
	if type(state1)==State:
		for j,state2 in enumerate(quasis):
			if k!=j and type(state2)==State:
				if state1.transitions==state2.transitions:
					print('yay')

					
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
yay
>>> for k,state1 in enumerate(quasis):
	if type(state1)==State:
		for j,state2 in enumerate(quasis):
			if k!=j and type(state2)==State:
				if state1.transitions==state2.transitions:
					print(k,j)

					
71 72
71 73
71 74
72 71
72 73
72 74
73 71
73 72
73 74
74 71
74 72
74 73
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#324>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 549, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in merge_links
    if type(state2)==State:
KeyboardInterrupt

>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 550, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 530, in merge_links
    replace_links(j,k)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 405, in replace_links
    for symbol in quasi.transitions:
TypeError: 'NoneType' object is not iterable
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 550, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 527, in merge_links
    if type(state2)==State:
KeyboardInterrupt

>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()

 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
merge
Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 550, in compile_add
    print('merge')
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
merge 0 71
merge 0 71
merge 0 71
merge 0 71
merge 0 71
merge 0 71
merge 0 71
merge 0 71
merge 0 71
merge 0 71
mergeTraceback (most recent call last):
  File "<pyshell#329>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 551, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 530, in merge_links
    print('merge',j,k)
KeyboardInterrupt
>>> quasis[0]
>>> quasis[71]
State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
merge 72 71
merge 73 71
merge 74 71
0 End(is_start=True, next_quasis=[63])
13 End(is_start=False, next_quasis=None)
63 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 67]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 67], '1': ['0', 0, 67], "0'": ['0', 0, 67], "1'": ['0', 0, 67], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
71 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
75 State(step=40, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 76], "0'": ['0', 0, 75], "1'": ['0', 1, 76], Symbol(symbol='B', offset=1): [None, 0, 93]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 76], "0'": ['1', 0, 75], "1'": ['1', 1, 76], Symbol(symbol='B', offset=1): [None, 1, 94]}, direction=1)
77 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 81]}, direction=None)
78 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 82]}, direction=None)
80 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 84]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Symbol(symbol='A', offset=-1): [None, 0, 85]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Symbol(symbol='A', offset=-1): [None, 1, 86]}, direction=-1)
84 State(step=42, acc=3, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 3, 84], "1'": ["1'", 3, 84], Symbol(symbol='A', offset=-1): [None, 3, 88]}, direction=-1)
85 State(step=43, acc=0, transitions={Symbol(symbol='A', offset=0): [None, 0, 89]}, direction=None)
86 State(step=43, acc=1, transitions={Symbol(symbol='A', offset=0): [None, 1, 90]}, direction=None)
88 State(step=43, acc=3, transitions={Symbol(symbol='A', offset=0): [None, 3, 92]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 89], '1': ['1', 0, 89], "0'": ['0', 0, 89], "1'": ['1', 0, 89], Symbol(symbol='A', offset=1): [None, 0, 13]}, direction=1)
90 State(step=44, acc=1, transitions={'0': ['0', 1, 90], '1': ['1', 1, 90], "0'": ['0', 1, 90], "1'": ['1', 1, 90], Symbol(symbol='A', offset=1): [None, 1, 13]}, direction=1)
92 State(step=44, acc=3, transitions={'0': ['0', 3, 92], '1': ['1', 3, 92], "0'": ['0', 3, 92], "1'": ['1', 3, 92], Symbol(symbol='A', offset=1): [None, 3, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 97]}, direction=None)
94 State(step=45, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 98]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 0, 97], "1'": ["1'", 0, 97], Symbol(symbol='B', offset=-1): [None, 0, 109]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 1, 98], "1'": ["1'", 1, 98], Symbol(symbol='B', offset=-1): [None, 1, 110]}, direction=-1)
101 State(step=47, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 105]}, direction=None)
102 State(step=47, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 106]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 93], '1': ["1'", 1, 110], "0'": ["0'", 0, 105], "1'": ["1'", 0, 105], Symbol(symbol='C', offset=-1): [None, 0, 109]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 112], '1': ["1'", 0, 93], "0'": ["0'", 1, 106], "1'": ["1'", 1, 106], Symbol(symbol='C', offset=-1): [None, 1, 110]}, direction=-1)
109 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 113]}, direction=None)
110 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 114]}, direction=None)
112 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 116]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 113], '1': ['1', 0, 113], "0'": ['0', 0, 113], "1'": ['1', 0, 113], Symbol(symbol='B', offset=1): [None, 0, 117]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 114], '1': ['1', 1, 114], "0'": ['0', 1, 114], "1'": ['1', 1, 114], Symbol(symbol='B', offset=1): [None, 1, 118]}, direction=1)
116 State(step=50, acc=3, transitions={'0': ['0', 3, 116], '1': ['1', 3, 116], "0'": ['0', 3, 116], "1'": ['1', 3, 116], Symbol(symbol='B', offset=1): [None, 3, 120]}, direction=1)
117 State(step=51, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 121]}, direction=None)
118 State(step=51, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 122]}, direction=None)
120 State(step=51, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 124]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 121], '1': ['1', 0, 121], "0'": ['0', 0, 121], "1'": ['1', 0, 121], Symbol(symbol='C', offset=1): [None, 0, 77]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 122], '1': ['1', 1, 122], "0'": ['0', 1, 122], "1'": ['1', 1, 122], Symbol(symbol='C', offset=1): [None, 1, 78]}, direction=1)
124 State(step=52, acc=3, transitions={'0': ['0', 3, 124], '1': ['1', 3, 124], "0'": ['0', 3, 124], "1'": ['1', 3, 124], Symbol(symbol='C', offset=1): [None, 3, 80]}, direction=1)
125 State(step=53, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 129]}, direction=None)
126 State(step=53, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 130]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 133], '1': ["1'", 1, 134], "0'": ["0'", 0, 129], "1'": ["1'", 0, 129], Symbol(symbol='C', offset=1): [None, 0, 149]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 134], '1': ["1'", 1, 134], "0'": ["0'", 1, 130], "1'": ["1'", 1, 130], Symbol(symbol='C', offset=1): [None, 1, 150]}, direction=1)
133 State(step=55, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 137]}, direction=None)
134 State(step=55, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 138]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ['0', 0, 141], '1': ['1', 3, 144], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ['0', 1, 142], '1': ['1', 0, 141], "0'": ["0'", 1, 138], "1'": ["1'", 1, 138], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
141 State(step=57, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 145]}, direction=None)
142 State(step=57, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 146]}, direction=None)
144 State(step=57, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 148]}, direction=None)
145 State(step=58, acc=0, transitions={'0': ["0'", 0, 125], '1': ["0'", 0, 125], "0'": ["0'", 0, 145], "1'": ["1'", 0, 145], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
146 State(step=58, acc=1, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 1, 146], "1'": ["1'", 1, 146], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
148 State(step=58, acc=3, transitions={'0': ["1'", 1, 126], '1': ["1'", 1, 126], "0'": ["0'", 3, 148], "1'": ["1'", 3, 148], Symbol(symbol='B', offset=1): [None, 3, 152]}, direction=1)
149 State(step=59, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 153]}, direction=None)
150 State(step=59, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 154]}, direction=None)
152 State(step=59, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 156]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 153], '1': ['1', 0, 153], "0'": ['0', 0, 153], "1'": ['1', 0, 153], Symbol(symbol='C', offset=1): [None, 0, 157]}, direction=1)
154 State(step=60, acc=1, transitions={'0': ['0', 1, 154], '1': ['1', 1, 154], "0'": ['0', 1, 154], "1'": ['1', 1, 154], Symbol(symbol='C', offset=1): [None, 1, 158]}, direction=1)
156 State(step=60, acc=3, transitions={'0': ['0', 3, 156], '1': ['1', 3, 156], "0'": ['0', 3, 156], "1'": ['1', 3, 156], Symbol(symbol='C', offset=1): [None, 3, 160]}, direction=1)
157 State(step=61, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 161]}, direction=None)
158 State(step=61, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 162]}, direction=None)
160 State(step=61, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 164]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 161], '1': ['1', 0, 161], "0'": ['0', 0, 161], "1'": ['1', 0, 161], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
162 State(step=62, acc=1, transitions={'0': ['0', 1, 162], '1': ['1', 1, 162], "0'": ['0', 1, 162], "1'": ['1', 1, 162], Symbol(symbol='B', offset=1): [None, 1, 71]}, direction=1)
164 State(step=62, acc=3, transitions={'0': ['0', 3, 164], '1': ['1', 3, 164], "0'": ['0', 3, 164], "1'": ['1', 3, 164], Symbol(symbol='B', offset=1): [None, 3, 71]}, direction=1)
>>> len(used_states)
65
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==Instruction and quasi.command=='SUBs':
		print(k)

		
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==Instruction:
		print(k,quasi.command)

		
1 ZEROs
3 SLLs
5 MAP
6 STORE
7 BRANCH
10 JUMP
12 UNREAD
16 LOAD
17 LOAD
18 MAP
19 BRANCH
21 UNREAD
22 UNREAD
26 LOAD
27 MAP
28 LOAD
29 MAP
30 MAP
31 STORE
32 JUMP
34 UNREAD
35 UNREAD
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==Step and quasi.step in [28,31]:
		print(k)

		
Traceback (most recent call last):
  File "<pyshell#343>", line 2, in <module>
    if type(quasi)==Step and quasi.step in [28,31]:
AttributeError: 'Step' object has no attribute 'step'
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==Step and quasi.instruction in [28,31]:
		print(k)

		
55
56
57
58
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State and quasi.step in [55,56,57,58]:
		print(k)

		
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
>>> memory_command('LOADBIG')
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    memory_command('LOADBIG')
NameError: name 'memory_command' is not defined
>>> is_memory_command('LOADBIG')
['LOAD', [], ['BIG']]
>>> not ['LOAD', [], ['BIG']][2]
False
>>> not is_memory_command('LOAD')[2]
True
>>> is_memory_command('LOADI')
>>> for k,quasi in quasis:
	if type(quasi)==State and not quasis[quasi.step].is_found and len(quasis[quasi.step].next_quasis)!=1:
		print(k)

		
Traceback (most recent call last):
  File "<pyshell#356>", line 1, in <module>
    for k,quasi in quasis:
TypeError: cannot unpack non-iterable End object
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State and not quasis[quasi.step].is_found and len(quasis[quasi.step].next_quasis)!=1:
		print(k)

		
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
merge 72 71
merge 73 71
merge 74 71
0 End(is_start=True, next_quasis=[63])
13 End(is_start=False, next_quasis=None)
63 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 67]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 67], '1': ['0', 0, 67], "0'": ['0', 0, 67], "1'": ['0', 0, 67], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
71 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
75 State(step=40, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 76], "0'": ['0', 0, 75], "1'": ['0', 1, 76], Symbol(symbol='B', offset=1): [None, 0, 93]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 76], "0'": ['1', 0, 75], "1'": ['1', 1, 76], Symbol(symbol='B', offset=1): [None, 1, 94]}, direction=1)
77 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 81]}, direction=None)
78 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 82]}, direction=None)
80 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 84]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Symbol(symbol='A', offset=0): [None, 0, 85]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Symbol(symbol='A', offset=0): [None, 1, 86]}, direction=-1)
84 State(step=42, acc=3, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 3, 84], "1'": ["1'", 3, 84], Symbol(symbol='A', offset=0): [None, 3, 88]}, direction=-1)
85 State(step=43, acc=0, transitions={Symbol(symbol='A', offset=0): [None, 0, 89]}, direction=None)
86 State(step=43, acc=1, transitions={Symbol(symbol='A', offset=0): [None, 1, 90]}, direction=None)
88 State(step=43, acc=3, transitions={Symbol(symbol='A', offset=0): [None, 3, 92]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 89], '1': ['1', 0, 89], "0'": ['0', 0, 89], "1'": ['1', 0, 89], Symbol(symbol='A', offset=1): [None, 0, 13]}, direction=1)
90 State(step=44, acc=1, transitions={'0': ['0', 1, 90], '1': ['1', 1, 90], "0'": ['0', 1, 90], "1'": ['1', 1, 90], Symbol(symbol='A', offset=1): [None, 1, 13]}, direction=1)
92 State(step=44, acc=3, transitions={'0': ['0', 3, 92], '1': ['1', 3, 92], "0'": ['0', 3, 92], "1'": ['1', 3, 92], Symbol(symbol='A', offset=1): [None, 3, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 97]}, direction=None)
94 State(step=45, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 98]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 0, 97], "1'": ["1'", 0, 97], Symbol(symbol='B', offset=0): [None, 0, 109]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 1, 98], "1'": ["1'", 1, 98], Symbol(symbol='B', offset=0): [None, 1, 110]}, direction=-1)
101 State(step=47, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 105]}, direction=None)
102 State(step=47, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 106]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 93], '1': ["1'", 1, 110], "0'": ["0'", 0, 105], "1'": ["1'", 0, 105], Symbol(symbol='C', offset=0): [None, 0, 109]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 112], '1': ["1'", 0, 93], "0'": ["0'", 1, 106], "1'": ["1'", 1, 106], Symbol(symbol='C', offset=0): [None, 1, 110]}, direction=-1)
109 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 113]}, direction=None)
110 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 114]}, direction=None)
112 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 116]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 113], '1': ['1', 0, 113], "0'": ['0', 0, 113], "1'": ['1', 0, 113], Symbol(symbol='B', offset=1): [None, 0, 117]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 114], '1': ['1', 1, 114], "0'": ['0', 1, 114], "1'": ['1', 1, 114], Symbol(symbol='B', offset=1): [None, 1, 118]}, direction=1)
116 State(step=50, acc=3, transitions={'0': ['0', 3, 116], '1': ['1', 3, 116], "0'": ['0', 3, 116], "1'": ['1', 3, 116], Symbol(symbol='B', offset=1): [None, 3, 120]}, direction=1)
117 State(step=51, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 121]}, direction=None)
118 State(step=51, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 122]}, direction=None)
120 State(step=51, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 124]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 121], '1': ['1', 0, 121], "0'": ['0', 0, 121], "1'": ['1', 0, 121], Symbol(symbol='C', offset=1): [None, 0, 77]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 122], '1': ['1', 1, 122], "0'": ['0', 1, 122], "1'": ['1', 1, 122], Symbol(symbol='C', offset=1): [None, 1, 78]}, direction=1)
124 State(step=52, acc=3, transitions={'0': ['0', 3, 124], '1': ['1', 3, 124], "0'": ['0', 3, 124], "1'": ['1', 3, 124], Symbol(symbol='C', offset=1): [None, 3, 80]}, direction=1)
125 State(step=53, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 129]}, direction=None)
126 State(step=53, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 130]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 133], '1': ["1'", 1, 134], "0'": ["0'", 0, 129], "1'": ["1'", 0, 129], Symbol(symbol='C', offset=1): [None, 0, 149]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 134], '1': ["1'", 1, 134], "0'": ["0'", 1, 130], "1'": ["1'", 1, 130], Symbol(symbol='C', offset=1): [None, 1, 150]}, direction=1)
133 State(step=55, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 137]}, direction=None)
134 State(step=55, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 138]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ['0', 0, 141], '1': ['1', 3, 144], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ['0', 1, 142], '1': ['1', 0, 141], "0'": ["0'", 1, 138], "1'": ["1'", 1, 138], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
141 State(step=57, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 145]}, direction=None)
142 State(step=57, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 146]}, direction=None)
144 State(step=57, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 148]}, direction=None)
145 State(step=58, acc=0, transitions={'0': ["0'", 0, 125], '1': ["0'", 0, 125], "0'": ["0'", 0, 145], "1'": ["1'", 0, 145], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
146 State(step=58, acc=1, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 1, 146], "1'": ["1'", 1, 146], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
148 State(step=58, acc=3, transitions={'0': ["1'", 1, 126], '1': ["1'", 1, 126], "0'": ["0'", 3, 148], "1'": ["1'", 3, 148], Symbol(symbol='B', offset=1): [None, 3, 152]}, direction=1)
149 State(step=59, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 153]}, direction=None)
150 State(step=59, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 154]}, direction=None)
152 State(step=59, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 156]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 153], '1': ['1', 0, 153], "0'": ['0', 0, 153], "1'": ['1', 0, 153], Symbol(symbol='C', offset=1): [None, 0, 157]}, direction=1)
154 State(step=60, acc=1, transitions={'0': ['0', 1, 154], '1': ['1', 1, 154], "0'": ['0', 1, 154], "1'": ['1', 1, 154], Symbol(symbol='C', offset=1): [None, 1, 158]}, direction=1)
156 State(step=60, acc=3, transitions={'0': ['0', 3, 156], '1': ['1', 3, 156], "0'": ['0', 3, 156], "1'": ['1', 3, 156], Symbol(symbol='C', offset=1): [None, 3, 160]}, direction=1)
157 State(step=61, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 161]}, direction=None)
158 State(step=61, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 162]}, direction=None)
160 State(step=61, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 164]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 161], '1': ['1', 0, 161], "0'": ['0', 0, 161], "1'": ['1', 0, 161], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
162 State(step=62, acc=1, transitions={'0': ['0', 1, 162], '1': ['1', 1, 162], "0'": ['0', 1, 162], "1'": ['1', 1, 162], Symbol(symbol='B', offset=1): [None, 1, 71]}, direction=1)
164 State(step=62, acc=3, transitions={'0': ['0', 3, 164], '1': ['1', 3, 164], "0'": ['0', 3, 164], "1'": ['1', 3, 164], Symbol(symbol='B', offset=1): [None, 3, 71]}, direction=1)
>>> len(used_states)
65
>>> for k,quasi in quasis:
	print(k,quasi)

	
Traceback (most recent call last):
  File "<pyshell#363>", line 1, in <module>
    for k,quasi in quasis:
TypeError: cannot unpack non-iterable End object
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[63])
1 Instruction(ZEROs, vard=B, next_quasis=[39])
2 None
3 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
4 FunctionCall(command='SLT', args=['B', 'C'], next_quasis=[41])
5 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[0])
6 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 43])
7 Instruction(BRANCH, next_quasis=[24, 39, 24, 24])
8 None
9 FunctionCall(command='SUBs', args=['B', 'C'], next_quasis=[10])
10 Instruction(JUMP, next_quasis=[39])
11 None
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[93])
15 None
16 Instruction(LOADNEXTBIG, vard=B, next_quasis=[47, 49])
17 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 49])
18 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[19])
19 Instruction(BRANCH, next_quasis=[45, 49, 49, 49])
20 None
21 Instruction(UNREAD, vard=B, next_quasis=[51])
22 Instruction(UNREAD, vard=C, next_quasis=[23])
23 End(is_start=False, next_quasis=[41])
24 End(is_start=True, next_quasis=[125])
25 None
26 Instruction(LOADNEXT, vard=C, next_quasis=[27, 59])
27 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[55])
28 Instruction(LOAD, vard=B, next_quasis=[29, 59])
29 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[57])
30 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
31 Instruction(STORENEXT, vard=B, next_quasis=[32, 59])
32 Instruction(JUMP, next_quasis=[53])
33 None
34 Instruction(UNREAD, vard=C, next_quasis=[61])
35 Instruction(UNREAD, vard=B, next_quasis=[36])
36 End(is_start=False, next_quasis=[10])
37 Step(instruction=1, is_found=False, variable='B', next_quasis=[38], direction=None)
38 Step(instruction=1, is_found=True, variable='B', next_quasis=[39], direction=None)
39 Step(instruction=3, is_found=False, variable='B', next_quasis=[40], direction=None)
40 Step(instruction=3, is_found=True, variable='B', next_quasis=[14], direction=None)
41 Step(instruction=6, is_found=False, variable='A', next_quasis=[42], direction=None)
42 Step(instruction=6, is_found=True, variable='A', next_quasis=[7, 43], direction=None)
43 Step(instruction=12, is_found=False, variable='A', next_quasis=[44], direction=None)
44 Step(instruction=12, is_found=True, variable='A', next_quasis=[13], direction=None)
45 Step(instruction=16, is_found=False, variable='B', next_quasis=[46], direction=None)
46 Step(instruction=16, is_found=True, variable='B', next_quasis=[47, 49], direction=None)
47 Step(instruction=17, is_found=False, variable='C', next_quasis=[48], direction=None)
48 Step(instruction=17, is_found=True, variable='C', next_quasis=[18, 49], direction=None)
49 Step(instruction=21, is_found=False, variable='B', next_quasis=[50], direction=None)
50 Step(instruction=21, is_found=True, variable='B', next_quasis=[51], direction=None)
51 Step(instruction=22, is_found=False, variable='C', next_quasis=[52], direction=None)
52 Step(instruction=22, is_found=True, variable='C', next_quasis=[23], direction=None)
53 Step(instruction=26, is_found=False, variable='C', next_quasis=[54], direction=None)
54 Step(instruction=26, is_found=True, variable='C', next_quasis=[27, 59], direction=None)
55 Step(instruction=28, is_found=False, variable='B', next_quasis=[56], direction=None)
56 Step(instruction=28, is_found=True, variable='B', next_quasis=[29, 59], direction=None)
57 Step(instruction=31, is_found=False, variable='B', next_quasis=[58], direction=None)
58 Step(instruction=31, is_found=True, variable='B', next_quasis=[32, 59], direction=None)
59 Step(instruction=34, is_found=False, variable='C', next_quasis=[60], direction=None)
60 Step(instruction=34, is_found=True, variable='C', next_quasis=[61], direction=None)
61 Step(instruction=35, is_found=False, variable='B', next_quasis=[62], direction=None)
62 Step(instruction=35, is_found=True, variable='B', next_quasis=[36], direction=None)
63 State(step=37, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 67]}, direction=None)
64 State(step=37, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 68]}, direction=None)
65 State(step=37, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 69]}, direction=None)
66 State(step=37, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 70]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 67], '1': ['0', 0, 67], "0'": ['0', 0, 67], "1'": ['0', 0, 67], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
68 State(step=38, acc=1, transitions={'0': ['0', 1, 68], '1': ['0', 1, 68], "0'": ['0', 1, 68], "1'": ['0', 1, 68], Symbol(symbol='B', offset=1): [None, 1, 71]}, direction=1)
69 State(step=38, acc=2, transitions={'0': ['0', 2, 69], '1': ['0', 2, 69], "0'": ['0', 2, 69], "1'": ['0', 2, 69], Symbol(symbol='B', offset=1): [None, 2, 71]}, direction=1)
70 State(step=38, acc=3, transitions={'0': ['0', 3, 70], '1': ['0', 3, 70], "0'": ['0', 3, 70], "1'": ['0', 3, 70], Symbol(symbol='B', offset=1): [None, 3, 71]}, direction=1)
71 State(step=39, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 1, 76]}, direction=None)
72 None
73 None
74 None
75 State(step=40, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 76], "0'": ['0', 0, 75], "1'": ['0', 1, 76], Symbol(symbol='B', offset=1): [None, 0, 93]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 76], "0'": ['1', 0, 75], "1'": ['1', 1, 76], Symbol(symbol='B', offset=1): [None, 1, 94]}, direction=1)
77 State(step=41, acc=0, transitions={Symbol(symbol='A', offset=1): [None, 0, 81]}, direction=None)
78 State(step=41, acc=1, transitions={Symbol(symbol='A', offset=1): [None, 1, 82]}, direction=None)
79 State(step=41, acc=2, transitions={Symbol(symbol='A', offset=1): [None, 2, 83]}, direction=None)
80 State(step=41, acc=3, transitions={Symbol(symbol='A', offset=1): [None, 3, 84]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Symbol(symbol='A', offset=0): [None, 0, 85]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Symbol(symbol='A', offset=0): [None, 1, 86]}, direction=-1)
83 State(step=42, acc=2, transitions={'0': ["0'", 2, 127], '1': ["1'", 2, 127], "0'": ["0'", 2, 83], "1'": ["1'", 2, 83], Symbol(symbol='A', offset=0): [None, 2, 87]}, direction=-1)
84 State(step=42, acc=3, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 3, 84], "1'": ["1'", 3, 84], Symbol(symbol='A', offset=0): [None, 3, 88]}, direction=-1)
85 State(step=43, acc=0, transitions={Symbol(symbol='A', offset=0): [None, 0, 89]}, direction=None)
86 State(step=43, acc=1, transitions={Symbol(symbol='A', offset=0): [None, 1, 90]}, direction=None)
87 State(step=43, acc=2, transitions={Symbol(symbol='A', offset=0): [None, 2, 91]}, direction=None)
88 State(step=43, acc=3, transitions={Symbol(symbol='A', offset=0): [None, 3, 92]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 89], '1': ['1', 0, 89], "0'": ['0', 0, 89], "1'": ['1', 0, 89], Symbol(symbol='A', offset=1): [None, 0, 13]}, direction=1)
90 State(step=44, acc=1, transitions={'0': ['0', 1, 90], '1': ['1', 1, 90], "0'": ['0', 1, 90], "1'": ['1', 1, 90], Symbol(symbol='A', offset=1): [None, 1, 13]}, direction=1)
91 State(step=44, acc=2, transitions={'0': ['0', 2, 91], '1': ['1', 2, 91], "0'": ['0', 2, 91], "1'": ['1', 2, 91], Symbol(symbol='A', offset=1): [None, 2, 13]}, direction=1)
92 State(step=44, acc=3, transitions={'0': ['0', 3, 92], '1': ['1', 3, 92], "0'": ['0', 3, 92], "1'": ['1', 3, 92], Symbol(symbol='A', offset=1): [None, 3, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Symbol(symbol='B', offset=1): [None, 0, 97]}, direction=None)
94 State(step=45, acc=1, transitions={Symbol(symbol='B', offset=1): [None, 1, 98]}, direction=None)
95 State(step=45, acc=2, transitions={Symbol(symbol='B', offset=1): [None, 2, 99]}, direction=None)
96 State(step=45, acc=3, transitions={Symbol(symbol='B', offset=1): [None, 3, 100]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 0, 97], "1'": ["1'", 0, 97], Symbol(symbol='B', offset=0): [None, 0, 109]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 1, 98], "1'": ["1'", 1, 98], Symbol(symbol='B', offset=0): [None, 1, 110]}, direction=-1)
99 State(step=46, acc=2, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 2, 99], "1'": ["1'", 2, 99], Symbol(symbol='B', offset=0): [None, 2, 111]}, direction=-1)
100 State(step=46, acc=3, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 3, 100], "1'": ["1'", 3, 100], Symbol(symbol='B', offset=0): [None, 3, 112]}, direction=-1)
101 State(step=47, acc=0, transitions={Symbol(symbol='C', offset=1): [None, 0, 105]}, direction=None)
102 State(step=47, acc=1, transitions={Symbol(symbol='C', offset=1): [None, 1, 106]}, direction=None)
103 State(step=47, acc=2, transitions={Symbol(symbol='C', offset=1): [None, 2, 107]}, direction=None)
104 State(step=47, acc=3, transitions={Symbol(symbol='C', offset=1): [None, 3, 108]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 93], '1': ["1'", 1, 110], "0'": ["0'", 0, 105], "1'": ["1'", 0, 105], Symbol(symbol='C', offset=0): [None, 0, 109]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 112], '1': ["1'", 0, 93], "0'": ["0'", 1, 106], "1'": ["1'", 1, 106], Symbol(symbol='C', offset=0): [None, 1, 110]}, direction=-1)
107 State(step=48, acc=2, transitions={'0': ["0'", 2, 111], '1': ["1'", 2, 111], "0'": ["0'", 2, 107], "1'": ["1'", 2, 107], Symbol(symbol='C', offset=0): [None, 2, 111]}, direction=-1)
108 State(step=48, acc=3, transitions={'0': ["0'", 3, 112], '1': ["1'", 3, 112], "0'": ["0'", 3, 108], "1'": ["1'", 3, 108], Symbol(symbol='C', offset=0): [None, 3, 112]}, direction=-1)
109 State(step=49, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 113]}, direction=None)
110 State(step=49, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 114]}, direction=None)
111 State(step=49, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 115]}, direction=None)
112 State(step=49, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 116]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 113], '1': ['1', 0, 113], "0'": ['0', 0, 113], "1'": ['1', 0, 113], Symbol(symbol='B', offset=1): [None, 0, 117]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 114], '1': ['1', 1, 114], "0'": ['0', 1, 114], "1'": ['1', 1, 114], Symbol(symbol='B', offset=1): [None, 1, 118]}, direction=1)
115 State(step=50, acc=2, transitions={'0': ['0', 2, 115], '1': ['1', 2, 115], "0'": ['0', 2, 115], "1'": ['1', 2, 115], Symbol(symbol='B', offset=1): [None, 2, 119]}, direction=1)
116 State(step=50, acc=3, transitions={'0': ['0', 3, 116], '1': ['1', 3, 116], "0'": ['0', 3, 116], "1'": ['1', 3, 116], Symbol(symbol='B', offset=1): [None, 3, 120]}, direction=1)
117 State(step=51, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 121]}, direction=None)
118 State(step=51, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 122]}, direction=None)
119 State(step=51, acc=2, transitions={Symbol(symbol='C', offset=0): [None, 2, 123]}, direction=None)
120 State(step=51, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 124]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 121], '1': ['1', 0, 121], "0'": ['0', 0, 121], "1'": ['1', 0, 121], Symbol(symbol='C', offset=1): [None, 0, 77]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 122], '1': ['1', 1, 122], "0'": ['0', 1, 122], "1'": ['1', 1, 122], Symbol(symbol='C', offset=1): [None, 1, 78]}, direction=1)
123 State(step=52, acc=2, transitions={'0': ['0', 2, 123], '1': ['1', 2, 123], "0'": ['0', 2, 123], "1'": ['1', 2, 123], Symbol(symbol='C', offset=1): [None, 2, 79]}, direction=1)
124 State(step=52, acc=3, transitions={'0': ['0', 3, 124], '1': ['1', 3, 124], "0'": ['0', 3, 124], "1'": ['1', 3, 124], Symbol(symbol='C', offset=1): [None, 3, 80]}, direction=1)
125 State(step=53, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 129]}, direction=None)
126 State(step=53, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 130]}, direction=None)
127 State(step=53, acc=2, transitions={Symbol(symbol='C', offset=0): [None, 2, 131]}, direction=None)
128 State(step=53, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 132]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 133], '1': ["1'", 1, 134], "0'": ["0'", 0, 129], "1'": ["1'", 0, 129], Symbol(symbol='C', offset=1): [None, 0, 149]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 134], '1': ["1'", 1, 134], "0'": ["0'", 1, 130], "1'": ["1'", 1, 130], Symbol(symbol='C', offset=1): [None, 1, 150]}, direction=1)
131 State(step=54, acc=2, transitions={'0': ["0'", 2, 135], '1': ["1'", 2, 135], "0'": ["0'", 2, 131], "1'": ["1'", 2, 131], Symbol(symbol='C', offset=1): [None, 2, 151]}, direction=1)
132 State(step=54, acc=3, transitions={'0': ["0'", 3, 136], '1': ["1'", 0, 133], "0'": ["0'", 3, 132], "1'": ["1'", 3, 132], Symbol(symbol='C', offset=1): [None, 3, 152]}, direction=1)
133 State(step=55, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 137]}, direction=None)
134 State(step=55, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 138]}, direction=None)
135 State(step=55, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 139]}, direction=None)
136 State(step=55, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 140]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ['0', 0, 141], '1': ['1', 3, 144], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ['0', 1, 142], '1': ['1', 0, 141], "0'": ["0'", 1, 138], "1'": ["1'", 1, 138], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
139 State(step=56, acc=2, transitions={'0': ['0', 2, 143], '1': ['1', 2, 143], "0'": ["0'", 2, 139], "1'": ["1'", 2, 139], Symbol(symbol='B', offset=1): [None, 2, 151]}, direction=1)
140 State(step=56, acc=3, transitions={'0': ['0', 3, 144], '1': ['1', 2, 143], "0'": ["0'", 3, 140], "1'": ["1'", 3, 140], Symbol(symbol='B', offset=1): [None, 3, 152]}, direction=1)
141 State(step=57, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 145]}, direction=None)
142 State(step=57, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 146]}, direction=None)
143 State(step=57, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 147]}, direction=None)
144 State(step=57, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 148]}, direction=None)
145 State(step=58, acc=0, transitions={'0': ["0'", 0, 125], '1': ["0'", 0, 125], "0'": ["0'", 0, 145], "1'": ["1'", 0, 145], Symbol(symbol='B', offset=1): [None, 0, 149]}, direction=1)
146 State(step=58, acc=1, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 1, 146], "1'": ["1'", 1, 146], Symbol(symbol='B', offset=1): [None, 1, 150]}, direction=1)
147 State(step=58, acc=2, transitions={'0': ["1'", 0, 125], '1': ["1'", 0, 125], "0'": ["0'", 2, 147], "1'": ["1'", 2, 147], Symbol(symbol='B', offset=1): [None, 2, 151]}, direction=1)
148 State(step=58, acc=3, transitions={'0': ["1'", 1, 126], '1': ["1'", 1, 126], "0'": ["0'", 3, 148], "1'": ["1'", 3, 148], Symbol(symbol='B', offset=1): [None, 3, 152]}, direction=1)
149 State(step=59, acc=0, transitions={Symbol(symbol='C', offset=0): [None, 0, 153]}, direction=None)
150 State(step=59, acc=1, transitions={Symbol(symbol='C', offset=0): [None, 1, 154]}, direction=None)
151 State(step=59, acc=2, transitions={Symbol(symbol='C', offset=0): [None, 2, 155]}, direction=None)
152 State(step=59, acc=3, transitions={Symbol(symbol='C', offset=0): [None, 3, 156]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 153], '1': ['1', 0, 153], "0'": ['0', 0, 153], "1'": ['1', 0, 153], Symbol(symbol='C', offset=1): [None, 0, 157]}, direction=1)
154 State(step=60, acc=1, transitions={'0': ['0', 1, 154], '1': ['1', 1, 154], "0'": ['0', 1, 154], "1'": ['1', 1, 154], Symbol(symbol='C', offset=1): [None, 1, 158]}, direction=1)
155 State(step=60, acc=2, transitions={'0': ['0', 2, 155], '1': ['1', 2, 155], "0'": ['0', 2, 155], "1'": ['1', 2, 155], Symbol(symbol='C', offset=1): [None, 2, 159]}, direction=1)
156 State(step=60, acc=3, transitions={'0': ['0', 3, 156], '1': ['1', 3, 156], "0'": ['0', 3, 156], "1'": ['1', 3, 156], Symbol(symbol='C', offset=1): [None, 3, 160]}, direction=1)
157 State(step=61, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 161]}, direction=None)
158 State(step=61, acc=1, transitions={Symbol(symbol='B', offset=0): [None, 1, 162]}, direction=None)
159 State(step=61, acc=2, transitions={Symbol(symbol='B', offset=0): [None, 2, 163]}, direction=None)
160 State(step=61, acc=3, transitions={Symbol(symbol='B', offset=0): [None, 3, 164]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 161], '1': ['1', 0, 161], "0'": ['0', 0, 161], "1'": ['1', 0, 161], Symbol(symbol='B', offset=1): [None, 0, 71]}, direction=1)
162 State(step=62, acc=1, transitions={'0': ['0', 1, 162], '1': ['1', 1, 162], "0'": ['0', 1, 162], "1'": ['1', 1, 162], Symbol(symbol='B', offset=1): [None, 1, 71]}, direction=1)
163 State(step=62, acc=2, transitions={'0': ['0', 2, 163], '1': ['1', 2, 163], "0'": ['0', 2, 163], "1'": ['1', 2, 163], Symbol(symbol='B', offset=1): [None, 2, 71]}, direction=1)
164 State(step=62, acc=3, transitions={'0': ['0', 3, 164], '1': ['1', 3, 164], "0'": ['0', 3, 164], "1'": ['1', 3, 164], Symbol(symbol='B', offset=1): [None, 3, 71]}, direction=1)
>>> quasi=quasis[137]
>>> type(quasi)==State
True
>>> step = quasis[quasi.step]
>>> step
Step(instruction=28, is_found=True, variable='B', next_quasis=[29, 59], direction=None)
>>> instruction = quasis[step.instruction]
>>> instruction
<__main__.Instruction object at 0x03D9F3F0>
>>> print(instruction)
Instruction(LOAD, vard=B, next_quasis=[29, 59])
>>> command = instruction.command
>>> step.is_found and command in ['LOAD','STORE']
True
>>> quasi.transitions
{'0': ['0', 0, 141], '1': ['1', 3, 144], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Symbol(symbol='B', offset=1): [None, 0, 149]}
>>> symbol = '0'
>>> quasi2 = quasis[quasi.transitions[symbol][2]]
>>> quasi2
State(step=57, acc=0, transitions={Symbol(symbol='B', offset=0): [None, 0, 145]}, direction=None)
>>> type(quasi2)==State
True
>>> step2 = quasis[quasi2.step]
>>> step2
Step(instruction=31, is_found=False, variable='B', next_quasis=[58], direction=None)
>>> not step.is_found and step.variable==step2.variable
False
>>> step.variable
'B'
>>> step2.variable
'B'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#385>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 581, in compile_add
    skip_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 512, in skip_searches
    transition = quasis[quasi2.transitions[0][2]].transitions
KeyError: 0
>>> quasi2
Traceback (most recent call last):
  File "<pyshell#386>", line 1, in <module>
    quasi2
NameError: name 'quasi2' is not defined
>>> quasi=quasis[137]
>>> quasi.transitions.keys()
Traceback (most recent call last):
  File "<pyshell#388>", line 1, in <module>
    quasi.transitions.keys()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\idlelib\rpc.py", line 621, in displayhook
    text = repr(value)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 143, in __repr__
    return 'Sym(\''+symbol+'\'+'+str(offset)+')'
NameError: name 'symbol' is not defined
>>> quasi.transitions
Traceback (most recent call last):
  File "<pyshell#389>", line 1, in <module>
    quasi.transitions
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\idlelib\rpc.py", line 621, in displayhook
    text = repr(value)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 143, in __repr__
    return 'Sym(\''+symbol+'\'+'+str(offset)+')'
NameError: name 'symbol' is not defined
>>> quasi
Traceback (most recent call last):
  File "<pyshell#390>", line 1, in <module>
    quasi
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\lib\idlelib\rpc.py", line 621, in displayhook
    text = repr(value)
  File "<string>", line 2, in __repr__
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 143, in __repr__
    return 'Sym(\''+symbol+'\'+'+str(offset)+')'
NameError: name 'symbol' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> quasi=quasis[137]
Traceback (most recent call last):
  File "<pyshell#391>", line 1, in <module>
    quasi=quasis[137]
IndexError: list index out of range
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#392>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 581, in compile_add
    skip_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 512, in skip_searches
    transition = quasis[quasi2.transitions[0][2]].transitions
KeyError: 0
>>> quasi=quasis[137]
>>> quasi.transitions.keys()
dict_keys(['0', '1', "0'", "1'", Sym('B'+1)])
>>> quasi.transitions.keys()[0]
Traceback (most recent call last):
  File "<pyshell#395>", line 1, in <module>
    quasi.transitions.keys()[0]
TypeError: 'dict_keys' object does not support indexing
>>> list(quasi.transitions.keys())[0]
'0'
>>> quasi.transitions.value()
Traceback (most recent call last):
  File "<pyshell#397>", line 1, in <module>
    quasi.transitions.value()
AttributeError: 'dict' object has no attribute 'value'
>>> quasi.transitions.values()
dict_values([['0', 0, 141], ['1', 3, 144], ["0'", 0, 137], ["1'", 0, 137], [None, 0, 149]])
>>> quasi.transitions.values()[0]
Traceback (most recent call last):
  File "<pyshell#399>", line 1, in <module>
    quasi.transitions.values()[0]
TypeError: 'dict_values' object does not support indexing
>>> list(quasi.transitions.values())[0]
['0', 0, 141]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
merge 72 71
merge 73 71
merge 74 71
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 586, in compile_add
    find_successors(0)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 546, in find_successors
    find_successors(j)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 552, in find_successors
    find_successors(j)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 552, in find_successors
    find_successors(j)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 552, in find_successors
    find_successors(j)
  [Previous line repeated 15 more times]
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 550, in find_successors
    if not j in used_states:
TypeError: unhashable type: 'dict'
>>> used_states
{0, 130, 134, 138, 13, 63, 67, 71, 75, 76, 77, 78, 81, 82, 86, 90, 93, 97, 101, 105, 109, 110, 113, 114, 117, 118, 121, 122, 126}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#403>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 583, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 562, in merge_links
    replace_links(j,k)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 408, in replace_links
    if quasi.transitions[symbol][2] == a:
KeyError: 2
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
['0', 0, 141] {'0': ["0'", 0, 125], '1': ["0'", 0, 125], "0'": ["0'", 0, 145], "1'": ["1'", 0, 145], Sym('B'+1): [None, 0, 149]}
['1', 3, 144] {'0': ["1'", 1, 126], '1': ["1'", 1, 126], "0'": ["0'", 3, 148], "1'": ["1'", 3, 148], Sym('B'+1): [None, 3, 152]}
['0', 1, 142] {'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 1, 146], "1'": ["1'", 1, 146], Sym('B'+1): [None, 1, 150]}
['1', 0, 141] {'0': ["0'", 0, 125], '1': ["0'", 0, 125], "0'": ["0'", 0, 145], "1'": ["1'", 0, 145], Sym('B'+1): [None, 0, 149]}
['0', 2, 143] {'0': ["1'", 0, 125], '1': ["1'", 0, 125], "0'": ["0'", 2, 147], "1'": ["1'", 2, 147], Sym('B'+1): [None, 2, 151]}
['1', 2, 143] {'0': ["1'", 0, 125], '1': ["1'", 0, 125], "0'": ["0'", 2, 147], "1'": ["1'", 2, 147], Sym('B'+1): [None, 2, 151]}
['0', 3, 144] {'0': ["1'", 1, 126], '1': ["1'", 1, 126], "0'": ["0'", 3, 148], "1'": ["1'", 3, 148], Sym('B'+1): [None, 3, 152]}
['1', 2, 143] {'0': ["1'", 0, 125], '1': ["1'", 0, 125], "0'": ["0'", 2, 147], "1'": ["1'", 2, 147], Sym('B'+1): [None, 2, 151]}
Traceback (most recent call last):
  File "<pyshell#404>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 584, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 563, in merge_links
    replace_links(j,k)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 408, in replace_links
    if quasi.transitions[symbol][2] == a:
KeyError: 2
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
0 End(is_start=True, next_quasis=[63])
13 End(is_start=False, next_quasis=None)
63 State(step=37, acc=0, transitions={Sym('B'+0): [None, 0, 67]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 67], '1': ['0', 0, 67], "0'": ['0', 0, 67], "1'": ['0', 0, 67], Sym('B'+1): [None, 0, 71]}, direction=1)
71 State(step=39, acc=0, transitions={Sym('B'+0): [None, 1, 76]}, direction=None)
75 State(step=40, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 76], "0'": ['0', 0, 75], "1'": ['0', 1, 76], Sym('B'+1): [None, 0, 93]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 76], "0'": ['1', 0, 75], "1'": ['1', 1, 76], Sym('B'+1): [None, 1, 94]}, direction=1)
77 State(step=41, acc=0, transitions={Sym('A'+1): [None, 0, 81]}, direction=None)
78 State(step=41, acc=1, transitions={Sym('A'+1): [None, 1, 82]}, direction=None)
80 State(step=41, acc=3, transitions={Sym('A'+1): [None, 3, 84]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Sym('A'+0): [None, 0, 85]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Sym('A'+0): [None, 1, 86]}, direction=-1)
84 State(step=42, acc=3, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 3, 84], "1'": ["1'", 3, 84], Sym('A'+0): [None, 3, 88]}, direction=-1)
85 State(step=43, acc=0, transitions={Sym('A'+0): [None, 0, 89]}, direction=None)
86 State(step=43, acc=1, transitions={Sym('A'+0): [None, 1, 90]}, direction=None)
88 State(step=43, acc=3, transitions={Sym('A'+0): [None, 3, 92]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 89], '1': ['1', 0, 89], "0'": ['0', 0, 89], "1'": ['1', 0, 89], Sym('A'+1): [None, 0, 13]}, direction=1)
90 State(step=44, acc=1, transitions={'0': ['0', 1, 90], '1': ['1', 1, 90], "0'": ['0', 1, 90], "1'": ['1', 1, 90], Sym('A'+1): [None, 1, 13]}, direction=1)
92 State(step=44, acc=3, transitions={'0': ['0', 3, 92], '1': ['1', 3, 92], "0'": ['0', 3, 92], "1'": ['1', 3, 92], Sym('A'+1): [None, 3, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Sym('B'+1): [None, 0, 97]}, direction=None)
94 State(step=45, acc=1, transitions={Sym('B'+1): [None, 1, 98]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 0, 97], "1'": ["1'", 0, 97], Sym('B'+0): [None, 0, 109]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 1, 98], "1'": ["1'", 1, 98], Sym('B'+0): [None, 1, 110]}, direction=-1)
101 State(step=47, acc=0, transitions={Sym('C'+1): [None, 0, 105]}, direction=None)
102 State(step=47, acc=1, transitions={Sym('C'+1): [None, 1, 106]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 93], '1': ["1'", 1, 110], "0'": ["0'", 0, 105], "1'": ["1'", 0, 105], Sym('C'+0): [None, 0, 109]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 112], '1': ["1'", 0, 93], "0'": ["0'", 1, 106], "1'": ["1'", 1, 106], Sym('C'+0): [None, 1, 110]}, direction=-1)
109 State(step=49, acc=0, transitions={Sym('B'+0): [None, 0, 113]}, direction=None)
110 State(step=49, acc=1, transitions={Sym('B'+0): [None, 1, 114]}, direction=None)
112 State(step=49, acc=3, transitions={Sym('B'+0): [None, 3, 116]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 113], '1': ['1', 0, 113], "0'": ['0', 0, 113], "1'": ['1', 0, 113], Sym('B'+1): [None, 0, 117]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 114], '1': ['1', 1, 114], "0'": ['0', 1, 114], "1'": ['1', 1, 114], Sym('B'+1): [None, 1, 118]}, direction=1)
116 State(step=50, acc=3, transitions={'0': ['0', 3, 116], '1': ['1', 3, 116], "0'": ['0', 3, 116], "1'": ['1', 3, 116], Sym('B'+1): [None, 3, 120]}, direction=1)
117 State(step=51, acc=0, transitions={Sym('C'+0): [None, 0, 121]}, direction=None)
118 State(step=51, acc=1, transitions={Sym('C'+0): [None, 1, 122]}, direction=None)
120 State(step=51, acc=3, transitions={Sym('C'+0): [None, 3, 124]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 121], '1': ['1', 0, 121], "0'": ['0', 0, 121], "1'": ['1', 0, 121], Sym('C'+1): [None, 0, 77]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 122], '1': ['1', 1, 122], "0'": ['0', 1, 122], "1'": ['1', 1, 122], Sym('C'+1): [None, 1, 78]}, direction=1)
124 State(step=52, acc=3, transitions={'0': ['0', 3, 124], '1': ['1', 3, 124], "0'": ['0', 3, 124], "1'": ['1', 3, 124], Sym('C'+1): [None, 3, 80]}, direction=1)
125 State(step=53, acc=0, transitions={Sym('C'+0): [None, 0, 129]}, direction=None)
126 State(step=53, acc=1, transitions={Sym('C'+0): [None, 1, 130]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 133], '1': ["1'", 1, 134], "0'": ["0'", 0, 129], "1'": ["1'", 0, 129], Sym('C'+1): [None, 0, 149]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 134], '1': ["1'", 1, 134], "0'": ["0'", 1, 130], "1'": ["1'", 1, 130], Sym('C'+1): [None, 1, 150]}, direction=1)
133 State(step=55, acc=0, transitions={Sym('B'+0): [None, 0, 137]}, direction=None)
134 State(step=55, acc=1, transitions={Sym('B'+0): [None, 1, 138]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ["0'", 0, 125], '1': ["1'", 1, 126], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Sym('B'+1): [None, 0, 149]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ["0'", 1, 126], '1': ["0'", 0, 125], "0'": ["0'", 1, 138], "1'": ["1'", 1, 138], Sym('B'+1): [None, 1, 150]}, direction=1)
149 State(step=59, acc=0, transitions={Sym('C'+0): [None, 0, 153]}, direction=None)
150 State(step=59, acc=1, transitions={Sym('C'+0): [None, 1, 154]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 153], '1': ['1', 0, 153], "0'": ['0', 0, 153], "1'": ['1', 0, 153], Sym('C'+1): [None, 0, 157]}, direction=1)
154 State(step=60, acc=1, transitions={'0': ['0', 1, 154], '1': ['1', 1, 154], "0'": ['0', 1, 154], "1'": ['1', 1, 154], Sym('C'+1): [None, 1, 158]}, direction=1)
157 State(step=61, acc=0, transitions={Sym('B'+0): [None, 0, 161]}, direction=None)
158 State(step=61, acc=1, transitions={Sym('B'+0): [None, 1, 162]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 161], '1': ['1', 0, 161], "0'": ['0', 0, 161], "1'": ['1', 0, 161], Sym('B'+1): [None, 0, 71]}, direction=1)
162 State(step=62, acc=1, transitions={'0': ['0', 1, 162], '1': ['1', 1, 162], "0'": ['0', 1, 162], "1'": ['1', 1, 162], Sym('B'+1): [None, 1, 71]}, direction=1)
>>> len(used_states)
55
>>> quasis[quasis[62].instruction]
<__main__.Instruction object at 0x039BFA10>
>>> print(quasis[quasis[62].instruction])
Instruction(UNREAD, vard=B, next_quasis=[36])
>>> for k in range(37,63):
	print(k,quasis[quasis[k].instruction])

	
37 Instruction(ZEROs, vard=B, next_quasis=[39])
38 Instruction(ZEROs, vard=B, next_quasis=[39])
39 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
40 Instruction(SLLs, vard=B, imm=1, next_quasis=[14])
41 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 43])
42 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 43])
43 Instruction(UNREAD, vard=A, next_quasis=[13])
44 Instruction(UNREAD, vard=A, next_quasis=[13])
45 Instruction(LOADNEXTBIG, vard=B, next_quasis=[47, 49])
46 Instruction(LOADNEXTBIG, vard=B, next_quasis=[47, 49])
47 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 49])
48 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 49])
49 Instruction(UNREAD, vard=B, next_quasis=[51])
50 Instruction(UNREAD, vard=B, next_quasis=[51])
51 Instruction(UNREAD, vard=C, next_quasis=[23])
52 Instruction(UNREAD, vard=C, next_quasis=[23])
53 Instruction(LOADNEXT, vard=C, next_quasis=[27, 59])
54 Instruction(LOADNEXT, vard=C, next_quasis=[27, 59])
55 Instruction(LOAD, vard=B, next_quasis=[29, 59])
56 Instruction(LOAD, vard=B, next_quasis=[29, 59])
57 Instruction(STORENEXT, vard=B, next_quasis=[32, 59])
58 Instruction(STORENEXT, vard=B, next_quasis=[32, 59])
59 Instruction(UNREAD, vard=C, next_quasis=[61])
60 Instruction(UNREAD, vard=C, next_quasis=[61])
61 Instruction(UNREAD, vard=B, next_quasis=[36])
62 Instruction(UNREAD, vard=B, next_quasis=[36])
>>> for k in range(37,63):
	print(k,quasis[quasis[k].instruction],quasis[k].is_found)

	
37 Instruction(ZEROs, vard=B, next_quasis=[39]) False
38 Instruction(ZEROs, vard=B, next_quasis=[39]) True
39 Instruction(SLLs, vard=B, imm=1, next_quasis=[14]) False
40 Instruction(SLLs, vard=B, imm=1, next_quasis=[14]) True
41 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 43]) False
42 Instruction(STORENEXTBIG, vard=A, next_quasis=[7, 43]) True
43 Instruction(UNREAD, vard=A, next_quasis=[13]) False
44 Instruction(UNREAD, vard=A, next_quasis=[13]) True
45 Instruction(LOADNEXTBIG, vard=B, next_quasis=[47, 49]) False
46 Instruction(LOADNEXTBIG, vard=B, next_quasis=[47, 49]) True
47 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 49]) False
48 Instruction(LOADNEXTBIG, vard=C, next_quasis=[18, 49]) True
49 Instruction(UNREAD, vard=B, next_quasis=[51]) False
50 Instruction(UNREAD, vard=B, next_quasis=[51]) True
51 Instruction(UNREAD, vard=C, next_quasis=[23]) False
52 Instruction(UNREAD, vard=C, next_quasis=[23]) True
53 Instruction(LOADNEXT, vard=C, next_quasis=[27, 59]) False
54 Instruction(LOADNEXT, vard=C, next_quasis=[27, 59]) True
55 Instruction(LOAD, vard=B, next_quasis=[29, 59]) False
56 Instruction(LOAD, vard=B, next_quasis=[29, 59]) True
57 Instruction(STORENEXT, vard=B, next_quasis=[32, 59]) False
58 Instruction(STORENEXT, vard=B, next_quasis=[32, 59]) True
59 Instruction(UNREAD, vard=C, next_quasis=[61]) False
60 Instruction(UNREAD, vard=C, next_quasis=[61]) True
61 Instruction(UNREAD, vard=B, next_quasis=[36]) False
62 Instruction(UNREAD, vard=B, next_quasis=[36]) True
>>> a={0:1,2:3}
>>> b={4:5,6:7}
>>> a.keys()+b.keys()
Traceback (most recent call last):
  File "<pyshell#416>", line 1, in <module>
    a.keys()+b.keys()
TypeError: unsupported operand type(s) for +: 'dict_keys' and 'dict_keys'
>>> a.keys()|b.keys()
{0, 2, 4, 6}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
Traceback (most recent call last):
  File "<pyshell#418>", line 1, in <module>
    compile_add()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 606, in compile_add
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 583, in merge_links
    if equal_states(k,j):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 153, in equal_states
    transition2 = get_none_transition(state2,symbol)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 143, in get_none_transition
    transition = [symbol,0,k]
NameError: name 'k' is not defined
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_add()
0 End(is_start=True, next_quasis=[63])
13 End(is_start=False, next_quasis=None)
63 State(step=37, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 67]}, direction=None)
67 State(step=38, acc=0, transitions={'0': ['0', 0, 67], '1': ['0', 0, 67], "0'": ['0', 0, 67], "1'": ['0', 0, 67], Sym('B'+1): [Sym('B'+1), 0, 71]}, direction=1)
71 State(step=39, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 1, 76]}, direction=None)
75 State(step=40, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 76], "0'": ['0', 0, 75], "1'": ['0', 1, 76], Sym('B'+1): [None, 0, 93]}, direction=1)
76 State(step=40, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 76], "0'": ['1', 0, 75], "1'": ['1', 1, 76], Sym('B'+1): [None, 1, 94]}, direction=1)
77 State(step=41, acc=0, transitions={Sym('A'+1): [Sym('A'+1), 0, 81]}, direction=None)
78 State(step=41, acc=1, transitions={Sym('A'+1): [Sym('A'+1), 1, 82]}, direction=None)
81 State(step=42, acc=0, transitions={'0': ["0'", 1, 126], '1': ["0'", 1, 126], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Sym('A'+0): [Sym('A'+0), 0, 85]}, direction=-1)
82 State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Sym('A'+0): [None, 1, 85]}, direction=-1)
85 State(step=43, acc=0, transitions={Sym('A'+0): [Sym('A'+0), 0, 89]}, direction=None)
89 State(step=44, acc=0, transitions={'0': ['0', 0, 89], '1': ['1', 0, 89], "0'": ['0', 0, 89], "1'": ['1', 0, 89], Sym('A'+1): [Sym('A'+1), 0, 13]}, direction=1)
93 State(step=45, acc=0, transitions={Sym('B'+1): [Sym('B'+1), 0, 97]}, direction=None)
94 State(step=45, acc=1, transitions={Sym('B'+1): [Sym('B'+1), 1, 98]}, direction=None)
97 State(step=46, acc=0, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 0, 97], "1'": ["1'", 0, 97], Sym('B'+0): [Sym('B'+0), 0, 109]}, direction=-1)
98 State(step=46, acc=1, transitions={'0': ["0'", 0, 101], '1': ["1'", 1, 102], "0'": ["0'", 1, 98], "1'": ["1'", 1, 98], Sym('B'+0): [Sym('B'+0), 1, 110]}, direction=-1)
101 State(step=47, acc=0, transitions={Sym('C'+1): [Sym('C'+1), 0, 105]}, direction=None)
102 State(step=47, acc=1, transitions={Sym('C'+1): [Sym('C'+1), 1, 106]}, direction=None)
105 State(step=48, acc=0, transitions={'0': ["0'", 0, 93], '1': ["1'", 1, 110], "0'": ["0'", 0, 105], "1'": ["1'", 0, 105], Sym('C'+0): [None, 0, 109]}, direction=-1)
106 State(step=48, acc=1, transitions={'0': ["0'", 3, 109], '1': ["1'", 0, 93], "0'": ["0'", 1, 106], "1'": ["1'", 1, 106], Sym('C'+0): [None, 1, 110]}, direction=-1)
109 State(step=49, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 113]}, direction=None)
110 State(step=49, acc=1, transitions={Sym('B'+0): [Sym('B'+0), 1, 114]}, direction=None)
113 State(step=50, acc=0, transitions={'0': ['0', 0, 113], '1': ['1', 0, 113], "0'": ['0', 0, 113], "1'": ['1', 0, 113], Sym('B'+1): [Sym('B'+1), 0, 117]}, direction=1)
114 State(step=50, acc=1, transitions={'0': ['0', 1, 114], '1': ['1', 1, 114], "0'": ['0', 1, 114], "1'": ['1', 1, 114], Sym('B'+1): [Sym('B'+1), 1, 118]}, direction=1)
117 State(step=51, acc=0, transitions={Sym('C'+0): [Sym('C'+0), 0, 121]}, direction=None)
118 State(step=51, acc=1, transitions={Sym('C'+0): [Sym('C'+0), 1, 122]}, direction=None)
121 State(step=52, acc=0, transitions={'0': ['0', 0, 121], '1': ['1', 0, 121], "0'": ['0', 0, 121], "1'": ['1', 0, 121], Sym('C'+1): [Sym('C'+1), 0, 77]}, direction=1)
122 State(step=52, acc=1, transitions={'0': ['0', 1, 122], '1': ['1', 1, 122], "0'": ['0', 1, 122], "1'": ['1', 1, 122], Sym('C'+1): [Sym('C'+1), 1, 78]}, direction=1)
125 State(step=53, acc=0, transitions={Sym('C'+0): [Sym('C'+0), 0, 129]}, direction=None)
126 State(step=53, acc=1, transitions={Sym('C'+0): [Sym('C'+0), 1, 130]}, direction=None)
129 State(step=54, acc=0, transitions={'0': ["0'", 0, 133], '1': ["1'", 1, 134], "0'": ["0'", 0, 129], "1'": ["1'", 0, 129], Sym('C'+1): [None, 0, 149]}, direction=1)
130 State(step=54, acc=1, transitions={'0': ["0'", 1, 134], '1': ["1'", 1, 134], "0'": ["0'", 1, 130], "1'": ["1'", 1, 130], Sym('C'+1): [None, 1, 149]}, direction=1)
133 State(step=55, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 137]}, direction=None)
134 State(step=55, acc=1, transitions={Sym('B'+0): [Sym('B'+0), 1, 138]}, direction=None)
137 State(step=56, acc=0, transitions={'0': ["0'", 0, 125], '1': ["1'", 1, 126], "0'": ["0'", 0, 137], "1'": ["1'", 0, 137], Sym('B'+1): [None, 0, 149]}, direction=1)
138 State(step=56, acc=1, transitions={'0': ["0'", 1, 126], '1': ["0'", 0, 125], "0'": ["0'", 1, 138], "1'": ["1'", 1, 138], Sym('B'+1): [None, 1, 149]}, direction=1)
149 State(step=59, acc=0, transitions={Sym('C'+0): [Sym('C'+0), 0, 153]}, direction=None)
153 State(step=60, acc=0, transitions={'0': ['0', 0, 153], '1': ['1', 0, 153], "0'": ['0', 0, 153], "1'": ['1', 0, 153], Sym('C'+1): [Sym('C'+1), 0, 157]}, direction=1)
157 State(step=61, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 161]}, direction=None)
161 State(step=62, acc=0, transitions={'0': ['0', 0, 161], '1': ['1', 0, 161], "0'": ['0', 0, 161], "1'": ['1', 0, 161], Sym('B'+1): [Sym('B'+1), 0, 71]}, direction=1)
>>> len(used_states)
41
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#421>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 593, in compile_function
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 304, in evaluate_function_call
    new_function = functioncall2instruction(line.apply(index,argsdict))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 65, in apply
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 65, in <listcomp>
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> len(quasis)
51
>>> quasis[-1]
End(is_start=False, next_quasis=[24])
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[14])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3])
3 None
4 None
5 None
6 None
7 None
8 None
9 None
10 None
11 None
12 None
13 None
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[28])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[19])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[38, 17, 38, 38])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[24])
24 Instruction(JUMP, next_quasis=[17])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[3])
28 End(is_start=True, next_quasis=[30])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[40])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[24])
>>> for function in functions:
	print(function)

	
FunctionHeader(command='ADD', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='SUB', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}], next_quasis=[4]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}], next_quasis=[6]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='BOL', params=['vard', 'var0', 'var1', 'map'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'ACC'], next_quasis=[3, 7]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[4, 7]), FunctionCall(command='MAP', args=['map'], next_quasis=[5]), FunctionCall(command='STORENEXT', args=['vard', 'ACC'], next_quasis=[7, 7]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[8]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[9]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[10]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='ADDs', params=['vard', 'var0'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4]), FunctionCall(command='LOAD', args=['vard', 'TEMP'], next_quasis=[5, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[12]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='SUBs', params=['vard', 'var0'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}], next_quasis=[4]), FunctionCall(command='LOAD', args=['vard', 'TEMP'], next_quasis=[5, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}], next_quasis=[6]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[12]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='BOLs', params=['vard', 'var0', 'map'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'ACC'], next_quasis=[3, 7]), FunctionCall(command='LOAD', args=['vard', 'TEMP'], next_quasis=[4, 7]), FunctionCall(command='MAP', args=['map'], next_quasis=[5]), FunctionCall(command='STORENEXT', args=['vard', 'ACC'], next_quasis=[7, 7]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[8]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[9]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='SLL', params=['vard', 'var0', 'imm'], lines=[End(is_start=True, next_quasis=[1]), FunctionCall(command='LOADNEXTBIG', args=['var0', 'TEMP'], next_quasis=[3, 7]), Label(name='start'), FunctionCall(command='LOADNEXTBIG', args=['var0', 'ACC'], next_quasis=[4, 7]), FunctionCall(command='STORENEXTBIG', args=['vard', 'ACC'], next_quasis=[5, 7]), FunctionCall(command='JUMP', args=['start'], next_quasis=[3]), Label(name='oob'), FunctionCall(command='LOADI', args=['imm', 'TEMP'], next_quasis=[8]), FunctionCall(command='STORENEXTBIG', args=['vard', 'TEMP'], next_quasis=[9, None]), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[10]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[11]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='SRL', params=['vard', 'var0', 'imm'], lines=[End(is_start=True, next_quasis=[1]), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 7]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'ACC'], next_quasis=[4, 7]), FunctionCall(command='STORENEXT', args=['vard', 'ACC'], next_quasis=[5, 7]), FunctionCall(command='JUMP', args=['start'], next_quasis=[3]), Label(name='oob'), FunctionCall(command='LOADI', args=['imm', 'TEMP'], next_quasis=[8]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[9, None]), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[10]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[11]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='SLT', params=['var0', 'var1'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXTBIG', args=['var0', 'ACC'], next_quasis=[3, 7]), FunctionCall(command='LOADNEXTBIG', args=['var1', 'TEMP'], next_quasis=[4, 7]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}], next_quasis=[5]), FunctionCall(command='BRANCH', args=['start', 'oob', 'null', 'oob'], next_quasis=[2, 7, 7, 7]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[8]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[9]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='MULT', params=['vard', 'var0', 'var1'], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'ACC'], next_quasis=[3, 10]), FunctionCall(command='BRANCH', args=['shift', 'add', 'null', 'null'], next_quasis=[7, 5, 5, 5]), Label(name='add'), FunctionCall(command='ADDs', args=['vard', 'var1'], next_quasis=[7]), Label(name='shift'), FunctionCall(command='SLLs', args=['var1', 0], next_quasis=[8]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='RECP', params=['vard', 'varr', 'var0'], lines=[End(is_start=True, next_quasis=[1]), FunctionCall(command='ZEROs', args=['varr', 0], next_quasis=[3]), Label(name='start'), FunctionCall(command='SLLs', args=['varr', 1], next_quasis=[4]), FunctionCall(command='SLT', args=['varr', 'var0'], next_quasis=[5]), FunctionCall(command='MAP', args=[{(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}], next_quasis=[6]), FunctionCall(command='STORENEXTBIG', args=['vard', 'TEMP'], next_quasis=[7, 12]), FunctionCall(command='BRANCH', args=['sub', 'start', 'null', 'null'], next_quasis=[9, 3, 9, 9]), Label(name='sub'), FunctionCall(command='SUBs', args=['varr', 'var0'], next_quasis=[10]), FunctionCall(command='JUMP', args=['start'], next_quasis=[3]), Label(name='oob'), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13]), End(is_start=False, next_quasis=[])])
FunctionHeader(command='PI', params=[], lines=[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3]), FunctionCall(command='LOAD', args=['S', 'ACC'], next_quasis=[4, None]), FunctionCall(command='BRANCH', args=['add', 'null', 'null', 'null'], next_quasis=[7, 5, 5, 5]), FunctionCall(command='COMPs', args=['V'], next_quasis=[7]), Label(name='add'), FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[8]), FunctionCall(command='ADDIs', args=['N', 2], next_quasis=[9]), FunctionCall(command='BRANCH', args=['null', 'end', 'null', 'null'], next_quasis=[10, 13, 10, 10]), FunctionCall(command='NOTs', args=['S'], next_quasis=[11]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='end'), End(is_start=False, next_quasis=[])])
>>> for function in functions:
	print(function.next_quasis)

	
Traceback (most recent call last):
  File "<pyshell#431>", line 2, in <module>
    print(function.next_quasis)
AttributeError: 'FunctionHeader' object has no attribute 'next_quasis'
>>> function = LineParser.line.parse('PI').value
>>> function
FunctionCall(command='PI', args=[], next_quasis=None)
>>> function = LineParser.line.parse('RECP A B C').value
>>> function
FunctionCall(command='RECP', args=['A', 'B', 'C'], next_quasis=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#436>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 593, in compile_function
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 304, in evaluate_function_call
    new_function = functioncall2instruction(line.apply(index,argsdict))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 65, in apply
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 65, in <listcomp>
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3])
FunctionCall(command='ZEROs', args=['varr', 0], next_quasis=[3])
FunctionCall(command='SLLs', args=['varr', 1], next_quasis=[4])
FunctionCall(command='SLT', args=['varr', 'var0'], next_quasis=[5])
FunctionCall(command='LOADNEXTBIG', args=['var0', 'ACC'], next_quasis=[3, 7])
FunctionCall(command='LOADNEXTBIG', args=['var1', 'TEMP'], next_quasis=[4, 7])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}], next_quasis=[5])
FunctionCall(command='BRANCH', args=['start', 'oob', 'null', 'oob'], next_quasis=[2, 7, 7, 7])
FunctionCall(command='UNREAD', args=['var0'], next_quasis=[8])
FunctionCall(command='UNREAD', args=['var1'], next_quasis=[9])
FunctionCall(command='MAP', args=[{(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}], next_quasis=[6])
FunctionCall(command='STORENEXTBIG', args=['vard', 'TEMP'], next_quasis=[7, 12])
FunctionCall(command='BRANCH', args=['sub', 'start', 'null', 'null'], next_quasis=[9, 3, 9, 9])
FunctionCall(command='SUBs', args=['varr', 'var0'], next_quasis=[10])
FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}], next_quasis=[4])
FunctionCall(command='LOAD', args=['vard', 'TEMP'], next_quasis=[5, 10])
FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}], next_quasis=[6])
FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7])
FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10])
FunctionCall(command='JUMP', args=['start'], next_quasis=[2])
FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11])
FunctionCall(command='UNREAD', args=['vard'], next_quasis=[12])
FunctionCall(command='JUMP', args=['start'], next_quasis=[3])
FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13])
FunctionCall(command='LOAD', args=['S', 'ACC'], next_quasis=[4, None])
Traceback (most recent call last):
  File "<pyshell#437>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 594, in compile_function
    evaluate_function_call(function)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 305, in evaluate_function_call
    new_function = functioncall2instruction(line.apply(index,argsdict))
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 65, in apply
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 65, in <listcomp>
    next_quasis=[index+next_quasi for next_quasi in self.next_quasis])
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
0 End(is_start=True, next_quasis=[14])
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[64])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[138])
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [Sym('V'+1), 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [None, 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [None, 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 2]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [None, 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [None, 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [None, 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [None, 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [None, 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [None, 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [None, 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [Sym('V'+1), 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [Sym('V'+1), 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> len(used_states)
68
>>> quasis[71]
Step(instruction=10, is_found=True, variable='S', next_quasis=[11], direction=None)
>>> quasis[10]
<__main__.Instruction object at 0x037A2B10>
>>> print(quasis[10])
Instruction(NOTs, vard=S, next_quasis=[11])
>>> print(quasis[11])
Instruction(JUMP, next_quasis=[2])
>>> print(quasis[2])
FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[64])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#445>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 595, in compile_function
    evaluate_function_call(function)
TypeError: evaluate_function_call() missing 1 required positional argument: 'j'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
2 14
18 28
23 38
7 51
0 End(is_start=True, next_quasis=[14])
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[64])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[138])
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [Sym('V'+1), 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [Sym('N'+1), 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [Sym('N'+1), 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 2]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [None, 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [None, 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [None, 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [Sym('N'+1), 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [Sym('N'+1), 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [None, 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [None, 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [Sym('V'+1), 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
[End(is_start=True, next_quasis=[2]), None, FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3]), None, None, None, None, None, None, None, None, None, None, None] 2 14
[End(is_start=True, next_quasis=[14]), None, FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3]), None, None, None, None, None, None, None, None, None, None, None, End(is_start=True, next_quasis=[15]), <__main__.Instruction object at 0x03612430>, None, <__main__.Instruction object at 0x03612470>, FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[19]), None, None, None, None, None, None, None, None, None] 18 28
[End(is_start=True, next_quasis=[14]), None, FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3]), None, None, None, None, None, None, None, None, None, None, None, End(is_start=True, next_quasis=[15]), <__main__.Instruction object at 0x03612430>, None, <__main__.Instruction object at 0x03612470>, FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[19]), <__main__.Instruction object at 0x036126B0>, <__main__.Instruction object at 0x03612530>, <__main__.Instruction object at 0x03612730>, None, FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[24]), None, None, None, None, End(is_start=True, next_quasis=[30]), None, <__main__.Instruction object at 0x036124D0>, <__main__.Instruction object at 0x03612510>, <__main__.Instruction object at 0x036125D0>, <__main__.Instruction object at 0x03612610>, None, <__main__.Instruction object at 0x03612650>, <__main__.Instruction object at 0x03612690>, End(is_start=False, next_quasis=[19])] 23 38
[End(is_start=True, next_quasis=[14]), None, FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3]), <__main__.Instruction object at 0x035FE470>, <__main__.Instruction object at 0x03612AD0>, <__main__.Instruction object at 0x03612B10>, None, FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[8]), None, None, None, None, None, None, End(is_start=True, next_quasis=[15]), <__main__.Instruction object at 0x03612430>, None, <__main__.Instruction object at 0x03612470>, FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[19]), <__main__.Instruction object at 0x036126B0>, <__main__.Instruction object at 0x03612530>, <__main__.Instruction object at 0x03612730>, None, FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[24]), <__main__.Instruction object at 0x03612A30>, None, <__main__.Instruction object at 0x03612A70>, End(is_start=False, next_quasis=[3]), End(is_start=True, next_quasis=[30]), None, <__main__.Instruction object at 0x036124D0>, <__main__.Instruction object at 0x03612510>, <__main__.Instruction object at 0x036125D0>, <__main__.Instruction object at 0x03612610>, None, <__main__.Instruction object at 0x03612650>, <__main__.Instruction object at 0x03612690>, End(is_start=False, next_quasis=[19]), End(is_start=True, next_quasis=[40]), None, <__main__.Instruction object at 0x036127D0>, <__main__.Instruction object at 0x03612850>, <__main__.Instruction object at 0x03612870>, <__main__.Instruction object at 0x036128D0>, <__main__.Instruction object at 0x03612910>, <__main__.Instruction object at 0x036128F0>, <__main__.Instruction object at 0x03612990>, None, <__main__.Instruction object at 0x036129D0>, <__main__.Instruction object at 0x03612A10>, End(is_start=False, next_quasis=[24])] 7 51
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 608, in compile_function
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 585, in merge_links
    if equal_states(k,j):
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 152, in equal_states
    transition1 = get_none_transition(state1,symbol,k)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 137, in get_none_transition
    def get_none_transition(state,symbol,k):
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
0 End(is_start=True, next_quasis=[14])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[138])
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [None, 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [None, 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [None, 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 108]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [Sym('V'+0), 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [None, 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [None, 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [None, 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [None, 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [Sym('varr'+1), 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [Sym('varr'+1), 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [None, 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [None, 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [None, 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [None, 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> len(used_states)
67
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
0 End(is_start=True, next_quasis=[14])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[138])
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [None, 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [None, 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [None, 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 108]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [None, 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [None, 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [None, 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [None, 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [Sym('varr'+1), 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [Sym('varr'+1), 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [None, 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
18 28
23 38
2 14
7 51
3 64
5 66
8 68
10 70
15 72
17 74
20 76
26 78
30 80
31 82
35 84
36 86
40 88
42 90
45 92
48 94
49 96
53 98
55 100
58 102
61 104
62 106
19 76
44 92
57 102
19 0
44 0
57 0
117 116
113 112
109 108
118 116
114 112
110 108
119 116
115 112
111 108
123 122
124 122
125 122
135 134
131 130
136 134
132 130
137 134
133 130
147 146
143 142
139 138
148 146
144 142
140 138
149 146
145 142
141 138
165 164
161 160
166 164
162 160
167 164
163 160
159 156
155 152
199 196
195 192
191 188
187 184
175 172
171 168
222 214
218 210
237 236
233 232
229 228
225 224
238 236
234 232
230 228
226 224
239 236
235 232
231 228
227 224
263 255
259 251
277 276
273 272
269 268
265 264
278 276
274 272
270 268
266 264
279 276
275 272
271 268
267 264
0 End(is_start=True, next_quasis=[14])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[138])
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [None, 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [Sym('N'+1), 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [None, 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 108]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [Sym('V'+0), 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [Sym('N'+0), 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [Sym('N'+1), 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [Sym('N'+1), 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [None, 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [None, 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [None, 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> quasis[14]
End(is_start=True, next_quasis=[138])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
18 28
23 38
2 14
7 51
3 64
5 66
8 68
10 70
15 72
17 74
20 76
26 78
30 80
31 82
35 84
36 86
40 88
42 90
45 92
48 94
49 96
53 98
55 100
58 102
61 104
62 106
19 76
44 92
57 102
19 0
44 0
57 0
117 116
113 112
109 108
118 116
114 112
110 108
119 116
115 112
111 108
123 122
124 122
125 122
135 134
131 130
136 134
132 130
137 134
133 130
147 146
143 142
139 138
148 146
144 142
140 138
149 146
145 142
141 138
165 164
161 160
166 164
162 160
167 164
163 160
159 156
155 152
199 196
195 192
191 188
187 184
175 172
171 168
222 214
218 210
237 236
233 232
229 228
225 224
238 236
234 232
230 228
226 224
239 236
235 232
231 228
227 224
263 255
259 251
277 276
273 272
269 268
265 264
278 276
274 272
270 268
266 264
279 276
275 272
271 268
267 264
0 End(is_start=True, next_quasis=[14])
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[64])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[138])
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [Sym('V'+1), 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [Sym('N'+1), 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [None, 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 2]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [Sym('varr'+1), 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [Sym('V'+0), 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [Sym('N'+0), 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [Sym('N'+1), 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [Sym('N'+1), 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [Sym('varr'+1), 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [Sym('varr'+1), 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [Sym('V'+1), 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> functions[0].lines
[End(is_start=True, next_quasis=[2]), Label(name='start'), FunctionCall(command='LOADNEXT', args=['var0', 'TEMP'], next_quasis=[3, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}], next_quasis=[4]), FunctionCall(command='LOADNEXT', args=['var1', 'TEMP'], next_quasis=[5, 10]), FunctionCall(command='MAP', args=[{(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}], next_quasis=[6]), FunctionCall(command='MAP', args=[{(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}], next_quasis=[7]), FunctionCall(command='STORENEXT', args=['vard', 'TEMP'], next_quasis=[8, 10]), FunctionCall(command='JUMP', args=['start'], next_quasis=[2]), Label(name='oob'), FunctionCall(command='UNREAD', args=['var0'], next_quasis=[11]), FunctionCall(command='UNREAD', args=['var1'], next_quasis=[12]), FunctionCall(command='UNREAD', args=['vard'], next_quasis=[13]), End(is_start=False, next_quasis=[])]
>>> functions[0].command
'ADD'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> len(quasis)
0
>>> len(functions)
12
>>> function = LineParser.line.parse('PI').value
>>> function
FunctionCall(command='PI', args=[], next_quasis=None)
>>> quasis
[]
>>> evaluate_function_call(function)
18 28
23 38
2 14
7 51
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[14])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[51, 5, 5, 5])
5 Instruction(COMPs, vard=V, next_quasis=[51])
6 None
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[8])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[10, 13, 10, 10])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[2])
12 None
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[28])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[19])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[38, 17, 38, 38])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[24])
24 Instruction(JUMP, next_quasis=[17])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[3])
28 End(is_start=True, next_quasis=[30])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[40])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[24])
51 End(is_start=True, next_quasis=[53])
52 None
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
60 None
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[63])
63 End(is_start=False, next_quasis=[8])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('PI').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[2])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[3])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[7, 5, 5, 5])
5 Instruction(COMPs, vard=V, next_quasis=[7])
6 None
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[8])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[10, 13, 10, 10])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[2])
12 None
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[18])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[19])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[23, 17, 23, 23])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[24])
24 Instruction(JUMP, next_quasis=[17])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[3])
28 End(is_start=True, next_quasis=[30])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[40])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[24])
51 End(is_start=True, next_quasis=[53])
52 None
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
60 None
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[63])
63 End(is_start=False, next_quasis=[8])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('PI').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[2])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[14])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[7, 5, 5, 5])
5 Instruction(COMPs, vard=V, next_quasis=[7])
6 None
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[51])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[10, 13, 10, 10])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[2])
12 None
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[18])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[28])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[23, 17, 23, 23])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[38])
24 Instruction(JUMP, next_quasis=[17])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[14])
28 End(is_start=True, next_quasis=[30])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[28])
38 End(is_start=True, next_quasis=[40])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[38])
51 End(is_start=True, next_quasis=[53])
52 None
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
60 None
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[63])
63 End(is_start=False, next_quasis=[51])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
3 64
5 66
8 68
10 70
15 72
17 74
20 76
26 78
30 80
31 82
35 84
36 86
40 88
42 90
45 92
48 94
49 96
53 98
55 100
58 102
61 104
62 106
19 76
44 92
57 102
19 0
44 0
57 0
117 116
113 112
109 108
118 116
114 112
110 108
119 116
115 112
111 108
123 122
124 122
125 122
147 146
143 142
139 138
135 134
131 130
148 146
144 142
140 138
136 134
132 130
149 146
145 142
141 138
137 134
133 130
165 164
161 160
166 164
162 160
167 164
163 160
159 156
155 152
222 214
218 210
263 255
259 251
0 End(is_start=True, next_quasis=[2])
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[14])
>>> len(quasis)
280
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('PI').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[2])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[14])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[7, 5, 5, 5])
5 Instruction(COMPs, vard=V, next_quasis=[7])
6 None
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[51])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[10, 13, 10, 10])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[2])
12 None
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[18])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[28])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[23, 17, 23, 23])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[38])
24 Instruction(JUMP, next_quasis=[17])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[14])
28 End(is_start=True, next_quasis=[30])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[28])
38 End(is_start=True, next_quasis=[40])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[38])
51 End(is_start=True, next_quasis=[53])
52 None
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
60 None
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[63])
63 End(is_start=False, next_quasis=[51])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('PI').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[2])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[51])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[7, 5, 5, 5])
5 Instruction(COMPs, vard=V, next_quasis=[7])
6 None
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[64])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[10, 13, 10, 10])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[2])
12 None
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[18])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[38])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[23, 17, 23, 23])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[51])
24 Instruction(JUMP, next_quasis=[17])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[3])
28 End(is_start=True, next_quasis=[30])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[40])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[24])
51 End(is_start=True, next_quasis=[53])
52 None
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
60 None
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[63])
63 End(is_start=False, next_quasis=[8])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('PI').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	if quasi:
		print(k,quasi)

		
0 End(is_start=True, next_quasis=[2])
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[14])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[7, 5, 5, 5])
5 Instruction(COMPs, vard=V, next_quasis=[7])
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[51])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[10, 13, 10, 10])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[2])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[18])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[28])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[23, 17, 23, 23])
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[38])
24 Instruction(JUMP, next_quasis=[17])
26 Instruction(UNREAD, vard=V, next_quasis=[27])
27 End(is_start=False, next_quasis=[3])
28 End(is_start=True, next_quasis=[30])
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[37])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[40])
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[50])
50 End(is_start=False, next_quasis=[24])
51 End(is_start=True, next_quasis=[53])
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[63])
63 End(is_start=False, next_quasis=[8])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> function = LineParser.line.parse('PI').value
>>> evaluate_function_call(function)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

        
>>> for k,quasi in enumerate(quasis):
	if quasi:
		print(k,quasi)

		
0 End(is_start=True, next_quasis=[15])
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[15])
3 Instruction(LOAD, vard=S, next_quasis=[4, 5])
4 Instruction(BRANCH, next_quasis=[53])
5 Instruction(COMPs, vard=V, next_quasis=[53])
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[53])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=None)
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[15])
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[15])
15 Instruction(ZEROs, vard=varr, next_quasis=[17])
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[30])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[30])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[20])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 26])
21 Instruction(BRANCH, next_quasis=[40])
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[40])
24 Instruction(JUMP, next_quasis=[17])
26 Instruction(UNREAD, vard=V, next_quasis=[3])
27 End(is_start=False, next_quasis=[3])
28 End(is_start=True, next_quasis=[30])
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[31, 35])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 35])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[30, 35, 35, 35])
35 Instruction(UNREAD, vard=varr, next_quasis=[36])
36 Instruction(UNREAD, vard=N, next_quasis=[19])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[40])
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 48])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[42])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 48])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[45])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 48])
46 Instruction(JUMP, next_quasis=[40])
48 Instruction(UNREAD, vard=N, next_quasis=[49])
49 Instruction(UNREAD, vard=varr, next_quasis=[24])
50 End(is_start=False, next_quasis=[24])
51 End(is_start=True, next_quasis=[53])
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 61])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[55])
55 Instruction(LOAD, vard=P, next_quasis=[56, 61])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[58])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 61])
59 Instruction(JUMP, next_quasis=[53])
61 Instruction(UNREAD, vard=V, next_quasis=[62])
62 Instruction(UNREAD, vard=P, next_quasis=[8])
63 End(is_start=False, next_quasis=[8])
>>> used_states = {0}
>>> def find_successors(k):
	global quasis,used_states
	if type(quasis[k])!=Instruction and quasis[k].next_quasis:
		for j in quasis[k].next_quasis:
			if not j in used_states:
				used_states.add(j)
				find_successors(j)

				
>>> find_successors(0)
>>> used_states
{0, 15}
>>> def find_successors(k):
	global quasis,used_states
	if type(quasis[k])!=Instruction:
		print(k)
	if quasis[k] and quasis[k].next_quasis:
		for j in quasis[k].next_quasis:
			if not j in used_states:
				used_states.add(j)
				find_successors(j)

				
>>> used_states={0}
>>> find_successors(0)
0
>>> used_states
{0, 3, 4, 5, 8, 9, 15, 17, 19, 20, 21, 24, 26, 30, 31, 32, 33, 35, 36, 40, 41, 42, 43, 44, 45, 46, 48, 49, 53, 54, 55, 56, 57, 58, 59, 61, 62}
>>> instructions2steps()
3 64
5 66
8 68
10 70
15 72
17 74
20 76
26 78
30 80
31 82
35 84
36 86
40 88
42 90
45 92
48 94
49 96
53 98
55 100
58 102
61 104
62 106
>>> steps2states()
>>> len(quasis)
280
>>> more_posts,more_pres = True,True
>>> while (more_posts or more_pres):
        if more_posts:
            more_posts = apply_posts()
        if more_pres:
            more_pres = apply_pres()

            
Traceback (most recent call last):
  File "<pyshell#509>", line 3, in <module>
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 481, in apply_posts
    transition[2] = quasi2.next_quasis[transition[1]]
IndexError: list index out of range
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
3 64
5 66
8 68
10 70
15 72
17 74
20 76
26 78
30 80
31 82
35 84
36 86
40 88
42 90
45 92
48 94
49 96
53 98
55 100
58 102
61 104
62 106
Traceback (most recent call last):
  File "<pyshell#510>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 618, in compile_function
    more_posts = apply_posts()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 481, in apply_posts
    transition[2] = quasi2.next_quasis[transition[1]]
IndexError: list index out of range
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[72])
1 None
2 FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[72])
3 Instruction(LOAD, vard=S, next_quasis=[4, 66])
4 Instruction(BRANCH, next_quasis=[98])
5 Instruction(COMPs, vard=V, next_quasis=[98])
6 None
7 FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[98])
8 Instruction(ADDIs, vard=N, imm=2, next_quasis=[9])
9 Instruction(BRANCH, next_quasis=[70, 13, 70, 70])
10 Instruction(NOTs, vard=S, next_quasis=[11])
11 Instruction(JUMP, next_quasis=[72])
12 None
13 End(is_start=False, next_quasis=None)
14 End(is_start=True, next_quasis=[72])
15 Instruction(ZEROs, vard=varr, next_quasis=[74])
16 None
17 Instruction(SLLs, vard=varr, imm=1, next_quasis=[80])
18 FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[80])
19 Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[76])
20 Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 78])
21 Instruction(BRANCH, next_quasis=[88])
22 None
23 FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[88])
24 Instruction(JUMP, next_quasis=[74])
25 None
26 Instruction(UNREAD, vard=V, next_quasis=[64])
27 End(is_start=False, next_quasis=[64])
28 End(is_start=True, next_quasis=[80])
29 None
30 Instruction(LOADNEXTBIG, vard=varr, next_quasis=[82, 84])
31 Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 84])
32 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33])
33 Instruction(BRANCH, next_quasis=[80, 84, 84, 84])
34 None
35 Instruction(UNREAD, vard=varr, next_quasis=[86])
36 Instruction(UNREAD, vard=N, next_quasis=[19])
37 End(is_start=False, next_quasis=[19])
38 End(is_start=True, next_quasis=[88])
39 None
40 Instruction(LOADNEXT, vard=N, next_quasis=[41, 94])
41 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (3, 0): (3,), (3, 1): (0,)}, next_quasis=[90])
42 Instruction(LOAD, vard=varr, next_quasis=[43, 94])
43 Instruction(MAP, map={(0, 0): (0,), (0, 1): (3,), (1, 0): (1,), (1, 1): (0,), (3, 0): (3,), (3, 1): (2,)}, next_quasis=[44])
44 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[92])
45 Instruction(STORENEXT, vard=varr, next_quasis=[46, 94])
46 Instruction(JUMP, next_quasis=[88])
47 None
48 Instruction(UNREAD, vard=N, next_quasis=[96])
49 Instruction(UNREAD, vard=varr, next_quasis=[24])
50 End(is_start=False, next_quasis=[24])
51 End(is_start=True, next_quasis=[98])
52 None
53 Instruction(LOADNEXT, vard=V, next_quasis=[54, 104])
54 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[100])
55 Instruction(LOAD, vard=P, next_quasis=[56, 104])
56 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[57])
57 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[102])
58 Instruction(STORENEXT, vard=P, next_quasis=[59, 104])
59 Instruction(JUMP, next_quasis=[98])
60 None
61 Instruction(UNREAD, vard=V, next_quasis=[106])
62 Instruction(UNREAD, vard=P, next_quasis=[68])
63 End(is_start=False, next_quasis=[68])
64 Step(instruction=3, is_found=False, variable='S', next_quasis=[65], direction=None)
65 Step(instruction=3, is_found=True, variable='S', next_quasis=[4, 66], direction=None)
66 Step(instruction=5, is_found=False, variable='V', next_quasis=[67], direction=None)
67 Step(instruction=5, is_found=True, variable='V', next_quasis=[98], direction=None)
68 Step(instruction=8, is_found=False, variable='N', next_quasis=[69], direction=None)
69 Step(instruction=8, is_found=True, variable='N', next_quasis=[9], direction=None)
70 Step(instruction=10, is_found=False, variable='S', next_quasis=[71], direction=None)
71 Step(instruction=10, is_found=True, variable='S', next_quasis=[11], direction=None)
72 Step(instruction=15, is_found=False, variable='varr', next_quasis=[73], direction=None)
73 Step(instruction=15, is_found=True, variable='varr', next_quasis=[74], direction=None)
74 Step(instruction=17, is_found=False, variable='varr', next_quasis=[75], direction=None)
75 Step(instruction=17, is_found=True, variable='varr', next_quasis=[80], direction=None)
76 Step(instruction=20, is_found=False, variable='V', next_quasis=[77], direction=None)
77 Step(instruction=20, is_found=True, variable='V', next_quasis=[21, 78], direction=None)
78 Step(instruction=26, is_found=False, variable='V', next_quasis=[79], direction=None)
79 Step(instruction=26, is_found=True, variable='V', next_quasis=[64], direction=None)
80 Step(instruction=30, is_found=False, variable='varr', next_quasis=[81], direction=None)
81 Step(instruction=30, is_found=True, variable='varr', next_quasis=[82, 84], direction=None)
82 Step(instruction=31, is_found=False, variable='N', next_quasis=[83], direction=None)
83 Step(instruction=31, is_found=True, variable='N', next_quasis=[32, 84], direction=None)
84 Step(instruction=35, is_found=False, variable='varr', next_quasis=[85], direction=None)
85 Step(instruction=35, is_found=True, variable='varr', next_quasis=[86], direction=None)
86 Step(instruction=36, is_found=False, variable='N', next_quasis=[87], direction=None)
87 Step(instruction=36, is_found=True, variable='N', next_quasis=[19], direction=None)
88 Step(instruction=40, is_found=False, variable='N', next_quasis=[89], direction=None)
89 Step(instruction=40, is_found=True, variable='N', next_quasis=[41, 94], direction=None)
90 Step(instruction=42, is_found=False, variable='varr', next_quasis=[91], direction=None)
91 Step(instruction=42, is_found=True, variable='varr', next_quasis=[43, 94], direction=None)
92 Step(instruction=45, is_found=False, variable='varr', next_quasis=[93], direction=None)
93 Step(instruction=45, is_found=True, variable='varr', next_quasis=[46, 94], direction=None)
94 Step(instruction=48, is_found=False, variable='N', next_quasis=[95], direction=None)
95 Step(instruction=48, is_found=True, variable='N', next_quasis=[96], direction=None)
96 Step(instruction=49, is_found=False, variable='varr', next_quasis=[97], direction=None)
97 Step(instruction=49, is_found=True, variable='varr', next_quasis=[24], direction=None)
98 Step(instruction=53, is_found=False, variable='V', next_quasis=[99], direction=None)
99 Step(instruction=53, is_found=True, variable='V', next_quasis=[54, 104], direction=None)
100 Step(instruction=55, is_found=False, variable='P', next_quasis=[101], direction=None)
101 Step(instruction=55, is_found=True, variable='P', next_quasis=[56, 104], direction=None)
102 Step(instruction=58, is_found=False, variable='P', next_quasis=[103], direction=None)
103 Step(instruction=58, is_found=True, variable='P', next_quasis=[59, 104], direction=None)
104 Step(instruction=61, is_found=False, variable='V', next_quasis=[105], direction=None)
105 Step(instruction=61, is_found=True, variable='V', next_quasis=[106], direction=None)
106 Step(instruction=62, is_found=False, variable='P', next_quasis=[107], direction=None)
107 Step(instruction=62, is_found=True, variable='P', next_quasis=[68], direction=None)
108 State(step=64, acc=0, transitions={Sym('S'+0): [None, 0, 65]}, direction=None)
109 State(step=64, acc=1, transitions={Sym('S'+0): [None, 1, 65]}, direction=None)
110 State(step=64, acc=2, transitions={Sym('S'+0): [None, 2, 65]}, direction=None)
111 State(step=64, acc=3, transitions={Sym('S'+0): [None, 3, 65]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 98], '1': ['1', 1, 4], "0'": ["0'", 0, 65], "1'": ["1'", 0, 65], Sym('S'+1): [None, 0, 66]}, direction=1)
113 State(step=65, acc=1, transitions={'0': ['0', 0, 4], '1': ['1', 1, 4], "0'": ["0'", 1, 65], "1'": ["1'", 1, 65], Sym('S'+1): [None, 1, 66]}, direction=1)
114 State(step=65, acc=2, transitions={'0': ['0', 0, 4], '1': ['1', 1, 4], "0'": ["0'", 2, 65], "1'": ["1'", 2, 65], Sym('S'+1): [None, 2, 66]}, direction=1)
115 State(step=65, acc=3, transitions={'0': ['0', 0, 4], '1': ['1', 1, 4], "0'": ["0'", 3, 65], "1'": ["1'", 3, 65], Sym('S'+1): [None, 3, 66]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [None, 1, 67]}, direction=None)
117 State(step=66, acc=1, transitions={Sym('V'+0): [None, 1, 67]}, direction=None)
118 State(step=66, acc=2, transitions={Sym('V'+0): [None, 1, 67]}, direction=None)
119 State(step=66, acc=3, transitions={Sym('V'+0): [None, 1, 67]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 67], '1': ['0', 0, 67], "0'": ['1', 0, 67], "1'": ['0', 0, 67], Sym('V'+1): [None, 0, 98]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 67], '1': ['1', 0, 67], "0'": ['0', 1, 67], "1'": ['1', 0, 67], Sym('V'+1): [None, 1, 98]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [None, 2, 69]}, direction=None)
123 State(step=68, acc=1, transitions={Sym('N'+0): [None, 2, 69]}, direction=None)
124 State(step=68, acc=2, transitions={Sym('N'+0): [None, 2, 69]}, direction=None)
125 State(step=68, acc=3, transitions={Sym('N'+0): [None, 2, 69]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 69], '1': ['1', 0, 69], "0'": ['0', 0, 69], "1'": ['1', 0, 69], Sym('N'+1): [None, 0, 9]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 69], '1': ['0', 1, 69], "0'": ['1', 0, 69], "1'": ['0', 1, 69], Sym('N'+1): [None, 1, 9]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 69], '1': ['1', 1, 69], "0'": ['0', 1, 69], "1'": ['1', 1, 69], Sym('N'+1): [None, 2, 9]}, direction=1)
129 State(step=69, acc=3, transitions={'0': ['1', 1, 69], '1': ['0', 2, 69], "0'": ['1', 1, 69], "1'": ['0', 2, 69], Sym('N'+1): [None, 3, 9]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [None, 0, 71]}, direction=None)
131 State(step=70, acc=1, transitions={Sym('S'+0): [None, 1, 71]}, direction=None)
132 State(step=70, acc=2, transitions={Sym('S'+0): [None, 2, 71]}, direction=None)
133 State(step=70, acc=3, transitions={Sym('S'+0): [None, 3, 71]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 71], '1': ['0', 0, 71], "0'": ['1', 0, 71], "1'": ['0', 0, 71], Sym('S'+1): [None, 0, 11]}, direction=1)
135 State(step=71, acc=1, transitions={'0': ['1', 1, 71], '1': ['0', 1, 71], "0'": ['1', 1, 71], "1'": ['0', 1, 71], Sym('S'+1): [None, 1, 11]}, direction=1)
136 State(step=71, acc=2, transitions={'0': ['1', 2, 71], '1': ['0', 2, 71], "0'": ['1', 2, 71], "1'": ['0', 2, 71], Sym('S'+1): [None, 2, 11]}, direction=1)
137 State(step=71, acc=3, transitions={'0': ['1', 3, 71], '1': ['0', 3, 71], "0'": ['1', 3, 71], "1'": ['0', 3, 71], Sym('S'+1): [None, 3, 11]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [None, 0, 73]}, direction=None)
139 State(step=72, acc=1, transitions={Sym('varr'+0): [None, 1, 73]}, direction=None)
140 State(step=72, acc=2, transitions={Sym('varr'+0): [None, 2, 73]}, direction=None)
141 State(step=72, acc=3, transitions={Sym('varr'+0): [None, 3, 73]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 73], '1': ['0', 0, 73], "0'": ['0', 0, 73], "1'": ['0', 0, 73], Sym('varr'+1): [None, 0, 74]}, direction=1)
143 State(step=73, acc=1, transitions={'0': ['0', 1, 73], '1': ['0', 1, 73], "0'": ['0', 1, 73], "1'": ['0', 1, 73], Sym('varr'+1): [None, 1, 74]}, direction=1)
144 State(step=73, acc=2, transitions={'0': ['0', 2, 73], '1': ['0', 2, 73], "0'": ['0', 2, 73], "1'": ['0', 2, 73], Sym('varr'+1): [None, 2, 74]}, direction=1)
145 State(step=73, acc=3, transitions={'0': ['0', 3, 73], '1': ['0', 3, 73], "0'": ['0', 3, 73], "1'": ['0', 3, 73], Sym('varr'+1): [None, 3, 74]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [None, 1, 75]}, direction=None)
147 State(step=74, acc=1, transitions={Sym('varr'+0): [None, 1, 75]}, direction=None)
148 State(step=74, acc=2, transitions={Sym('varr'+0): [None, 1, 75]}, direction=None)
149 State(step=74, acc=3, transitions={Sym('varr'+0): [None, 1, 75]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 75], '1': ['0', 1, 75], "0'": ['0', 0, 75], "1'": ['0', 1, 75], Sym('varr'+1): [None, 0, 80]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 75], '1': ['1', 1, 75], "0'": ['1', 0, 75], "1'": ['1', 1, 75], Sym('varr'+1): [None, 1, 80]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [None, 0, 77]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [None, 1, 77]}, direction=None)
154 State(step=76, acc=2, transitions={Sym('V'+1): [None, 2, 77]}, direction=None)
155 State(step=76, acc=3, transitions={Sym('V'+1): [None, 3, 77]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 0, 21], '1': ["1'", 0, 21], "0'": ["0'", 0, 77], "1'": ["1'", 0, 77], Sym('V'+0): [None, 0, 78]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["0'", 1, 21], '1': ["1'", 1, 21], "0'": ["0'", 1, 77], "1'": ["1'", 1, 77], Sym('V'+0): [None, 1, 78]}, direction=-1)
158 State(step=77, acc=2, transitions={'0': ["0'", 2, 21], '1': ["1'", 2, 21], "0'": ["0'", 2, 77], "1'": ["1'", 2, 77], Sym('V'+0): [None, 2, 78]}, direction=-1)
159 State(step=77, acc=3, transitions={'0': ["0'", 3, 21], '1': ["1'", 3, 21], "0'": ["0'", 3, 77], "1'": ["1'", 3, 77], Sym('V'+0): [None, 3, 78]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [None, 0, 79]}, direction=None)
161 State(step=78, acc=1, transitions={Sym('V'+0): [None, 1, 79]}, direction=None)
162 State(step=78, acc=2, transitions={Sym('V'+0): [None, 2, 79]}, direction=None)
163 State(step=78, acc=3, transitions={Sym('V'+0): [None, 3, 79]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 79], '1': ['1', 0, 79], "0'": ['0', 0, 79], "1'": ['1', 0, 79], Sym('V'+1): [None, 0, 64]}, direction=1)
165 State(step=79, acc=1, transitions={'0': ['0', 1, 79], '1': ['1', 1, 79], "0'": ['0', 1, 79], "1'": ['1', 1, 79], Sym('V'+1): [None, 1, 64]}, direction=1)
166 State(step=79, acc=2, transitions={'0': ['0', 2, 79], '1': ['1', 2, 79], "0'": ['0', 2, 79], "1'": ['1', 2, 79], Sym('V'+1): [None, 2, 64]}, direction=1)
167 State(step=79, acc=3, transitions={'0': ['0', 3, 79], '1': ['1', 3, 79], "0'": ['0', 3, 79], "1'": ['1', 3, 79], Sym('V'+1): [None, 3, 64]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [None, 0, 81]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [None, 1, 81]}, direction=None)
170 State(step=80, acc=2, transitions={Sym('varr'+1): [None, 2, 81]}, direction=None)
171 State(step=80, acc=3, transitions={Sym('varr'+1): [None, 3, 81]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 82], '1': ["1'", 1, 82], "0'": ["0'", 0, 81], "1'": ["1'", 0, 81], Sym('varr'+0): [None, 0, 84]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 82], '1': ["1'", 1, 82], "0'": ["0'", 1, 81], "1'": ["1'", 1, 81], Sym('varr'+0): [None, 1, 84]}, direction=-1)
174 State(step=81, acc=2, transitions={'0': ["0'", 0, 82], '1': ["1'", 1, 82], "0'": ["0'", 2, 81], "1'": ["1'", 2, 81], Sym('varr'+0): [None, 2, 84]}, direction=-1)
175 State(step=81, acc=3, transitions={'0': ["0'", 0, 82], '1': ["1'", 1, 82], "0'": ["0'", 3, 81], "1'": ["1'", 3, 81], Sym('varr'+0): [None, 3, 84]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [None, 0, 83]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [None, 1, 83]}, direction=None)
178 State(step=82, acc=2, transitions={Sym('N'+1): [None, 2, 83]}, direction=None)
179 State(step=82, acc=3, transitions={Sym('N'+1): [None, 3, 83]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 32], '1': ["1'", 0, 32], "0'": ["0'", 0, 83], "1'": ["1'", 0, 83], Sym('N'+0): [None, 0, 84]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 1, 32], '1': ["1'", 1, 32], "0'": ["0'", 1, 83], "1'": ["1'", 1, 83], Sym('N'+0): [None, 1, 84]}, direction=-1)
182 State(step=83, acc=2, transitions={'0': ["0'", 2, 32], '1': ["1'", 2, 32], "0'": ["0'", 2, 83], "1'": ["1'", 2, 83], Sym('N'+0): [None, 2, 84]}, direction=-1)
183 State(step=83, acc=3, transitions={'0': ["0'", 3, 32], '1': ["1'", 3, 32], "0'": ["0'", 3, 83], "1'": ["1'", 3, 83], Sym('N'+0): [None, 3, 84]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [None, 0, 85]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [None, 1, 85]}, direction=None)
186 State(step=84, acc=2, transitions={Sym('varr'+0): [None, 2, 85]}, direction=None)
187 State(step=84, acc=3, transitions={Sym('varr'+0): [None, 3, 85]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 85], '1': ['1', 0, 85], "0'": ['0', 0, 85], "1'": ['1', 0, 85], Sym('varr'+1): [None, 0, 86]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 85], '1': ['1', 1, 85], "0'": ['0', 1, 85], "1'": ['1', 1, 85], Sym('varr'+1): [None, 1, 86]}, direction=1)
190 State(step=85, acc=2, transitions={'0': ['0', 2, 85], '1': ['1', 2, 85], "0'": ['0', 2, 85], "1'": ['1', 2, 85], Sym('varr'+1): [None, 2, 86]}, direction=1)
191 State(step=85, acc=3, transitions={'0': ['0', 3, 85], '1': ['1', 3, 85], "0'": ['0', 3, 85], "1'": ['1', 3, 85], Sym('varr'+1): [None, 3, 86]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [None, 0, 87]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [None, 1, 87]}, direction=None)
194 State(step=86, acc=2, transitions={Sym('N'+0): [None, 2, 87]}, direction=None)
195 State(step=86, acc=3, transitions={Sym('N'+0): [None, 3, 87]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 87], '1': ['1', 0, 87], "0'": ['0', 0, 87], "1'": ['1', 0, 87], Sym('N'+1): [None, 0, 19]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 87], '1': ['1', 1, 87], "0'": ['0', 1, 87], "1'": ['1', 1, 87], Sym('N'+1): [None, 1, 19]}, direction=1)
198 State(step=87, acc=2, transitions={'0': ['0', 2, 87], '1': ['1', 2, 87], "0'": ['0', 2, 87], "1'": ['1', 2, 87], Sym('N'+1): [None, 2, 19]}, direction=1)
199 State(step=87, acc=3, transitions={'0': ['0', 3, 87], '1': ['1', 3, 87], "0'": ['0', 3, 87], "1'": ['1', 3, 87], Sym('N'+1): [None, 3, 19]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [None, 0, 89]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [None, 1, 89]}, direction=None)
202 State(step=88, acc=2, transitions={Sym('N'+0): [None, 2, 89]}, direction=None)
203 State(step=88, acc=3, transitions={Sym('N'+0): [None, 3, 89]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 41], '1': ["1'", 0, 41], "0'": ["0'", 0, 89], "1'": ["1'", 0, 89], Sym('N'+1): [None, 0, 94]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 41], '1': ["1'", 1, 41], "0'": ["0'", 1, 89], "1'": ["1'", 1, 89], Sym('N'+1): [None, 1, 94]}, direction=1)
206 State(step=89, acc=2, transitions={'0': ["0'", 2, 41], '1': ["1'", 2, 41], "0'": ["0'", 2, 89], "1'": ["1'", 2, 89], Sym('N'+1): [None, 2, 94]}, direction=1)
207 State(step=89, acc=3, transitions={'0': ["0'", 3, 41], '1': ["1'", 3, 41], "0'": ["0'", 3, 89], "1'": ["1'", 3, 89], Sym('N'+1): [None, 3, 94]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [None, 0, 91]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [None, 1, 91]}, direction=None)
210 State(step=90, acc=2, transitions={Sym('varr'+0): [None, 2, 91]}, direction=None)
211 State(step=90, acc=3, transitions={Sym('varr'+0): [None, 3, 91]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ['0', 0, 43], '1': ['1', 0, 43], "0'": ["0'", 0, 91], "1'": ["1'", 0, 91], Sym('varr'+1): [None, 0, 94]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ['0', 1, 43], '1': ['1', 1, 43], "0'": ["0'", 1, 91], "1'": ["1'", 1, 91], Sym('varr'+1): [None, 1, 94]}, direction=1)
214 State(step=91, acc=2, transitions={'0': ['0', 2, 43], '1': ['1', 2, 43], "0'": ["0'", 2, 91], "1'": ["1'", 2, 91], Sym('varr'+1): [None, 2, 94]}, direction=1)
215 State(step=91, acc=3, transitions={'0': ['0', 3, 43], '1': ['1', 3, 43], "0'": ["0'", 3, 91], "1'": ["1'", 3, 91], Sym('varr'+1): [None, 3, 94]}, direction=1)
216 State(step=92, acc=0, transitions={Sym('varr'+0): [None, 0, 93]}, direction=None)
217 State(step=92, acc=1, transitions={Sym('varr'+0): [None, 1, 93]}, direction=None)
218 State(step=92, acc=2, transitions={Sym('varr'+0): [None, 2, 93]}, direction=None)
219 State(step=92, acc=3, transitions={Sym('varr'+0): [None, 3, 93]}, direction=None)
220 State(step=93, acc=0, transitions={'0': ["0'", 0, 46], '1': ["1'", 0, 46], "0'": ["0'", 0, 93], "1'": ["1'", 0, 93], Sym('varr'+1): [None, 0, 94]}, direction=1)
221 State(step=93, acc=1, transitions={'0': ["0'", 1, 46], '1': ["1'", 1, 46], "0'": ["0'", 1, 93], "1'": ["1'", 1, 93], Sym('varr'+1): [None, 1, 94]}, direction=1)
222 State(step=93, acc=2, transitions={'0': ["0'", 2, 46], '1': ["1'", 2, 46], "0'": ["0'", 2, 93], "1'": ["1'", 2, 93], Sym('varr'+1): [None, 2, 94]}, direction=1)
223 State(step=93, acc=3, transitions={'0': ["0'", 3, 46], '1': ["1'", 3, 46], "0'": ["0'", 3, 93], "1'": ["1'", 3, 93], Sym('varr'+1): [None, 3, 94]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [None, 0, 95]}, direction=None)
225 State(step=94, acc=1, transitions={Sym('N'+0): [None, 1, 95]}, direction=None)
226 State(step=94, acc=2, transitions={Sym('N'+0): [None, 2, 95]}, direction=None)
227 State(step=94, acc=3, transitions={Sym('N'+0): [None, 3, 95]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 95], '1': ['1', 0, 95], "0'": ['0', 0, 95], "1'": ['1', 0, 95], Sym('N'+1): [None, 0, 96]}, direction=1)
229 State(step=95, acc=1, transitions={'0': ['0', 1, 95], '1': ['1', 1, 95], "0'": ['0', 1, 95], "1'": ['1', 1, 95], Sym('N'+1): [None, 1, 96]}, direction=1)
230 State(step=95, acc=2, transitions={'0': ['0', 2, 95], '1': ['1', 2, 95], "0'": ['0', 2, 95], "1'": ['1', 2, 95], Sym('N'+1): [None, 2, 96]}, direction=1)
231 State(step=95, acc=3, transitions={'0': ['0', 3, 95], '1': ['1', 3, 95], "0'": ['0', 3, 95], "1'": ['1', 3, 95], Sym('N'+1): [None, 3, 96]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [None, 0, 97]}, direction=None)
233 State(step=96, acc=1, transitions={Sym('varr'+0): [None, 1, 97]}, direction=None)
234 State(step=96, acc=2, transitions={Sym('varr'+0): [None, 2, 97]}, direction=None)
235 State(step=96, acc=3, transitions={Sym('varr'+0): [None, 3, 97]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 97], '1': ['1', 0, 97], "0'": ['0', 0, 97], "1'": ['1', 0, 97], Sym('varr'+1): [None, 0, 24]}, direction=1)
237 State(step=97, acc=1, transitions={'0': ['0', 1, 97], '1': ['1', 1, 97], "0'": ['0', 1, 97], "1'": ['1', 1, 97], Sym('varr'+1): [None, 1, 24]}, direction=1)
238 State(step=97, acc=2, transitions={'0': ['0', 2, 97], '1': ['1', 2, 97], "0'": ['0', 2, 97], "1'": ['1', 2, 97], Sym('varr'+1): [None, 2, 24]}, direction=1)
239 State(step=97, acc=3, transitions={'0': ['0', 3, 97], '1': ['1', 3, 97], "0'": ['0', 3, 97], "1'": ['1', 3, 97], Sym('varr'+1): [None, 3, 24]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [None, 0, 99]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [None, 1, 99]}, direction=None)
242 State(step=98, acc=2, transitions={Sym('V'+0): [None, 2, 99]}, direction=None)
243 State(step=98, acc=3, transitions={Sym('V'+0): [None, 3, 99]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 54], '1': ["1'", 0, 54], "0'": ["0'", 0, 99], "1'": ["1'", 0, 99], Sym('V'+1): [None, 0, 104]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 54], '1': ["1'", 1, 54], "0'": ["0'", 1, 99], "1'": ["1'", 1, 99], Sym('V'+1): [None, 1, 104]}, direction=1)
246 State(step=99, acc=2, transitions={'0': ["0'", 2, 54], '1': ["1'", 2, 54], "0'": ["0'", 2, 99], "1'": ["1'", 2, 99], Sym('V'+1): [None, 2, 104]}, direction=1)
247 State(step=99, acc=3, transitions={'0': ["0'", 3, 54], '1': ["1'", 3, 54], "0'": ["0'", 3, 99], "1'": ["1'", 3, 99], Sym('V'+1): [None, 3, 104]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [None, 0, 101]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [None, 1, 101]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [None, 2, 101]}, direction=None)
251 State(step=100, acc=3, transitions={Sym('P'+0): [None, 3, 101]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ['0', 0, 56], '1': ['1', 0, 56], "0'": ["0'", 0, 101], "1'": ["1'", 0, 101], Sym('P'+1): [None, 0, 104]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ['0', 1, 56], '1': ['1', 1, 56], "0'": ["0'", 1, 101], "1'": ["1'", 1, 101], Sym('P'+1): [None, 1, 104]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ['0', 2, 56], '1': ['1', 2, 56], "0'": ["0'", 2, 101], "1'": ["1'", 2, 101], Sym('P'+1): [None, 2, 104]}, direction=1)
255 State(step=101, acc=3, transitions={'0': ['0', 3, 56], '1': ['1', 3, 56], "0'": ["0'", 3, 101], "1'": ["1'", 3, 101], Sym('P'+1): [None, 3, 104]}, direction=1)
256 State(step=102, acc=0, transitions={Sym('P'+0): [None, 0, 103]}, direction=None)
257 State(step=102, acc=1, transitions={Sym('P'+0): [None, 1, 103]}, direction=None)
258 State(step=102, acc=2, transitions={Sym('P'+0): [None, 2, 103]}, direction=None)
259 State(step=102, acc=3, transitions={Sym('P'+0): [None, 3, 103]}, direction=None)
260 State(step=103, acc=0, transitions={'0': ["0'", 0, 59], '1': ["1'", 0, 59], "0'": ["0'", 0, 103], "1'": ["1'", 0, 103], Sym('P'+1): [None, 0, 104]}, direction=1)
261 State(step=103, acc=1, transitions={'0': ["0'", 1, 59], '1': ["1'", 1, 59], "0'": ["0'", 1, 103], "1'": ["1'", 1, 103], Sym('P'+1): [None, 1, 104]}, direction=1)
262 State(step=103, acc=2, transitions={'0': ["0'", 2, 59], '1': ["1'", 2, 59], "0'": ["0'", 2, 103], "1'": ["1'", 2, 103], Sym('P'+1): [None, 2, 104]}, direction=1)
263 State(step=103, acc=3, transitions={'0': ["0'", 3, 59], '1': ["1'", 3, 59], "0'": ["0'", 3, 103], "1'": ["1'", 3, 103], Sym('P'+1): [None, 3, 104]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [None, 0, 105]}, direction=None)
265 State(step=104, acc=1, transitions={Sym('V'+0): [None, 1, 105]}, direction=None)
266 State(step=104, acc=2, transitions={Sym('V'+0): [None, 2, 105]}, direction=None)
267 State(step=104, acc=3, transitions={Sym('V'+0): [None, 3, 105]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 105], '1': ['1', 0, 105], "0'": ['0', 0, 105], "1'": ['1', 0, 105], Sym('V'+1): [None, 0, 106]}, direction=1)
269 State(step=105, acc=1, transitions={'0': ['0', 1, 105], '1': ['1', 1, 105], "0'": ['0', 1, 105], "1'": ['1', 1, 105], Sym('V'+1): [None, 1, 106]}, direction=1)
270 State(step=105, acc=2, transitions={'0': ['0', 2, 105], '1': ['1', 2, 105], "0'": ['0', 2, 105], "1'": ['1', 2, 105], Sym('V'+1): [None, 2, 106]}, direction=1)
271 State(step=105, acc=3, transitions={'0': ['0', 3, 105], '1': ['1', 3, 105], "0'": ['0', 3, 105], "1'": ['1', 3, 105], Sym('V'+1): [None, 3, 106]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [None, 0, 107]}, direction=None)
273 State(step=106, acc=1, transitions={Sym('P'+0): [None, 1, 107]}, direction=None)
274 State(step=106, acc=2, transitions={Sym('P'+0): [None, 2, 107]}, direction=None)
275 State(step=106, acc=3, transitions={Sym('P'+0): [None, 3, 107]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 107], '1': ['1', 0, 107], "0'": ['0', 0, 107], "1'": ['1', 0, 107], Sym('P'+1): [None, 0, 68]}, direction=1)
277 State(step=107, acc=1, transitions={'0': ['0', 1, 107], '1': ['1', 1, 107], "0'": ['0', 1, 107], "1'": ['1', 1, 107], Sym('P'+1): [None, 1, 68]}, direction=1)
278 State(step=107, acc=2, transitions={'0': ['0', 2, 107], '1': ['1', 2, 107], "0'": ['0', 2, 107], "1'": ['1', 2, 107], Sym('P'+1): [None, 2, 68]}, direction=1)
279 State(step=107, acc=3, transitions={'0': ['0', 3, 107], '1': ['1', 3, 107], "0'": ['0', 3, 107], "1'": ['1', 3, 107], Sym('P'+1): [None, 3, 68]}, direction=1)
>>> for quasi in quasis:
	if type(quasi)==State:
		for value in quasi.transitions.values():
			if len(value)!=3:
				print(quasi)

				
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
3 64
5 66
8 68
10 70
15 72
17 74
20 76
26 78
30 80
31 82
35 84
36 86
40 88
42 90
45 92
48 94
49 96
53 98
55 100
58 102
61 104
62 106
19 76
44 92
57 102
19 0
44 0
57 0
117 116
113 112
109 108
118 116
114 112
110 108
119 116
115 112
111 108
123 122
124 122
125 122
147 146
143 142
139 138
135 134
131 130
148 146
144 142
140 138
136 134
132 130
149 146
145 142
141 138
137 134
133 130
165 164
161 160
166 164
162 160
167 164
163 160
159 156
155 152
199 196
195 192
191 188
187 184
175 172
171 168
222 214
218 210
237 236
233 232
229 228
225 224
238 236
234 232
230 228
226 224
239 236
235 232
231 228
227 224
263 255
259 251
277 276
273 272
269 268
265 264
278 276
274 272
270 268
266 264
279 276
275 272
271 268
267 264
0 End(is_start=True, next_quasis=[138])
13 End(is_start=False, next_quasis=None)
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [None, 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [Sym('N'+1), 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [Sym('N'+1), 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 138]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [None, 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [None, 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [None, 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [Sym('N'+1), 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [Sym('N'+1), 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [Sym('varr'+1), 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [Sym('varr'+1), 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [None, 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [None, 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [None, 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [None, 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> len(used_states)
66
>>> {symbol for symbol in quasi.transitions for quasi in quasis if type(quasi)==State}
Traceback (most recent call last):
  File "<pyshell#522>", line 1, in <module>
    {symbol for symbol in quasi.transitions for quasi in quasis if type(quasi)==State}
NameError: name 'quasi' is not defined

>>> set([symbol for symbol in quasi.transitions for quasi in quasis if type(quasi)==State])
Traceback (most recent call last):
  File "<pyshell#523>", line 1, in <module>
    set([symbol for symbol in quasi.transitions for quasi in quasis if type(quasi)==State])
NameError: name 'quasi' is not defined
>>> set([quasi.transitions for quasi in quasis if type(quasi)==State])
Traceback (most recent call last):
  File "<pyshell#524>", line 1, in <module>
    set([quasi.transitions for quasi in quasis if type(quasi)==State])
TypeError: unhashable type: 'dict'
>>> symbols = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		symbols.update(set(quasi.transitions.keys()))

		
Traceback (most recent call last):
  File "<pyshell#529>", line 3, in <module>
    symbols.update(set(quasi.transitions.keys()))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> symbols
{}
>>> for quasi in quasis:
	if type(quasi)==State:
		new_symbols = set(quasi.transitions.keys())
		symbols.update(new_symbols)

		
Traceback (most recent call last):
  File "<pyshell#532>", line 4, in <module>
    symbols.update(new_symbols)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> new_symbols
{Sym('S'+0)}
>>> symbols = set()
>>> for quasi in quasis:
	if type(quasi)==State:
		new_symbols = set(quasi.transitions.keys())
		symbols.update(new_symbols)

		
>>> symbols
{Sym('N'+1), '0', "1'", Sym('P'+0), '1', Sym('varr'+0), Sym('S'+1), Sym('V'+0), Sym('N'+0), "0'", Sym('varr'+1), Sym('V'+1), Sym('P'+1), Sym('S'+0)}
>>> order = ['S','N','varr','V','P']
>>> @dataclass(frozen=True,eq=True)
class Symbol:
    symbol: str
    offset: int = 0

    def __repr__(self):
        return 'Sym(\''+self.symbol+'\'+'+str(self.offset)+')'

    def get_char(self):
        global order
        return order[(order.index(self.symbol)+self.offset)%len(order)]

>>> for symbol in symbols:
	if type(symbol)==Symbol:
		print(symbol,symbol.get_char())

		
>>> type(symbols[0])
Traceback (most recent call last):
  File "<pyshell#545>", line 1, in <module>
    type(symbols[0])
TypeError: 'set' object does not support indexing
>>> for symbol in symbols:
	print(type(symbol))

	
<class '__main__.Symbol'>
<class 'str'>
<class 'str'>
<class '__main__.Symbol'>
<class 'str'>
<class '__main__.Symbol'>
<class '__main__.Symbol'>
<class '__main__.Symbol'>
<class '__main__.Symbol'>
<class 'str'>
<class '__main__.Symbol'>
<class '__main__.Symbol'>
<class '__main__.Symbol'>
<class '__main__.Symbol'>
>>> type(symbol)
<class '__main__.Symbol'>
>>> type(symbol)==Symbol
False
>>> Symbol
<class '__main__.Symbol'>
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> symbols={Sym('N'+1), '0', "1'", Sym('P'+0), '1', Sym('varr'+0), Sym('S'+1), Sym('V'+0), Sym('N'+0), "0'", Sym('varr'+1), Sym('V'+1), Sym('P'+1), Sym('S'+0)}
Traceback (most recent call last):
  File "<pyshell#552>", line 1, in <module>
    symbols={Sym('N'+1), '0', "1'", Sym('P'+0), '1', Sym('varr'+0), Sym('S'+1), Sym('V'+0), Sym('N'+0), "0'", Sym('varr'+1), Sym('V'+1), Sym('P'+1), Sym('S'+0)}
NameError: name 'Sym' is not defined
>>> order = ['S','N','varr','V','P']
>>> symbol = Symbol('S',+1)
>>> symbol
Sym('S'+1)
>>> symbol.get_char()
'N'

>>> Symbol('P',+1).get_char()
'S'
>>> Symbol('P',-1).get_char()
'V'
>>> compile_function('PI')
0 End(is_start=True, next_quasis=[138])
13 End(is_start=False, next_quasis=None)
108 State(step=64, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 112]}, direction=None)
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
116 State(step=66, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 1, 121]}, direction=None)
120 State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [None, 0, 240]}, direction=1)
121 State(step=67, acc=1, transitions={'0': ['0', 1, 121], '1': ['1', 0, 120], "0'": ['0', 1, 121], "1'": ['1', 0, 120], Sym('V'+1): [None, 1, 241]}, direction=1)
122 State(step=68, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 2, 128]}, direction=None)
126 State(step=69, acc=0, transitions={'0': ['0', 0, 126], '1': ['1', 0, 126], "0'": ['0', 0, 126], "1'": ['1', 0, 126], Sym('N'+1): [Sym('N'+1), 0, 130]}, direction=1)
127 State(step=69, acc=1, transitions={'0': ['1', 0, 126], '1': ['0', 1, 127], "0'": ['1', 0, 126], "1'": ['0', 1, 127], Sym('N'+1): [Sym('N'+1), 1, 13]}, direction=1)
128 State(step=69, acc=2, transitions={'0': ['0', 1, 127], '1': ['1', 1, 127], "0'": ['0', 1, 127], "1'": ['1', 1, 127], Sym('N'+1): [None, 2, 130]}, direction=1)
130 State(step=70, acc=0, transitions={Sym('S'+0): [Sym('S'+0), 0, 134]}, direction=None)
134 State(step=71, acc=0, transitions={'0': ['1', 0, 134], '1': ['0', 0, 134], "0'": ['1', 0, 134], "1'": ['0', 0, 134], Sym('S'+1): [Sym('S'+1), 0, 138]}, direction=1)
138 State(step=72, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 142]}, direction=None)
142 State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
146 State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
150 State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [Sym('varr'+1), 0, 168]}, direction=1)
151 State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [Sym('varr'+1), 1, 169]}, direction=1)
152 State(step=76, acc=0, transitions={Sym('V'+1): [Sym('V'+1), 0, 156]}, direction=None)
153 State(step=76, acc=1, transitions={Sym('V'+1): [Sym('V'+1), 1, 157]}, direction=None)
156 State(step=77, acc=0, transitions={'0': ["0'", 1, 201], '1': ["0'", 1, 201], "0'": ["0'", 0, 156], "1'": ["1'", 0, 156], Sym('V'+0): [Sym('V'+0), 0, 160]}, direction=-1)
157 State(step=77, acc=1, transitions={'0': ["1'", 0, 146], '1': ["1'", 0, 146], "0'": ["0'", 1, 157], "1'": ["1'", 1, 157], Sym('V'+0): [Sym('V'+0), 1, 160]}, direction=-1)
160 State(step=78, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 164]}, direction=None)
164 State(step=79, acc=0, transitions={'0': ['0', 0, 164], '1': ['1', 0, 164], "0'": ['0', 0, 164], "1'": ['1', 0, 164], Sym('V'+1): [Sym('V'+1), 0, 108]}, direction=1)
168 State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
169 State(step=80, acc=1, transitions={Sym('varr'+1): [Sym('varr'+1), 1, 173]}, direction=None)
172 State(step=81, acc=0, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 0, 172], "1'": ["1'", 0, 172], Sym('varr'+0): [Sym('varr'+0), 0, 184]}, direction=-1)
173 State(step=81, acc=1, transitions={'0': ["0'", 0, 176], '1': ["1'", 1, 177], "0'": ["0'", 1, 173], "1'": ["1'", 1, 173], Sym('varr'+0): [Sym('varr'+0), 1, 185]}, direction=-1)
176 State(step=82, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 180]}, direction=None)
177 State(step=82, acc=1, transitions={Sym('N'+1): [Sym('N'+1), 1, 181]}, direction=None)
180 State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [Sym('N'+0), 0, 184]}, direction=-1)
181 State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1)
184 State(step=84, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 188]}, direction=None)
185 State(step=84, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 189]}, direction=None)
188 State(step=85, acc=0, transitions={'0': ['0', 0, 188], '1': ['1', 0, 188], "0'": ['0', 0, 188], "1'": ['1', 0, 188], Sym('varr'+1): [Sym('varr'+1), 0, 192]}, direction=1)
189 State(step=85, acc=1, transitions={'0': ['0', 1, 189], '1': ['1', 1, 189], "0'": ['0', 1, 189], "1'": ['1', 1, 189], Sym('varr'+1): [Sym('varr'+1), 1, 193]}, direction=1)
192 State(step=86, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 196]}, direction=None)
193 State(step=86, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 197]}, direction=None)
196 State(step=87, acc=0, transitions={'0': ['0', 0, 196], '1': ['1', 0, 196], "0'": ['0', 0, 196], "1'": ['1', 0, 196], Sym('N'+1): [Sym('N'+1), 0, 152]}, direction=1)
197 State(step=87, acc=1, transitions={'0': ['0', 1, 197], '1': ['1', 1, 197], "0'": ['0', 1, 197], "1'": ['1', 1, 197], Sym('N'+1): [Sym('N'+1), 1, 153]}, direction=1)
200 State(step=88, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 204]}, direction=None)
201 State(step=88, acc=1, transitions={Sym('N'+0): [Sym('N'+0), 1, 205]}, direction=None)
204 State(step=89, acc=0, transitions={'0': ["0'", 0, 208], '1': ["1'", 1, 209], "0'": ["0'", 0, 204], "1'": ["1'", 0, 204], Sym('N'+1): [Sym('N'+1), 0, 224]}, direction=1)
205 State(step=89, acc=1, transitions={'0': ["0'", 1, 209], '1': ["1'", 1, 209], "0'": ["0'", 1, 205], "1'": ["1'", 1, 205], Sym('N'+1): [Sym('N'+1), 1, 224]}, direction=1)
208 State(step=90, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 212]}, direction=None)
209 State(step=90, acc=1, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 213]}, direction=None)
212 State(step=91, acc=0, transitions={'0': ["0'", 0, 200], '1': ["1'", 1, 201], "0'": ["0'", 0, 212], "1'": ["1'", 0, 212], Sym('varr'+1): [Sym('varr'+1), 0, 224]}, direction=1)
213 State(step=91, acc=1, transitions={'0': ["0'", 1, 201], '1': ["0'", 0, 200], "0'": ["0'", 1, 213], "1'": ["1'", 1, 213], Sym('varr'+1): [Sym('varr'+1), 1, 224]}, direction=1)
224 State(step=94, acc=0, transitions={Sym('N'+0): [Sym('N'+0), 0, 228]}, direction=None)
228 State(step=95, acc=0, transitions={'0': ['0', 0, 228], '1': ['1', 0, 228], "0'": ['0', 0, 228], "1'": ['1', 0, 228], Sym('N'+1): [Sym('N'+1), 0, 232]}, direction=1)
232 State(step=96, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 236]}, direction=None)
236 State(step=97, acc=0, transitions={'0': ['0', 0, 236], '1': ['1', 0, 236], "0'": ['0', 0, 236], "1'": ['1', 0, 236], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
240 State(step=98, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 244]}, direction=None)
241 State(step=98, acc=1, transitions={Sym('V'+0): [Sym('V'+0), 1, 245]}, direction=None)
244 State(step=99, acc=0, transitions={'0': ["0'", 0, 248], '1': ["1'", 1, 249], "0'": ["0'", 0, 244], "1'": ["1'", 0, 244], Sym('V'+1): [None, 0, 264]}, direction=1)
245 State(step=99, acc=1, transitions={'0': ["0'", 1, 249], '1': ["1'", 2, 250], "0'": ["0'", 1, 245], "1'": ["1'", 1, 245], Sym('V'+1): [Sym('V'+1), 1, 264]}, direction=1)
248 State(step=100, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 252]}, direction=None)
249 State(step=100, acc=1, transitions={Sym('P'+0): [Sym('P'+0), 1, 253]}, direction=None)
250 State(step=100, acc=2, transitions={Sym('P'+0): [Sym('P'+0), 2, 254]}, direction=None)
252 State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1)
253 State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1)
254 State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1)
264 State(step=104, acc=0, transitions={Sym('V'+0): [Sym('V'+0), 0, 268]}, direction=None)
268 State(step=105, acc=0, transitions={'0': ['0', 0, 268], '1': ['1', 0, 268], "0'": ['0', 0, 268], "1'": ['1', 0, 268], Sym('V'+1): [Sym('V'+1), 0, 272]}, direction=1)
272 State(step=106, acc=0, transitions={Sym('P'+0): [Sym('P'+0), 0, 276]}, direction=None)
276 State(step=107, acc=0, transitions={'0': ['0', 0, 276], '1': ['1', 0, 276], "0'": ['0', 0, 276], "1'": ['1', 0, 276], Sym('P'+1): [Sym('P'+1), 0, 122]}, direction=1)
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						direction = +1 if order.index(step2.variable)>order.index(step.variable) else -1
						if k in directions and directions[k]!=direction:
							print(quasi,k)
						else:
							directions[k] = direction

							
Traceback (most recent call last):
  File "<pyshell#574>", line 12, in <module>
    if k in directions and directions[k]!=direction:
NameError: name 'directions' is not defined
>>> directions = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						direction = +1 if order.index(step2.variable)>order.index(step.variable) else -1
						if k in directions and directions[k]!=direction:
							print(quasi,k)
						else:
							directions[k] = direction

							
State(step=67, acc=0, transitions={'0': ['1', 0, 120], '1': ['0', 0, 120], "0'": ['1', 0, 120], "1'": ['0', 0, 120], Sym('V'+1): [None, 0, 240]}, direction=1) 240
State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [Sym('N'+0), 0, 184]}, direction=-1) 168
State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [Sym('N'+0), 0, 184]}, direction=-1) 185
State(step=83, acc=0, transitions={'0': ["0'", 0, 168], '1': ["1'", 1, 185], "0'": ["0'", 0, 180], "1'": ["1'", 0, 180], Sym('N'+0): [Sym('N'+0), 0, 184]}, direction=-1) 184
State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1) 184
State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1) 168
State(step=83, acc=1, transitions={'0': ["0'", 3, 184], '1': ["1'", 0, 168], "0'": ["0'", 1, 181], "1'": ["1'", 1, 181], Sym('N'+0): [Sym('N'+0), 1, 185]}, direction=-1) 185
State(step=83, acc=2, transitions={'0': ["0'", 2, 186], '1': ["1'", 2, 186], "0'": ["0'", 2, 182], "1'": ["1'", 2, 182], Sym('N'+0): [Sym('N'+0), 2, 186]}, direction=-1) 186
State(step=83, acc=2, transitions={'0': ["0'", 2, 186], '1': ["1'", 2, 186], "0'": ["0'", 2, 182], "1'": ["1'", 2, 182], Sym('N'+0): [Sym('N'+0), 2, 186]}, direction=-1) 186
State(step=83, acc=2, transitions={'0': ["0'", 2, 186], '1': ["1'", 2, 186], "0'": ["0'", 2, 182], "1'": ["1'", 2, 182], Sym('N'+0): [Sym('N'+0), 2, 186]}, direction=-1) 186
State(step=83, acc=3, transitions={'0': ["0'", 3, 184], '1': ["1'", 3, 184], "0'": ["0'", 3, 183], "1'": ["1'", 3, 183], Sym('N'+0): [Sym('N'+0), 3, 184]}, direction=-1) 184
State(step=83, acc=3, transitions={'0': ["0'", 3, 184], '1': ["1'", 3, 184], "0'": ["0'", 3, 183], "1'": ["1'", 3, 183], Sym('N'+0): [Sym('N'+0), 3, 184]}, direction=-1) 184
State(step=83, acc=3, transitions={'0': ["0'", 3, 184], '1': ["1'", 3, 184], "0'": ["0'", 3, 183], "1'": ["1'", 3, 183], Sym('N'+0): [Sym('N'+0), 3, 184]}, direction=-1) 184
State(step=101, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 1, 241], "0'": ["0'", 0, 252], "1'": ["1'", 0, 252], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1) 240
State(step=101, acc=1, transitions={'0': ["0'", 1, 241], '1': ["1'", 0, 240], "0'": ["0'", 1, 253], "1'": ["1'", 1, 253], Sym('P'+1): [Sym('P'+1), 1, 264]}, direction=1) 240
State(step=101, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 1, 241], "0'": ["0'", 2, 254], "1'": ["1'", 2, 254], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1) 240
State(step=103, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 0, 240], "0'": ["0'", 0, 260], "1'": ["1'", 0, 260], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1) 240
State(step=103, acc=0, transitions={'0': ["0'", 0, 240], '1': ["0'", 0, 240], "0'": ["0'", 0, 260], "1'": ["1'", 0, 260], Sym('P'+1): [Sym('P'+1), 0, 264]}, direction=1) 240
State(step=103, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 0, 240], "0'": ["0'", 2, 262], "1'": ["1'", 2, 262], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1) 240
State(step=103, acc=2, transitions={'0': ["1'", 0, 240], '1': ["1'", 0, 240], "0'": ["0'", 2, 262], "1'": ["1'", 2, 262], Sym('P'+1): [Sym('P'+1), 2, 264]}, direction=1) 240
>>> directions = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						direction = +1 if order.index(step2.variable)>order.index(step.variable) else -1
						if k in directions and directions[k]!=direction:
							print(k)
						else:
							directions[k] = direction

							
240
168
185
184
184
168
185
186
186
186
184
184
184
240
240
240
240
240
240
240
>>> quasis[98]
Step(instruction=53, is_found=False, variable='V', next_quasis=[99], direction=None)
>>> quasis[53]
Instruction(LOADNEXT, vard=V, next_quasis=[54, 104])
>>> sequences = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						sequences.add((step.variable,step2.variable))

						
Traceback (most recent call last):
  File "<pyshell#585>", line 11, in <module>
    sequences.add((step.variable,step2.variable))
AttributeError: 'dict' object has no attribute 'add'
>>> sequences = set()
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						sequences.add((step.variable,step2.variable))

						
>>> sequences
{('S', 'V'), ('V', 'N'), ('S', 'varr'), ('V', 'varr'), ('V', 'P'), ('V', 'V'), ('N', 'varr'), ('N', 'V'), ('P', 'V'), ('varr', 'varr'), ('P', 'N'), ('varr', 'N'), ('V', 'S'), ('N', 'N'), ('N', 'S')}
>>> for v1,v2 in sequence:
	if v1!=v2:
		print(v1,v2)

		
Traceback (most recent call last):
  File "<pyshell#593>", line 1, in <module>
    for v1,v2 in sequence:
NameError: name 'sequence' is not defined
>>> for v1,v2 in sequences:
	if v1!=v2:
		print(v1,v2)

		
S V
V N
S varr
V varr
V P
N varr
N V
P V
P N
varr N
V S
N S
>>> previouses = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						if not k in previouses:
							previouses[k]=[]
						previouses[k].append(step.variable)

						
>>> previouses = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						if not k in previouses:
							previouses[k]=[]
						previouses[k].append(step.variable)

						
>>> previouses
{240: ['S', 'V', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 116: ['S', 'S'], 241: ['V', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 130: ['N', 'N', 'N'], 138: ['S'], 146: ['varr', 'V', 'V', 'varr'], 168: ['varr', 'N', 'N'], 169: ['varr'], 201: ['V', 'V', 'varr', 'varr', 'varr', 'varr', 'varr', 'varr', 'varr'], 160: ['V', 'V', 'V'], 202: ['V', 'V'], 108: ['V'], 176: ['varr', 'varr', 'varr'], 177: ['varr', 'varr', 'varr'], 184: ['varr', 'N', 'N', 'N', 'N', 'N'], 185: ['varr', 'N', 'N'], 186: ['varr', 'N', 'N', 'N'], 192: ['varr'], 193: ['varr'], 194: ['varr'], 152: ['N'], 153: ['N'], 154: ['N'], 208: ['N', 'N'], 209: ['N', 'N', 'N'], 224: ['N', 'N', 'N', 'N', 'varr', 'varr', 'varr', 'varr', 'varr', 'varr', 'varr'], 210: ['N', 'N'], 211: ['N'], 200: ['varr', 'varr', 'varr', 'varr', 'varr', 'varr', 'varr'], 232: ['N'], 248: ['V'], 249: ['V', 'V'], 264: ['V', 'V', 'V', 'V', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 250: ['V', 'V', 'V'], 251: ['V', 'V'], 272: ['V'], 122: ['P']}
>>> previouses = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(step.variable)

						
>>> quasis[240].step.variable
Traceback (most recent call last):
  File "<pyshell#608>", line 1, in <module>
    quasis[240].step.variable
AttributeError: 'int' object has no attribute 'variable'
>>> quasis[quasis[240].step].variable
'V'
>>> for k in previouses:
	print(quasis[quasis[k].step].variable,previouses[k])

	
V {'P', 'S', 'V'}
V {'S'}
V {'P', 'V'}
S {'N'}
varr {'S'}
varr {'V', 'varr'}
varr {'N', 'varr'}
varr {'varr'}
N {'V', 'varr'}
V {'V'}
N {'V'}
S {'V'}
N {'varr'}
N {'varr'}
varr {'N', 'varr'}
varr {'N', 'varr'}
varr {'N', 'varr'}
N {'varr'}
N {'varr'}
N {'varr'}
V {'N'}
V {'N'}
V {'N'}
varr {'N'}
varr {'N'}
N {'N', 'varr'}
varr {'N'}
varr {'N'}
N {'varr'}
varr {'N'}
P {'V'}
P {'V'}
V {'P', 'V'}
P {'V'}
P {'V'}
P {'V'}
N {'P'}
>>> previouses = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found and step.variable!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(step.variable)

						
>>> for k in previouses:
	print(quasis[quasis[k].step].variable,previouses[k])

	
V {'P', 'S'}
V {'S'}
S {'N'}
varr {'S'}
N {'V', 'varr'}
varr {'V'}
N {'V'}
S {'V'}
N {'varr'}
N {'varr'}
varr {'N'}
varr {'N'}
varr {'N'}
varr {'N'}
N {'varr'}
N {'varr'}
N {'varr'}
V {'N'}
V {'N'}
V {'N'}
varr {'N'}
varr {'N'}
varr {'N'}
varr {'N'}
N {'varr'}
N {'varr'}
varr {'N'}
P {'V'}
P {'V'}
P {'V'}
P {'V'}
V {'P'}
V {'P'}
P {'V'}
N {'P'}
>>> order
['S', 'N', 'varr', 'V', 'P']
>>> for k in previouses:
	if len(previouses[k])>1:
		print(quasis[quasis[k].step].variable,previouses[k])

		
V {'P', 'S'}
N {'V', 'varr'}
>>> order = []previouses = {}
SyntaxError: invalid syntax
>>> previouses = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found and symbol!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(symbol)

						
>>> for k in previouses:
	if len(previouses[k])>1:
		print(quasis[quasis[k].step].variable,previouses[k])

		
V {Sym('V'+1), '0', '1'}
V {Sym('S'+1), '1'}
V {Sym('V'+1), '0', '1'}
varr {'1', '0', Sym('varr'+1)}
varr {'1', '0', Sym('varr'+1)}
N {'0', '1'}
N {'0', '1'}
varr {'0', Sym('N'+0), Sym('varr'+0), '1'}
varr {Sym('N'+0), Sym('varr'+0), '1'}
varr {'0', Sym('N'+0), Sym('varr'+0), '1'}
varr {'0', '1'}
varr {'0', '1'}
N {Sym('N'+1), Sym('varr'+1)}
varr {'0', '1'}
N {'0', '1'}
P {'0', '1'}
V {Sym('V'+1), Sym('P'+1)}
P {'0', '1'}
P {'0', '1'}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				if symbol in ['0','1']:
					last_symbol = step.variable
				elif symbol.offset==0:
					last_symbol = symbol.symbol
				else:
					last_symbol = symbol
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if not step2.is_found and last_symbol!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(last_symbol)

						
Traceback (most recent call last):
  File "<pyshell#628>", line 8, in <module>
    elif symbol.offset==0:
AttributeError: 'str' object has no attribute 'offset'
>>> previouses = {}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:				
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if symbol in ['0','1']:
						last_symbol = step.variable
					elif symbol.offset==0:
						last_symbol = symbol.symbol
					else:
						last_symbol = symbol
					if not step2.is_found and last_symbol!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(last_symbol)

						
Traceback (most recent call last):
  File "<pyshell#631>", line 12, in <module>
    elif symbol.offset==0:
AttributeError: 'str' object has no attribute 'offset'
>>> previouses
{240: {'S'}, 116: {'S'}}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if symbol in ['0','1','0\'','1\'']:
						last_symbol = step.variable
					elif symbol.offset==0:
						last_symbol = symbol.symbol
					else:
						last_symbol = symbol
					if not step2.is_found and last_symbol!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(last_symbol)

						
>>> previouses
{240: {'P', Sym('V'+1), 'S'}, 116: {Sym('S'+1), 'S'}, 241: {'P', Sym('V'+1)}, 130: {Sym('N'+1)}, 138: {Sym('S'+1)}, 146: {'V', Sym('varr'+1)}, 168: {'N', Sym('varr'+1)}, 169: {Sym('varr'+1)}, 201: {'V', 'varr'}, 202: {'V'}, 108: {Sym('V'+1)}, 176: {'varr'}, 177: {'varr'}, 185: {'N'}, 184: {'N'}, 186: {'N'}, 192: {Sym('varr'+1)}, 193: {Sym('varr'+1)}, 194: {Sym('varr'+1)}, 152: {Sym('N'+1)}, 153: {Sym('N'+1)}, 154: {Sym('N'+1)}, 208: {'N'}, 209: {'N'}, 224: {Sym('N'+1), Sym('varr'+1)}, 210: {'N'}, 211: {'N'}, 200: {'varr'}, 232: {Sym('N'+1)}, 248: {'V'}, 249: {'V'}, 264: {Sym('V'+1), Sym('P'+1)}, 250: {'V'}, 251: {'V'}, 272: {Sym('V'+1)}, 122: {Sym('P'+1)}}
>>> for k in previouses:
	if len(previouses[k])>1:
		print(quasis[quasis[k].step].variable,previouses[k])

		
V {'P', Sym('V'+1), 'S'}
V {Sym('S'+1), 'S'}
V {'P', Sym('V'+1)}
varr {'V', Sym('varr'+1)}
varr {'N', Sym('varr'+1)}
N {'V', 'varr'}
N {Sym('N'+1), Sym('varr'+1)}
V {Sym('V'+1), Sym('P'+1)}
>>> previouses={}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if symbol in ['0','1','0\'','1\'']:
						last_symbol = symbol(step.variable,+.5)
					elif symbol.offset==0:
						last_symbol = symbol.symbol
					else:
						last_symbol = symbol
					if not step2.is_found and last_symbol!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(last_symbol)

						
Traceback (most recent call last):
  File "<pyshell#640>", line 11, in <module>
    last_symbol = symbol(step.variable,+.5)
TypeError: 'str' object is not callable
>>> previouses={}
>>> for quasi in quasis:
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				k = quasi.transitions[symbol][2]
				quasi2 = quasis[k]
				if type(quasi2)==State:
					step2 = quasis[quasi2.step]
					if symbol in ['0','1','0\'','1\'']:
						last_symbol = Symbol(step.variable,+.5)
					elif symbol.offset==0:
						last_symbol = symbol.symbol
					else:
						last_symbol = symbol
					if not step2.is_found and last_symbol!=step2.variable:
						if not k in previouses:
							previouses[k] = set()
						previouses[k].add(last_symbol)

						
>>> for k in previouses:
	if len(previouses[k])>1:
		print(quasis[quasis[k].step].variable,previouses[k])

		
V {Sym('V'+1), Sym('P'+0.5), Sym('S'+0.5)}
V {Sym('S'+1), Sym('S'+0.5)}
V {Sym('V'+1), Sym('P'+0.5)}
varr {Sym('V'+0.5), Sym('varr'+1)}
varr {Sym('N'+0.5), Sym('varr'+1)}
N {Sym('varr'+0.5), Sym('V'+0.5)}
varr {'N', Sym('N'+0.5)}
varr {'N', Sym('N'+0.5)}
varr {'N', Sym('N'+0.5)}
N {Sym('N'+1), Sym('varr'+1)}
V {Sym('V'+1), Sym('P'+1)}
>>> Symbol('X',0)
Sym('X'+0)
>>> order = ['varr','V','N','P','S']
>>> for quasi in quasis:
	if type(quasi)==State:
		for symbol quasi.transitions:
			
SyntaxError: invalid syntax
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		for symbol in quasi.transitions:
			transition = quasi.transitions[symbol]
			
			if step.is_found:
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else transition[0],
				      
				'<current state> <current symbol> <new symbol> <direction> <new state>'
KeyboardInterrupt
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		for symbol in quasi.transitions:
			transition = quasi.transitions[symbol]
			step2 = quasis[quasis[transition[2]].step]
			if type(symbol)==Symbol:
				direction = order.index(step2.variable) - order.index(step.variable)
			else:
				direction = step.direction
			direction = 'l' if direction<0 else 'r'
			if step.is_found:
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))

				      
Traceback (most recent call last):
  File "<pyshell#658>", line 11, in <module>
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> directions = set()
				      
>>> )))
				
SyntaxError: invalid syntax
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		for symbol in quasi.transitions:
			transition = quasi.transitions[symbol]
			step2 = quasis[quasis[transition[2]].step]
			if type(symbol)==Symbol:
				direction = order.index(step2.variable) - order.index(step.variable)
			else:
				direction = step.direction
			try:
				direction = 'l' if direction<0 else 'r'
			except TypeError:
				print(k,quasi,symbol)
				1/0
			if step.is_found:
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))

				
112 State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1) 0
Traceback (most recent call last):
  File "<pyshell#662>", line 12, in <module>
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'NoneType' and 'int'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#662>", line 15, in <module>
    1/0
ZeroDivisionError: division by zero
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		for symbol in quasi.transitions:
			transition = quasi.transitions[symbol]
			step2 = quasis[quasis[transition[2]].step]
			if transition[2]==k:
				direction = step.direction
			else:
				direction = order.index(step2.variable) - order.index(step.variable)
			direction = 'l' if direction<0 else 'r'
				print(k,quasi,symbol)
				1/0
			if step.is_found:
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))
				
SyntaxError: unexpected indent
for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		for symbol in quasi.transitions:
			transition = quasi.transitions[symbol]
			step2 = quasis[quasis[transition[2]].step]
			if transition[2]==k:
				direction = step.direction
			else:
				direction = order.index(step2.variable) - order.index(step.variable)
			direction = 'l' if direction<0 else 'r'
				print(k,quasi,symbol)
				1/0
			if step.is_found:
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		for symbol in quasi.transitions:
			transition = quasi.transitions[symbol]
			step2 = quasis[quasis[transition[2]].step]
			if transition[2]==k:
				direction = step.direction
			else:
				direction = order.index(step2.variable) - order.index(step.variable)
			direction = 'l' if direction<0 else 'r'
			if step.is_found:
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))

				
112 0 0 l 240l
112 1 1 l 116l
Traceback (most recent call last):
  File "<pyshell#665>", line 11, in <module>
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> directions
{(116, 'l'), (240, 'l')}
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				transition = quasi.transitions[symbol]
				step2 = quasis[quasis[transition[2]].step]
				if transition[2]==k:
					direction = step.direction
				else:
					direction = order.index(step2.variable) - order.index(step.variable)
				direction = 'l' if direction<0 else 'r'
				if step.is_found:
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else transition[0],
					      direction,
					      str(transition[2])+direction)
					directions.add((transition[2],direction))

					
112 0 0 l 240l
112 1 1 l 116l
Traceback (most recent call last):
  File "<pyshell#668>", line 12, in <module>
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				print(k)
				transition = quasi.transitions[symbol]
				step2 = quasis[quasis[transition[2]].step]
				if transition[2]==k:
					direction = step.direction
				else:
					direction = order.index(step2.variable) - order.index(step.variable)
				direction = 'l' if direction<0 else 'r'
				if step.is_found:
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else transition[0],
					      direction,
					      str(transition[2])+direction)
					directions.add((transition[2],direction))

					
112
112 0 0 l 240l
112
112 1 1 l 116l
112
Traceback (most recent call last):
  File "<pyshell#670>", line 13, in <module>
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				print(k,symbol)
				transition = quasi.transitions[symbol]
				step2 = quasis[quasis[transition[2]].step]
				if transition[2]==k:
					direction = step.direction
				else:
					direction = order.index(step2.variable) - order.index(step.variable)
				direction = 'l' if direction<0 else 'r'
				if step.is_found:
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else transition[0],
					      direction,
					      str(transition[2])+direction)
					directions.add((transition[2],direction))

					
112 0
112 0 0 l 240l
112 1
112 1 1 l 116l
112 0'
Traceback (most recent call last):
  File "<pyshell#672>", line 13, in <module>
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'NoneType' and 'int'
>>> quasis[112]
State(step=65, acc=0, transitions={'0': ['0', 0, 240], '1': ['1', 1, 116], "0'": ["0'", 0, 112], "1'": ["1'", 0, 112], Sym('S'+1): [Sym('S'+1), 0, 116]}, direction=1)
>>> quasis[65]
Step(instruction=3, is_found=True, variable='S', next_quasis=[4, 66], direction=None)
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				print(k,symbol)
				transition = quasi.transitions[symbol]
				step2 = quasis[quasis[transition[2]].step]
				if transition[2]==k:
					direction = quasi.direction
				else:
					direction = order.index(step2.variable) - order.index(step.variable)
				direction = 'l' if direction<0 else 'r'
				if step.is_found:
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else transition[0],
					      direction,
					      str(transition[2])+direction)
					directions.add((transition[2],direction))

					
112 0
112 0 0 l 240l
112 1
112 1 1 l 116l
112 0'
112 0' 0' r 112r
112 1'
112 1' 1' r 112r
112 Sym('S'+1)
112 varr Sym('S'+1) l 116l
120 0
120 0 1 r 120r
120 1
120 1 0 r 120r
120 0'
120 0' 1 r 120r
120 1'
120 1' 0 r 120r
120 Sym('V'+1)
120 N * r 240r
121 0
121 0 0 r 121r
121 1
121 1 1 r 120r
121 0'
121 0' 0 r 121r
121 1'
121 1' 1 r 120r
121 Sym('V'+1)
121 N * r 241r
Traceback (most recent call last):
  File "<pyshell#676>", line 19, in <module>
    str(transition[2])+direction)
KeyboardInterrupt
>>> directions = set()
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				transition = quasi.transitions[symbol]
				step2 = quasis[quasis[transition[2]].step]
				if transition[2]==k:
					direction = quasi.direction
				else:
					direction = order.index(step2.variable) - order.index(step.variable)
				direction = 'l' if direction<0 else 'r'
				if step.is_found:
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else transition[0],
					      direction,
					      str(transition[2])+direction)
					directions.add((transition[2],direction))

					
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112r
112 1' 1' r 112r
112 varr Sym('S'+1) l 116l
120 0 1 r 120r
120 1 0 r 120r
120 0' 1 r 120r
120 1' 0 r 120r
120 N * r 240r
121 0 0 r 121r
121 1 1 r 120r
121 0' 0 r 121r
121 1' 1 r 120r
121 N * r 241r
126 0 0 r 126r
126 1 1 r 126r
Traceback (most recent call last):
  File "<pyshell#679>", line 18, in <module>
    str(transition[2])+direction)
KeyboardInterrupt
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				transition = quasi.transitions[symbol]
				step2 = quasis[quasis[transition[2]].step]
				if transition[2]==k:
					direction = quasi.direction
				else:
					direction = order.index(step2.variable) - order.index(step.variable)
				direction = 'l' if direction<0 else 'r'
				if step.is_found:
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else symbol.get_char() if type(transition[0])==Symbol else transition[0],
					      direction,
					      str(transition[2])+direction)
					directions.add((transition[2],direction))

					
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112r
112 1' 1' r 112r
112 varr varr l 116l
120 0 1 r 120r
120 1 0 r 120r
120 0' 1 r 120r
120 1' 0 r 120r
120 N * r 240r
121 0 0 r 121r
121 1 1 r 120r
121 0' 0 r 121r
121 1' 1 r 120r
121 N * r 241r
126 0 0 r 126r
126 1 1 r 126r
126 0' 0 r 126r
126 1' 1 r 126r
126 P P r 130r
127 0 1 r 126r
127 1 0 r 127r
127 0' 1 r 126r
127 1' 0 r 127r
Traceback (most recent call last):
  File "<pyshell#681>", line 7, in <module>
    step2 = quasis[quasis[transition[2]].step]
AttributeError: 'End' object has no attribute 'step'
>>> for k,quasi in enumerate(quasis):
	if type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				transition = quasi.transitions[symbol]
				if type(quasis[transition[2]])==State:
					step2 = quasis[quasis[transition[2]].step]
					if transition[2]==k:
						direction = quasi.direction
					else:
						direction = order.index(step2.variable) - order.index(step.variable)
					direction = 'l' if direction<0 else 'r'
				else:
					direction = '*'
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else symbol.get_char() if type(transition[0])==Symbol else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))

				
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112r
112 1' 1' r 112r
112 varr varr l 116l
120 0 1 r 120r
120 1 0 r 120r
120 0' 1 r 120r
120 1' 0 r 120r
120 N * r 240r
121 0 0 r 121r
121 1 1 r 120r
121 0' 0 r 121r
121 1' 1 r 120r
121 N * r 241r
126 0 0 r 126r
126 1 1 r 126r
126 0' 0 r 126r
126 1' 1 r 126r
126 P P r 130r
127 0 1 r 126r
127 1 0 r 127r
127 0' 1 r 126r
127 1' 0 r 127r
127 P P * 13*
128 0 0 r 127r
128 1 1 r 127r
128 0' 0 r 127r
128 1' 1 r 127r
128 P * r 130r
129 0 1 r 127r
129 1 0 r 128r
129 0' 1 r 127r
129 1' 0 r 128r
129 P * r 130r
134 0 1 r 134r
134 1 0 r 134r
134 0' 1 r 134r
134 1' 0 r 134r
134 varr varr l 138l
142 0 0 r 142r
142 1 0 r 142r
142 0' 0 r 142r
142 1' 0 r 142r
142 V V r 146r
150 0 0 r 150r
150 1 0 r 151r
150 0' 0 r 150r
150 1' 0 r 151r
150 V V r 168r
151 0 1 r 150r
151 1 1 r 151r
151 0' 1 r 150r
151 1' 1 r 151r
151 V V r 169r
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156l
156 1' 1' l 156l
156 V V r 160r
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157l
157 1' 1' l 157l
157 V V r 160r
158 0 0' r 202r
158 1 1' r 202r
158 0' 0' l 158l
158 1' 1' l 158l
158 V V r 160r
164 0 0 r 164r
164 1 1 r 164r
164 0' 0 r 164r
164 1' 1 r 164r
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172l
172 1' 1' l 172l
172 varr varr r 184r
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173l
173 1' 1' l 173l
173 varr varr r 185r
174 0 0' r 176r
174 1 1' r 177r
174 0' 0'Traceback (most recent call last):
  File "<pyshell#683>", line 20, in <module>
    str(transition[2])+direction)
KeyboardInterrupt
>>> used_states
{0, 128, 130, 134, 264, 138, 268, 13, 142, 272, 146, 276, 150, 151, 152, 153, 156, 157, 160, 164, 168, 169, 172, 173, 176, 177, 180, 181, 184, 185, 188, 189, 192, 193, 196, 197, 200, 201, 204, 205, 208, 209, 212, 213, 120, 224, 121, 228, 232, 250, 108, 236, 112, 240, 241, 244, 245, 116, 254, 248, 249, 122, 252, 253, 126, 127}
>>> directions = set()
>>> for k,quasi in enumerate(quasis):
	if k in used_states and type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				transition = quasi.transitions[symbol]
				if type(quasis[transition[2]])==State:
					step2 = quasis[quasis[transition[2]].step]
					if transition[2]==k:
						direction = quasi.direction
					else:
						direction = order.index(step2.variable) - order.index(step.variable)
					direction = 'l' if direction<0 else 'r'
				else:
					direction = '*'
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else symbol.get_char() if type(transition[0])==Symbol else transition[0],
				      direction,
				      str(transition[2])+direction)
				directions.add((transition[2],direction))

				
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112r
112 1' 1' r 112r
112 varr varr l 116l
120 0 1 r 120r
120 1 0 r 120r
120 0' 1 r 120r
120 1' 0 r 120r
120 N * r 240r
121 0 0 r 121r
121 1 1 r 120r
121 0' 0 r 121r
121 1' 1 r 120r
121 N * r 241r
126 0 0 r 126r
126 1 1 r 126r
126 0' 0 r 126r
126 1' 1 r 126r
126 P P r 130r
127 0 1 r 126r
127 1 0 r 127r
127 0' 1 r 126r
127 1' 0 r 127r
127 P P * 13*
128 0 0 r 127r
128 1 1 r 127r
128 0' 0 r 127r
128 1' 1 r 127r
128 P * r 130r
134 0 1 r 134r
134 1 0 r 134r
134 0' 1 r 134r
134 1' 0 r 134r
134 varr varr l 138l
142 0 0 r 142r
142 1 0 r 142r
142 0' 0 r 142r
142 1' 0 r 142r
142 V V r 146r
150 0 0 r 150r
150 1 0 r 151r
150 0' 0 r 150r
150 1' 0 r 151r
150 V V r 168r
151 0 1 r 150r
151 1 1 r 151r
151 0' 1 r 150r
151 1' 1 r 151r
151 V V r 169r
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156l
156 1' 1' l 156l
156 V V r 160r
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157l
157 1' 1' l 157l
157 V V r 160r
164 0 0 r 164r
164 1 1 r 164r
164 0' 0 r 164r
164 1' 1 r 164r
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172l
172 1' 1' l 172l
172 varr varr r 184r
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173l
173 1' 1' l 173l
173 varr varr r 185r
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180l
180 1' 1' l 180l
180 N N l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181l
181 1' 1' l 181l
181 N N l 185l
188 0 0 r 188r
188 1 1 r 188r
188 0' 0 r 188r
188 1' 1 r 188r
188 V V r 192r
189 0 0 r 189r
189 1 1 r 189r
189 0' 0 r 189r
189 1' 1 r 189r
189 V V r 193r
196 0 0 r 196r
196 1 1 r 196r
196 0' 0 r 196r
196 1' 1 r 196r
196 P P l 152l
197 0 0 r 197r
197 1 1 r 197r
197 0' 0 r 197r
197 1' 1 r 197r
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204r
204 1' 1' r 204r
204 P P r 224r
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205r
205 1' 1' r 205r
205 P P r 224r
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212r
212 1' 1' r 212r
212 V V r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213r
213 1' 1' r 213r
213 V V r 224r
228 0 0 r 228r
228 1 1 r 228r
228 0' 0 r 228r
228 1' 1 r 228r
228 P P l 232l
236 0 0 r 236r
236 1 1 r 236r
236 0' 0 r 236r
236 1' 1 r 236r
236 V V r 146r
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244r
244 1' 1' r 244r
244 N * r 264r
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245r
245 1' 1' r 245r
245 N N r 264r
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252r
252 1' 1' r 252r
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253r
253 1' 1' r 253r
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254r
254 1' 1' r 254r
254 S S l 264l
268 0 0 r 268r
268 1 1 r 268r
268 0' 0 r 268r
268 1' 1 r 268r
268 N N r 272r
276 0 0 r 276r
276 1 1 r 276r
276 0' 0 r 276r
276 1' 1 r 276r
276 S S l 122l
>>> directions
{(228, 'r'), (180, 'l'), (160, 'r'), (121, 'r'), (213, 'r'), (249, 'r'), (150, 'r'), (241, 'l'), (264, 'r'), (193, 'r'), (146, 'r'), (212, 'r'), (205, 'r'), (126, 'r'), (185, 'l'), (254, 'r'), (169, 'r'), (245, 'r'), (120, 'r'), (241, 'r'), (130, 'r'), (232, 'l'), (248, 'r'), (189, 'r'), (192, 'r'), (181, 'l'), (204, 'r'), (156, 'l'), (168, 'r'), (244, 'r'), (112, 'r'), (240, 'r'), (201, 'r'), (188, 'r'), (172, 'l'), (264, 'l'), (164, 'r'), (146, 'l'), (142, 'r'), (116, 'l'), (224, 'r'), (185, 'r'), (208, 'l'), (108, 'r'), (197, 'r'), (236, 'r'), (200, 'r'), (157, 'l'), (13, '*'), (152, 'l'), (276, 'r'), (272, 'r'), (250, 'r'), (134, 'r'), (151, 'r'), (184, 'r'), (177, 'r'), (173, 'l'), (168, 'l'), (196, 'r'), (253, 'r'), (127, 'r'), (240, 'l'), (268, 'r'), (122, 'l'), (209, 'l'), (184, 'l'), (153, 'l'), (176, 'r'), (252, 'r'), (138, 'l')}
>>> directions=set()
>>> for search in directions:
	state = quasis[search[0]]
	for k,quasi in enumerate(quasis):
		if k in used_states and type(quasi)==State:
			step = quasis[quasi.step]
			if step.is_found:
				for symbol in quasi.transitions:
					transition = quasi.transitions[symbol]
					if type(quasis[transition[2]])==State:
						step2 = quasis[quasis[transition[2]].step]
						if step2.is_found:
							direction = quasi.direction
						else:
							direction = order.index(step2.variable) - order.index(step.variable)
						direction = 'l' if direction<0 else 'r'
					else:
						direction = '*'
					print(k,
					      symbol.get_char() if type(symbol)==Symbol else symbol,
					      '*' if transition[0]==None else symbol.get_char() if type(transition[0])==Symbol else transition[0],
					      direction,
					      str(transition[2])+('' if step2.is_found else direction))
					if not step2.is_found:
						directions.add((transition[2],direction))

						
>>> for k,quasi in enumerate(quasis):
	if k in used_states and type(quasi)==State:
		step = quasis[quasi.step]
		if step.is_found:
			for symbol in quasi.transitions:
				transition = quasi.transitions[symbol]
				if type(quasis[transition[2]])==State:
					step2 = quasis[quasis[transition[2]].step]
					if step2.is_found:
						direction = quasi.direction
					else:
						direction = order.index(step2.variable) - order.index(step.variable)
					direction = 'l' if direction<0 else 'r'
				else:
					direction = '*'
				print(k,
				      symbol.get_char() if type(symbol)==Symbol else symbol,
				      '*' if transition[0]==None else symbol.get_char() if type(transition[0])==Symbol else transition[0],
				      direction,
				      str(transition[2])+('' if step2.is_found else direction))
				if not step2.is_found:
					directions.add((transition[2],direction))

					
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112
112 1' 1' r 112
112 varr varr l 116l
120 0 1 r 120
120 1 0 r 120
120 0' 1 r 120
120 1' 0 r 120
120 N * r 240r
121 0 0 r 121
121 1 1 r 120
121 0' 0 r 121
121 1' 1 r 120
121 N * r 241r
126 0 0 r 126
126 1 1 r 126
126 0' 0 r 126
126 1' 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 0' 1 r 126
127 1' 0 r 127
127 P P * 13
128 0 0 r 127
128 1 1 r 127
128 0' 0 r 127
128 1' 1 r 127
128 P * r 130r
134 0 1 r 134
134 1 0 r 134
134 0' 1 r 134
134 1' 0 r 134
134 varr varr l 138l
142 0 0 r 142
142 1 0 r 142
142 0' 0 r 142
142 1' 0 r 142
142 V V r 146r
150 0 0 r 150
150 1 0 r 151
150 0' 0 r 150
150 1' 0 r 151
150 V V r 168r
151 0 1 r 150
151 1 1 r 151
151 0' 1 r 150
151 1' 1 r 151
151 V V r 169r
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156
156 1' 1' l 156
156 V V r 160r
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157
157 1' 1' l 157
157 V V r 160r
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172
172 1' 1' l 172
172 varr varr r 184r
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173
173 1' 1' l 173
173 varr varr r 185r
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180
180 1' 1' l 180
180 N N l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181
181 1' 1' l 181
181 N N l 185l
188 0 0 r 188
188 1 1 r 188
188 0' 0 r 188
188 1' 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 0' 0 r 189
189 1' 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 0' 0 r 196
196 1' 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 0' 0 r 197
197 1' 1 r 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204
204 1' 1' r 204
204 P P r 224r
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205
205 1' 1' r 205
205 P P r 224r
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212
212 1' 1' r 212
212 V V r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213
213 1' 1' r 213
213 V V r 224r
228 0 0 r 228
228 1 1 r 228
228 0' 0 r 228
228 1' 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 0' 0 r 236
236 1' 1 r 236
236 V V r 146r
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244
244 1' 1' r 244
244 N * r 264r
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245
245 1' 1' r 245
245 N N r 264r
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252
252 1' 1' r 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253
253 1' 1' r 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254
254 1' 1' r 254
254 S S l 264l
268 0 0 r 268
268 1 1 r 268
268 0' 0 r 268
268 1' 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 0' 0 r 276
276 1' 1 r 276
276 S S l 122l
>>> directions
{(160, 'r'), (249, 'r'), (241, 'l'), (264, 'r'), (193, 'r'), (146, 'r'), (185, 'l'), (169, 'r'), (248, 'r'), (241, 'r'), (130, 'r'), (232, 'l'), (192, 'r'), (168, 'r'), (240, 'r'), (201, 'r'), (264, 'l'), (146, 'l'), (116, 'l'), (224, 'r'), (185, 'r'), (208, 'l'), (108, 'r'), (200, 'r'), (152, 'l'), (272, 'r'), (250, 'r'), (184, 'r'), (177, 'r'), (168, 'l'), (240, 'l'), (122, 'l'), (209, 'l'), (184, 'l'), (153, 'l'), (176, 'r'), (138, 'l')}
>>> for search in directions:
	state = quasis[search[0]]
	direction = search[1]
	for symbol in state.transitions:
		transition = state.transitions[symbol]
		next_direction = quasis[transition[2]].direction
		print(str(search[0])+direction,
		      list(state.transitions.keys())[0].get_char(),
		      '*',
		      'l' if next_direction<0 else 'r',
		      transition[2])
	print(str(search[0])+direction,'*','*',direction,'*')

	
160r V * r 164
160r * * r *
249r P * r 253
249r * * r *
241l V * r 245
241l * * l *
264r V * r 268
264r * * r *
193r N * r 197
193r * * r *
146r varr * r 151
146r * * r *
185l varr * r 189
185l * * l *
169r V * l 173
169r * * r *
248r P * r 252
248r * * r *
241r V * r 245
241r * * r *
130r S * r 134
130r * * r *
232l varr * r 236
232l * * l *
192r N * r 196
192r * * r *
168r V * l 172
168r * * r *
240r V * r 244
240r * * r *
201r N * r 205
201r * * r *
264l V * r 268
264l * * l *
146l varr * r 151
146l * * l *
116l V * r 121
116l * * l *
224r N * r 228
224r * * r *
185r varr * r 189
185r * * r *
208l varr * r 212
208l * * l *
108r S * r 112
108r * * r *
200r N * r 204
200r * * r *
152l N * l 156
152l * * l *
272r P * r 276
272r * * r *
250r P * r 254
250r * * r *
184r varr * r 188
184r * * r *
177r P * l 181
177r * * r *
168l V * l 172
168l * * l *
240l V * r 244
240l * * l *
122l N * r 128
122l * * l *
209l varr * r 213
209l * * l *
184l varr * r 188
184l * * l *
153l N * l 157
153l * * l *
176r P * l 180
176r * * r *
138l varr * r 142
138l * * l *
>>> quasis[0]
End(is_start=True, next_quasis=[138])
>>> order
['varr', 'V', 'N', 'P', 'S']
>>> sorted(directions)
[(108, 'r'), (116, 'l'), (122, 'l'), (130, 'r'), (138, 'l'), (146, 'l'), (146, 'r'), (152, 'l'), (153, 'l'), (160, 'r'), (168, 'l'), (168, 'r'), (169, 'r'), (176, 'r'), (177, 'r'), (184, 'l'), (184, 'r'), (185, 'l'), (185, 'r'), (192, 'r'), (193, 'r'), (200, 'r'), (201, 'r'), (208, 'l'), (209, 'l'), (224, 'r'), (232, 'l'), (240, 'l'), (240, 'r'), (241, 'l'), (241, 'r'), (248, 'r'), (249, 'r'), (250, 'r'), (264, 'l'), (264, 'r'), (272, 'r')]
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#713>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 628, in compile_function
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 602, in merge_links
    if equal_states(k,j):
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112
112 1' 1' r 112
112 varr varr l 116l
120 0 1 r 120
120 1 0 r 120
120 0' 1 r 120
120 1' 0 r 120
120 N N r 240r
121 0 0 r 121
121 1 1 r 120
121 0' 0 r 121
121 1' 1 r 120
121 N * r 241r
126 0 0 r 126
126 1 1 r 126
126 0' 0 r 126
126 1' 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 0' 1 r 126
127 1' 0 r 127
127 P * * 13
128 0 0 r 127
128 1 1 r 127
128 0' 0 r 127
128 1' 1 r 127
128 P * r 130r
134 0 1 r 134
134 1 0 r 134
134 0' 1 r 134
134 1' 0 r 134
134 varr varr l 138l
142 0 0 r 142
142 1 0 r 142
142 0' 0 r 142
142 1' 0 r 142
142 V V r 146r
150 0 0 r 150
150 1 0 r 151
150 0' 0 r 150
150 1' 0 r 151
150 V * r 168r
151 0 1 r 150
151 1 1 r 151
151 0' 1 r 150
151 1' 1 r 151
151 V * r 169r
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156
156 1' 1' l 156
156 V V r 160r
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157
157 1' 1' l 157
157 V * r 160r
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172
172 1' 1' l 172
172 varr varr r 184r
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173
173 1' 1' l 173
173 varr varr r 185r
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180
180 1' 1' l 180
180 N * l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181
181 1' 1' l 181
181 N * l 185l
188 0 0 r 188
188 1 1 r 188
188 0' 0 r 188
188 1' 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 0' 0 r 189
189 1' 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 0' 0 r 196
196 1' 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 0' 0 r 197
197 1' 1 r 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204
204 1' 1' r 204
204 P * r 224r
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205
205 1' 1' r 205
205 P * r 224r
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212
212 1' 1' r 212
212 V * r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213
213 1' 1' r 213
213 V * r 224r
228 0 0 r 228
228 1 1 r 228
228 0' 0 r 228
228 1' 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 0' 0 r 236
236 1' 1 r 236
236 V V r 146r
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244
244 1' 1' r 244
244 N * r 264r
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245
245 1' 1' r 245
245 N * r 264r
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252
252 1' 1' r 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253
253 1' 1' r 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254
254 1' 1' r 254
254 S S l 264l
268 0 0 r 268
268 1 1 r 268
268 0' 0 r 268
268 1' 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 0' 0 r 276
276 1' 1 r 276
276 S S l 122l
240l V * r 244
240r V * r 244
Traceback (most recent call last):
  File "<pyshell#714>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 677, in print_searches
    print(str(search[0])+direction,'*','*',direction,'*')
TypeError: 'int' object is not subscriptable
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112
112 1' 1' r 112
112 varr varr l 116l
120 0 1 r 120
120 1 0 r 120
120 0' 1 r 120
120 1' 0 r 120
120 N N r 240r
121 0 0 r 121
121 1 1 r 120
121 0' 0 r 121
121 1' 1 r 120
121 N N r 241r
126 0 0 r 126
126 1 1 r 126
126 0' 0 r 126
126 1' 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 0' 1 r 126
127 1' 0 r 127
127 P * * 13
128 0 0 r 127
128 1 1 r 127
128 0' 0 r 127
128 1' 1 r 127
128 P * r 130r
134 0 1 r 134
134 1 0 r 134
134 0' 1 r 134
134 1' 0 r 134
134 varr varr l 138l
142 0 0 r 142
142 1 0 r 142
142 0' 0 r 142
142 1' 0 r 142
142 V V r 146r
150 0 0 r 150
150 1 0 r 151
150 0' 0 r 150
150 1' 0 r 151
150 V * r 168r
151 0 1 r 150
151 1 1 r 151
151 0' 1 r 150
151 1' 1 r 151
151 V * r 169r
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156
156 1' 1' l 156
156 V V r 160r
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157
157 1' 1' l 157
157 V V r 160r
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172
172 1' 1' l 172
172 varr varr r 184r
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173
173 1' 1' l 173
173 varr varr r 185r
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180
180 1' 1' l 180
180 N * l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181
181 1' 1' l 181
181 N * l 185l
188 0 0 r 188
188 1 1 r 188
188 0' 0 r 188
188 1' 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 0' 0 r 189
189 1' 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 0' 0 r 196
196 1' 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 0' 0 r 197
197 1' 1 r 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204
204 1' 1' r 204
204 P * r 224r
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205
205 1' 1' r 205
205 P * r 224r
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212
212 1' 1' r 212
212 V V r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213
213 1' 1' r 213
213 V V r 224r
228 0 0 r 228
228 1 1 r 228
228 0' 0 r 228
228 1' 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 0' 0 r 236
236 1' 1 r 236
236 V V r 146r
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244
244 1' 1' r 244
244 N N r 264r
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245
245 1' 1' r 245
245 N N r 264r
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252
252 1' 1' r 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253
253 1' 1' r 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254
254 1' 1' r 254
254 S S l 264l
268 0 0 r 268
268 1 1 r 268
268 0' 0 r 268
268 1' 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 0' 0 r 276
276 1' 1 r 276
276 S S l 122l
240r V * r 244
240l V * r 244
240l * * l *
116l V * r 121
116l * * l *
241r V * r 245
241l V * r 245
241l * * l *
130r S * r 134
130r * * r *
138l varr * r 142
138l * * l *
146r varr * r 151
146l varr * r 151
146l * * l *
168r V * l 172
168l V * l 172
168l * * l *
169r V * l 173
169r * * r *
201r N * r 205
201r * * r *
160r V * r 164
160r * * r *
108r S * r 112
108r * * r *
176r P * l 180
176r * * r *
177r P * l 181
177r * * r *
184r varr * r 188
184l varr * r 188
184l * * l *
185r varr * r 189
185l varr * r 189
185l * * l *
192r N * r 196
192r * * r *
193r N * r 197
193r * * r *
152l N * l 156
152l * * l *
153l N * l 157
153l * * l *
208l varr * r 212
208l * * l *
209l varr * r 213
209l * * l *
224r N * r 228
224r * * r *
200r N * r 204
200r * * r *
232l varr * r 236
232l * * l *
248r P * r 252
248r * * r *
249r P * r 253
249r * * r *
264r V * r 268
264l V * r 268
264l * * l *
250r P * r 254
250r * * r *
272r P * r 276
272r * * r *
122l N * r 128
122l * * l *
>>> directions
{240: {'r', 'l'}, 116: {'l'}, 241: {'r', 'l'}, 130: {'r'}, 138: {'l'}, 146: {'r', 'l'}, 168: {'r', 'l'}, 169: {'r'}, 201: {'r'}, 160: {'r'}, 108: {'r'}, 176: {'r'}, 177: {'r'}, 184: {'r', 'l'}, 185: {'r', 'l'}, 192: {'r'}, 193: {'r'}, 152: {'l'}, 153: {'l'}, 208: {'l'}, 209: {'l'}, 224: {'r'}, 200: {'r'}, 232: {'l'}, 248: {'r'}, 249: {'r'}, 264: {'r', 'l'}, 250: {'r'}, 272: {'r'}, 122: {'l'}}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112
112 1' 1' r 112
112 varr varr l 116l
120 0 1 r 120
120 1 0 r 120
120 0' 1 r 120
120 1' 0 r 120
120 N * r 240r
121 0 0 r 121
121 1 1 r 120
121 0' 0 r 121
121 1' 1 r 120
121 N * r 241r
126 0 0 r 126
126 1 1 r 126
126 0' 0 r 126
126 1' 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 0' 1 r 126
127 1' 0 r 127
127 P P * 13
128 0 0 r 127
128 1 1 r 127
128 0' 0 r 127
128 1' 1 r 127
128 P P r 130r
134 0 1 r 134
134 1 0 r 134
134 0' 1 r 134
134 1' 0 r 134
134 varr varr l 138l
142 0 0 r 142
142 1 0 r 142
142 0' 0 r 142
142 1' 0 r 142
142 V V r 146r
150 0 0 r 150
150 1 0 r 151
150 0' 0 r 150
150 1' 0 r 151
150 V V r 168r
151 0 1 r 150
151 1 1 r 151
151 0' 1 r 150
151 1' 1 r 151
151 V V r 169r
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156
156 1' 1' l 156
156 V V r 160r
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157
157 1' 1' l 157
157 V V r 160r
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172
172 1' 1' l 172
172 varr varr r 184r
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173
173 1' 1' l 173
173 varr varr r 185r
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180
180 1' 1' l 180
180 N N l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181
181 1' 1' l 181
181 N N l 185l
188 0 0 r 188
188 1 1 r 188
188 0' 0 r 188
188 1' 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 0' 0 r 189
189 1' 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 0' 0 r 196
196 1' 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 0' 0 r 197
197 1' 1 r 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204
204 1' 1' r 204
204 P P r 224r
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205
205 1' 1' r 205
205 P P r 224r
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212
212 1' 1' r 212
212 V V r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213
213 1' 1' r 213
213 V V r 224r
228 0 0 r 228
228 1 1 r 228
228 0' 0 r 228
228 1' 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 0' 0 r 236
236 1' 1 r 236
236 V V r 146r
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244
244 1' 1' r 244
244 N * r 264r
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245
245 1' 1' r 245
245 N * r 264r
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252
252 1' 1' r 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253
253 1' 1' r 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254
254 1' 1' r 254
254 S S l 264l
268 0 0 r 268
268 1 1 r 268
268 0' 0 r 268
268 1' 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 0' 0 r 276
276 1' 1 r 276
276 S S l 122l
240l V * r 244
240l * * l *
240r V * r 244
240r * * r *
116l V * r 121
116l * * l *
241l V * r 245
241l * * l *
241r V * r 245
241r * * r *
130r S * r 134
130r * * r *
138l varr * r 142
138l * * l *
146l varr * r 151
146l * * l *
146r varr * r 151
146r * * r *
168l V * l 172
168l * * l *
168r V * l 172
168r * * r *
169r V * l 173
169r * * r *
201r N * r 205
201r * * r *
160r V * r 164
160r * * r *
108r S * r 112
108r * * r *
176r P * l 180
176r * * r *
177r P * l 181
177r * * r *
184l varr * r 188
184l * * l *
184r varr * r 188
184r * * r *
185l varr * r 189
185l * * l *
185r varr * r 189
185r * * r *
192r N * r 196
192r * * r *
193r N * r 197
193r * * r *
152l N * l 156
152l * * l *
153l N * l 157
153l * * l *
208l varr * r 212
208l * * l *
209l varr * r 213
209l * * l *
224r N * r 228
224r * * r *
200r N * r 204
200r * * r *
232l varr * r 236
232l * * l *
248r P * r 252
248r * * r *
249r P * r 253
249r * * r *
264l V * r 268
264l * * l *
264r V * r 268
264r * * r *
250r P * r 254
250r * * r *
272r P * r 276
272r * * r *
122l N * r 128
122l * * l *
>>> quasis[142]
State(step=73, acc=0, transitions={'0': ['0', 0, 142], '1': ['0', 0, 142], "0'": ['0', 0, 142], "1'": ['0', 0, 142], Sym('varr'+1): [Sym('varr'+1), 0, 146]}, direction=1)
>>> quasis[146]
State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
>>> k,quasi in 142,quasis[142]
Traceback (most recent call last):
  File "<pyshell#720>", line 1, in <module>
    k,quasi in 142,quasis[142]
NameError: name 'k' is not defined
>>> k,quasi = 142,quasis[142]
>>> k in used_states and type(quasi)==State
True
>>> step = quasis[quasi.step]
>>> step.is_found
True
>>> symbol = Sym('varr'+1)
Traceback (most recent call last):
  File "<pyshell#725>", line 1, in <module>
    symbol = Sym('varr'+1)
NameError: name 'Sym' is not defined
>>> symbol = Symbol('varr',+1)
>>> transition = quasi.transitions[symbol]
>>> if type(quasis[transition[2]])==State:
                        step2 = quasis[quasis[transition[2]].step]
                        if step2.is_found:
                            direction = quasi.direction
                        else:
                            direction = order.index(step2.variable) - order.index(step.variable)
                        direction = 'l' if direction<0 else 'r'
                    else:
                        direction = '*'
                        
SyntaxError: unindent does not match any outer indentation level
>>> if type(quasis[transition[2]])==State:
	step2 = quasis[quasis[transition[2]].step]
	if step2.is_found:
		direction = quasi.direction
	else:
		direction = order.index(step2.variable) - order.index(step.variable)
	direction = 'l' if direction<0 else 'r'
else:
	direction = '*'

	
>>> direction
'r'
>>> step2 = quasis[quasis[transition[2]].step]
>>> step2
Step(instruction=17, is_found=False, variable='varr', next_quasis=[75], direction=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#734>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 632, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 665, in print_founds
    direction = 'l' if direction<0 else 'r'
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' 1 112
112 1' 1' 1 112
112 varr varr l 116l
120 0 1 1 120
120 1 0 1 120
120 0' 1 1 120
120 1' 0 1 120
120 N N l 240l
121 0 0 1 121
121 1 1 1 120
121 0' 0 1 121
121 1' 1 1 120
121 N * l 241l
126 0 0 1 126
126 1 1 1 126
126 0' 0 1 126
126 1' 1 1 126
126 P P r 130r
127 0 1 1 126
127 1 0 1 127
127 0' 1 1 126
127 1' 0 1 127
127 P P * 13
128 0 0 1 127
128 1 1 1 127
128 0' 0 1 127
128 1' 1 1 127
128 P * r 130r
134 0 1 1 134
134 1 0 1 134
134 0' 1 1 134
134 1' 0 1 134
134 varr varr l 138l
142 0 0 1 142
142 1 0 1 142
142 0' 0 1 142
142 1' 0 1 142
142 V V l 146l
150 0 0 1 150
150 1 0 1 151
150 0' 0 1 150
150 1' 0 1 151
150 V * l 168l
151 0 1 1 150
151 1 1 1 151
151 0' 1 1 150
151 1' 1 1 151
151 V * l 169l
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' -1 156
156 1' 1' -1 156
156 V V * 160*
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' -1 157
157 1' 1' -1 157
157 V * * 160*
164 0 0 1 164
164 1 1 1 164
164 0' 0 1 164
164 1' 1 1 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' -1 172
172 1' 1' -1 172
172 varr varr * 184*
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' -1 173
173 1' 1' -1 173
173 varr varr * 185*
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' -1 180
180 1' 1' -1 180
180 N * l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' -1 181
181 1' 1' -1 181
181 N * l 185l
188 0 0 1 188
188 1 1 1 188
188 0' 0 1 188
188 1' 1 1 188
188 V V r 192r
189 0 0 1 189
189 1 1 1 189
189 0' 0 1 189
189 1' 1 1 189
189 V V r 193r
196 0 0 1 196
196 1 1 1 196
196 0' 0 1 196
196 1' 1 1 196
196 P P l 152l
197 0 0 1 197
197 1 1 1 197
197 0' 0 1 197
197 1' 1 1 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' 1 204
204 1' 1' 1 204
204 P P l 224l
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' 1 205
205 1' 1' 1 205
205 P P l 224l
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' 1 212
212 1' 1' 1 212
212 V * r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' 1 213
213 1' 1' 1 213
213 V * r 224r
228 0 0 1 228
228 1 1 1 228
228 0' 0 1 228
228 1' 1 1 228
228 P P l 232l
236 0 0 1 236
236 1 1 1 236
236 0' 0 1 236
236 1' 1 1 236
236 V V l 146l
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' 1 244
244 1' 1' 1 244
244 N * l 264l
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' 1 245
245 1' 1' 1 245
245 N N l 264l
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' 1 252
252 1' 1' 1 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' 1 253
253 1' 1' 1 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' 1 254
254 1' 1' 1 254
254 S S l 264l
268 0 0 1 268
268 1 1 1 268
268 0' 0 1 268
268 1' 1 1 268
268 N N r 272r
276 0 0 1 276
276 1 1 1 276
276 0' 0 1 276
276 1' 1 1 276
276 S S l 122l
240l V * r 244
240l * * l *
116l V * r 121
116l * * l *
241l V * r 245
241l * * l *
130r S * r 134
130r * * r *
138l varr * r 142
138l * * l *
146l varr * r 151
146l * * l *
168l V * l 172
168l * * l *
169l V * l 173
169l * * l *
201r N * r 205
201r * * r *
160* V * r 164
160* * * * *
108r S * r 112
108r * * r *
176r P * l 180
176r * * r *
177r P * l 181
177r * * r *
184* varr * r 188
184* * * * *
184l varr * r 188
184l * * l *
185* varr * r 189
185* * * * *
185l varr * r 189
185l * * l *
192r N * r 196
192r * * r *
193r N * r 197
193r * * r *
152l N * l 156
152l * * Traceback (most recent call last):
  File "<pyshell#735>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 690, in print_searches
    print(str(search)+direction,'*','*',direction,'*')
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112
112 1' 1' r 112
112 varr varr l 116l
120 0 1 r 120
120 1 0 r 120
120 0' 1 r 120
120 1' 0 r 120
120 N * l 240l
121 0 0 r 121
121 1 1 r 120
121 0' 0 r 121
121 1' 1 r 120
121 N * l 241l
126 0 0 r 126
126 1 1 r 126
126 0' 0 r 126
126 1' 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 0' 1 r 126
127 1' 0 r 127
127 P * * 13
128 0 0 r 127
128 1 1 r 127
128 0' 0 r 127
128 1' 1 r 127
128 P * r 130r
134 0 1 r 134
134 1 0 r 134
134 0' 1 r 134
134 1' 0 r 134
134 varr varr l 138l
142 0 0 r 142
142 1 0 r 142
142 0' 0 r 142
142 1' 0 r 142
142 V V l 146l
150 0 0 r 150
150 1 0 r 151
150 0' 0 r 150
150 1' 0 r 151
150 V * l 168l
151 0 1 r 150
151 1 1 r 151
151 0' 1 r 150
151 1' 1 r 151
151 V * l 169l
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156
156 1' 1' l 156
156 V V * 160*
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157
157 1' 1' l 157
157 V * * 160*
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172
172 1' 1' l 172
172 varr varr * 184*
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173
173 1' 1' l 173
173 varr varr * 185*
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180
180 1' 1' l 180
180 N * l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181
181 1' 1' l 181
181 N N l 185l
188 0 0 r 188
188 1 1 r 188
188 0' 0 r 188
188 1' 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 0' 0 r 189
189 1' 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 0' 0 r 196
196 1' 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 0' 0 r 197
197 1' 1 r 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204
204 1' 1' r 204
204 P * l 224l
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205
205 1' 1' r 205
205 P * l 224l
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212
212 1' 1' r 212
212 V V r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213
213 1' 1' r 213
213 V V r 224r
228 0 0 r 228
228 1 1 r 228
228 0' 0 r 228
228 1' 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 0' 0 r 236
236 1' 1 r 236
236 V V l 146l
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244
244 1' 1' r 244
244 N * l 264l
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245
245 1' 1' r 245
245 N * l 264l
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252
252 1' 1' r 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253
253 1' 1' r 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254
254 1' 1' r 254
254 S S l 264l
268 0 0 r 268
268 1 1 r 268
268 0' 0 r 268
268 1' 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 0' 0 r 276
276 1' 1 r 276
276 S S l 122l
240l V * r 244
240l * * l *
116l V * r 121
116l * * l *
241l V * r 245
241l * * l *
130r S * r 134
130r * * r *
138l varr * r 142
138l * * l *
146l varr * r 151
146l * * l *
168l V * l 172
168l * * l *
169l V * l 173
169l * * l *
201r N * r 205
201r * * r *
160* V * r 164
160* * * * *
108r S * r 112
108r * * r *
176r P * l 180
176r * * r *
177r P * l 181
177r * * r *
184l varr * r 188
184l * * l *
184* varr * r 188
184* * * * *
185l varr * r 189
185l * * l *
185* varr * r 189
185* * * * *
192r N * r 196
192r * * r *
193r N * r 197
193r * * r *
152l N * l 156
152l * * l *
153l N * l 157
153l * * l *
208l varr * r 212
208l * * l *
209l varr * r 213
209l * * l *
224r N * r 228
224r * * r *
224l N * r 228
224l * * l *
200r N * r 204
200r * * r *
232l varr * r 236
232l * * l *
248r P * r 252
248r * * r *
249r P * r 253
249r * * r *
264l V * r 268
264l * * l *
250r P * r 254
250r * * r *
272r P * r 276
272r * * r *
122l N * r 128
122l * * l *
>>> quasis[80]
Step(instruction=30, is_found=False, variable='varr', next_quasis=[81], direction=None)
>>> quasis[81]
Step(instruction=30, is_found=True, variable='varr', next_quasis=[82, 84], direction=None)
>>> quasis[30]
Instruction(LOADNEXTBIG, vard=varr, next_quasis=[82, 84])
>>> quasis[:40]
[End(is_start=True, next_quasis=[138]), None, FunctionCall(command='RECP', args=['V', 'varr', 'N'], next_quasis=[15]), Instruction(LOAD, vard=S, next_quasis=[4, 66]), Instruction(BRANCH, next_quasis=[98, 66, 66, 66]), Instruction(COMPs, vard=V, next_quasis=[98]), None, FunctionCall(command='ADDs', args=['P', 'V'], next_quasis=[53]), Instruction(ADDIs, vard=N, imm=2, next_quasis=[9]), Instruction(BRANCH, next_quasis=[70, 13, 70, 70]), Instruction(NOTs, vard=S, next_quasis=[11]), Instruction(JUMP, next_quasis=[72]), None, End(is_start=False, next_quasis=None), End(is_start=True, next_quasis=[138]), Instruction(ZEROs, vard=varr, next_quasis=[74]), None, Instruction(SLLs, vard=varr, imm=1, next_quasis=[80]), FunctionCall(command='SLT', args=['varr', 'N'], next_quasis=[30]), Instruction(MAP, map={(0,): (0, 1), (1,): (1, 0), (3,): (0, 1)}, next_quasis=[0]), Instruction(STORENEXTBIG, vard=V, next_quasis=[21, 78]), Instruction(BRANCH, next_quasis=[88, 74, 88, 88]), None, FunctionCall(command='SUBs', args=['varr', 'N'], next_quasis=[40]), Instruction(JUMP, next_quasis=[74]), None, Instruction(UNREAD, vard=V, next_quasis=[64]), End(is_start=False, next_quasis=[64]), End(is_start=True, next_quasis=[168]), None, Instruction(LOADNEXTBIG, vard=varr, next_quasis=[82, 84]), Instruction(LOADNEXTBIG, vard=N, next_quasis=[32, 84]), Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[33]), Instruction(BRANCH, next_quasis=[80, 84, 84, 84]), None, Instruction(UNREAD, vard=varr, next_quasis=[86]), Instruction(UNREAD, vard=N, next_quasis=[76]), End(is_start=False, next_quasis=[76]), End(is_start=True, next_quasis=[200]), None]
>>> quasis[15]
Instruction(ZEROs, vard=varr, next_quasis=[74])
>>> quasis[17]
Instruction(SLLs, vard=varr, imm=1, next_quasis=[80])
>>> quasis[72]
Step(instruction=15, is_found=False, variable='varr', next_quasis=[73], direction=None)
>>> quasis[15]
Instruction(ZEROs, vard=varr, next_quasis=[74])
>>> quasis[146]
State(step=74, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 1, 151]}, direction=None)
>>> quasis[74]
Step(instruction=17, is_found=False, variable='varr', next_quasis=[75], direction=None)
>>> quasis[17]
Instruction(SLLs, vard=varr, imm=1, next_quasis=[80])
>>> quasis[151]
State(step=75, acc=1, transitions={'0': ['1', 0, 150], '1': ['1', 1, 151], "0'": ['1', 0, 150], "1'": ['1', 1, 151], Sym('varr'+1): [None, 1, 169]}, direction=1)
>>> quasis[75]
Step(instruction=17, is_found=True, variable='varr', next_quasis=[80], direction=None)
>>> quasis[17]
Instruction(SLLs, vard=varr, imm=1, next_quasis=[80])
>>> quasis[150]
State(step=75, acc=0, transitions={'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}, direction=1)
>>> quasis[168]
State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
>>> quasis[80]
Step(instruction=30, is_found=False, variable='varr', next_quasis=[81], direction=None)
>>> quasis[30]
Instruction(LOADNEXTBIG, vard=varr, next_quasis=[82, 84])
>>> directions[168]
{'l'}
>>> k,quasi = 150,quasis[150]
>>> k in used_states and type(quasi)==State
True
>>> step = quasis[quasi.step]
>>> step.is_found
True
>>> quasi.transitions
{'0': ['0', 0, 150], '1': ['0', 1, 151], "0'": ['0', 0, 150], "1'": ['0', 1, 151], Sym('varr'+1): [None, 0, 168]}
>>> symbol=Sym('varr'+1)
Traceback (most recent call last):
  File "<pyshell#761>", line 1, in <module>
    symbol=Sym('varr'+1)
NameError: name 'Sym' is not defined
>>> symbol=Symbol('varr',+1)
>>> transition = quasi.transitions[symbol]
>>> type(quasis[transition[2]])==State
True
>>> step2 = quasis[quasis[transition[2]].step]
>>> step2.is_found
False
>>> next_var = order.index(step2.variable)
>>> next_var
0
>>> step2
Step(instruction=30, is_found=False, variable='varr', next_quasis=[81], direction=None)
>>> quasis[transition[2]]
State(step=80, acc=0, transitions={Sym('varr'+1): [Sym('varr'+1), 0, 172]}, direction=None)
>>> quasi2 = quasis[transition[2]]
>>> list(quasi2.transitions.keys())[0]
Sym('varr'+1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 0' 0' r 112
112 1' 1' r 112
112 varr varr l 116l
120 0 1 r 120
120 1 0 r 120
120 0' 1 r 120
120 1' 0 r 120
120 N N l 240l
121 0 0 r 121
121 1 1 r 120
121 0' 0 r 121
121 1' 1 r 120
121 N N l 241l
126 0 0 r 126
126 1 1 r 126
126 0' 0 r 126
126 1' 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 0' 1 r 126
127 1' 0 r 127
127 P * * 13
128 0 0 r 127
128 1 1 r 127
128 0' 0 r 127
128 1' 1 r 127
128 P * r 130r
134 0 1 r 134
134 1 0 r 134
134 0' 1 r 134
134 1' 0 r 134
134 varr varr l 138l
142 0 0 r 142
142 1 0 r 142
142 0' 0 r 142
142 1' 0 r 142
142 V V l 146l
150 0 0 r 150
150 1 0 r 151
150 0' 0 r 150
150 1' 0 r 151
150 V * * 168*
151 0 1 r 150
151 1 1 r 151
151 0' 1 r 150
151 1' 1 r 151
151 V * * 169*
156 0 0' r 201r
156 1 0' r 201r
156 0' 0' l 156
156 1' 1' l 156
156 V V * 160*
157 0 1' l 146l
157 1 1' l 146l
157 0' 0' l 157
157 1' 1' l 157
157 V V * 160*
164 0 0 r 164
164 1 1 r 164
164 0' 0 r 164
164 1' 1 r 164
164 N N r 108r
172 0 0' r 176r
172 1 1' r 177r
172 0' 0' l 172
172 1' 1' l 172
172 varr varr * 184*
173 0 0' r 176r
173 1 1' r 177r
173 0' 0' l 173
173 1' 1' l 173
173 varr varr * 185*
180 0 0' l 168l
180 1 1' l 185l
180 0' 0' l 180
180 1' 1' l 180
180 N * l 184l
181 0 0' l 184l
181 1 1' l 168l
181 0' 0' l 181
181 1' 1' l 181
181 N * l 185l
188 0 0 r 188
188 1 1 r 188
188 0' 0 r 188
188 1' 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 0' 0 r 189
189 1' 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 0' 0 r 196
196 1' 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 0' 0 r 197
197 1' 1 r 197
197 P P l 153l
204 0 0' l 208l
204 1 1' l 209l
204 0' 0' r 204
204 1' 1' r 204
204 P P l 224l
205 0 0' l 209l
205 1 1' l 209l
205 0' 0' r 205
205 1' 1' r 205
205 P P l 224l
212 0 0' r 200r
212 1 1' r 201r
212 0' 0' r 212
212 1' 1' r 212
212 V V r 224r
213 0 0' r 201r
213 1 0' r 200r
213 0' 0' r 213
213 1' 1' r 213
213 V V r 224r
228 0 0 r 228
228 1 1 r 228
228 0' 0 r 228
228 1' 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 0' 0 r 236
236 1' 1 r 236
236 V V l 146l
244 0 0' r 248r
244 1 1' r 249r
244 0' 0' r 244
244 1' 1' r 244
244 N N l 264l
245 0 0' r 249r
245 1 1' r 250r
245 0' 0' r 245
245 1' 1' r 245
245 N N l 264l
252 0 0' l 240l
252 1 0' l 241l
252 0' 0' r 252
252 1' 1' r 252
252 S S l 264l
253 0 0' l 241l
253 1 1' l 240l
253 0' 0' r 253
253 1' 1' r 253
253 S S l 264l
254 0 1' l 240l
254 1 1' l 241l
254 0' 0' r 254
254 1' 1' r 254
254 S S l 264l
268 0 0 r 268
268 1 1 r 268
268 0' 0 r 268
268 1' 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 0' 0 r 276
276 1' 1 r 276
276 S S l 122l
240l V * r 244
240l * * l *
116l V * r 121
116l * * l *
241l V * r 245
241l * * l *
130r S * r 134
130r * * r *
138l varr * r 142
138l * * l *
146l varr * r 151
146l * * l *
168l V * l 172
168l * * l *
168* V * l 172
168* * * * *
169* V * l 173
169* * * * *
201r N * r 205
201r * * r *
160* V * r 164
160* * * * *
108r S * r 112
108r * * r *
176r P * l 180
176r * * r *
177r P * l 181
177r * * r *
184l varr * r 188
184l * * l *
184* varr * r 188
184* * * * *
185l varr * r 189
185l * * l *
185* varr * r 189
185* * * * *
192r N * r 196
192r * * r *
193r N * r 197
193r * * r *
152l N * l 156
152l * * l *
153l N * l 157
153l * * l *
208l varr * r 212
208l * * l *
209l varr * r 213
209l * * l *
224l N * r 228
224l * * l *
224r N * r 228
224r * * r *
200r N * r 204
200r * * r *
232l varr * r 236
232l * * l *
248r P * r 252
248r * * r *
249r P * r 253
249r * * r *
264l V * r 268
264l * * l *
250r P * r 254
250r * * r *
272r P * r 276
272r * * r *
122l N * r 128
122l * * l *
>>> bin(255//1)
'0b11111111'
>>> bin(255//3)
'0b1010101'
>>> bin(255//5)
'0b110011'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('RECP V r N')
67 0 0 r 67
67 1 0 r 67
67 0' 0 r 67
67 1' 0 r 67
Traceback (most recent call last):
  File "<pyshell#777>", line 1, in <module>
    compile_function('RECP V r N')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 632, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 655, in print_founds
    next_var = order.index(symbol2.symbol)+symbol2.offset
ValueError: 'r' is not in list
>>> compile_function('RECP V varr N')
Traceback (most recent call last):
  File "<pyshell#778>", line 1, in <module>
    compile_function('RECP V varr N')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 615, in compile_function
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 329, in remove_ends
    if type(quasi2)!=Instruction and quasi2.next_quasis:
AttributeError: 'State' object has no attribute 'next_quasis'
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('RECP V varr N')
67 0 0 r 67
67 1 0 r 67
67 0' 0 r 67
67 1' 0 r 67
67 V V l 71l
75 0 0 r 75
75 1 0 r 76
75 0' 0 r 75
75 1' 0 r 76
75 V V * 93*
76 0 1 r 75
76 1 1 r 76
76 0' 1 r 75
76 1' 1 r 76
76 V * * 94*
81 0 0' r 126r
81 1 0' r 126r
81 0' 0' l 81
81 1' 1' l 81
81 V V * 85*
82 0 1' l 71l
82 1 1' l 71l
82 0' 0' l 82
82 1' 1' l 82
82 V * * 85*
89 0 0 r 89
89 1 1 r 89
89 0' 0 r 89
89 1' 1 r 89
89 N N * 13
97 0 0' r 101r
97 1 1' r 102r
97 0' 0' l 97
97 1' 1' l 97
97 varr varr * 109*
98 0 0' r 101r
98 1 1' r 102r
98 0' 0' l 98
98 1' 1' l 98
98 varr varr * 110*
105 0 0' l 93l
105 1 1' l 110l
105 0' 0' l 105
105 1' 1' l 105
105 N * l 109l
106 0 0' l 109l
106 1 1' l 93l
106 0' 0' l 106
106 1' 1' l 106
106 N * l 110l
113 0 0 r 113
113 1 1 r 113
113 0' 0 r 113
113 1' 1 r 113
113 V V r 117r
114 0 0 r 114
114 1 1 r 114
114 0' 0 r 114
114 1' 1 r 114
114 V V r 118r
121 0 0 r 121
121 1 1 r 121
121 0' 0 r 121
121 1' 1 r 121
121 P P l 77l
122 0 0 r 122
122 1 1 r 122
122 0' 0 r 122
122 1' 1 r 122
122 P P l 78l
129 0 0' l 133l
129 1 1' l 134l
129 0' 0' r 129
129 1' 1' r 129
129 P * l 149l
130 0 0' l 134l
130 1 1' l 134l
130 0' 0' r 130
130 1' 1' r 130
130 P * l 149l
137 0 0' r 125r
137 1 1' r 126r
137 0' 0' r 137
137 1' 1' r 137
137 V V r 149r
138 0 0' r 126r
138 1 0' r 125r
138 0' 0' r 138
138 1' 1' r 138
138 V V r 149r
153 0 0 r 153
153 1 1 r 153
153 0' 0 r 153
153 1' 1 r 153
153 P P l 157l
161 0 0 r 161
161 1 1 r 161
161 0' 0 r 161
161 1' 1 r 161
161 V V l 71l
71l varr * r 76
71l * * l *
93l V * l 97
93l * * l *
93* V * l 97
93* * * * *
94* V * l 98
94* * * * *
126r N * r 130
126r * * r *
85* V * r 89
85* * * * *
101r P * l 105
101r * * r *
102r P * l 106
102r * * r *
109l varr * r 113
109l * * l *
109* varr * r 113
109* * * * *
110l varr * r 114
110l * * l *
110* varr * r 114
110* * * * *
117r N * r 121
117r * * r *
118r N * r 122
118r * * r *
77l N * l 81
77l * * l *
78l N * l 82
78l * * l *
133l varr * r 137
133l * * l *
134l varr * r 138
134l * * l *
149r N * r 153
149r * * r *
149l N * r 153
149l * * l *
125r N * r 129
125r * * r *
157l varr * r 161
157l * * l *
>>> order
['varr', 'V', 'N', 'P', 'S']
>>> quasis[0]
End(is_start=True, next_quasis=[63])
>>> quasis[63]
State(step=37, acc=0, transitions={Sym('varr'+0): [Sym('varr'+0), 0, 67]}, direction=None)
>>> used_states
{0, 129, 130, 133, 134, 137, 138, 13, 149, 153, 157, 161, 63, 67, 71, 75, 76, 77, 78, 81, 82, 85, 89, 93, 94, 97, 98, 101, 102, 105, 106, 109, 110, 113, 114, 117, 118, 121, 122, 125, 126}
>>> quasis[82]
State(step=42, acc=1, transitions={'0': ["1'", 0, 71], '1': ["1'", 0, 71], "0'": ["0'", 1, 82], "1'": ["1'", 1, 82], Sym('V'+0): [None, 1, 85]}, direction=-1)
>>> quasis[42]
Step(instruction=6, is_found=True, variable='V', next_quasis=[7, 43], direction=None)
>>> quasis[6]
Instruction(STORENEXTBIG, vard=V, next_quasis=[7, 43])
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order = ['A','B']
>>> compile_function('SLT A B')
22 0 0' r 26r
22 1 1' r 27r
22 0' 0' l 22
22 1' 1' l 22
22 A A * 34*
30 0 0' l 18l
30 1 1' l 34l
30 0' 0' l 30
30 1' 1' l 30
30 B B l 34l
31 0 0' l 34l
31 1 1' l 18l
31 0' 0' l 31
31 1' 1' l 31
31 B B l 34l
38 0 0 r 38
38 1 1 r 38
38 0' 0 r 38
38 1' 1 r 38
38 B B * 42*
46 0 0 r 46
46 1 1 r 46
46 0' 0 r 46
46 1' 1 r 46
46 A A * 9
26r A * l 30
26r * * r *
27r A * l 31
27r * * r *
34* A * r 38
34* * * * *
34l A * r 38
34l * * l *
18l B * l 22
18l * * l *
42* B * r 46
42* * * * *
>>> quasis[0]
End(is_start=True, next_quasis=[18])
>>> quasis[18]
State(step=10, acc=0, transitions={Sym('A'+1): [Sym('A'+1), 0, 22]}, direction=None)
>>> quasis[:10]
[End(is_start=True, next_quasis=[18]), None, Instruction(LOADNEXTBIG, vard=A, next_quasis=[12, 14]), Instruction(LOADNEXTBIG, vard=B, next_quasis=[4, 14]), Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (3,), (1, 1): (0,)}, next_quasis=[5]), Instruction(BRANCH, next_quasis=[10, 14, 14, 14]), None, Instruction(UNREAD, vard=A, next_quasis=[16]), Instruction(UNREAD, vard=B, next_quasis=[9]), End(is_start=False, next_quasis=None)]
>>> quasis[9]
End(is_start=False, next_quasis=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('ADD A B C')
Traceback (most recent call last):
  File "<pyshell#793>", line 1, in <module>
    compile_function('ADD A B C')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 632, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 667, in print_founds
    next_var = order.index(symbol2.symbol)+symbol2.offset
ValueError: 'C' is not in list
>>> order = ['A','B','C']
>>> compile_function('ADD A B C')
Traceback (most recent call last):
  File "<pyshell#795>", line 1, in <module>
    compile_function('ADD A B C')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 615, in compile_function
    more_ends = remove_ends()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 329, in remove_ends
    if type(quasi2)!=Instruction and quasi2.next_quasis:
AttributeError: 'State' object has no attribute 'next_quasis'
>>> len(quasis)
88
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[26])
1 None
2 Instruction(LOADNEXT, vard=B, next_quasis=[3, 20])
3 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[16])
4 Instruction(LOADNEXT, vard=C, next_quasis=[5, 20])
5 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[18])
6 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[0])
7 Instruction(STORENEXT, vard=A, next_quasis=[8, 20])
8 Instruction(JUMP, next_quasis=[14])
9 None
10 Instruction(UNREAD, vard=B, next_quasis=[22])
11 Instruction(UNREAD, vard=C, next_quasis=[24])
12 Instruction(UNREAD, vard=A, next_quasis=[13])
13 End(is_start=False, next_quasis=None)
14 Step(instruction=2, is_found=False, variable='B', next_quasis=[15], direction=None)
15 Step(instruction=2, is_found=True, variable='B', next_quasis=[3, 20], direction=None)
16 Step(instruction=4, is_found=False, variable='C', next_quasis=[17], direction=None)
17 Step(instruction=4, is_found=True, variable='C', next_quasis=[5, 20], direction=None)
18 Step(instruction=7, is_found=False, variable='A', next_quasis=[19], direction=None)
19 Step(instruction=7, is_found=True, variable='A', next_quasis=[8, 20], direction=None)
20 Step(instruction=10, is_found=False, variable='B', next_quasis=[21], direction=None)
21 Step(instruction=10, is_found=True, variable='B', next_quasis=[22], direction=None)
22 Step(instruction=11, is_found=False, variable='C', next_quasis=[23], direction=None)
23 Step(instruction=11, is_found=True, variable='C', next_quasis=[24], direction=None)
24 Step(instruction=12, is_found=False, variable='A', next_quasis=[25], direction=None)
25 Step(instruction=12, is_found=True, variable='A', next_quasis=[13], direction=None)
26 State(step=14, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 30]}, direction=None)
27 State(step=14, acc=1, transitions={Sym('B'+0): [Sym('B'+0), 1, 31]}, direction=None)
28 State(step=14, acc=2, transitions={Sym('B'+0): [Sym('B'+0), 2, 32]}, direction=None)
29 State(step=14, acc=3, transitions={Sym('B'+0): [Sym('B'+0), 3, 33]}, direction=None)
30 State(step=15, acc=0, transitions={'0': ["0'", 0, 34], '1': ["1'", 1, 35], "0'": ["0'", 0, 30], "1'": ["1'", 0, 30], Sym('B'+1): [None, 0, 50]}, direction=1)
31 State(step=15, acc=1, transitions={'0': ["0'", 1, 35], '1': ["1'", 2, 36], "0'": ["0'", 1, 31], "1'": ["1'", 1, 31], Sym('B'+1): [Sym('B'+1), 1, 50]}, direction=1)
32 State(step=15, acc=2, transitions={'0': ["0'", 2, 36], '1': ["1'", 2, 36], "0'": ["0'", 2, 32], "1'": ["1'", 2, 32], Sym('B'+1): [Sym('B'+1), 2, 50]}, direction=1)
33 State(step=15, acc=3, transitions={'0': ["0'", 3, 37], '1': ["1'", 3, 37], "0'": ["0'", 3, 33], "1'": ["1'", 3, 33], Sym('B'+1): [None, 3, 50]}, direction=1)
34 State(step=16, acc=0, transitions={Sym('C'+0): [Sym('C'+0), 0, 38]}, direction=None)
35 State(step=16, acc=1, transitions={Sym('C'+0): [Sym('C'+0), 1, 39]}, direction=None)
36 State(step=16, acc=2, transitions={Sym('C'+0): [Sym('C'+0), 2, 40]}, direction=None)
37 State(step=16, acc=3, transitions={Sym('C'+0): [Sym('C'+0), 3, 41]}, direction=None)
38 State(step=17, acc=0, transitions={'0': ["0'", 0, 42], '1': ["1'", 1, 43], "0'": ["0'", 0, 38], "1'": ["1'", 0, 38], Sym('C'+1): [None, 0, 50]}, direction=1)
39 State(step=17, acc=1, transitions={'0': ["0'", 1, 43], '1': ["1'", 2, 44], "0'": ["0'", 1, 39], "1'": ["1'", 1, 39], Sym('C'+1): [None, 1, 50]}, direction=1)
40 State(step=17, acc=2, transitions={'0': ["0'", 2, 44], '1': ["1'", 3, 45], "0'": ["0'", 2, 40], "1'": ["1'", 2, 40], Sym('C'+1): [Sym('C'+1), 2, 50]}, direction=1)
41 State(step=17, acc=3, transitions={'0': ["0'", 3, 45], '1': ["1'", 3, 45], "0'": ["0'", 3, 41], "1'": ["1'", 3, 41], Sym('C'+1): [Sym('C'+1), 3, 50]}, direction=1)
42 State(step=18, acc=0, transitions={Sym('A'+0): [Sym('A'+0), 0, 46]}, direction=None)
43 State(step=18, acc=1, transitions={Sym('A'+0): [Sym('A'+0), 1, 47]}, direction=None)
44 State(step=18, acc=2, transitions={Sym('A'+0): [Sym('A'+0), 2, 48]}, direction=None)
45 State(step=18, acc=3, transitions={Sym('A'+0): [Sym('A'+0), 3, 49]}, direction=None)
46 State(step=19, acc=0, transitions={'0': ["0'", 0, 26], '1': ["0'", 0, 26], "0'": ["0'", 0, 46], "1'": ["1'", 0, 46], Sym('A'+1): [Sym('A'+1), 0, 50]}, direction=1)
47 State(step=19, acc=1, transitions={'0': ["0'", 1, 27], '1': ["0'", 1, 27], "0'": ["0'", 1, 47], "1'": ["1'", 1, 47], Sym('A'+1): [Sym('A'+1), 1, 50]}, direction=1)
48 State(step=19, acc=2, transitions={'0': ["1'", 0, 26], '1': ["1'", 0, 26], "0'": ["0'", 2, 48], "1'": ["1'", 2, 48], Sym('A'+1): [Sym('A'+1), 2, 50]}, direction=1)
49 State(step=19, acc=3, transitions={'0': ["1'", 1, 27], '1': ["1'", 1, 27], "0'": ["0'", 3, 49], "1'": ["1'", 3, 49], Sym('A'+1): [Sym('A'+1), 3, 50]}, direction=1)
50 State(step=20, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 54]}, direction=None)
51 None
52 None
53 None
54 State(step=21, acc=0, transitions={'0': ['0', 0, 54], '1': ['1', 0, 54], "0'": ['0', 0, 54], "1'": ['1', 0, 54], Sym('B'+1): [Sym('B'+1), 0, 58]}, direction=1)
55 None
56 None
57 None
58 State(step=22, acc=0, transitions={Sym('C'+0): [Sym('C'+0), 0, 62]}, direction=None)
59 None
60 None
61 None
62 State(step=23, acc=0, transitions={'0': ['0', 0, 62], '1': ['1', 0, 62], "0'": ['0', 0, 62], "1'": ['1', 0, 62], Sym('C'+1): [Sym('C'+1), 0, 66]}, direction=1)
63 None
64 None
65 None
66 State(step=24, acc=0, transitions={Sym('A'+0): [Sym('A'+0), 0, 70]}, direction=None)
67 None
68 None
69 None
70 State(step=25, acc=0, transitions={'0': ['0', 0, 70], '1': ['1', 0, 70], "0'": ['0', 0, 70], "1'": ['1', 0, 70], Sym('A'+1): [Sym('A'+1), 0, 13]}, direction=1)
71 None
72 None
73 None
74 End(is_start=True, next_quasis=[76])
75 None
76 Instruction(LOADNEXT, vard=B, next_quasis=[77, 84])
77 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[78])
78 Instruction(LOADNEXT, vard=C, next_quasis=[79, 84])
79 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[80])
80 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[81])
81 Instruction(STORENEXT, vard=A, next_quasis=[82, 84])
82 Instruction(JUMP, next_quasis=[76])
83 None
84 Instruction(UNREAD, vard=B, next_quasis=[85])
85 Instruction(UNREAD, vard=C, next_quasis=[86])
86 Instruction(UNREAD, vard=A, next_quasis=[87])
87 End(is_start=False, next_quasis=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('ADD A B C')
Traceback (most recent call last):
  File "<pyshell#800>", line 1, in <module>
    compile_function('ADD A B C')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 668, in print_founds
    next_var = order.index(symbol2.symbol)+symbol2.offset
ValueError: 'C' is not in list
>>> order = ['A','B','C']
>>> quasis = []
>>> compile_function('ADD A B C')
30  2 r 34r
30  3 r 35r
30 2 2 r 30
30 3 3 r 30
30 C * l 50l
31  2 r 35r
31  3 r 36r
31 2 2 r 31
31 3 3 r 31
31 C C l 50l
38  2 l 42l
38  3 l 43l
38 2 2 r 38
38 3 3 r 38
38 A * l 50l
39  2 l 43l
39  3 l 44l
39 2 2 r 39
39 3 3 r 39
39 A * l 50l
40  2 l 44l
40  3 l 45l
40 2 2 r 40
40 3 3 r 40
40 A A l 50l
46  2 r 26r
46  2 r 26r
46 2 2 r 46
46 3 3 r 46
46 B * * 50*
47  2 r 27r
47  2 r 27r
47 2 2 r 47
47 3 3 r 47
47 B * * 50*
48  3 r 26r
48  3 r 26r
48 2 2 r 48
48 3 3 r 48
48 B * * 50*
49  3 r 27r
49  3 r 27r
49 2 2 r 49
49 3 3 r 49
49 B * * 50*
54   r 54
54   r 54
54 2  r 54
54 3  r 54
54 C C * 58*
62   r 62
62   r 62
62 2  r 62
62 3  r 62
62 A A l 66l
70   r 70
70   r 70
70 2  r 70
70 3  r 70
70 B B * 13
34r C * r 38
34r * * r *
35r C * r 39
35r * * r *
50l B * r 54
50l * * l *
50* B * r 54
50* * * * *
36r C * r 40
36r * * r *
42l A * r 46
42l * * l *
43l A * r 47
43l * * l *
44l A * r 48
44l * * l *
45l A * r 49
45l * * l *
26r B * r 30
26r * * r *
27r B * r 31
27r * * r *
58* C * r 62
58* * * * *
66l A * r 70
66l * * l *
>>> quasis[0]
End(is_start=True, next_quasis=[26])
>>> quasis[26]
State(step=14, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 30]}, direction=None)
>>> quasis[70]
State(step=25, acc=0, transitions={'0': ['0', 0, 70], '1': ['1', 0, 70], "0'": ['0', 0, 70], "1'": ['1', 0, 70], Sym('A'+1): [Sym('A'+1), 0, 13]}, direction=1)
>>> to_char('0')
''
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order = ['A','B','C']
>>> compile_function('ADD A B C')
30 0 2 r 34r
30 1 3 r 35r
30 2 2 r 30
30 3 3 r 30
30 C * l 50l
31 0 2 r 35r
31 1 3 r 36r
31 2 2 r 31
31 3 3 r 31
31 C * l 50l
38 0 2 l 42l
38 1 3 l 43l
38 2 2 r 38
38 3 3 r 38
38 A * l 50l
39 0 2 l 43l
39 1 3 l 44l
39 2 2 r 39
39 3 3 r 39
39 A * l 50l
40 0 2 l 44l
40 1 3 l 45l
40 2 2 r 40
40 3 3 r 40
40 A * l 50l
46 0 2 r 26r
46 1 2 r 26r
46 2 2 r 46
46 3 3 r 46
46 B * * 50*
47 0 2 r 27r
47 1 2 r 27r
47 2 2 r 47
47 3 3 r 47
47 B * * 50*
48 0 3 r 26r
48 1 3 r 26r
48 2 2 r 48
48 3 3 r 48
48 B * * 50*
49 0 3 r 27r
49 1 3 r 27r
49 2 2 r 49
49 3 3 r 49
49 B * * 50*
54 0 0 r 54
54 1 1 r 54
54 2 0 r 54
54 3 1 r 54
54 C C * 58*
62 0 0 r 62
62 1 1 r 62
62 2 0 r 62
62 3 1 r 62
62 A A l 66l
70 0 0 r 70
70 1 1 r 70
70 2 0 r 70
70 3 1 r 70
70 B B * 13
34r C * r 38
34r * * r *
35r C * r 39
35r * * r *
50l B * r 54
50l * * l *
50* B * r 54
50* * * * *
36r C * r 40
36r * * r *
42l A * r 46
42l * * l *
43l A * r 47
43l * * l *
44l A * r 48
44l * * l *
45l A * r 49
45l * * l *
26r B * r 30
26r * * r *
27r B * r 31
27r * * r *
58* C * r 62
58* * * * *
66l A * r 70
66l * * l *
>>> order = []
>>> compile_function('ADDs A B')
Traceback (most recent call last):
  File "<pyshell#811>", line 1, in <module>
    compile_function('ADDs A B')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 668, in print_founds
    next_var = order.index(symbol2.symbol)+symbol2.offset
ValueError: 'A' is not in list
>>> order = ['A','B']
>>> compile_function('ADDs A B')
27 0 2 l 31l
27 1 3 l 32l
27 2 2 r 27
27 3 3 r 27
27 A * l 47l
28 0 2 l 32l
28 1 3 l 33l
28 2 2 r 28
28 3 3 r 28
28 A * l 47l
35 0 2 r 23r
35 1 2 r 24r
35 2 2 r 35
35 3 3 r 35
35 B * * 47*
36 0 2 r 24r
36 1 3 r 23r
36 2 2 r 36
36 3 3 r 36
36 B * * 47*
37 0 3 r 23r
37 1 3 r 24r
37 2 2 r 37
37 3 3 r 37
37 B * * 47*
51 0 0 r 51
51 1 1 r 51
51 2 0 r 51
51 3 1 r 51
51 A A l 55l
59 0 0 r 59
59 1 1 r 59
59 2 0 r 59
59 3 1 r 59
59 B B * 12
31l A * r 35
31l * * l *
32l A * r 36
32l * * l *
47l B * r 51
47l * * l *
47* B * r 51
47* * * * *
33l A * r 37
33l * * l *
23r B * r 27
23r * * r *
24r B * r 28
24r * * r *
55l A * r 59
55l * * l *
>>> quasis[0]
End(is_start=True, next_quasis=[23])
>>> quasis[23]
State(step=13, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 27]}, direction=None)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('ADDs A B')
Traceback (most recent call last):
  File "<pyshell#816>", line 1, in <module>
    compile_function('ADDs A B')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 659, in print_founds
    add_initial()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 655, in add_initial
    next_var = order.index(symbol.symbol)+symbol.offset
ValueError: 'B' is not in list
>>> order = ['A','B']
>>> compile_function('ADDs A B')
27 0 2 l 31l
27 1 3 l 32l
27 2 2 r 27
27 3 3 r 27
27 A * l 47l
28 0 2 l 32l
28 1 3 l 33l
28 2 2 r 28
28 3 3 r 28
28 A * l 47l
35 0 2 r 23r
35 1 2 r 24r
35 2 2 r 35
35 3 3 r 35
35 B B * 47*
36 0 2 r 24r
36 1 3 r 23r
36 2 2 r 36
36 3 3 r 36
36 B B * 47*
37 0 3 r 23r
37 1 3 r 24r
37 2 2 r 37
37 3 3 r 37
37 B B * 47*
51 0 0 r 51
51 1 1 r 51
51 2 0 r 51
51 3 1 r 51
51 A A l 55l
59 0 0 r 59
59 1 1 r 59
59 2 0 r 59
59 3 1 r 59
59 B B * 12
23r B * r 27
23r * * r *
31l A * r 35
31l * * l *
32l A * r 36
32l * * l *
47* B * r 51
47* * * * *
47l B * r 51
47l * * l *
33l A * r 37
33l * * l *
24r B * r 28
24r * * r *
55l A * r 59
55l * * l *
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('ADDs A B')
Traceback (most recent call last):
  File "<pyshell#819>", line 1, in <module>
    compile_function('ADDs A B')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 659, in print_founds
    add_initial()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 655, in add_initial
    next_var = order.index(symbol.symbol)+symbol.offset
ValueError: 'B' is not in list
>>> order = ['A','B']
>>> compile_function('ADDs A B')
27 0 2 l 31l
27 1 3 l 32l
27 2 2 r 27
27 3 3 r 27
27 A A l 47l
28 0 2 l 32l
28 1 3 l 33l
28 2 2 r 28
28 3 3 r 28
28 A A l 47l
35 0 2 r 23r
35 1 2 r 24r
35 2 2 r 35
35 3 3 r 35
35 B B * 47*
36 0 2 r 24r
36 1 3 r 23r
36 2 2 r 36
36 3 3 r 36
36 B B * 47*
37 0 3 r 23r
37 1 3 r 24r
37 2 2 r 37
37 3 3 r 37
37 B B * 47*
51 0 0 r 51
51 1 1 r 51
51 2 0 r 51
51 3 1 r 51
51 A A l 55l
59 0 0 r 59
59 1 1 r 59
59 2 0 r 59
59 3 1 r 59
59 B B * halt
23r B * r 27
23r * * r *
31l A * r 35
31l * * l *
32l A * r 36
32l * * l *
47* B * r 51
47* * * * *
47l B * r 51
47l * * l *
33l A * r 37
33l * * l *
24r B * r 28
24r * * r *
55l A * r 59
55l * * l *
>>> compile_function('ADDIs A 3')
Traceback (most recent call last):
  File "<pyshell#822>", line 1, in <module>
    compile_function('ADDIs A 3')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 631, in compile_function
    find_successors(0)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 584, in find_successors
    if type(quasis[k])==End and quasis[k].next_quasis:
IndexError: list index out of range
>>> quasis=[]
>>> order=['A']
>>> compile_function('ADDIs A 3')
Traceback (most recent call last):
  File "<pyshell#825>", line 1, in <module>
    compile_function('ADDIs A 3')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 631, in compile_function
    find_successors(0)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 584, in find_successors
    if type(quasis[k])==End and quasis[k].next_quasis:
IndexError: list index out of range
>>> len(quasis)
0
>>> compile_function('TEST')
Traceback (most recent call last):
  File "<pyshell#827>", line 1, in <module>
    compile_function('TEST')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 631, in compile_function
    find_successors(0)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 584, in find_successors
    if type(quasis[k])==End and quasis[k].next_quasis:
IndexError: list index out of range
>>> len(quasis)
0
>>> function = LineParser.line.parse('TEST').value
>>> evaluate_function_call(function)
>>> len(quasis)
0
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> compile_function('TEST')
Traceback (most recent call last):
  File "<pyshell#832>", line 1, in <module>
    compile_function('TEST')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 633, in compile_function
    print_founds()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 659, in print_founds
    add_initial()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 655, in add_initial
    next_var = order.index(symbol.symbol)+symbol.offset
ValueError: 'A' is not in list
>>> order=['A']
>>> compile_function('TEST')
Traceback (most recent call last):
  File "<pyshell#834>", line 1, in <module>
    compile_function('TEST')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 618, in compile_function
    steps2states()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 434, in steps2states
    transitions,direction = get_found_transitions(k,acc)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 400, in get_found_transitions
    transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 400, in <dictcomp>
    transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
TypeError: unsupported operand type(s) for +: 'Symbol' and 'str'
>>> len(quasis)
9
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[3])
1 Instruction(ADDIs, vard=A, imm=3, next_quasis=[2])
2 End(is_start=False, next_quasis=None)
3 Step(instruction=1, is_found=False, variable='A', next_quasis=[4], direction=None)
4 Step(instruction=1, is_found=True, variable='A', next_quasis=[2], direction=None)
5 State(step=3, acc=0, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
6 State(step=3, acc=1, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
7 State(step=3, acc=2, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
8 State(step=3, acc=3, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
>>> quasis=[]
>>> compile_function('TEST')
Traceback (most recent call last):
  File "<pyshell#840>", line 1, in <module>
    compile_function('TEST')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 618, in compile_function
    steps2states()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 434, in steps2states
    transitions,direction = get_found_transitions(k,acc)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 400, in get_found_transitions
    transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 400, in <dictcomp>
    transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
TypeError: unsupported operand type(s) for +: 'Symbol' and 'str'
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[3])
1 Instruction(ADDIs, vard=A, imm=3, next_quasis=[2])
2 End(is_start=False, next_quasis=None)
3 Step(instruction=1, is_found=False, variable='A', next_quasis=[4], direction=None)
4 Step(instruction=1, is_found=True, variable='A', next_quasis=[2], direction=None)
5 State(step=3, acc=0, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
6 State(step=3, acc=1, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
7 State(step=3, acc=2, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
8 State(step=3, acc=3, transitions={Sym('A'+0): [None, 3, 4]}, direction=None)
>>> quasi = quasis[4]
>>> acc=0
>>> get_found_transitions(4,0)
Traceback (most recent call last):
  File "<pyshell#845>", line 1, in <module>
    get_found_transitions(4,0)
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 400, in get_found_transitions
    transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 400, in <dictcomp>
    transitions.update({symbol+'\'':transitions[symbol] for symbol in transitions})
TypeError: unsupported operand type(s) for +: 'Symbol' and 'str'
>>> transitions = more_transitions['ADDIs'][0]
>>> transitions
{'0': ['0', 0, 9, 4, 4, 4, 4, 4, 4], '1': ['1', 0, 9, 4, 4, 4, 4, 4, 4], "0'": ['0', 0, 9, 4, 4, 4, 4, 4, 4], "1'": ['1', 0, 9, 4, 4, 4, 4, 4, 4], Sym('A'+1): [None, 0, 2, 4, 4, 4]}
>>> transitions=[]
>>> transitions = more_transitions['ADDIs'][0]
>>> transitions
{'0': ['0', 0, 9, 4, 4, 4, 4, 4, 4], '1': ['1', 0, 9, 4, 4, 4, 4, 4, 4], "0'": ['0', 0, 9, 4, 4, 4, 4, 4, 4], "1'": ['1', 0, 9, 4, 4, 4, 4, 4, 4], Sym('A'+1): [None, 0, 2, 4, 4, 4]}
>>> more_transitions['ADDIs'][0]
{'0': ['0', 0, 9, 4, 4, 4, 4, 4, 4], '1': ['1', 0, 9, 4, 4, 4, 4, 4, 4], "0'": ['0', 0, 9, 4, 4, 4, 4, 4, 4], "1'": ['1', 0, 9, 4, 4, 4, 4, 4, 4], Sym('A'+1): [None, 0, 2, 4, 4, 4]}
>>> more_transitions
{'COMPs': {0: {'0': ['1', 0], '1': ['0', 0]}, 1: {'0': ['0', 1], '1': ['1', 0]}}, 'SLLs': {0: {'0': ['0', 0], '1': ['0', 1]}, 1: {'0': ['1', 0], '1': ['1', 1]}}, 'SRLs': {0: {'0': ['0', 0], '1': ['0', 1]}, 1: {'0': ['1', 0], '1': ['1', 1]}}, 'SLL2s': {0: {'0': ['0', 0], '1': ['0', 2]}, 1: {'0': ['1', 0], '1': ['1', 2]}, 2: {'0': ['0', 1], '1': ['0', 3]}, 3: {'0': ['1', 1], '1': ['1', 3]}}, 'SRL2s': {0: {'0': ['0', 0], '1': ['0', 1]}, 2: {'0': ['1', 0], '1': ['1', 1]}, 1: {'0': ['0', 2], '1': ['0', 3]}, 3: {'0': ['1', 2], '1': ['1', 3]}}, 'ADDIs': {0: {'0': ['0', 0, 9, 4, 4, 4, 4, 4, 4], '1': ['1', 0, 9, 4, 4, 4, 4, 4, 4], "0'": ['0', 0, 9, 4, 4, 4, 4, 4, 4], "1'": ['1', 0, 9, 4, 4, 4, 4, 4, 4], Sym('A'+1): [None, 0, 2, 4, 4, 4]}, 1: {'0': ['1', 0, 9], '1': ['0', 1, 10], "0'": ['1', 0, 9], "1'": ['0', 1, 10], Sym('A'+1): [None, 1, 2]}, 2: {'0': ['0', 1, 10], '1': ['1', 1, 10], "0'": ['0', 1, 10], "1'": ['1', 1, 10], Sym('A'+1): [None, 2, 2]}, 3: {'0': ['1', 1, 10], '1': ['0', 2, 11], "0'": ['1', 1, 10], "1'": ['0', 2, 11], Sym('A'+1): [None, 3, 2]}}, 'SUBIs': {0: {'0': ['0', 0], '1': ['1', 0]}, 1: {'0': ['1', 1], '1': ['0', 0]}, 2: {'0': ['0', 1], '1': ['1', 1]}, 3: {'0': ['1', 2], '1': ['0', 1]}}}
>>> transitions = {0:[1,2],3:[4,5]}
>>> t2 = transitions
>>> t2[3][1]+=100
>>> transitions
{0: [1, 2], 3: [4, 105]}
>>> t2 = {symbol:transitions[symbol] for symbol in transitions}
>>> t2
{0: [1, 2], 3: [4, 105]}
>>> transitions
{0: [1, 2], 3: [4, 105]}
>>> t2[3][1]+=100
>>> t2
{0: [1, 2], 3: [4, 205]}
>>> transitions
{0: [1, 2], 3: [4, 205]}
>>> t2 = {symbol:transitions[symbol][:] for symbol in transitions}
>>> t2
{0: [1, 2], 3: [4, 205]}
>>> transitions
{0: [1, 2], 3: [4, 205]}
>>> t2[3][1]+=100
>>> t2
{0: [1, 2], 3: [4, 305]}
>>> transitions
{0: [1, 2], 3: [4, 205]}
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order=['A']
>>> compile_function('TEST')
9 0 0 r 9
9 1 1 r 9
9 2 0 r 9
9 3 1 r 9
9 A A * halt
10 0 1 r 9
10 1 0 r 10
10 2 1 r 9
10 3 0 r 10
10 A A * halt
11 0 0 r 10
11 1 1 r 10
11 2 0 r 10
11 3 1 r 10
11 A A * halt
12 0 1 r 10
12 1 0 r 11
12 2 1 r 10
12 3 0 r 11
12 A A * halt
5* A * r 12
5* * * * *
>>> quasis[0]
End(is_start=True, next_quasis=[5])
>>> order = ['A','B']
>>> compile_function('ADDs A B')
27 0 2 l 31l
27 1 3 l 32l
27 2 2 r 27
27 3 3 r 27
27 A * l 47l
28 0 2 l 32l
28 1 3 l 33l
28 2 2 r 28
28 3 3 r 28
28 A A l 47l
35 0 2 r 23r
35 1 2 r 24r
35 2 2 r 35
35 3 3 r 35
35 B B * 47*
36 0 2 r 24r
36 1 3 r 23r
36 2 2 r 36
36 3 3 r 36
36 B B * 47*
37 0 3 r 23r
37 1 3 r 24r
37 2 2 r 37
37 3 3 r 37
37 B B * 47*
51 0 0 r 51
51 1 1 r 51
51 2 0 r 51
51 3 1 r 51
51 A A l 55l
59 0 0 r 59
59 1 1 r 59
59 2 0 r 59
59 3 1 r 59
59 B B * halt
23r B * r 27
23r * * r *
31l A * r 35
31l * * l *
32l A * r 36
32l * * l *
47l B * r 51
47l * * l *
47* B * r 51
47* * * * *
33l A * r 37
33l * * l *
24r B * r 28
24r * * r *
55l A * r 59
55l * * l *
>>> for k,quasi in quasis:
	if k in used_states:
		print(k,quasi)

		
Traceback (most recent call last):
  File "<pyshell#877>", line 1, in <module>
    for k,quasi in quasis:
TypeError: cannot unpack non-iterable End object
>>> for k,quasi in enumerate(quasis):
	if k in used_states:
		print(k,quasi)

		
0 End(is_start=True, next_quasis=[23])
12 End(is_start=False, next_quasis=None)
23 State(step=13, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 27]}, direction=None)
24 State(step=13, acc=1, transitions={Sym('B'+0): [Sym('B'+0), 1, 28]}, direction=None)
27 State(step=14, acc=0, transitions={'0': ["0'", 0, 31], '1': ["1'", 1, 32], "0'": ["0'", 0, 27], "1'": ["1'", 0, 27], Sym('B'+1): [None, 0, 47]}, direction=1)
28 State(step=14, acc=1, transitions={'0': ["0'", 1, 32], '1': ["1'", 2, 33], "0'": ["0'", 1, 28], "1'": ["1'", 1, 28], Sym('B'+1): [Sym('B'+1), 1, 47]}, direction=1)
31 State(step=15, acc=0, transitions={Sym('A'+0): [Sym('A'+0), 0, 35]}, direction=None)
32 State(step=15, acc=1, transitions={Sym('A'+0): [Sym('A'+0), 1, 36]}, direction=None)
33 State(step=15, acc=2, transitions={Sym('A'+0): [Sym('A'+0), 2, 37]}, direction=None)
35 State(step=16, acc=0, transitions={'0': ["0'", 0, 23], '1': ["0'", 1, 24], "0'": ["0'", 0, 35], "1'": ["1'", 0, 35], Sym('A'+1): [Sym('A'+1), 0, 47]}, direction=1)
36 State(step=16, acc=1, transitions={'0': ["0'", 1, 24], '1': ["1'", 0, 23], "0'": ["0'", 1, 36], "1'": ["1'", 1, 36], Sym('A'+1): [Sym('A'+1), 1, 47]}, direction=1)
37 State(step=16, acc=2, transitions={'0': ["1'", 0, 23], '1': ["1'", 1, 24], "0'": ["0'", 2, 37], "1'": ["1'", 2, 37], Sym('A'+1): [Sym('A'+1), 2, 47]}, direction=1)
47 State(step=19, acc=0, transitions={Sym('B'+0): [Sym('B'+0), 0, 51]}, direction=None)
51 State(step=20, acc=0, transitions={'0': ['0', 0, 51], '1': ['1', 0, 51], "0'": ['0', 0, 51], "1'": ['1', 0, 51], Sym('B'+1): [Sym('B'+1), 0, 55]}, direction=1)
55 State(step=21, acc=0, transitions={Sym('A'+0): [Sym('A'+0), 0, 59]}, direction=None)
59 State(step=22, acc=0, transitions={'0': ['0', 0, 59], '1': ['1', 0, 59], "0'": ['0', 0, 59], "1'": ['1', 0, 59], Sym('A'+1): [Sym('A'+1), 0, 12]}, direction=1)
>>> quasis = []
>>> function = LineParser.line.parse('ADDs A B').value
>>> evaluate_function_call(function)
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[2])
1 None
2 Instruction(LOADNEXT, vard=B, next_quasis=[3, 10])
3 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[4])
4 Instruction(LOAD, vard=A, next_quasis=[5, 10])
5 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[6])
6 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[7])
7 Instruction(STORENEXT, vard=A, next_quasis=[8, 10])
8 Instruction(JUMP, next_quasis=[2])
9 None
10 Instruction(UNREAD, vard=B, next_quasis=[11])
11 Instruction(UNREAD, vard=A, next_quasis=[12])
12 End(is_start=False, next_quasis=None)
>>> more_ends = True
>>> while more_ends:
        more_ends = remove_ends()

    
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[2])
1 None
2 Instruction(LOADNEXT, vard=B, next_quasis=[3, 10])
3 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[4])
4 Instruction(LOAD, vard=A, next_quasis=[5, 10])
5 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[6])
6 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[7])
7 Instruction(STORENEXT, vard=A, next_quasis=[8, 10])
8 Instruction(JUMP, next_quasis=[2])
9 None
10 Instruction(UNREAD, vard=B, next_quasis=[11])
11 Instruction(UNREAD, vard=A, next_quasis=[12])
12 End(is_start=False, next_quasis=None)
>>> instructions2steps()
>>> steps2states()
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[13])
1 None
2 Instruction(LOADNEXT, vard=B, next_quasis=[3, 19])
3 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[15])
4 Instruction(LOAD, vard=A, next_quasis=[5, 19])
5 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[6])
6 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[17])
7 Instruction(STORENEXT, vard=A, next_quasis=[8, 19])
8 Instruction(JUMP, next_quasis=[13])
9 None
10 Instruction(UNREAD, vard=B, next_quasis=[21])
11 Instruction(UNREAD, vard=A, next_quasis=[12])
12 End(is_start=False, next_quasis=None)
13 Step(instruction=2, is_found=False, variable='B', next_quasis=[14], direction=None)
14 Step(instruction=2, is_found=True, variable='B', next_quasis=[3, 19], direction=None)
15 Step(instruction=4, is_found=False, variable='A', next_quasis=[16], direction=None)
16 Step(instruction=4, is_found=True, variable='A', next_quasis=[5, 19], direction=None)
17 Step(instruction=7, is_found=False, variable='A', next_quasis=[18], direction=None)
18 Step(instruction=7, is_found=True, variable='A', next_quasis=[8, 19], direction=None)
19 Step(instruction=10, is_found=False, variable='B', next_quasis=[20], direction=None)
20 Step(instruction=10, is_found=True, variable='B', next_quasis=[21], direction=None)
21 Step(instruction=11, is_found=False, variable='A', next_quasis=[22], direction=None)
22 Step(instruction=11, is_found=True, variable='A', next_quasis=[12], direction=None)
23 State(step=13, acc=0, transitions={Sym('B'+0): [None, 0, 14]}, direction=None)
24 State(step=13, acc=1, transitions={Sym('B'+0): [None, 1, 14]}, direction=None)
25 State(step=13, acc=2, transitions={Sym('B'+0): [None, 2, 14]}, direction=None)
26 State(step=13, acc=3, transitions={Sym('B'+0): [None, 3, 14]}, direction=None)
27 State(step=14, acc=0, transitions={'0': ["0'", 0, 3], '1': ["1'", 0, 3], "0'": ["0'", 0, 14], "1'": ["1'", 0, 14], Sym('B'+1): [None, 0, 19]}, direction=1)
28 State(step=14, acc=1, transitions={'0': ["0'", 1, 3], '1': ["1'", 1, 3], "0'": ["0'", 1, 14], "1'": ["1'", 1, 14], Sym('B'+1): [None, 1, 19]}, direction=1)
29 State(step=14, acc=2, transitions={'0': ["0'", 2, 3], '1': ["1'", 2, 3], "0'": ["0'", 2, 14], "1'": ["1'", 2, 14], Sym('B'+1): [None, 2, 19]}, direction=1)
30 State(step=14, acc=3, transitions={'0': ["0'", 3, 3], '1': ["1'", 3, 3], "0'": ["0'", 3, 14], "1'": ["1'", 3, 14], Sym('B'+1): [None, 3, 19]}, direction=1)
31 State(step=15, acc=0, transitions={Sym('A'+0): [None, 0, 16]}, direction=None)
32 State(step=15, acc=1, transitions={Sym('A'+0): [None, 1, 16]}, direction=None)
33 State(step=15, acc=2, transitions={Sym('A'+0): [None, 2, 16]}, direction=None)
34 State(step=15, acc=3, transitions={Sym('A'+0): [None, 3, 16]}, direction=None)
35 State(step=16, acc=0, transitions={'0': ['0', 0, 5], '1': ['1', 0, 5], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
36 State(step=16, acc=1, transitions={'0': ['0', 1, 5], '1': ['1', 1, 5], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
37 State(step=16, acc=2, transitions={'0': ['0', 2, 5], '1': ['1', 2, 5], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
38 State(step=16, acc=3, transitions={'0': ['0', 3, 5], '1': ['1', 3, 5], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
39 State(step=17, acc=0, transitions={Sym('A'+0): [None, 0, 18]}, direction=None)
40 State(step=17, acc=1, transitions={Sym('A'+0): [None, 1, 18]}, direction=None)
41 State(step=17, acc=2, transitions={Sym('A'+0): [None, 2, 18]}, direction=None)
42 State(step=17, acc=3, transitions={Sym('A'+0): [None, 3, 18]}, direction=None)
43 State(step=18, acc=0, transitions={'0': ["0'", 0, 8], '1': ["1'", 0, 8], "0'": ["0'", 0, 18], "1'": ["1'", 0, 18], Sym('A'+1): [None, 0, 19]}, direction=1)
44 State(step=18, acc=1, transitions={'0': ["0'", 1, 8], '1': ["1'", 1, 8], "0'": ["0'", 1, 18], "1'": ["1'", 1, 18], Sym('A'+1): [None, 1, 19]}, direction=1)
45 State(step=18, acc=2, transitions={'0': ["0'", 2, 8], '1': ["1'", 2, 8], "0'": ["0'", 2, 18], "1'": ["1'", 2, 18], Sym('A'+1): [None, 2, 19]}, direction=1)
46 State(step=18, acc=3, transitions={'0': ["0'", 3, 8], '1': ["1'", 3, 8], "0'": ["0'", 3, 18], "1'": ["1'", 3, 18], Sym('A'+1): [None, 3, 19]}, direction=1)
47 State(step=19, acc=0, transitions={Sym('B'+0): [None, 0, 20]}, direction=None)
48 State(step=19, acc=1, transitions={Sym('B'+0): [None, 1, 20]}, direction=None)
49 State(step=19, acc=2, transitions={Sym('B'+0): [None, 2, 20]}, direction=None)
50 State(step=19, acc=3, transitions={Sym('B'+0): [None, 3, 20]}, direction=None)
51 State(step=20, acc=0, transitions={'0': ['0', 0, 20], '1': ['1', 0, 20], "0'": ['0', 0, 20], "1'": ['1', 0, 20], Sym('B'+1): [None, 0, 21]}, direction=1)
52 State(step=20, acc=1, transitions={'0': ['0', 1, 20], '1': ['1', 1, 20], "0'": ['0', 1, 20], "1'": ['1', 1, 20], Sym('B'+1): [None, 1, 21]}, direction=1)
53 State(step=20, acc=2, transitions={'0': ['0', 2, 20], '1': ['1', 2, 20], "0'": ['0', 2, 20], "1'": ['1', 2, 20], Sym('B'+1): [None, 2, 21]}, direction=1)
54 State(step=20, acc=3, transitions={'0': ['0', 3, 20], '1': ['1', 3, 20], "0'": ['0', 3, 20], "1'": ['1', 3, 20], Sym('B'+1): [None, 3, 21]}, direction=1)
55 State(step=21, acc=0, transitions={Sym('A'+0): [None, 0, 22]}, direction=None)
56 State(step=21, acc=1, transitions={Sym('A'+0): [None, 1, 22]}, direction=None)
57 State(step=21, acc=2, transitions={Sym('A'+0): [None, 2, 22]}, direction=None)
58 State(step=21, acc=3, transitions={Sym('A'+0): [None, 3, 22]}, direction=None)
59 State(step=22, acc=0, transitions={'0': ['0', 0, 22], '1': ['1', 0, 22], "0'": ['0', 0, 22], "1'": ['1', 0, 22], Sym('A'+1): [None, 0, 12]}, direction=1)
60 State(step=22, acc=1, transitions={'0': ['0', 1, 22], '1': ['1', 1, 22], "0'": ['0', 1, 22], "1'": ['1', 1, 22], Sym('A'+1): [None, 1, 12]}, direction=1)
61 State(step=22, acc=2, transitions={'0': ['0', 2, 22], '1': ['1', 2, 22], "0'": ['0', 2, 22], "1'": ['1', 2, 22], Sym('A'+1): [None, 2, 12]}, direction=1)
62 State(step=22, acc=3, transitions={'0': ['0', 3, 22], '1': ['1', 3, 22], "0'": ['0', 3, 22], "1'": ['1', 3, 22], Sym('A'+1): [None, 3, 12]}, direction=1)
>>> apply_posts()
True
>>> apply_posts()
False
>>> for k,quasi in enumerate(quasis):
	print(k,quasi)

	
0 End(is_start=True, next_quasis=[13])
1 None
2 Instruction(LOADNEXT, vard=B, next_quasis=[3, 19])
3 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,)}, next_quasis=[15])
4 Instruction(LOAD, vard=A, next_quasis=[5, 19])
5 Instruction(MAP, map={(0, 0): (0,), (0, 1): (1,), (1, 0): (1,), (1, 1): (2,), (2, 0): (2,), (2, 1): (3,)}, next_quasis=[6])
6 Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[17])
7 Instruction(STORENEXT, vard=A, next_quasis=[8, 19])
8 Instruction(JUMP, next_quasis=[13])
9 None
10 Instruction(UNREAD, vard=B, next_quasis=[21])
11 Instruction(UNREAD, vard=A, next_quasis=[12])
12 End(is_start=False, next_quasis=None)
13 Step(instruction=2, is_found=False, variable='B', next_quasis=[14], direction=None)
14 Step(instruction=2, is_found=True, variable='B', next_quasis=[3, 19], direction=None)
15 Step(instruction=4, is_found=False, variable='A', next_quasis=[16], direction=None)
16 Step(instruction=4, is_found=True, variable='A', next_quasis=[5, 19], direction=None)
17 Step(instruction=7, is_found=False, variable='A', next_quasis=[18], direction=None)
18 Step(instruction=7, is_found=True, variable='A', next_quasis=[8, 19], direction=None)
19 Step(instruction=10, is_found=False, variable='B', next_quasis=[20], direction=None)
20 Step(instruction=10, is_found=True, variable='B', next_quasis=[21], direction=None)
21 Step(instruction=11, is_found=False, variable='A', next_quasis=[22], direction=None)
22 Step(instruction=11, is_found=True, variable='A', next_quasis=[12], direction=None)
23 State(step=13, acc=0, transitions={Sym('B'+0): [None, 0, 14]}, direction=None)
24 State(step=13, acc=1, transitions={Sym('B'+0): [None, 1, 14]}, direction=None)
25 State(step=13, acc=2, transitions={Sym('B'+0): [None, 2, 14]}, direction=None)
26 State(step=13, acc=3, transitions={Sym('B'+0): [None, 3, 14]}, direction=None)
27 State(step=14, acc=0, transitions={'0': ["0'", 0, 15], '1': ["1'", 1, 15], "0'": ["0'", 0, 14], "1'": ["1'", 0, 14], Sym('B'+1): [None, 0, 19]}, direction=1)
28 State(step=14, acc=1, transitions={'0': ["0'", 1, 15], '1': ["1'", 2, 15], "0'": ["0'", 1, 14], "1'": ["1'", 1, 14], Sym('B'+1): [None, 1, 19]}, direction=1)
29 State(step=14, acc=2, transitions={'0': ["0'", 2, 15], '1': ["1'", 2, 15], "0'": ["0'", 2, 14], "1'": ["1'", 2, 14], Sym('B'+1): [None, 2, 19]}, direction=1)
30 State(step=14, acc=3, transitions={'0': ["0'", 3, 15], '1': ["1'", 3, 15], "0'": ["0'", 3, 14], "1'": ["1'", 3, 14], Sym('B'+1): [None, 3, 19]}, direction=1)
31 State(step=15, acc=0, transitions={Sym('A'+0): [None, 0, 16]}, direction=None)
32 State(step=15, acc=1, transitions={Sym('A'+0): [None, 1, 16]}, direction=None)
33 State(step=15, acc=2, transitions={Sym('A'+0): [None, 2, 16]}, direction=None)
34 State(step=15, acc=3, transitions={Sym('A'+0): [None, 3, 16]}, direction=None)
35 State(step=16, acc=0, transitions={'0': ['0', 0, 6], '1': ['1', 1, 6], "0'": ["0'", 0, 16], "1'": ["1'", 0, 16], Sym('A'+1): [None, 0, 19]}, direction=1)
36 State(step=16, acc=1, transitions={'0': ['0', 1, 6], '1': ['1', 2, 6], "0'": ["0'", 1, 16], "1'": ["1'", 1, 16], Sym('A'+1): [None, 1, 19]}, direction=1)
37 State(step=16, acc=2, transitions={'0': ['0', 2, 6], '1': ['1', 3, 6], "0'": ["0'", 2, 16], "1'": ["1'", 2, 16], Sym('A'+1): [None, 2, 19]}, direction=1)
38 State(step=16, acc=3, transitions={'0': ['0', 3, 6], '1': ['1', 3, 6], "0'": ["0'", 3, 16], "1'": ["1'", 3, 16], Sym('A'+1): [None, 3, 19]}, direction=1)
39 State(step=17, acc=0, transitions={Sym('A'+0): [None, 0, 18]}, direction=None)
40 State(step=17, acc=1, transitions={Sym('A'+0): [None, 1, 18]}, direction=None)
41 State(step=17, acc=2, transitions={Sym('A'+0): [None, 2, 18]}, direction=None)
42 State(step=17, acc=3, transitions={Sym('A'+0): [None, 3, 18]}, direction=None)
43 State(step=18, acc=0, transitions={'0': ["0'", 0, 13], '1': ["1'", 0, 13], "0'": ["0'", 0, 18], "1'": ["1'", 0, 18], Sym('A'+1): [None, 0, 19]}, direction=1)
44 State(step=18, acc=1, transitions={'0': ["0'", 1, 13], '1': ["1'", 1, 13], "0'": ["0'", 1, 18], "1'": ["1'", 1, 18], Sym('A'+1): [None, 1, 19]}, direction=1)
45 State(step=18, acc=2, transitions={'0': ["0'", 2, 13], '1': ["1'", 2, 13], "0'": ["0'", 2, 18], "1'": ["1'", 2, 18], Sym('A'+1): [None, 2, 19]}, direction=1)
46 State(step=18, acc=3, transitions={'0': ["0'", 3, 13], '1': ["1'", 3, 13], "0'": ["0'", 3, 18], "1'": ["1'", 3, 18], Sym('A'+1): [None, 3, 19]}, direction=1)
47 State(step=19, acc=0, transitions={Sym('B'+0): [None, 0, 20]}, direction=None)
48 State(step=19, acc=1, transitions={Sym('B'+0): [None, 1, 20]}, direction=None)
49 State(step=19, acc=2, transitions={Sym('B'+0): [None, 2, 20]}, direction=None)
50 State(step=19, acc=3, transitions={Sym('B'+0): [None, 3, 20]}, direction=None)
51 State(step=20, acc=0, transitions={'0': ['0', 0, 20], '1': ['1', 0, 20], "0'": ['0', 0, 20], "1'": ['1', 0, 20], Sym('B'+1): [None, 0, 21]}, direction=1)
52 State(step=20, acc=1, transitions={'0': ['0', 1, 20], '1': ['1', 1, 20], "0'": ['0', 1, 20], "1'": ['1', 1, 20], Sym('B'+1): [None, 1, 21]}, direction=1)
53 State(step=20, acc=2, transitions={'0': ['0', 2, 20], '1': ['1', 2, 20], "0'": ['0', 2, 20], "1'": ['1', 2, 20], Sym('B'+1): [None, 2, 21]}, direction=1)
54 State(step=20, acc=3, transitions={'0': ['0', 3, 20], '1': ['1', 3, 20], "0'": ['0', 3, 20], "1'": ['1', 3, 20], Sym('B'+1): [None, 3, 21]}, direction=1)
55 State(step=21, acc=0, transitions={Sym('A'+0): [None, 0, 22]}, direction=None)
56 State(step=21, acc=1, transitions={Sym('A'+0): [None, 1, 22]}, direction=None)
57 State(step=21, acc=2, transitions={Sym('A'+0): [None, 2, 22]}, direction=None)
58 State(step=21, acc=3, transitions={Sym('A'+0): [None, 3, 22]}, direction=None)
59 State(step=22, acc=0, transitions={'0': ['0', 0, 22], '1': ['1', 0, 22], "0'": ['0', 0, 22], "1'": ['1', 0, 22], Sym('A'+1): [None, 0, 12]}, direction=1)
60 State(step=22, acc=1, transitions={'0': ['0', 1, 22], '1': ['1', 1, 22], "0'": ['0', 1, 22], "1'": ['1', 1, 22], Sym('A'+1): [None, 1, 12]}, direction=1)
61 State(step=22, acc=2, transitions={'0': ['0', 2, 22], '1': ['1', 2, 22], "0'": ['0', 2, 22], "1'": ['1', 2, 22], Sym('A'+1): [None, 2, 12]}, direction=1)
62 State(step=22, acc=3, transitions={'0': ['0', 3, 22], '1': ['1', 3, 22], "0'": ['0', 3, 22], "1'": ['1', 3, 22], Sym('A'+1): [None, 3, 12]}, direction=1)
>>> k,quasi=6,quasis[6]
>>> quasi
Instruction(MAP, map={(0,): (0, 0), (1,): (0, 1), (2,): (1, 0), (3,): (1, 1)}, next_quasis=[17])
>>> type(quasi)==Instruction
True
>>> quasi.command=='MAP' or quasi.command=='LOADI' and quasi.loadto=='TEMP'
True
>>> quasi.command=='MAP'
True
>>> size = validate_maps(quasi.map_)
>>> size
(1, 2)
>>> quasi.command=='LOADI' or size==(1,2)
True
>>> quasi2 = quasis[44]
>>> (type(quasi2)==State and quasis[quasi2.step].is_found and
                                quasis[quasi.next_quasis[0]].next_quasis[0]==quasi2.step)
True
>>> symbol = '1'
>>> symbol = '0'
>>> quasi.command=='MAP'
True
>>> (quasi2.acc,) in quasi.map_
True
>>> mapping = quasi.map_[(quasi2.acc,)]
>>> mapping
(0, 1)
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order = ['A','B']
>>> compile_function('ADDs A B')
27 0 2 l 31l
27 1 3 l 32l
27 2 2 r 27
27 3 3 r 27
27 A * l 47l
28 0 2 l 32l
28 1 3 l 33l
28 2 2 r 28
28 3 3 r 28
28 A * l 47l
35 0 2 r 23r
35 1 3 r 23r
35 2 2 r 35
35 3 3 r 35
35 B B * 47*
36 0 3 r 23r
36 1 2 r 24r
36 2 2 r 36
36 3 3 r 36
36 B B * 47*
37 0 2 r 24r
37 1 3 r 24r
37 2 2 r 37
37 3 3 r 37
37 B B * 47*
51 0 0 r 51
51 1 1 r 51
51 2 0 r 51
51 3 1 r 51
51 A A l 55l
59 0 0 r 59
59 1 1 r 59
59 2 0 r 59
59 3 1 r 59
59 B B * halt
23r B * r 27
23r * * r *
31l A * r 35
31l * * l *
32l A * r 36
32l * * l *
47* B * r 51
47* * * * *
47l B * r 51
47l * * l *
33l A * r 37
33l * * l *
24r B * r 28
24r * * r *
55l A * r 59
55l * * l *
>>> order = ['varr','V','N']
>>> compile_function('RECP V varr N')
67 0 0 r 67
67 1 0 r 67
67 2 0 r 67
67 3 0 r 67
67 V V l 71l
75 0 0 r 75
75 1 0 r 76
75 2 0 r 75
75 3 0 r 76
75 V * * 93*
76 0 1 r 75
76 1 1 r 76
76 2 1 r 75
76 3 1 r 76
76 V * * 94*
81 0 3 r 125r
81 1 3 r 125r
81 2 2 l 81
81 3 3 l 81
81 V V * 85*
82 0 2 l 71l
82 1 2 l 71l
82 2 2 l 82
82 3 3 l 82
82 V * * 85*
89 0 0 r 89
89 1 1 r 89
89 2 0 r 89
89 3 1 r 89
89 N N * halt
97 0 2 r 101r
97 1 3 r 102r
97 2 2 l 97
97 3 3 l 97
97 varr varr * 109*
98 0 2 r 101r
98 1 3 r 102r
98 2 2 l 98
98 3 3 l 98
98 varr varr * 110*
105 0 2 l 93l
105 1 3 l 110l
105 2 2 l 105
105 3 3 l 105
105 N * l 109l
106 0 2 l 109l
106 1 3 l 93l
106 2 2 l 106
106 3 3 l 106
106 N N l 110l
113 0 0 r 113
113 1 1 r 113
113 2 0 r 113
113 3 1 r 113
113 V V r 117r
114 0 0 r 114
114 1 1 r 114
114 2 0 r 114
114 3 1 r 114
114 V V r 118r
121 0 0 r 121
121 1 1 r 121
121 2 0 r 121
121 3 1 r 121
121 varr varr l 77l
122 0 0 r 122
122 1 1 r 122
122 2 0 r 122
122 3 1 r 122
122 varr varr l 78l
129 0 2 l 133l
129 1 3 l 134l
129 2 2 r 129
129 3 3 r 129
129 varr * l 149l
130 0 2 l 134l
130 1 3 l 134l
130 2 2 r 130
130 3 3 r 130
130 varr * l 149l
137 0 2 r 125r
137 1 3 r 126r
137 2 2 r 137
137 3 3 r 137
137 V V r 149r
138 0 3 r 125r
138 1 2 r 125r
138 2 2 r 138
138 3 3 r 138
138 V V r 149r
153 0 0 r 153
153 1 1 r 153
153 2 0 r 153
153 3 1 r 153
153 varr varr l 157l
161 0 0 r 161
161 1 1 r 161
161 2 0 r 161
161 3 1 r 161
161 V V l 71l
63* varr * r 67
63* * * * *
71l varr * r 76
71l * * l *
93* V * l 97
93* * * * *
93l V * l 97
93l * * l *
94* V * l 98
94* * * * *
125r N * r 129
125r * * r *
85* V * r 89
85* * * * *
101r varr * l 105
101r * * r *
102r varr * l 106
102r * * Traceback (most recent call last):
  File "<pyshell#916>", line 1, in <module>
    compile_function('RECP V varr N')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 635, in compile_function
    print_searches()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 717, in print_searches
    print(str(search)+direction,'*','*',direction,'*')
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order = ['varr','V','N']
>>> compile_function('RECP V varr N')
67 0 0 r 67
67 1 0 r 67
67 2 0 r 67
67 3 0 r 67
67 V V l 71l
75 0 0 r 75
75 1 0 r 76
75 2 0 r 75
75 3 0 r 76
75 V * * 93*
76 0 1 r 75
76 1 1 r 76
76 2 1 r 75
76 3 1 r 76
76 V * * 94*
81 0 3 r 125r
81 1 3 r 125r
81 2 2 l 81
81 3 3 l 81
81 V V * 85*
82 0 2 l 71l
82 1 2 l 71l
82 2 2 l 82
82 3 3 l 82
82 V * * 85*
89 0 0 r 89
89 1 1 r 89
89 2 0 r 89
89 3 1 r 89
89 N N * halt
97 0 2 r 101r
97 1 3 r 102r
97 2 2 l 97
97 3 3 l 97
97 r r * 109*
98 0 2 r 101r
98 1 3 r 102r
98 2 2 l 98
98 3 3 l 98
98 r r * 110*
105 0 2 l 93l
105 1 3 l 110l
105 2 2 l 105
105 3 3 l 105
105 N * l 109l
106 0 2 l 109l
106 1 3 l 93l
106 2 2 l 106
106 3 3 l 106
106 N * l 110l
113 0 0 r 113
113 1 1 r 113
113 2 0 r 113
113 3 1 r 113
113 V V r 117r
114 0 0 r 114
114 1 1 r 114
114 2 0 r 114
114 3 1 r 114
114 V V r 118r
121 0 0 r 121
121 1 1 r 121
121 2 0 r 121
121 3 1 r 121
121 r r l 77l
122 0 0 r 122
122 1 1 r 122
122 2 0 r 122
122 3 1 r 122
122 r r l 78l
129 0 2 l 133l
129 1 3 l 134l
129 2 2 r 129
129 3 3 r 129
129 r * l 149l
130 0 2 l 134l
130 1 3 l 134l
130 2 2 r 130
130 3 3 r 130
130 r * l 149l
137 0 2 r 125r
137 1 3 r 126r
137 2 2 r 137
137 3 3 r 137
137 V * r 149r
138 0 3 r 125r
138 1 2 r 125r
138 2 2 r 138
138 3 3 r 138
138 V * r 149r
153 0 0 r 153
153 1 1 r 153
153 2 0 r 153
153 3 1 r 153
153 r r l 157l
161 0 0 r 161
161 1 1 r 161
161 2 0 r 161
161 3 1 r 161
161 V V l 71l
63* varr * r 67
63* * * * *
71l varr * r 76
71l * * l *
93l V * l 97
93l * * l *
93* V * l 97
93* * * * *
94* V * l 98
94* * * * *
125r N * r 129
125r * * r *
85* V * r 89
85* * * * *
101r varr * l 105
101r * * r *
102r varr * l 106
102r * * r *
109l varr * r 113
109l * * l *
109* varr * r 113
109* * * * *
110l varr * r 114
110l * * l *
110* varr * r 114
110* * * * *
117r N * r 121
117r * * r *
118r N * r 122
118r * * r *
77l N * l 81
77l * * l *
78l N * l 82
78l * * l *
133l varr * r 137
133l * * l *
134l varr * r 138
134l * * l *
149r N * r 153
149r * * r *
149l N * r 153
149l * * l *
126r N * r 130
126r * * r *
157l varr * r 161
157l * * l *
>>> quasis[0]
End(is_start=True, next_quasis=[63])
>>> directions
{63: {'*'}, 71: {'l'}, 93: {'l', '*'}, 94: {'*'}, 125: {'r'}, 85: {'*'}, 101: {'r'}, 102: {'r'}, 109: {'l', '*'}, 110: {'l', '*'}, 117: {'r'}, 118: {'r'}, 77: {'l'}, 78: {'l'}, 133: {'l'}, 134: {'l'}, 149: {'r', 'l'}, 126: {'r'}, 157: {'l'}}
>>> quasis[101]
State(step=47, acc=0, transitions={Sym('N'+1): [Sym('N'+1), 0, 105]}, direction=None)
>>> order
['varr', 'V', 'N']
>>> order = ['varr', 'V', 'N','P','S']
>>> compile_function('PI')
Traceback (most recent call last):
  File "<pyshell#924>", line 1, in <module>
    compile_function('PI')
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 630, in compile_function
    more_merges = merge_links()
  File "C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py", line 603, in merge_links
    if equal_states(k,j):
KeyboardInterrupt
>>> 
 RESTART: C:\Users\joshm\AppData\Local\Programs\Python\Python37-32\Mathison\MathisonCompiler.py 
>>> order = ['varr', 'V', 'N','P','S']
>>> compile_function('PI')
112 0 0 l 240l
112 1 1 l 116l
112 2 2 r 112
112 3 3 r 112
112 r r l 116l
120 0 1 r 120
120 1 0 r 120
120 2 1 r 120
120 3 0 r 120
120 N * l 240l
121 0 0 r 121
121 1 1 r 120
121 2 0 r 121
121 3 1 r 120
121 N * l 241l
126 0 0 r 126
126 1 1 r 126
126 2 0 r 126
126 3 1 r 126
126 P P r 130r
127 0 1 r 126
127 1 0 r 127
127 2 1 r 126
127 3 0 r 127
127 P * * halt
128 0 0 r 127
128 1 1 r 127
128 2 0 r 127
128 3 1 r 127
128 P * r 130r
134 0 1 r 134
134 1 0 r 134
134 2 1 r 134
134 3 0 r 134
134 r r l 138l
142 0 0 r 142
142 1 0 r 142
142 2 0 r 142
142 3 0 r 142
142 V V l 146l
150 0 0 r 150
150 1 0 r 151
150 2 0 r 150
150 3 0 r 151
150 V * * 168*
151 0 1 r 150
151 1 1 r 151
151 2 1 r 150
151 3 1 r 151
151 V V * 169*
156 0 3 r 200r
156 1 3 r 200r
156 2 2 l 156
156 3 3 l 156
156 V V * 160*
157 0 2 l 146l
157 1 2 l 146l
157 2 2 l 157
157 3 3 l 157
157 V * * 160*
164 0 0 r 164
164 1 1 r 164
164 2 0 r 164
164 3 1 r 164
164 N N r 108r
172 0 2 r 176r
172 1 3 r 177r
172 2 2 l 172
172 3 3 l 172
172 r r * 184*
173 0 2 r 176r
173 1 3 r 177r
173 2 2 l 173
173 3 3 l 173
173 r r * 185*
180 0 2 l 168l
180 1 3 l 185l
180 2 2 l 180
180 3 3 l 180
180 N * l 184l
181 0 2 l 184l
181 1 3 l 168l
181 2 2 l 181
181 3 3 l 181
181 N * l 185l
188 0 0 r 188
188 1 1 r 188
188 2 0 r 188
188 3 1 r 188
188 V V r 192r
189 0 0 r 189
189 1 1 r 189
189 2 0 r 189
189 3 1 r 189
189 V V r 193r
196 0 0 r 196
196 1 1 r 196
196 2 0 r 196
196 3 1 r 196
196 P P l 152l
197 0 0 r 197
197 1 1 r 197
197 2 0 r 197
197 3 1 r 197
197 P P l 153l
204 0 2 l 208l
204 1 3 l 209l
204 2 2 r 204
204 3 3 r 204
204 P P l 224l
205 0 2 l 209l
205 1 3 l 209l
205 2 2 r 205
205 3 3 r 205
205 P P l 224l
212 0 2 r 200r
212 1 3 r 201r
212 2 2 r 212
212 3 3 r 212
212 V V r 224r
213 0 3 r 200r
213 1 2 r 200r
213 2 2 r 213
213 3 3 r 213
213 V V r 224r
228 0 0 r 228
228 1 1 r 228
228 2 0 r 228
228 3 1 r 228
228 P P l 232l
236 0 0 r 236
236 1 1 r 236
236 2 0 r 236
236 3 1 r 236
236 V V l 146l
244 0 2 r 248r
244 1 3 r 249r
244 2 2 r 244
244 3 3 r 244
244 N * l 264l
245 0 2 r 249r
245 1 3 r 250r
245 2 2 r 245
245 3 3 r 245
245 N * l 264l
252 0 2 l 240l
252 1 3 l 240l
252 2 2 r 252
252 3 3 r 252
252 S * l 264l
253 0 3 l 240l
253 1 2 l 241l
253 2 2 r 253
253 3 3 r 253
253 S * l 264l
254 0 2 l 241l
254 1 3 l 241l
254 2 2 r 254
254 3 3 r 254
254 S * l 264l
268 0 0 r 268
268 1 1 r 268
268 2 0 r 268
268 3 1 r 268
268 N N r 272r
276 0 0 r 276
276 1 1 r 276
276 2 0 r 276
276 3 1 r 276
276 S S l 122l
138l r * r 142
138l * * l *
138* r * r 142
138* * * * *
240l V * r 244
240l * * l *
116l V * r 121
116l * * l *
241l V * r 245
241l * * l *
130r S * r 134
130r * * r *
146l r * r 151
146l * * l *
168l V * l 172
168l * * l *
168* V * l 172
168* * * * *
169* V * l 173
169* * * * *
200r N * r 204
200r * * r *
160* V * r 164
160* * * * *
108r S * r 112
108r * * r *
176r P * l 180
176r * * r *
177r P * l 181
177r * * r *
184l r * r 188
184l * * l *
184* r * r 188
184* * * * *
185l r * r 189
185l * * l *
185* r * r 189
185* * * * *
192r N * r 196
192r * * r *
193r N * r 197
193r * * r *
152l N * l 156
152l * * l *
153l N * l 157
153l * * l *
208l r * r 212
208l * * l *
209l r * r 213
209l * * l *
224l N * r 228
224l * * l *
224r N * r 228
224r * * r *
201r N * r 205
201r * * r *
232l r * r 236
232l * * l *
248r P * r 252
248r * * r *
249r P * r 253
249r * * r *
264l V * r 268
264l * * l *
250r P * r 254
250r * * r *
272r P * r 276
272r * * r *
122l N * r 128
122l * * l *
>>> quasis[0]
End(is_start=True, next_quasis=[138])
>>> 
