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

