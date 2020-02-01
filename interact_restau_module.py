from restaurant_module import Pizza_Hut
from user_module import User
from restaurant_module import Sec_Privileges


my_restaurant = Restaurant('Bei Anne', 'Vegetarian Specialities')
print(my_restaurant.describe_restaurant())

pizza_hut = Pizza_Hut('Pizza Hut', 'American')
pizza_hut.update_prices()


# define an admin
print("\n")
admin = Admin('Anne', 'Kleine', '28', 'female', 'blue')
admin.show_privileges()