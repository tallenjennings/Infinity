char = 'a'
x = []
for letter in char:
    if letter in char <= chr(1):
        pass
    else:
        x += chr((ord(char))+1)

print(char)
print(x)

