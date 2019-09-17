

def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return[lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l

data = list(('abc'))
#print(perm1)
for p in perm1(data):
    pass
#    print(p)


a1 = []
b1 = [a1]
c1 = [b1]
d1 = [c1]
e1 = [d1]
f1 = [e1]
g1 = [f1]
h1 = [g1]
i1 = [h1]

def perm2(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                yield [x]+p

#data = list(('abcdefghij'))
#print(perm1)
#for p in perm1(data):
#    print(p)

data = list(i1+h1+g1+f1+e1+d1+c1+b1)
#print(perm2)
for p in perm2(data):
    print(p)
