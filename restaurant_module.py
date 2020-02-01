"""The restaurant module"""

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

class Pizza_Hut(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.prices = 10
    def update_prices(self):
        self.prices += 5
        print(f"\nAt pizza hut, the prices have been raised and now a pizza costs {self.prices} Euros")


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, fav_color):
        super().__init__(first_name, last_name, age, gender, fav_color)
        self.privileges = ['can add post', 'can ban user', 'can edit posts', 'can write blog entries']
        self.privileges_new = Sec_Privileges()
    def show_privileges(self):
        print("The first admin has the following privileges:")
        for privileges in self.privileges:
            print(f"- {privileges}")

class Sec_Privileges:
    def __init__(self):
        self.privileges_new = ['move the blue elephant', 'paint the rabbit', 'enjoy the sun', 'dance in the rain']
    def show_privileges_new(self):
        print("\nThe second admin has the following privileges:")
        for privilege in self.privileges_new:
            print(f"- {privilege}")

