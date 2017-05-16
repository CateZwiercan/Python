import random

answer="y"
while answer =="y":
    die1=random.randint(1,6)
    die2=random.randrange(6)+1
    total=die1+die2
    if total==7 :
        print("you win")
    else: print("you lose")
    answer=input("Do you wnat to play again?")
print("Thanks for playing")
