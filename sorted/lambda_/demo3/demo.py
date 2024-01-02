numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda n: n * n, numbers)

print(list(squared_nums))

#########################################

lambda n: n % 2 != 0


odd_nums = filter(lambda n: n % 2 != 0, numbers)

print(list(odd_nums))
