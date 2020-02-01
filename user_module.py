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
