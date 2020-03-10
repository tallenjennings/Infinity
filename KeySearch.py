'''This program will take a key and convert it to binary'''


binaryKey = int(input("Binary Key>>"))
 
power = 1
 
binary = ""
 
while 2**power < binaryKey:
    power += 1
    print("power " + str(power) + ": ")
    
sum = 2**power
 
if sum == binaryKey:
    pass
elif sum - 1 == binaryKey:
	pass
else:
    power = power - 1
    print("minus 1 power")

 
print("2 ** " + str(power) + " equals: ")
 
print("sum: " + str(sum))
 
base = sum - 1
print("base: " + str(base))
 
binaryLength = power * "0"
print("binary length: " + str(binaryLength))

halfPower = (2**int(power))/2
print("half base: " + str(halfPower))

base = (2**power)-1

	

for char in binaryLength:

	if base + halfPower <= binaryKey:
	    base = base + halfPower
	    print("base: " + str(base))
	    halfPower = halfPower/2
	    binary = binary + "1"
	    print("binary 1: " + binary)
	    
	else:
		halfPower = halfPower/2
		print("base: " + str(base))
		binary = binary + "0"
		print("binary 0: " + binary)
		


print("binary solution: " + binary)
