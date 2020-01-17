magicians = ['mona', 'abraham', 'mama', 'simon', 'philipp']
for magician in magicians:
	print(f"Hey {magician.title()}, that was a great...\nTRICK!")
	print(f"Cannot wait to see your next trick, {magician.title()}\n")


animals = ['turtle', 'beever', 'hamster', 'bird']
for animal in animals: 
	print(f"You are a great creature, {animal.title()}.")

print("\nAll these animals are great creatures.")


for value in range (1, 5): 
	print(value)


odd_numbers = list(range(1,11,2))
print(odd_numbers)


squares = []
for value in range (1,8):
	square = value**2
	squares.append(square)

print(squares)

squares2 = []
for value in range (1,8):
	squares2.append(value**2)
print(squares2)


## list comprehension 
square3 = [value**2 for value in range(1,9,2)]
print(square3)

multiple_3 = [value*3 for value in range(1,9)]
print(multiple_3)

## looping through a slice 
players = range(1,8,2)
[player**2 for player in players[2:3]]

player_names = ['real', 'tokyo', 'mama', 'joko']
for player in player_names:
	print("wow,") 
	print(player.title()) 
	print("is really good!\n")

## slicing 
favorite_foods = ['milk rice', 'banana pie', 'pizza', 'spaghetthi']
print("My favorite foods are:")
print(favorite_foods)

Jokos_favorite_foods = favorite_foods[:]
Jokos_favorite_foods.append('marmelade')

favorite_foods.append('ice cream')

print("Jokos favorite foods are:")
print(Jokos_favorite_foods)
print("\nMy favorite foods are")
print(favorite_foods)

print("My favorite foods are:")
for food in favorite_foods:
	print(food)

print("\nJoko's favorite foods are:")
for food in Jokos_favorite_foods:
	print(food)


## Tuples 
# tuples are immutable lists (they cannot change)
dimensions = (222, 4)
print(dimensions[0])
print(dimensions[1])

restaurant_offers = ('canneloni', 'carrot cake', 'caviar', 'cookies')
for food in restaurant_offers: 
	print("\nyummy:")
	print(food)

