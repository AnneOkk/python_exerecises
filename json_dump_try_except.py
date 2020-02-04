import json

def store_fav_num():
    """Store the user's favorite number"""
    fav_num = input("Please tell me your favorite number: ")
    fav_num = int(fav_num)
    filename = 'user_num.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)

def get_stored_fav_num():
    """Get the user's favorite number"""
    filename = 'user_number.json'
    try:
        with open(filename) as f:
            fav_nums = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_nums

def store_fav_num2():
    """Store fav num if it was not already in file"""
    fav_nums = get_stored_fav_num()
    if fav_nums:
        return fav_nums
    else:
        fav_nums = input("Please tell me your favorite number: ")
        return fav_nums
        filename = 'user_number.json'
        with open(filename, 'w') as f:
            json.dump(fav_nums, f)
            print(f"Now I know that your favorite number is {fav_nums} - I'll remember that!")

def ask_established_user():
    """ask whether it is the same user"""
    filename = 'user_number.json'
    with open(filename) as f:
        fav_nums = json.load(f)
        user_status = input(f"Is your favorite number {fav_nums} or are you a new user? Please enter 'yes' or 'new'!")
        if user_status == 'yes':
            print(f"Great, then I know your favorite number is {fav_nums} you can continue here.")
        elif user_status == 'new':
            fav_num2 = input("Alright, then please tell me your favorite number: ")
            filename = 'user_number2.json'
            with open(filename, 'w') as f:
                json.dump(fav_num2, f)
                print(f"Okay, new user, your favorite number, which is {fav_num2} has been stored!")
        else:
            print("Then what exactly do you do here?")

def get_fav_num_first_users():
    """Display the favorite number of the first user"""
    filename = 'user_number.json'
    with open(filename) as f:
        fav_1 = json.load(f)
        print(f"The favorite number of the first user is {fav_1}.")

def get_fav_num_second_users():
    """Display the favorite number of the second user"""
    filename = 'user_number2.json'
    with open(filename) as f:
        fav_2 = json.load(f)
        print(f"The favorite number of the second user is {fav_2}.")

get_stored_fav_num()
store_fav_num2()
ask_established_user()
get_fav_num_first_users()
get_fav_num_second_users()

