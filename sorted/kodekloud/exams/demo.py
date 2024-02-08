print(type(100))

x = 0o11
y = 0x12b
z = 6
print(x, y, z)


x = 'abcd'
for i in range(len(x)):
    x[i].upper()
    print(x[i].upper())
    
print(x[0])
print(x)