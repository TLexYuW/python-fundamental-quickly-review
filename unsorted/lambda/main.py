def add(x, y):
    return x + y


ladd = lambda x, y: x + y

print(ladd(5, 3))

def make_adder(n):
    return lambda x: x+n

plus_x = make_adder(5)
print(plus_x(3))