## Exercises
# Dice
from random import randint
from random import sample

class Die:
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self):
        for throw in range(1,10):
            roll = randint(1, self.sides)
            print(roll)


die1 = Die(6)
die1.roll_die()


## random winner list
list_draw = [1, 2, 'f', 'ff', 5, 'rr', 6, 'gg', 1, 2, 'ss']
winner_list = sample(list_draw, 4)
print(f"And the winner list iiiiis...{winner_list}!")

draw = sample(list_draw, 4)
count = 0
while draw != winner_list:
    draw = sample(list_draw, 4)
    print(draw)
    count += 1
    print(count)
    if draw == winner_list:
        print("Yeah, we found a winner!")

