summer = 'great'
if summer == 'great':
	print("Wow, the season is great")

if summer != 'bad':
	print("This is just true.")

if summer == 'great':
	print(f"{summer.upper()}")


if summer != 'dunno':
	print(f"\nWhy is this not so {summer.lower()}?")

if 5 <= 6:
	print(f"\nthis is {summer.upper()}")

great_books = ['der zauberberg', 'das kunstseidene maedchen', 'harry potter']

if 'der zauberberg' in great_books and 'harry noname' not in great_books:
	print("\nOkay, this is a good book.")


age = 19 
if age >= 18:
	print("\nYou are old enough to vote")
else:
	print("\nyou are just not old enough")

## if, elif, else
age = -6
if age >= 18:
	print("okay!")
elif age == 17:
	print("not now, but soon!")
else:
	print("Just too young.")

## hmmm... maybe better to check whether realistic age? 
age = -6
if age >= 18:
	print("okay!")
elif age == 17:
	print("not now, but soon!")
elif age < 17 and age > 0:
	print("Just too young.")

## when more than one condition can be true and you want to check all conditions, use only if 
# statements 
good_pizza = ['mushroom', 'cheese', 'tomato', 'some salt', 'some cream']

if 'some cream' in good_pizza:
	print("Adding cream.")
if 'tomato' in good_pizza:
	print("Something healthy.")



requested_toppings = ['calamaris', 'zucchini', 'cucumber', 'cheddar', 'marmelade']
if requested_toppings:
	for topping in requested_toppings: 
		print(f"Okay, we add {topping.upper()} to your pizza now.")

bah_toppings = ['marmelade', 'nutella', 'chocolate']
yummy_toppings = ['cheddar', 'feta', 'mushrooms', 'salami']

topping = 'feta'
if topping in bah_toppings:
	print(f"Ough, do you really want {topping.upper()} on your pizza???")
elif topping in yummy_toppings:
	print(f"Yes, it's a very wise choice to put {topping.upper()} on your pizza!!!")
else:
	print(f"Sorry, but {topping.upper()} is not available.")


toppings = ['feta', 'mushrooms', 'salami', 'nutella', 'bread']
for topping in toppings:
	if topping in bah_toppings:
		print(f"Ough, do you really want {topping.upper()} on your pizza???")
	elif topping in yummy_toppings:
		print(f"Yes, it's a very wise choice to put {topping.upper()} on your pizza!!!")
	else:
		print(f"Sorry, but {topping.upper()} is not available.")

