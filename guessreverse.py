# Nate Genter
# 1-9-16

# Guess my number reversed
# In this program the computer will try and guess your number

import random


print("\nWelcome to Liberty North.")
print("Lets play a game.")
print("\nPlease select a number, from 1-100 and I will guess it.")


number = int(input("Please enter your number: "))

if number <= 0 or number >= 101:
    print("That is not a valid number.")

tries = 1
guess = ()

while number != guess:

    tries == 1       
    guess = random.randint(1,100)
    print(guess)
    if guess != number:
        tries += 1
    
print("\nIt took me", tries, "tries.")

input("\nPress the enter key to exit.")
