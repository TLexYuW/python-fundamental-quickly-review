import random

def hi(name):
    print('Hello {}'.format(name))
    
    
hi('abc')

def getAns(num):
    if num == 1:
        return 'It is 1'
    elif num == 2:
        return 'It is 2'

r = random.randint(1, 2)
f = getAns(r)
print(f)

print('Hello', end='')
print('world')

print('cat', 'dogs', 'mice', sep=',')

def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)
