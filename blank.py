text = input("Text to Key>> ")
result = ''.join('{0:08b}'.format(ord(x), 'b') for x in text)
print(result)
