def fruits(*args):
    for fruit in args:
        print(fruit)
        
        
print(fruits("apples", "bananas", "grapes"))

def fruit(**kwargs):
    for key, value in kwargs.items():
        print("{0}: {1}".format(key, value))
        
print(fruit(name = 'apple', color = 'red'))