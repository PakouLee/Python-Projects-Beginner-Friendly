"""
Create a short story using Madlibs!
    * Give users prompts to select an animal as the protagonist of the story.
    * Allow users to give a name to the protagonist.
    * have the user help make a cake and smoothie for their best friend Speedy's birthday.
    * Pick a number for Speedy's birthday age.
    * End the story by singing the birthday song for Speedy.
"""


# Introduce the story.
print("Hi friend, help me write a story about Speedy the turtle's birthday surprise and "
      "choose what kind of cake Speedy will get on his birthday.")

#User Input.
animal = input("Enter a animal (cat, dog, duck): ")
animal_name = input("Enter your animal name: ")
speedy_birthday = input("Enter a number for Speedy's Age: ")
cake_fruit = input("Pick a fruit for Speedy's cake: ")
smoothy_fruit = input("Pick a fruit for Speedy's surprise smoothy: ")

#The Story:
story_intro = (f"Today is {animal_name} the {animal}'s best friend Speedy's {speedy_birthday} birthday. "
               f"{animal_name} has decided to surprise Speedy with a special cake and smoothy! "
               f"{animal_name} checked the refrigerator and realized that there was not have enough "
               f"fruits for Speedy’s surprise cake and smoothy." )

story_body1 = (f"{animal_name} decided to go to the grocery store and buy the needed fruit for the cake and smoothy. "
              f"To make sure that {animal_name} did not miss anything, a list was created. "
              f"Today is {animal_name} the {animal}'s best friend's birthday. ")

grocery_List = (f"\nThe list reads as follows:\n"
              f"\n\t 1. Cake flour, "
              f"\n\t 2. whipped cream, "
              f"\n\t 3. Ice cream, "
              f"\n\t 4. {cake_fruit}, "
              f"\n\t 5. {smoothy_fruit}, "
              f"\n\t 6. Juice \n")
story_body2 = (f"{animal_name} hopped on the bike waiting outside and headed to the store. "
               f"After arriving home form the grocery story {animal_name} ran into the kitchen "
               f"and started on making the {cake_fruit} cake and {smoothy_fruit} smoothy. "
               f"\nOnce {animal_name} put the cake into the oven, {animal_name} "
               f"started to make the {smoothy_fruit} smoothy. When the smoothy was done, {animal_name} "
               f"put the {smoothy_fruit} smoothy to the side and grabbed the cake out of the oven. "
               f"\nOnce the cake was cooled off, {animal_name} added the whipped cream and "
               f"extra {cake_fruit} and added to the top of the cake. , {animal_name} then grabbed "
               f"the finished cake and smoothy put it into a basket and walked out of the house to "
               f"go to meet up with Speedy at the park.")


story_end = (f"\n{animal_name} found Speedy on the playing on th swing. {animal_name} Took the cake out of the basket"
             f"and lit the candle on the cake. Let's help {animal_name} wish Speedy Happy Birthday by sing the birthday song.")

birthday_song = f"\nHappy birthday to you, happy birthday to you, happy birthday to dear SPEEDY, happy birthday to you!!!"

#Display the Story with all user input

print("\nHere's a story about how you help celebrate Speedy the Turtle's birthday:  \n")
print(story_intro)
print(story_body1)
print(grocery_List)
print(story_body2)
print(story_end)
print(birthday_song)


