## Exercises
print("Please enter two numbers that will be added!")
while True:
    print("Enter 'q' to quit")
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    sec_num = input("\nsecond number: ")
    if sec_num == 'q':
        break
    try:
        answer = int(first_num) + int(sec_num)
    except ValueError:
        print("Sorry, both have to be numbers!")
    else:
        print(answer)


cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

cat_names = ['Gundula', 'Margarete', 'Hollunder']
dog_names = ['Paolo', 'Sirikane', 'Manila']

with open(cats_file, 'w') as cats:
    for name in cat_names:
        cats.write('%s\n' % name)

with open(dogs_file, 'w') as dogs:
    for name in dog_names:
        dogs.write('%s\n' % name)


with open('dogs.txt') as dogs:
    try:
        dog_names = dogs.read()
    except FileNotFoundError:
        print("The file 'dogs.txt' was not found!")
    else:
        print(dog_names)

try:
    with open('cats.txt') as cats:
        cat_names = cats.read()
except FileNotFoundError:
    print("The file 'cats.txt' was not found!")
else:
    print(cat_names)

try:
    with open('elephants.txt') as eles:
        ele_names = eles.read()
except FileNotFoundError:
    pass
else:
    print(ele_names)

with open('gutenberg_ex.txt') as guti:
    content = guti.read()

print(content)
content.count('love')
content.lower().count('love')
content.lower().count('love ')

content.count('and')
content.lower().count('and')

