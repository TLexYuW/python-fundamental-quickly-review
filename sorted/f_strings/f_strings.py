person = "XXXXX"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)

player = {"person": "L", "coins": 3}


message = "\n{person} has {coins} coins left.".format(**player)
print(message)

###########################################

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {100 * 10} coins left."
print(message)

message = f"\n{person.lower()} has {coins} coins left."
print(message)

message = f"\n{str(player['person']).lower()} has {coins} coins left."
print(message)

###########################################

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

print("\n###########################################")
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
print("###########################################")
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
print("###########################################\n")
