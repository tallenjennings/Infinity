char = 'a'
print(char)


for letter in char:
    if letter in char <= chr(1):
        pass
    else:
        x = chr((ord(char))+1) + '[' + char + ']'
        char = chr((ord(char))+1)
        y = chr((ord(char))+1) + '[' + char + ']'
        print(char)

for letter in char:
    if letter in char <= chr(1):
        pass
    else:
        x = chr((ord(char))+1) + '[' + char + ']'
        char = chr((ord(char))+1)
        y = chr((ord(char))+1) + '[' + char + ']'
        print(char)




#print(char)
print(x)
print(y)
