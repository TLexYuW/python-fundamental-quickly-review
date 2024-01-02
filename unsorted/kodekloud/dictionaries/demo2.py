testdict = {
    "brand": "Samsung",
    "ram": "3",
    "Os": "Android",
    "year": 2020
}

print(testdict.items())

testdict2 = {
    "brand": "apple",
    "ram": "3",
    "year": 2020,
    "year": 2021
}

print(testdict2)

testdict2.popitem()
print(testdict2)

del testdict2["ram"]
print(testdict2)
