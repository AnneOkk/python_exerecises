## Check whether something is NOT in a list 
banned_users = ['marie', 'thomas', 'else', 'elke']
user = 'anton'
if user not in banned_users:
	print(f"Hey {user.title()}, you can write something")

## Hello Admin 
users = []

if users == []:
	print("Oh no, no users!")
for user in users:
	if user == 'admin':
		print("Hello, you are the admin")
	elif user == 'marie':
		print(f"Sorry, {user.upper()}, but you are banned.")
	else:
	 	print(f"Welcome to the game, {user.upper()}")



## user names

old = ['marie', 'thomas', 'else', 'elke']
new = ['marie', 'anne', 'else', 'nick']

for news in new:
	if news in old:
		print("This name has been used")
	else:
		print("name is available")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

for number in numbers:
	if number == 1:
		print(f"{number}st")
	if number == 2:
		print(f"{number}nd")
	if number == 3:
		print(f"{number}rd")
	if number > 3 and number <10:
		print(f"{number}th")