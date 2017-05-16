#Pia Singh
#November 15, 2016
#Usernames and Passwords Program

import random
print("Welcome to your program. This program will generate you a username and password.")
response="yes" #sentary variable
while response=="yes":
    
          firstname=input("\nWhat is your first name?") #enter info for username & password
          lastname= input("\nWhat is your last name?")
          username=(firstname[0]) + (lastname[0:7]) #generates your username here 
          print("\nYour username is " + username.lower()) #gives username in all lowercase
          password=lastname[0:2] + str(random.randint(100,999)) + firstname[0:2]
          print("\nYour password is "+ password.lower()+".") #this generates the password in lower case
          response=input("\n Would you like to enter another name?>") #using the sentary variable

print("Wow you've finsihed generating a username and password!")
print("Great work")
      

