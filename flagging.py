prompt = "\nTell me how to use flagging"
prompt += "\nEnter quit to stop"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    elif message == "parrot":
        active = False
    else:
        print(message)


## using break to exit a loop
user_answer = "\nplease enter the cities you like most"
user_answer += "\nenter quit to exit the program"

while True: # while True will run forever until break statement
    city = input(user_answer)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

## using continue in a loop
current_number = 0
while current_number < 20:
    current_number += 1
    if current_number % 4 == 0:
        continue

    print(current_number)

## Exercise p. 123
prompt = "\nPlease enter a pizza topping"
prompt += "\n If you are ready, type 'ready'!"
pizza_list = []

active = True
while active:
    pizza = input(prompt)
    if pizza != 'ready':
        print(f"You've added {pizza} to your pizza!")
    if pizza == 'ready':

        print("Well done!")
        active = False

## cost of movie ticket
age = input("Tell me your age!")
age = int(age)

if age < 3:
    print("Your ticket is free!")
elif age >3 & age <12:
    print("Your ticket costs 12 dollar")
else:
    print("Your ticket is suuuper expensive because you are so old!")


## Three exits
number = 0

while number < 30:
    number += 1
    if number % 2 == 0:
        print(f"{number} is even!")
    elif number % 4 == 0:
        print(f"{number} is a multiple of four")
    elif number % 3 == 0:
        go = input("Give me sth")
        print(go)
    else:
        print(f"{number} is sth else")



active = True
promt = "Tell me sth \nSay quit if you wanna quit"
while active:
    po = input(promt)
    print(po)
    if po == 'quit':
        active = False


promt = "\nTell me sth \nSay quit if you wanna quit"
while True:
    po = input(promt)
    print(po)
    if po == 'quit':
        break















