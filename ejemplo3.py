# Strings

myStr = "Renzo Zamora"

# print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('hello', 'bye'))
print(myStr.count('l'))

print(myStr.startswith('hola'))
print(myStr.startswith('Hello'))

print(myStr.endswith('World'))
print(myStr.endswith('Universe'))

print(myStr.split('o'))
print(myStr.find('d'))

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
print(myStr[-1])

print("Mi nombre es " + myStr)
print(f"Mi nombre es {myStr}")