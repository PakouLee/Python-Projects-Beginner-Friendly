"""
You will create a program that generates the lyrics of the children’s song Old MacDonald had a farm.
The user will supply the names and sounds for the animals and when they are finished you will print the lyrics to the song.
"""
import sys

lyrics_list = []

for song in range (3):
    animal = input("Please Input an Animal: ")
    if animal == '-1':
        sys.exit(0)
    sound = input("Please Input a Sound: ")
    if sound == '-1':
        sys.exit(0)     
    
    lyrics = "Old Macdonald had a farm, E- I- E- I- O," " And on that farm he had a %s, E- I- E- I- O." " With a %s - %s here, and a %s - %s there," " here a %s, there a %s, everywhere a %s - %s" " Old Macdonald had a farm, E- I- E- I- O!" % (animal, sound, sound, sound, sound, sound, sound, sound, sound)
    lyrics_list.append(lyrics)

for lyric in lyrics_list:
    print(lyric)
    
   
