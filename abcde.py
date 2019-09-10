Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=['']
>>> b=a+a
>>> b
['', '']
>>> b=[a]
>>> a
['']
>>> b
[['']]
>>> c=a+b
>>> c
['', ['']]
>>> c=[b]
>>> c
[[['']]]
>>> a=[]
>>> c
[[['']]]
>>> b
[['']]
>>> a
[]
>>> b=[a]
>>> b
[[]]
>>> c=[b]
>>> d=[c]
>>> e=[d]
>>> f=[e]
>>> g=[f]
>>> h=[g]
>>> i=[h=
   
SyntaxError: invalid syntax
>>> i=[g]
>>> a
[]
>>> b
[[]]
>>> c
[[[]]]
>>> d
[[[[]]]]
>>> e
[[[[[]]]]]
>>> g
[[[[[[[]]]]]]]
>>> h
[[[[[[[[]]]]]]]]
>>> i
[[[[[[[[]]]]]]]]
>>> a+a
[]
>>> b+b
[[], []]
>>> h+h+b
[[[[[[[[]]]]]]], [[[[[[[]]]]]]], []]
>>> aa=a+b+c
>>> aa
[[], [[]]]
>>> cls
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> a
[]
>>> b
[[]]
>>> c
[[[]]]
>>> b+b
[[], []]
>>> d
[[[[]]]]
>>> c+a
[[[]]]
>>> c+b
[[[]], []]
>>> a=['']
>>> c+a
[[[]], '']
>>> [[[][]]]
SyntaxError: invalid syntax
>>> c[a]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c[a]
TypeError: list indices must be integers or slices, not list
>>> a
['']
>>> b
[[]]
>>> b=[a]
>>> b
[['']]
>>> c
[[[]]]
>>> c=[b]
>>> d=[c]
>>> d
[[[['']]]]
>>> d+c
[[[['']]], [['']]]
>>> d+a
[[[['']]], '']
>>> b+b+a
[[''], [''], '']
>>> b
[['']]
>>> c
[[['']]]
>>> c1=[b]
>>> c1
[[['']]]
>>> c2=b+b
>>> c2
[[''], ['']]
>>> d
[[[['']]]]
>>> d2=[c2+a]
>>> d2
[[[''], [''], '']]
>>> e2=[d2+a]
>>> e2
[[[[''], [''], ''], '']]
>>> 
