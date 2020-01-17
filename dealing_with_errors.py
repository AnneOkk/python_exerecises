try:
	value = 10/0
	number = int("Enter a number: ")
	print(number)
except ZeroDivisionError:
	print("divided by zero")
except ValueError:
	print("invalid input")


try:
	value = "hh"
	number = int("Enter a number: ")
	print(number)
except ZeroDivisionError as err:
	print(err)
except ValueError as VE:
	print(VE)


## read content of other files 
new = open("translator.py", "r")
# read multiple lines
print(new.readline())
print(new.readline())

## read line one:
print(new.readline()[1])

for employee in new.readline():
	print(employee)

# close it afterward! 
new.close()

