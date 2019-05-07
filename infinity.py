"""The INFINITY TREE Algorithym"""



#Beginning of the Infinity Tree
x = []
infinite = x


#Infinity Tree Expanded
for i in range(10):
 infinite += [x]
 while infinite == infinite:
     infinite += infinite
     
 print(infinite)
