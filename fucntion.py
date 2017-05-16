def func1():
    localVar="This is local"
    print("func1-globalVar:"+ globalVar)
    print("func1-localVar:"+ localVar)


#main program-----------

globalVar="This is global"
func1()
print("\nglobal-globalVar:"+ globalVar)
print("func1-localVar:"+ localVar)

