#Name:Tessa Mazzarella Date:9/15/2015
#MadLib program

print ("Welcome to a Madlib program! Enter in words when asked and . . . \nBAM! \nYou have a silly paragraph!")


adverb1 = input("Enter an adverb > ")
girls_name = input("Enter any girl\'s name > ")
illness = input("Enter a type of illness > ")
adjective1 = input("Enter in an adjective > ")
adjective2 = input("Enter another adjective > ")
silly_word = input("Enter any silly word you can think of > ")
place = input("Enter your favorite place to go to > ")
number = input("Enter a random number > ")
noun_plural1 = input("Enter a plural noun > ")
noun_plural2 = input("Enter another plural noun > ")
friend_name = input("Enter in one of your friend\'s names > ")


#input is done. Now put in the actual paragraph
#break up the inputs from the story with a '-'


print ("-" * 25)


print ("\nSchool Note")

print ("\nDear Nurse", adverb1 + ",")

#Need to figure out how to make the line below indent

print ('\t' + girls_name + " will not be attending school today.")

print ("She has come down with a case of", illness + " and has a \nhorrible", adjective1 + " fever.")  

print ("\tWe have made an appointment with the" , adjective2 + " \nDr." , silly_word + " who studied for many years in", place)

print ("and has", number + " degress in pediatrics." + " He will send \nyou all the", noun_plural1 + " you need. In the meantime, would you")

print ("send her", noun_plural2 + " home with", friend_name + "?")

print ("\nThank you!")

print ("Mom") 

