"""
& conjunction AND
| disjunction OR
~ negation
^ exclusive XOR
"""

"""
1 & 1 ===> 1

1 | 1 ===> 1
0 | 1 ===> 1

0 ^ 1 ===> 1
"""

"""
0 0 0 0 1 1 1 1
0 0 0 1 0 1 1 0
"""
print(bin(15))
print(bin(22))
"""
0 0 0 0 0 1 1 0
"""
print(15 & 22)
print(bin(6))  # 0b110
"""
0 0 0 1 1 1 1 1
"""
print(15 | 22)
print(bin(31))  # 0b11111
"""
0 0 0 1 1 0 0 1
"""
print(15 ^ 22)
print(bin(25))  # 0b11001

print("/////////////")
"""
Bit Shifting
>> 
<<
"""
"""
0 0 0 1 0 1 1 0
0 0 0 0 1 0 1 1
"""
print(bin(22))
print(22 >> 1)
print(bin(11))
"""
0 0 0 1 0 1 1 0
0 0 1 0 1 1 0 0
"""
print(22 << 1)
print(bin(44))
"""
print(22 // 2) ---> print(22 >> 1)

print(22 // 4) ---> print(22 >> 2)

print(22 * 2) ---> print(22 << 1)

print(22 * 4) ---> print(22 << 2)
"""

print("/////////////")
#
a = 20
b = 5
print("a & b =", a & b)

print("/////////////")
#
"""
 0b11001000  --- 200
 0b11001001  --- 201
 0b00110111
"""
print(bin(200))
print(bin(201))
print(~200)
print(bin(-201))

# binary_representation = "0b11001000"
# print(int(binary_representation, 2) + 1)
# result_binary = bin(int(binary_representation, 2) + 1)
# print(result_binary)

print("/////////////")
print(5 ^ 11)


print("/////////////")
a = 20
b = 5
print("a | b =", a | b)
