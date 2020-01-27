## returns the remainder
p = 5 % 3
print(p)

## Exercise p. 117
rest_vis = input("How many people are in your dinner group?")
rest_vis = int(rest_vis)

if rest_vis > 8:
    print("You have to wait for a table")
else:
    print("Okay, you can have a seat")


mult_of_ten = input("Give me a number and I tell you whether it is a multiple of 10!")
mult_of_ten = int(mult_of_ten)

if mult_of_ten % 10 == 0:
    print("Yes, this is a multiple of 10!")
else:
    print("Nope, not a multiple of 10!")


