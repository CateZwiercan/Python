#cate Zwiercan
#09/24/15
#the purpose of this program is for users to ask questions to the magic 8 ball and get a repsonse.

#welcome and Introduce the user to the program
import random

name=input("What is your name? ")

print("Hello "+ name.capitalize() + "! Welcome to the Magic 8 ball machine.\nThe Magic 8 ball will tell you all you want to know. Ask a question and it will give you an answer to your future...\n\n") 

#input the question

response="yes" or "no"

while response=="yes": 
    input("\nThou may now ask your question ") 

#give an answer
#need to input random with 8 responses

    answer= random.randint(1,8)

    if answer==1:
        print("As I see it, yes")
    elif answer==2:
        print("Sorry to let you down but it\'s not looking good")
    elif answer==3:
        print("The stars say no")
    elif answer==4:
        print("Count on it")
    elif answer==5:
        print("Focus and ask again")
    elif answer==6:
        print("Absolutley")
    elif answer==7:
        print("No doubt about it")
    elif answer==8:
        print("Sorry but no")
    else:print("You broke it, you have to pay me for repairs.")

    response=input("Do you want to play again? ") 



