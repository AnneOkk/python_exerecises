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


