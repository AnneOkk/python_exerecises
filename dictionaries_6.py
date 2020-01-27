## define a dictionry
alien = {'color' : 'red', 'points' : '5'}
print(alien)

alien['x_pos'] = 0
alien['ypos'] = 25
print(alien)

## moving the alien around
alien['speed'] = 'medium'

if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

print(f"The alien's new position is {alien['x_pos'] + x_increment}")


## the delete function del
del alien['color']
print(alien)