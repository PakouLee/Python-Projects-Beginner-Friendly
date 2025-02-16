"""
Write a program that generates a random number in the range of 1 through 100, and asks the user to guess what the number is.
 If the user’s guess is higher than the random number, the program should display “Too high, try again.”
 If the user’s guess is lower than the random number, the program should display “Too low, try again.”
 If the user guesses the number, the application should congratulate the user and then generate a new
 random number so the game can start over. If the user enters 0 for the guess, the game terminates.
"""
import random
import sys

num = random.randint(1, 5)
guess = None

while guess != num:
	guess = int(input("guess a number between 1 and 5 (to Exit, enter 0): "))

	if guess == 0:
		print("You have selected to Exit the game!")
		#break
	if guess == num:
		print("congratulations! you won!")
		#break
	elif guess < num:
		print("Too Low, Try again!")
	elif guess > num:
		print("Too High, Try again")

#NOTE: need to find a way to loop it back even if guessed the Number So that the only way to exit the loop is to press "0"

