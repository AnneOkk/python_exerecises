with open('test.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())

## Exercise
with open('python_learned.txt') as learnt_stuff:
    learnt = learnt_stuff.read()

print(learnt)

with open('python_learned.txt') as learnt_stuff2:
    for line in learnt_stuff2:
        print(line.strip())

with open('python_learned.txt') as learnt_stuff3:
    lines = learnt_stuff3.readlines()

for line in lines:
    print(line.strip())

print(lines)
for line in lines:
    new_line = line.replace('learned', 'found out')
    print(new_line.strip())

## Writing to an empty file
guests = 'guest_list.txt'

invites = []

while True:
    print("Enter q to quit!")
    invitee = input("Please enter your name: ")
    invites.append(invitee)
    if invitee == 'q':
        break

with open(guests, 'w') as guest_list:
    for listitem in invites:
        guest_list.write('%s\n' % listitem)


guest_fav_dest = 'guest_fav_dest.txt'

fav_dest = []
while True:
    print("Enter q to quit!")
    invitee = input("Please enter your name: ")
    if invitee == 'q':
        break
    favorites = input(f"Welcome {invitee.title()}, now please enter your favorite place in the world: ")
    fav_dest.append(favorites)


with open(guest_fav_dest, 'w') as favor_dest:
    for listitem in fav_dest:
        favor_dest.write('%s\n' % listitem)


with open(guest_fav_dest, 'a') as favor_dest:
    reasons = []
    while True:
        print("Enter q to quit")
        reason = input("Just tell me why you like Groningen")
        if reason == 'q':
            break
        reasons.append(reason)
    for listitem in reasons:
        favor_dest.write('%s\n' % listitem)





