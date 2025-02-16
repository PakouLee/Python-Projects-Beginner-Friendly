"""
Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
1.	When the program begins, it asks the user how many rounds should be played (e.g. best of three, best of five, etc.). We will allow best of 2, 4, etc. also.
2.	Then  a random number in the range of 1 through 3 is generated (for computer’s choice).
    For this, you need to import the random library   (import random) and use the randint function (  random.randint(1, 3) )
3.	If the number is 1, then the computer has chosen rock. If the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors. (Don’t display the computer’s choice yet.)
4.	The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
    You can say something like:
    Enter 1 for rock, 2 for paper, 3 for scissors
5.	The computer’s choice is displayed. And the User’s choice is displayed.
6.	A winner is selected according to the following rules:
        * If one player chooses rock and the other player chooses scissors, then rock wins. (The rock smashes the scissors.)
        * If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper.)
        * If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.)
        * If both players make the same choice, the game is considered a draw.
7.	When the desired number of rounds are finished. Display the Wins/Draws as following:
        * Computer Wins: x
        * User Wins: x
        *Draws: x
"""

import random

listCh = ["R", "P", "S"]


userScore = 0
computerScore = 0
i = 1

chance = int(input("How many rounds will you like to play? Select a number from 1 to 5: "))
print(f"\n Great, lets begin! Best out of {chance} wins!\n")

while i <= chance:
    computerCh = str(random.choice(listCh))

    userCh = input("Enter 'R' for Rock, 'P' for Paper,and 'S' for Scissors: ").upper()

    if userCh == computerCh:
        print("\n\t Tie You Both Entered Same")

    elif userCh == "R":
        print("\n\t Computer Enter: ", computerCh)
        if computerCh == "P":
            print("\n\t You lose! Paper covers Rock")
            computerScore += 1
        else:
            print("\n\t You win! Rock smashes Scissors")
            userScore += 1
    elif userCh == "P":
        print("\n\t Computer Enter: ", computerCh)
        if computerCh == "S":
			
            print("\n\t You lose! Scissor cut Paper")
            computerScore += 1
        else:
            print("\n\t You win! Paper covers Rock")
            userScore += 1

    elif userCh == "S":
        print("Computer Enter: ", computerCh)
        if computerCh == "R":
            print("\n\t You lose! Rock smashes Scissors")
            computerScore += 1
        else:
            print("\n\t You win! Scissor cut Paper")
            userScore += 1
    else:
        print(":(")

    print(f"\n Game No:[{i}]")   
    print("\n\t ****** Total Score ******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\n\t")
    i += 1
