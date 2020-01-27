user = {
	'username' : 'kiwi',
	'first': 'Nick', 
	'last' : 'kytz'
}

for key, value in user.items():
	print(f"\nKey: {key}")
	print(f"\nValue: {value}")

christmas = {
	'mama' : 'some gardenstuff',
	'simon' : 'a pullover', 
	'papa' : 'a hat' 
}

for person, present in christmas.items():
	print(f"\nI know that {person.upper()} will get {present.upper()}")

## looping only though the keys:
for person in christmas.keys():
	print(f"\n{person.title()}")


## combine it with an if function 
possible = ['summer', 'winter']
nice_places = {
	'summer' : 'norway', 
	'winter' : 'hawaii', 
	'spring' : 'canada',
	'autumn' : 'canada'
}

for season, place in nice_places.items():
	print(f"in {season}, I like to travel to {place}")

for season in nice_places.keys(): 
	print(f"\nI do so much like the {season.upper()}!")

	if season in possible:
		place = nice_places[season].title()
		print(f"Oh, how nice, I can go to {place} in {season}")

## sort the list before
for season in sorted(nice_places.keys()): 
	print(f"\nI do so much like the {season.upper()}!")

	if season in possible:
		place = nice_places[season].title()
		print(f"Oh, how nice, I can go to {place} in {season}")

## print just the values
print("The following places have been mentioned:")
for place in sorted(nice_places.values()):
	print(place.title())


## use a set to only print unique values
for place in set(nice_places.values()):
	print("\nThis is unique:")
	print(place.title())


## dictionary exercise
no_pairs = ['robert', 'angela', 'anne']

some_people_dict = {
	'robert' : 'banana',
	'paul' : 'apple',
	'angela' : 'strawberry',
	'marie' : 'raspberry', 
	'simon' : 'pear', 
	'anne' : 'grapes'
}

for person in some_people_dict: 
	print(f"Oh, it's nice that you are here, {person.upper()}")
	if person in no_pairs:
		fruit = some_people_dict[person].title()
		print(f"but you didn't bring {fruit}!")


## A list of dictionaries 
aliens = []

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print(len(aliens))


## change the color of the first three aliens 
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'

print(aliens[:3])

## Store a list in a dictionary 
pizza = {
	'dough' : 'full-grain',
	'toppings' : ['mushrooms', 'cheese', 'tomato'],
	'order' : 'tonight'
}

print(f"You ordered a {pizza['dough']}-pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

## you can call the list inside the list with another for loop
favorite_places = {
	'early_morning' : ['the forrest'],
	'midday' : ['the swimming pool', 'a cozy couch'],
	'afternoon' : ['the green hill', 'on a mountain'],
	'evening' : ['the cinema']
}

for times, places in favorite_places.items():
	if len(places) == 1:
		print(f"\nthe time is: \n \t{times}"
			" \nand the according place is:")
		for place in places:
			print(f"\t{place}")
	else:
		print(f"\nthe time is: \n \t{times}"
			" \nand the according places are:")
		for place in places:
			print(f"\t{place}")


## store a dictionary in a dictionary 
offices = {
	'371' : {
		'one' : 'anne',
		'two' : 'burkkard'},
	'374' : {
		'one' : 'antje',
		'two' : 'kiki'},
	'378' : {
		'one' : 'elissa', 
		'two' : 'max'}
	}

for rooms, info in offices.items():
	print(f"the room {rooms} is occupied by:")
	person_one = info['one'] 
	person_two = info['two']
	print(f"{person_one} and {person_two}")


## store a dictionary in a dictionary 
offices = {
	'371' : {
		'one' : 'anne',
		'two_first' : 'burkkard',
		'two_last' : 'woertler'},
	'374' : {
		'one' : 'antje',
		'two_first' : 'kiki',
		'two_last' : 'no idea'},
	'378' : {
		'one' : 'elissa', 
		'two_first' : 'max',
		'two_last' : 'agostini'}
	}


valid_users = ['burkkard', 'antje']
for rooms, info in offices.items():
	print(f"\nthe room {rooms} is occupied by:")
	person_one = info['one'] 
	person_two_full = f"{info['two_first']} {info['two_last']}"
	if person_one in valid_users:
		print(f"{person_one} and {person_two_full}")
	else: 
		print(f"Sorry, this room is already occupied! But {person_two_full} is still here")




import sys
print(sys.version)


