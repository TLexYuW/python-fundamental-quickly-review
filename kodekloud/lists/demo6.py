classroom = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["I", "J", "K", "L"]]

l = classroom[2]

print(l)


a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a[3][3])

a = []
for i in range(2):
    a.append([])
    for j in range(2):
        a[i].append(j)

print(a)

countries = [
    ["Egypt", "USA", "India"],
    ["Dubai", "America", "Spain"],
    ["London", "England", "France"],
]

# countries2 = [
#     country for sublist in countries for country in sublist if len(country) < 4
# ]
countries2 = []
for sublist in countries:
    for country in sublist:
        if len(country) < 4:
            countries2.append(country)

print(countries2)


# matrix = [[j for j in range(3)] for i in range(3)]

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(j)
    matrix.append(row)

print(matrix)
print(matrix[1][2])
