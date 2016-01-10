# Guess how much Liberty North is looking to gross this year
# Nathaiel Genter
# 1-9-16

print("Welcome to Liberty North.")
print("This program randomly picks a number, between 1-100.")
print("It is on you to guess the correct number.")
print("I will supply some hints, and count the number of your guesses.")

import random

the_number = random.randint(1, 100)
guess = int(input("Take a guess; "))
tries = 1

# Guessing loop

while guess != the_number:
      if guess > the_number:
          print("Lower...")
      else:
          print("higher...")

      guess = int(input("Take a guess: "))
      tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

if tries > 10:
    print("You dumb mother fucker.")
      
      
input("Press the enter key to exit.")
