from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)


names = ["Dave Gray", "Sara Ito", "John Wick"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
