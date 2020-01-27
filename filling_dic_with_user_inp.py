responses = {}

polling_active = True

while polling_active:
    name = input("What is your name?")
    street = input("In which street do you live?")
    responses[name] = street
    repeat = input("Would you like to continue?")
    if repeat == 'no':
        polling_active = False

print("\nPoll_results:")
for name, street in responses.items():
    print(f"\n{name} lives here: {street}.")


## Exercises p. 127
sandwiches = ['tuna sandwich', 'avocado sandwich', 'salmon sandwich', 'pesto sandwich', 'tuna sandwich', 'tuna sandwich',
              'tuna sandwich']
made_sand = []

print("no tuna sandwich anymore!")
while 'tuna sandwich' in sandwiches:
    sandwiches.remove('tuna sandwich')

while sandwiches:
    new = sandwiches.pop()
    print(f"I make you a {new}")
    made_sand.append(new)

print(f"\nI made you these sandwiches:")
print(made_sand)


polling_active = True
responses = {}
while polling_active:
    next_place = input("Where would you like to travel next?")
    with_whom = input("Who should come with you?")
    responses[next_place] = with_whom
    more = input("Do you want to be asked more?")
    if more == 'no':
        polling_active = False
        print("That's it for today!")

print("\nDream place results:")
for next_place in responses.items():
    print(f"I want to go to {next_place} with {with_whom}")
