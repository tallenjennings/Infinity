''' This program takes a binary string and tells you what key value it has in a binary infinity tree'''


#enter binary string to be converted
binary = input('Input Binary String>>')
print("\n")


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
			
	
	
	
location(binary)