#a = []
#ch = 'a'
#b = [a]
#c = [b]
#def add():
#b = [a]
#c = b + [a]
#d = c + b
#e = d + c
#f = e + d
#add()
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
#print(f)

#chr((ord(ch)+1))

def iter():
    if len(lst) == 0:
            yield []
    elif len(lst) == 1:
        yield lst

iter()        


list=('a')
for p in iter():
    print(list)

