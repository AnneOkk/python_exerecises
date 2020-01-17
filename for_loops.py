## With string 

for letter in "Elephant": 
	print(letter)

## Arrays 
friends = ["Jimmy", "Maren", "Karol"]
for friend in friends: 
	print(friend)


## number range 
ranger = range(1,10)
for t in ranger:
	print(t)

## Arrays 
friends = ["Jimmy", "Maren", "Karol"]
for index in range(len(friends)): 
	print(friends[index])


for index in range(5):
	if index == 0:
		print("first iteration")
	else: 
		print("not first")


print(2**3) 

## create a function 
def raise_to_power(base_number, power_number):
	result = (base_number**power_number)
	print(result)


## ...ooor... 
def raise_to_power2(base_number, power_number):
	result = 1
	for index in range(power_number):
		result = result * base_number
	return result 

print(raise_to_power2(2, 3))
print(raise_to_power(2, 3))

print(raise_to_power2(5, 7))
print(raise_to_power(5, 7))

print(raise_to_power2(8, 9))
print(raise_to_power(8, 9))

number_grid = [1,2,3,4,6]

## lists in lists
number_g = [
	[1,2,3],
	[5,6,7],
	[7,8,9],
	[0]
]

print(number_g[0][0])
print(number_g[1][2])

for row in number_g:
	print(row)

for row in number_g:
	for col in row: 
		print(col)


