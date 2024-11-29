import random
def oddeven():
    play=5 
    comscore=0
    userscore=0
    for i in range(play):
        user=input("enter the choice 'odd' or 'even'\n").lower()
        if user not in ["odd","even"]:
            print("invalid input.enter the input 'odd' or 'even' ")
            continue
        com=random.randint(0,6)
        # print("computer value",com)
        userchoice=int(input("enter the value 1-6 :"))
        if userchoice<1 or userchoice>6:
            print("invalid input.enter the input 1-6")
            continue

        result=userchoice+com
        if result%2==0:
            if user=="even":
                print("user win")
                userscore+=1
            else:
                print("computer win")
                comscore+=1

        else:
            if user=="odd":
                print("user win")
                userscore+=1
            else:
                print("computer win")
                comscore+=1
        print("computer score=",comscore)
        print("user score =",userscore)
    print("computer score=",comscore)
    print("user score =",userscore)
try:
    oddeven()
except ValueError:
    print("invalid.enter the valid number")
    oddeven()
    
