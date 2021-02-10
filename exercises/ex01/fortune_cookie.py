"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730135317"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")

fortune = randint(1, 5)

if fortune == 1:
    print(" A beautiful, smart, and loving person will be coming into your life.")
else: 
    if fortune == 2:
        print("your life will be happy and peaceful.")
    else: 
        if fortune == 3:
            print("Your future is cloudy.")
        else:
            if fortune == 4: 
                print("you will find something that you were looking for.")
            else:
                if fortune == 5:
                    print("I see a wellness day in your future.")
print("Now, go spread positive vibes!")