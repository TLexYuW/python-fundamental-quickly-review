list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
    print(index, j)


list1 = [10, 11, 12, 13, 14]
print(list1[::1])


list2 = [[1, 2, 3, 2, 5], [4, 5, 6, 7], [8, 9, 10]]
for i in list2:
    if len(i) == 3:
        print(i)
