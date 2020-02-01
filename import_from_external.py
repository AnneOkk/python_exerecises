## Exercises
# Dice
from random import randint

class Die:
    def __init__(self, sides):
        self.throws = list(range(1,10))
        self.sides = sides
    def roll_die(self):
        for throw in range(1,10):
            roll = randint(1, self.sides + 1)
            print(roll)


die1 = Die(6)
die1.roll_die()

