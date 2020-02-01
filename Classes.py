class Restaurant:
    """A simple example to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Describing the attributes"""
        attributes = f"The restaurant has two attributes: It's name is {self.restaurant_name}"
                           f"and its cuisine type is {self.cuisine_type}!"
        return attributes
    def open_restaurant(self):
        open = "The restaurant is open!"
        return open


restaurant = Restaurant('Ragazzi', 'Italian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())


class User:
    def __init__(self, first_name, last_name, age, gender, fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.fav_color = fav_color
    def describe_user(self):
        description = f"User characteristics:\n" \
                      f"- Name = {self.first_name} {self.last_name}\n" \
                      f"- Age = {self.age}\n" \
                      f"- Gender = {self.gender}\n" \
                      f"- Favorite color = {self.fav_color}"
        return description
    def greet_user(self):
        greet = f"\nNice to have you here, {self.first_name} {self.last_name}"
        return greet

user1 = User('Anne-Kathrin', 'Kleine', '28', 'female', 'blue')
print(user1.describe_user())
print(user1.greet_user())

## Exercises
class Restaurant:
    """A simple example to represent a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Describing the attributes"""
        attributes = f"The restaurant has two attributes: It's name is {self.restaurant_name} and its cuisine type is {self.cuisine_type}!"
        return attributes
    def open_restaurant(self):
        open = "The restaurant is open!"
        return open
    def read_number_served(self):
       print(f"The number of guests that have been served is {self.number_served}")
    def update_guest_number(self, number):
        self.number_served = number
    def increment_guest_number(self, guests):
        self.number_served += guests



restaurant = Restaurant('Ragazzi', 'Italian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
restaurant.read_number_served()

restaurant.number_served = 2
restaurant.read_number_served()

restaurant.update_guest_number(3)
restaurant.read_number_served()

restaurant.increment_guest_number(4)
restaurant.read_number_served()



class User:
    def __init__(self, first_name, last_name, age, gender, fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.fav_color = fav_color
        self.login_attempts = 0
    def describe_user(self):
        description = f"User characteristics:\n" \
                      f"- Name = {self.first_name} {self.last_name}\n" \
                      f"- Age = {self.age}\n" \
                      f"- Gender = {self.gender}\n" \
                      f"- Favorite color = {self.fav_color}"
        return description
    def greet_user(self):
        greet = f"\nNice to have you here, {self.first_name} {self.last_name}"
        return greet
    def update_login_attempts(self, logins):
        self.login_attempts = logins
        print(f"\nThe number of login attempts is {self.login_attempts}!")
    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print(f"\nThe number of attempts has now reached {self.login_attempts}!")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nThe number of attempts was reset to {self.login_attempts}!")

user1 = User('Anne-Kathrin', 'Kleine', '28', 'female', 'blue')
print(user1.describe_user())
print(user1.greet_user())

user1.update_login_attempts(3)
user1.increment_login_attempts(4)
user1.reset_login_attempts()


