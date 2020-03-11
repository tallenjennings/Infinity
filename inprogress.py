'''This program will allow you to search through a binary infinity'''

 
def key(binaryKey):
 
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

    halfPower = (2**power)/2
    print("half base: " + str(halfPower))

    base = (2**power)-1

	

    for char in binaryLength:
	
    	if base + halfPower <= binaryKey:
    	    base = base + halfPower
    	    print("base: " + str(base))
    	    halfPower = halfPower/2
    	    binary = binary + "1"
    	    print("binary 1: " + binary)
    	    pass
	    
    	else:
    		halfPower = halfPower/2
    		print("base: " + str(base))
    		binary = binary + "0"
    		print("binary 0: " + binary)
    		pass

    print("binary solution: " + binary)
  





#key function
def location(binary):
	
	#returns length of string
	digits = len(binary)
	print("Digits: " + str(digits))
	
	#returns power of digits 
	power = 2**digits
	print("Number of Permientations in column: " + str(power))
	
	baseKey = power - 1
	key = baseKey
	
	print("Base Key: " + str(baseKey))
	
	binaryBaseKey = digits * "0"
	print("Binary Base Key: " + binaryBaseKey + "\n")
	
	count = digits
	
	powerSum = power
	
	binaryKey = str(binary)
	
	for char in binaryKey:
		#baseKey = power - 1
		if char == "0":
			print("looking at char: 0")
			count = count - 1
			print("digit in string: " + str(count))
			powerSum = powerSum / 2
			print("number to add to change digit: " + str(int(powerSum)))
			print("key at char " + str(count) + ": " + str(key) + "\n")
			
		elif char == "1":
			print("looking at char: 1")
			count = count - 1
			print("digit in string: " + str(count))
			powerSum = (powerSum / 2)
			print("number to add to change digit: " + str(int(powerSum)))
			
			
			key += powerSum
			print("key at char " + str(count) + ": " + str(int(key)) + "\n")
			
		else:
			print("one of the characters werent binary")


	print("final key: " + str(int(key)))
			
	
	
	





answer = input("Key : 1\n"
                            "Binary : 2\n"
                            ">>")

if answer == "1":
	binaryKey = int(input("Binary Key>>"))
	key(binaryKey)
else:
	binary = input("Binary String>>")
	location(binary)
	
