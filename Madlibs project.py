#Cate Zwiercan  9/10/15
#this program inputs information that the user inputed for the prompts that were given
#into the paragraph that was created by the developer.

#introduction to the program
user_name=input("What is your name?")
print("Hey "+user_name.capitalize()+"!")
print("Are you bored at home or have a long trip in the car?\nPlay this game of MadLibs and have a hilarious story to laugh at with your friends and family!")
print("All you have to do is enter in a word that matches the descrption that we give you!")
print("Sound easy? Great, lets get started!\n\n") 
#enter in a name
name_1=input("type in a name") 
#enter in another name
name_2=input("type in a name")
#enter in a number
number=input("type in a number") 
#enter in a game
game=input("type in a name of a game") 
#enter in an adjective
adjective_1=input("type in an adjective") 
#enter in verb ening in "ing"
verb_ing_1=input("type in a verb ening in \"ing\"")
#enter in an animal
animal=input("type in an animal") 
#enter in an adjective
adjective_2=input("type in an adjective") 
#enter in an adjective
adjective_3=input("type in an adjective") 
#enter in verb ending in "ing"
verb_ing_2=input("type in a verb ening in \"ing\"")
#enter in place
place=input("type in a place")
#enter in verb
verb=input("type in a verb")
#mad libs story with user input
print()
print("Great job "+user_name.capitalize()+"! You\'re all finished now. Here is your Madlibs!")
print()
print("My Vacation")
print()
print("Last month, I went to "+name_1.capitalize()+"\'s World with my friend "+name_2.capitalize()+".")
print("We travelled "+number+" hours to get there and played "+game.capitalize()+" to pass the time.")
print("Once there, we saw "+adjective_1+" people "+verb_ing_1+" everywhere.")
print("There were also people dressed in  "+animal+" costumes that looked very "+adjective_2+".")
print("We went to some "+adjective_3+ " rides where my friend nearly fell off and had to be "+verb_ing_2+" to the first aid station.")
print("Next year I want to go to "+place+ " where we can "+verb+ " instead.")
print("\nCongratulations you have finished your MadLibs game! Enjoy!") 
