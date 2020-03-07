'''This program will take a key and convert it to binary'''


#enter key to be converted
binaryKey = int(input("enter binary key>>"))
print("\n")


#key function
def location(binaryKey):

    count =0

    key =1

    binary = ""

    while key < binaryKey:

        if 2**count < binaryKey:

            print("figuring out the power: ")
            count += 1
            print("count: " + str(count))
            key = (2**(count)/2)-1
            print("key: " + str(int(key)) + "\n")

        else:
            break

    while count > 1:

        if (key + ((2**count)/2)) <= binaryKey:
            key = key + ((2**count)/2)
            print("Power: ")
            count -= 1
            print("count: " + str(count))
            print("key: " + str(int(key)) + "\n")
            binary = binary + "1"
            print("binary: " + binary + "\n")

        #elif (key + ((2**count)/2)) < binaryKey:
            #key = key + ((2**count)/2)
            #count -= 1
            #print("count: " + str(count))
            #binary = binary + "1"

        else:
            print("Power: ")
            count -= 1
            print("count: " + str(count))
            print("key: " + str(int(key)) + "\n")
            binary = binary + "0"
            print("binary: " + binary + "\n")



    print("Binary key: " + str(binary))


location(binaryKey)
