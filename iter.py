#a=[]
#b = [a]
#ch = 'a'
#x = 25
#for i in range(x):
#    ch = chr((ord(ch)+1))
#    
#    print(ch)



a1 = ['']
b1 = [a1]
c1 = [b1]
d1 = [c1]
def inf():
    print(a1)
    print(b1)
    print(c1)
    c2 = b1+b1
    print(c2)
    print(d1)
    d2 = [b1+b1]
    print(d2)
    d3 = c1+b1
    print(d3)
    d4 = b1+c1
    print(d4)
    d5 = c2+b1
    print(d5)

    
    
inf()

