# Coin Flip
# Nate Genter
# 1-9-16

# A program to emulate a coin flip, record heads or tails, and loop until one
# score is > to 100.  Declare that side the winner, and wait for the user
# to hit the enter key to exit.

import random



score_h = 1
score_t = 1

while score_h != 100 and score_t != 100:
    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        score_h += 1
    else:
        score_t += 1
    
print("\nHeads Score", score_h)
print("Tails Score", score_t)

input("press the enter key to exit.")
