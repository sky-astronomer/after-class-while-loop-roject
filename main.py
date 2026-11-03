print("welcome to my homework completion program")
name=input("Enter your name: ")
homeworks=int(input("Enter how many homeworks you have: "))
print(name, "you have ", homeworks, "number of homeworks")
numofhw=0
cmh=[]
while numofhw<homeworks:
    home=input("What homework do you have to do?")
    rep=input("Have you completed the" + home + "homework?" )
    while rep!="yes":
        print("Go complete" , home, "homework right now")
        rep=input("Have you completed the" + home + "homework?" )
        cmh.append(home)
        numofhw+=1
        storedhw=homeworks-numofhw
        print(name,"You have ", storedhw,"number of homeworks remaining")
        print("you have completed",numofhw,"homeworks and have remained",storedhw,"homeworks" )
