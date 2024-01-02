import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number: "))
while guess != secret_number:
    guess = int(input("Guess a number: "))
else:
    print("Congratulations, u got it!")
