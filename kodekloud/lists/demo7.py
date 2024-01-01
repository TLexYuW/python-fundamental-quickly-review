countries = [
    ["Egypt", "USA", "India"],
    ["Dubai", "America", "Spain"],
    ["London", "England", "France"],
]

# countries2 = [
#     country for sublist in countries for country in sublist if len(country) < 6
# ]

countries2 = []

for sublist in countries:
    for country in sublist:
        if len(country) < 6:
            countries2.append(country)

print(countries2)
