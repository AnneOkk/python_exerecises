current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


## Letting the user choose when to quit

prompt = "\n Tell me something!"
prompt += "\n enter quit to end the program"

message = "kukuk" # this is here so python has sth to check first time
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"\tvery well, {message} is a good choice!")