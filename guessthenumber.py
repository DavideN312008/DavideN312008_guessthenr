import numbers
import random

number = (random.randrange(1, 754))
guess = int(input("Guess the number between 1 - 754: "))


while guess != number:
    if guess < number:
        print("Guess HIGHER.")
        guess = int(input("Guess the number between 1 - 754: "))
    else:
        print("Guess LOWER.")
        guess = int(input("Guess the number between 1 - 754: "))

print("You have guessed the number! GJ...")
