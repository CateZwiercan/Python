#Cate Zwiercan
#10/7/15

# this program is to convert celcius and fahrenheit temperatures

#give sentry variable
celsius=0
fahrenheit=0
temp_type= input("Is temperature celsius(C) or fahrenheit(F)? Enter either a C or F ")
temp=float(input("\nWhat is the temperature in "+temp_type+ "? "))

#make if statement for one for each response


#Celsius
if temp_type=="C":
    fahrenheit=(9.0/5)* temp +32
    print(temp, "C =" , fahrenheit, "F")

#fahrenheit

elif temp_type=="F":
    celsius=(temp-32)*(5/9.0)
    print(temp, "F =" , celsius, "C") 

#invalid

else:
    print("Invalid input") 
