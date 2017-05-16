# Cate Zwiercan
#11/23/15

# This program will translate any phrase and change it into ICAO for you.


# make a dictionary of all of the letters and numbers
ICAO={"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta", "e": "echo",
          "f":"foxtrot", "g":"golf", "h": "hotel", "i": "india", "j": "juliett",
          "k": "kilo", "l": "lima", "m":"mike", "n": "november", "o": "oscar",
          "p": "papa", "q": "quebec", "r":"romeo", "s": "sierra", "t": "tango",
          "u": "uniform", "v": "victor", "w": "whiskey", "x":"x-ray", "y": "yankee",
          "z": "zulu", "0": "zero", "1": "one", "2": "two", "3": "three",
          "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "niner"}

# Introduce program
response= input( "Welcome to CateTranslate! Here, we can turn any phrase you want into ICAO code. \n\nWould you like to begin? ") 

#create a while loop so that they can do it as many times as they want
while response=="yes" or response=="Yes":
    
# ask them for phrase to translate
    phrase=input("\nEnter phrase to be translated: ") 
    phrase=phrase.lower() 
    
    icao=""
# create for loop
    for letter in phrase:
 
# make if statement for character in dictionary
        if letter in ICAO:
 
            word=ICAO[letter]+ " "
            icao+= word

# print the original statement and new one
    print( "\nOriginal: ",phrase, "\nICAO: ", icao) 
    response=input( "\nWould you like to translate another phrase? ")
    
print("Thanks for using CateTranslate!") 
