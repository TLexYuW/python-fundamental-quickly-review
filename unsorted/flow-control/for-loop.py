import random

for i in range(5):
    print('Five Times ({})'.format(str(i)))
    
for i in range(0, 10, 2):
    print(i)
    
for i in range(5, -1, -1):
    print(i)

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
else:
    print("only executed when no item of the list is equal to 3")
    
print('------------------------------------------')

for i in range(5):
    print(random.randint(1, 10))