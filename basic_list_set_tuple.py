Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T1 = ()
>>> T1
()
>>> type(T1)
<class 'tuple'>
>>> typeof(T1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    typeof(T1)
NameError: name 'typeof' is not defined
>>> L1 = (1,2,3,4,5,6)
>>> T2 = ("Hello",4,6,7)
>>> T2
('Hello', 4, 6, 7)
>>> T3 = (4,6,7,"Hello")
>>> T3
(4, 6, 7, 'Hello')
>>> T4 = (1,2,3,[1,4])
>>> T4
(1, 2, 3, [1, 4])
>>> type(T4)
<class 'tuple'>
>>> T4[3]
[1, 4]
>>> T5 = ("hello")
>>> t5
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t5
NameError: name 't5' is not defined
>>> T5
'hello'
>>> type(T5)
<class 'str'>
>>> T6 = ([1,2,3,4,5])
>>> T6
[1, 2, 3, 4, 5]
>>> NameError: name 't5' is not defined
SyntaxError: invalid syntax
>>> T4[:2]
(1, 2)
>>> T4.append(3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    T4.append(3)
AttributeError: 'tuple' object has no attribute 'append'
>>> id(T3)
1928420184928
>>> id(T4)
1928420185488
>>> T3+T4
(4, 6, 7, 'Hello', 1, 2, 3, [1, 4])
>>> id(T3+T4)
1928419923216
>>> T3+T4
(4, 6, 7, 'Hello', 1, 2, 3, [1, 4])
>>> T2 = (1,3,5)
>>> T3 = (2,4,6)
>>> T2/T3
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    T2/T3
TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'
>>> T2-T3
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    T2-T3
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
>>> T2[2]-T3[2]
-1
>>> len(T3)
3
>>> L3.sort()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    L3.sort()
NameError: name 'L3' is not defined
>>> T3.sort()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    T3.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> sorted(T3)
[2, 4, 6]
>>> sorted(T3,reverse="True")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sorted(T3,reverse="True")
TypeError: an integer is required (got type str)
>>> sorted(T3,reverse="false")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sorted(T3,reverse="false")
TypeError: an integer is required (got type str)
>>> sorted(T3)
[2, 4, 6]
>>> del T4
>>> T4
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    T4
NameError: name 'T4' is not defined
>>> pop(T4)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    pop(T4)
NameError: name 'pop' is not defined
>>> # Sets
>>> 
>>> 
>>> 
>>> S1 = {}
>>> S1
{}
>>> S1.append(2)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    S1.append(2)
AttributeError: 'dict' object has no attribute 'append'
>>> S1.add(2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    S1.add(2)
AttributeError: 'dict' object has no attribute 'add'
>>> S1 = set{}
SyntaxError: invalid syntax
>>> S1 = set()
>>> S1
set()
>>> type(S1)
<class 'set'>
>>> S1.add(2)
>>> S1
{2}
>>> S2 = {1,2,3,"Hello"}
>>> S2
{1, 2, 3, 'Hello'}
>>> S1.add(2)
>>> id(S2
   )
1928420261440
>>> S1.add(3)
>>> id(S2)
1928420261440
>>> 
>>> S2[2] = 3
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    S2[2] = 3
TypeError: 'set' object does not support item assignment
>>> pop(S2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    pop(S2)
NameError: name 'pop' is not defined
>>> S2.pop()
1
>>> S2
{2, 3, 'Hello'}
>>> S2.add([2,3])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    S2.add([2,3])
TypeError: unhashable type: 'list'
>>> S2.add(2,3)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    S2.add(2,3)
TypeError: set.add() takes exactly one argument (2 given)
>>> S2.add((2,3))
>>> S2
{2, 3, 'Hello', (2, 3)}
>>> S2[-1][0]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    S2[-1][0]
TypeError: 'set' object is not subscriptable
>>> S2[-1]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    S2[-1]
TypeError: 'set' object is not subscriptable
>>> 
>>> for i in S2:
	print(i)

	
2
3
Hello
(2, 3)
>>> 
>>> len(S2)
4
>>> max(S2)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    max(S2)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> S2.remove(2)
>>> S2.remove("Hello")
>>> S2
{3, (2, 3)}
>>> S2.max()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    S2.max()
AttributeError: 'set' object has no attribute 'max'
>>> S4 = {1,2,3,4,5}
>>> S4
{1, 2, 3, 4, 5}
>>> S4.sum()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    S4.sum()
AttributeError: 'set' object has no attribute 'sum'
>>> sum(S4)
15
>>> max(S4)
5
>>> max(S2)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    max(S2)
TypeError: '>' not supported between instances of 'tuple' and 'int'
>>> sorted(S4)
[1, 2, 3, 4, 5]
>>> sorted(S4,reverse=True)
[5, 4, 3, 2, 1]
>>> S4.sort()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    S4.sort()
AttributeError: 'set' object has no attribute 'sort'
>>> 
>>> S1.union(S3)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    S1.union(S3)
NameError: name 'S3' is not defined
>>> S1.union(S4)
{1, 2, 3, 4, 5}
>>> S1
{2, 3}
>>> S1.union(S2)
{(2, 3), 2, 3}
>>> S1.intersection(S4)
{2, 3}
>>> S1.difference(S4)
set()
>>> l3 = list(S1.union(S4))
>>> l3
[1, 2, 3, 4, 5]
>>> S1.symmetric_difference(S3)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    S1.symmetric_difference(S3)
NameError: name 'S3' is not defined
>>> S1.symmetric_difference(S2)
{(2, 3), 2}
>>> S1.symmetric_difference(S4)
{1, 4, 5}
>>> 