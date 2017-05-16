#Cate Zwiercan
#10/15/15

import random

# This program is to generate unsernames and passwords for the user

#Welcome the user and explain what this does
print("Hi! If you are the kind of person that has trouble coming up with new passwords,this is the program for you.\nHere we will make a username and password for you by using your first and last name.") 
print("Sound easy? Great let's get started!") 



#ask for first name
FIRST_NAME=input("\nWhat is your first name? ") 

#ask for last name
LAST_NAME=input("What is your last name? ")


#enter a yes or no question if they want to make a user name/password
response=input("Are you ready to have your username and password? ")

#make a while loop

while response=="yes" or response == "Yes": 

#make the username by her first initial and first 7 letters of last name
    username=FIRST_NAME[0]+LAST_NAME[:7]
   


#generate password (first 2 charachters of last name with 3 digits)
     
    password=LAST_NAME[:2]+str(random.randint(100,999))+FIRST_NAME[0:2]
    print("\nYour username is, "+username.lower()+ " and your password is, "+password.lower()+ ".")
    
    response=input("\nWould you like a different password? ")


