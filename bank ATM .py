#Cate Zwiercan
#12/14/15

# this program simulates an atm


#function-----------------------------------------------------

#menu

def menu():
    print("""\n              1) Login or Create new user account
              2) Make a deposit
              3) Request a withdrawl
              4) Check Balance
              5) Logout of Account
              0) Exit the program
              """)
    choice = int(input("""         Enter the number of your choice: 
             """))
    return choice


#login or create account
def login_create_account():
    username=input("\n\nEnter your name: ")
    return username

#make a deposit
def deposit(total):
    amount=int(input("\n\nEnter amount to be deposited: "))
    username_account[username]=amount
    total = total + amount
    return total
    

#request a withdrawl
def withdrawl(total):
    withdrawl_amount=int(input("\n\nEnter the amount you would like to withdrawl: "))
    if total < withdrawl_amount:
        print("You cannot take this much money out you only have,",total,".")
    if withdrawl_amount < total:       
        total= total - withdrawl_amount
    return total

#Check balance
def balance(total):
    print("\n\nYour balance is,",total, ".") 



#main----------------------------------------------------------


#create dictionary with name and amount
total=0
username=""
username_account={username:total} 
#welcome the user
print("""                   Welcome to the Bank of Dad!
 """)
print()

pick=7

LoggedIn = False 

#make a while loop to redo it again

while pick !=0: 

    
#give bank menu
    if pick != 0:
         pick = menu()
    
# if choice 1
    if pick == 1:
        username=login_create_account()

        username_account[username]=username
        if username in username_account:
            LoggedIn= True
                 
# if choice 2
    elif pick == 2 and LoggedIn == True:
       total= deposit(total)
         
# if choice 3
    elif pick == 3 and LoggedIn == True:
        total= withdrawl(total)
        if total <= 0:
            print("You don't have any money in your account!") 

# if choice 4
    elif pick == 4 and LoggedIn == True:
        balance(total)

# if choice 5
    elif pick == 5:
        if LoggedIn == True:
            LoggedIn = False
            print("You are now logged out!") 

# if choice 0
    elif pick == 0:
        print("\nThanks for using Bank of Dad!")
        
#make if statement checking if input was invalid
    else:
        if LoggedIn == False: 
            print("\n\nYou must log in before doing anything else.")
        else: print("\n\nMake sure you entered a vaild number.") 

        
print("\nCome back soon!") 
    

