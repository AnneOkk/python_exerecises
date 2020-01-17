### can be used in REPL!

magic_word = "giraffe"
guess = ""
count = 0
guess_limit = 4
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