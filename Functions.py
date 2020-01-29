def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

def like_doing(person, place):
    print(f"I would love to go to {place.title()} with {person.title()} as soon as posible")

like_doing("Tim", "Bali")

## using keyword arguments
def favorite_days(season, daytime):
    print(f"What I like the most are {daytime} in {season}.")

favorite_days(season='summer', daytime='evenings')

def favorite_cities(city, season = 'summer'):
    print(f"My favorite city is {city} and I would like to visit it in {season}")

favorite_cities("Barcelona", 'winter')

def get_full_name(first_name, last_name):
    full_name = (f"{first_name } {last_name}")
    return full_name.title()

name = get_full_name('Anne ', 'Kleine')
print(name)

## Returning a dictionary
def build_person(first_name, last_name):
    person = {'first' : first_name, 'last' : last_name}
    return person
print(build_person('anne', 'kleine'))

## optionally add another key-value pair
def build_person(first_name, last_name, age =None): # none as placeholder -> can evaluate to False in conditional statem.
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person
print(build_person('anne', 'kleine', age = 28))

## Using a function in a while loop
def build_person(first_name, last_name, age =None): # none as placeholder -> can evaluate to False in conditional statem.
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

while True:
    print("\nPlease enter your user name!")
    print("\tEnter 'q' to exit the game!")
    f_name = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break
    full_name = get_full_name(f_name, l_name)
    print(f"Hello, {full_name}, welcome to the game!")


### city-country pairs
def city_country(city, country):
    print(f"Well, {city} is a city in {country}!")

city_country('Berlin', 'Germany')


## favorite music dict
while True:
    print("Okay, what's your favorite music stuff?")
    print("You can enter q to quit!")
    artist = input("My favorite arist: ")
    if artist == 'q':
        break
    album = input("my favorite album: ")
    if album == 'q':
        break
    music = {'artist' : artist, 'album' : album}
    print(music)


## Passing a list to a function:
def greet_users(usernames):
    for name in usernames:
        msg = f"Welcome, {name.title()}!"
        print(msg)

names = ['hannah', 'ty', 'maria']

greet_users(names)

## Modifying a list in a function:
nice_places = ['bali', 'thailand', 'mosambique']
seen_places = []
while nice_places:
    current_places = nice_places.pop()
    print(f"Okay, I plan to visit {current_places.title()} soon!")
    seen_places.append(current_places)
print("the following places will be visited:")
for seen_place in seen_places:
    print(seen_place)


## make this into two functions!
nice_places = ['the best coffee place in town', 'the museum', 'the spa', 'plaza sportiva']
seen_places = []
def places(nice_places, seen_places):
    while nice_places:
        current_places = nice_places.pop()
        print(f"I plan to visit {current_places}")
        seen_places.append(current_places)

def show_places(seen_places):
    print("\nThe following places will be visited soon: ")
    for seen_place in seen_places:
        print(seen_place)


places(nice_places, seen_places)
show_places(seen_places)

## Exercise
new_food = ['cucumber', 'strawberry cake', 'mustard soup', 'lasagna']
eaten_food = []
def food(new_food, eaten_food):
    while new_food:
        current_food = new_food.pop()
        print(f"I want to eat this soon: {current_food}.")
        eaten_food.append(current_food)

def show_food(eaten_food):
    print("\nThis will be eaten soon: ")
    for food in eaten_food:
        print(food)

food(new_food, eaten_food)
show_food(eaten_food)

## Passing an arbitrary number of arguments:
def make_pizza(country, *toppings):
    if country == 'usa':
        country = country.upper()
    else:
        country = country.title()
    print(f"\nMake yummy pizza from {country} with the following toppings: ")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza("usa", 'peperoni')
make_pizza("Italia", 'cheese', 'calzone', 'tomato', 'avocado')


## Using arbitrary keyword arguments:
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'switzerland',
                             field = 'physics')

print(user_profile)


def buy_next(item, date, **other):
    other['item_1'] = item
    other['date_1'] = date
    return(other)

buy = buy_next('pullover', 'next week', color = 'blue', size = 'cozy')
print(buy)

