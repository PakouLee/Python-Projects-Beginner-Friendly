"""
In RandomNumberGuess, we tried to find guess what is the number based on the computer's selection.
Let's reverse the guess and have the computer guess our number instead.
Write a program that will allow the user to tell the computer if the computer's guess is too high,
too low or if the guess is right. Allow users to set upper and lower limits for the computer to
guess the number.
"""
import random

#random.randint(a,b) returns a random integer N such that a<= N <=b. Alias for randrange(a,b+1). "a" and "b" are
#the parameters for this argument.

print(f"\nWelcome! Pick a number and let the computer try to guess your number. Give the computer a range by using lower and upper bonds. \n")
# Taking Inputs
lower = int(input("Enter Lower bound: "))

# Taking Inputs
upper = int(input("Enter Upper bound: "))

#define the function.
def computer_guess(x):
    low = lower
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        #the user will input h,l, or c to let the computer know if the computer's guess is too high, low, or is correct.
        #pro-tip: adding '.lower' to the end will force the user's input to be lower case since we wrote our function with a lower case 'c'.
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback =='h':
        # if guess is too high, adjustment to the upper bound will need to be made.
            high=guess - 1
        # use elif because feedback can only be either too high or too low it can't be both.
        elif feedback == 'l':
            low = guess + 1
        #Note: we don't need a statement for when the guess is correct, because the while loop will take care of it and the computer will then exit the loop.
    print(f"You are correct! The correct number is {guess}!")


computer_guess(upper)


