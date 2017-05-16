#cate Zwiercan
#10/5/15

# the purpose of this porgram is to add up the "prices" of items from a persons shopping spree
#and give them thier total


#make a sentry variable

total=0
price=9
input("What are you buying today? ")


#start the while loop
#give the instructions for the while loop

while (price>0):
 
    price=float(input("\nWhat is the price of this item? "))
    total=total+price
    print("Your total is ",total)

#end the while loop by printing a statement with total in it

 
