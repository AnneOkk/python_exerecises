## Moving Items from one list to another
unconfirmed = ['alice', 'mama', 'peter', 'nick', 'freddi']
confirmed = []

while unconfirmed:
    current = unconfirmed.pop()

    print(f"Verifying user: {current.title()}")
    confirmed.append(current)

print("\n The following users have been confirmed:")
for confi in confirmed:
    print(confi.title())


pets = ['dog', 'lion', 'goldfish', 'parrot', 'lion', 'lion', 'lion']
while 'lion' in pets:
    pets.remove('lion')

print(pets)