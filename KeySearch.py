'''This program will take a key and convert it to binary'''

#enter key to be converted
binaryKey = input("enter binary key>>")
print("\n")


#key function
def location(keyBinary):

    count = 0

    baseKey = 1

    powerSum = (2 ** count) -1

    while (baseKey != int(binaryKey)):

        if 2**count < int(binaryKey):
            count += 1
            print("base key: " + str(baseKey))
            print("count: " + str(count))
            power = 2**count
            print("power: " + str(power))

        elif 2**count == int(binaryKey):
            print("\n")
            print("correct power: " + "2**" + str(count))

            break
        elif 2**count > int(binaryKey):
            print("\n")
            print("correct power: " + "2**" + str(count))

            break
        else:
            print("pass")
            pass


    print("key asked for: " + str(binaryKey))
    print("base string: " + count * "0"  )
    baseStringKey = 2**count - 1
    print("base key: " + str(baseStringKey))

    #key = 15555
    #binary string = 1110011000100
    countTwo = 0
    while countTwo < count:
        countTwo += 1
        key = 2**countTwo
        print("num")




    print(key)


location(binaryKey)
