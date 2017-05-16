#Cate Zwiercan
#word jumble
#
#the computer picks a random word and then "jumbles"it
#the player has to guess the original word

import random

#create a sequence of words to choose from
WORDS= ("aquafina","snapple","gatorade", "trumoo", "fanta", "pepsi")

#create corresponding hints
HINTS=("This is a water bottle brand and also sounds like a name.",
       "This is a popular Ice Tea brand",
       "A lot of athletes drink this",
       "Children love to have this with breakfast in the morning\n and its very chocolaty",
       "This is a very tangy, orange drink",
       "It's not coke it's...")

#pick one owrd randomly from the tuple
word=random.choice(WORDS)
index=WORDS.index(word)

#create a varibale to use later to see if the guess is correct
correct=word

#create an empty jumble word
jumble=""

#while the chosen word has letters in it
while word:
 
#extract a random letter from the chosen word
       position=random.randrange(len(word)) 
#add the random letter to the jumble word
       jumble +=word[position]
       word= word[:position] + word[(position + 1):]

       
     
#start the game
print( """
                Welcome to Jumble Gym!

          Unscramble the letters to make a word.
       All of the words are different beverage brands.
         (press enter key at prompt to quit)
        
        """)

#insert while loop to restart the game if she wants to       

print("The Jumble is: ",jumble)

guess= input("\nYour guess: ")

count=1

if guess=="":
       print("\nThe answer was ",correct,".")
       count=1
while guess != correct and guess !="":
       hint=input("sorry, that is not the right word. Would you like a hint? ")
    
#give hints
       if hint=="yes" or hint=="Yes":
              print(HINTS[index])
          
       print("Try again Old Sport")
       guess=input("\nYour guess: ")
       count=count+1
    
       if guess==correct:
              print("Thats it! You guessed it. It took you", count,"tries.\n")
           
#ask if they want to play again    
      

#add the game over signal
print(
        """
         _____      ___       ___  ___   _______
        /  ___|    /   |     /   |/   | |   ____| 
        | |       /    |    / /|   /| | |  |__
        | |  _   /  /| |   / / |__/ | | |   __|
        | |_| | /  ___ |  / /       | | |  |____
        \_____//_/   |_| /_/        |_| |_______|
        

         _____    _     _   ______   ______
        /  _  \  | |   / / | _____| |  _   \
        | | | |  | |  / /  | |__    | |_|  |
        | | | |  | | / /   |  __|   |  _   /
        | |_| |  | |/ /    | |____  | | \  \
        \_____/  |___/     |______| |_|  \__\
        

        """
     )
#prompt them to exit
input("\n\n\n\nPress enter key to exit") 
