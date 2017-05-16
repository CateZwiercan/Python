#Cate Zwiercan
#11/16/15
#a teacher can input student's test scores and puts them in a
#list and gives the average, highest and lowest scores

#introduce the user and explain what the program does
print("Welcome to GradesPro! Here you can input your students grades and we\n will tell you the highest, lowest and average score as well as the letter grade for each student.\nInput a negative number to say that there are no more students.\n\n")



#have user input scores
scores=[]
students=[]

grade=33

student=""

#make while loop

while grade >= 0: 
    grade=int(input("\nEnter student score: "))
    
#add student names
    if grade >=0:
        student=input("Enter student name: ")
    scores.append(grade)
    students.append(student) 
 
    
#delete the last number score to get rid of the neative
    
del scores[(len(scores)-1)]

# get total number of socres   
total=0

for number in scores:
    total=total + number
    
#find highest score
    
highest= max(scores)

#find lowest score

lowest=min(scores)

#find average score
letter = []
average= total / len(scores)

#letter grades
for gr in scores:
    
    if gr >= highest - 10:
        lettergrade="A"
    
    elif gr >= highest - 20:
        lettergrade="B"
    
    elif gr >= highest - 30:
        lettergrade="C"
    
    elif gr >= highest - 40:
        lettergrade="D"

    else:
        lettergrade="F"
    letter.append(lettergrade)

#print scores and each score for each student with letter grade
print("\nHighest score: ",highest,"   Lowest score: ",lowest,"   Average score: ",average)

um = 0
for item in scores:
    print("\nStudent "+str(um)+ "  "+students[um].capitalize()+ "\tscore is "+str(scores[um])+ " and letter grade is " +letter[um])
    um= um +1
