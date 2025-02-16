"""
Write a program that generates a selects a number within the range that is determined by the user. Then Asks the user to guess what the number is.
The user will be given a select number of guesses based on range that they choose. This should be calculated and not set by the programmer.
 If the user’s guess is higher than the random number, the program should display “Too high, try again.”
 If the user’s guess is lower than the random number, the program should display “Too low, try again.”
 If the user guesses the number, the application should congratulate the user and then generate a new
 random number so the game can start over. If the user enters 0 for the guess, the game terminates.
"""
import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")


