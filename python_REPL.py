Python 2.7.17 (default, Nov  7 2019, 10:07:09) 
[GCC 7.4.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> magic_word = "giraffe"
guess = ""
count = 0
guess_limit = 3
out_of_guesses = False 

while guess != magic_word and not(out_of_guesses):
	if count < guess_limit:
		guess = input("Enter guess: ")
		count += 1
	else: 
		out_of_guesses = True

if out_of_guesses:
	print("Out of guesses, YOU LOSE!")
else: 
	print("You win!")
>>> >>> >>> >>> >>> >>> ... ... ... ... ... ... Enter guess: Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "<string>", line 1
    if out_of_guesses:
     ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    print("Out of guesses, YOU LOSE!")
    ^
IndentationError: unexpected indent
>>>   File "<stdin>", line 1
    else: 
       ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
    print("You win!")
    ^
IndentationError: unexpected indent
>>> 

>>> 
>>> magic_word = "giraffe"
guess = ""
count = 0
guess_limit = 3
out_of_guesses = False 

while guess != magic_word and not(out_of_guesses):
	if count < guess_limit:
		guess = input("Enter guess: ")
		count += 1
	else: 
		out_of_guesses = True

if out_of_guesses:
	print("Out of guesses, YOU LOSE!")
else: 