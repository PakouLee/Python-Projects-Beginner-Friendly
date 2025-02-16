"""
You will create a program that generates the lyrics of the children’s song Old MacDonald had a farm.
The user will supply the names and sounds for the animals and when they are finished you will print the lyrics to the song.
The user should be able to enter as many pairs of names and sounds as they wish before the lyrics are shown.
Your program must define a module for the lyrics that accepts 2 parameters as input, as shown in the Modules unit video.
You will collect user input in a loop and store the pair of answers in a list. Store these lists inside another list.
Use some special input to indicate that the user is done entering data. Once the user has completed their data entry,
output the lyrics one verse at a time by working through your list and calling the module.
Print a blank link between each verse.
"""

import sys
lyrics_list = []
i = 1

Num_Of_Animals = int(input("How many animal would you like to have? "))

while i <= Num_Of_Animals :
	for song in range (Num_Of_Animals):
		animal = input("Please Input an animal (or -1 to quit): ")
		if animal == '-1':
			sys.exit(0)
		sound = input("Please Input Sound for animal(or -1 to quit): ")
		if sound == '-1':
			sys.exit(0)     
		Song_lyrics = "\n Old Macdonald had a farm, E- I- E- I- O," " And on that farm he had a %s, E- I- E- I- O." " With a %s - %s here, and a %s - %s there," " here a %s, there a %s, everywhere a %s - %s" " Old Macdonald had a farm, E- I- E- I- O!" % (animal, sound, sound, sound, sound, sound, sound, sound, sound)
		lyrics_list.append(Song_lyrics)
	for Song_lyrics in lyrics_list:
		print(Song_lyrics)	
		i += 1
