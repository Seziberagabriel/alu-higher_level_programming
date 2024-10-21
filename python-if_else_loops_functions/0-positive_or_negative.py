#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # This generates a random signed number between -10 and 10

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
