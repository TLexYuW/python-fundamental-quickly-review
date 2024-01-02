# immutable
tuple1 = (1, 2, 3)

tuple2 = ('a',)

tuple3 = 1, 2, 3

# x = tuple(3)
# print(x)


d = {
    1: "a",
    2: "b",
    3: "c",
}

print(d)

for key in d.keys():
    print(int(key), "-", str(d[key]))


for value in d.values():
    print(value)

for item in d.items():
    print(item)

d.update({4: "d"})

print(d)
