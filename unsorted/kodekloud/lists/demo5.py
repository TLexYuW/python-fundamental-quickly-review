# list[start:end]

letters = ["A", "B", "C", "D", "E"]
print(letters[1:])

print(letters[:])  # copy

del letters[1:3]
print(letters)

print("B" in letters)

print("E" in letters)

print("Z" not in letters)


list1 = [0, 3, 4, 1, 2]
list1[2:5] = [8, 9]
print(list1)
