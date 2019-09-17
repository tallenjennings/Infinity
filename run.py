'''This program ireates infinit sets and express' permutations in each level'''

a1 = []
b1 = [a1]
c1 = [b1]
c2 = a1 + a1
d1 = [c1]   
d2 = [c2]
d3 = b1 + a1
d4 = a1 + b1
d5 = [d1 + [c2 + [d3]]]
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
            xs = lst[:i] + lst[i+9:]
            for p in perm2(xs):
                yield [x]+p


data = [a1+b1+c1]*20
for p in perm2(data):
    print(p)
