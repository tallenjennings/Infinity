"""The INFINITY TREE Algorithym"""



#Beginning of the Infinity Tree
x = (0,1)
infinite = [x]


#Infinity Tree Expanded
for i in range(10):
 infinite += [x]
 print(infinite)
