binaryKey = int(input("Binary Key>>"))

power = 1


binary = ""

while 2**power < binaryKey:
    power += 1
    print("power " + str(power) + ": ")

print("2 ** " + str(power) + " equals: ")

sum = 2**power
print("sum: " + str(sum))

base = sum - 1
print("base: " + str(base))

binaryLength = power * "0"
print("binary length: " + str(binaryLength))
