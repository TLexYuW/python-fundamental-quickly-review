a = [1,3,5,7,9,11]
print([i - 1 for i in a])

b = {"abc", 'def'}
print({s.upper() for s in b})

c = {'name': 'p', 'age': 50}

print({v: k for k, v in c.items()})