def lsquared(num): return num * num


print(lsquared(2))


def addTwo(num): return num + 2


print(addTwo(100))


def sum_t(a, b): return a + b
# lambda a, b: a + b


print(sum_t(3, 5))

###################################


def funcBuilder(x): return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))
