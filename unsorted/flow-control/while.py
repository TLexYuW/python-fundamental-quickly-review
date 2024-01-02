spam = 0
while spam < 5:
    print('Hello, world')
    spam += 1
    
while True:
    print('Please type your name.')
    name = input()
    if name == 'test':
        break
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'J':
        continue
    print('Hello, J. What is the password? (It is a fish.)')
    password = input()
    if password == 'fish':
        break
print('Access granted')