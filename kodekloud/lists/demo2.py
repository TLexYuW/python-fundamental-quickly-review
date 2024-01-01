list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.append(11)
list1.insert(1, "ABC")
print(list1)

# Swap
temp = list1[0]
list1[0] = list1[1]
list1[1] = temp
print(list1)

list1[2], list1[3] = list1[3], list1[2]
print(list1)

list2 = [100, 3, 4, 9, 10000, 3333]
list2.sort()
print(list2)

list2.reverse()
print(list2)
