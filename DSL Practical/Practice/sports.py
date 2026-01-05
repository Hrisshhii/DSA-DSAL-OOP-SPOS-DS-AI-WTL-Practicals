football=[]
cricket=[]
badminton=[]

def getdata():
    print("\nWHOS DATA YOU WANT TO ENTER\n1.FOOTBALL\n2.CRICKET\n3.BADMINTON")
    choice=int(input("\nENTER YOUR CHOICE: "))
    if choice==1:
        n=int(input("\nENTER THE NUMBER OF STUDENS WHO PLAYS FOOTBALL: "))
        for i in range(n):
            prn=int(input("ENTER THE PRN: "))
            football.append(prn)
    elif choice==2:
        n=int(input("\nENTER THE NUMBER OF STUDENS WHO PLAYS CRICKET: "))
        for i in range(n):
            prn=int(input("ENTER THE PRN: "))
            cricket.append(prn)
    elif choice==3:
        n=int(input("\nENTER THE NUMBER OF STUDENS WHO PLAYS BADMINTON: "))
        for i in range(n):
            prn=int(input("ENTER THE PRN: "))
            badminton.append(prn)
    else:
        print("INVALID CHOICE!!!")

def badminton_and_cricket():
    both=[]
    for i in badminton:
        for j in cricket:
            if(i==j):
                both.append(i)
    print(f"People who like both CRICKET AND BADMINTON ARE: \n{both}")

def circket_or_badminton_not_both():
    either=[]
    for i in badminton:
        found=False
        for k in cricket:
            if i == k:
                found=True
                break
        if(found==False):
            either.append(i)
    for j in cricket:
        found=False
        for k in badminton:
            if j == k:
                found=True
                break
        if(found==False):
            either.append(j)
    print(f"List of students who play either cricket or badminton but not both:{either}")

def cricket_and_football_not_badmiton():
    crick_foot=[]
    for i in cricket:
        for j in football:
            if(i==j):
                is_in_badminton=False
                for k in badminton:
                    if(i==k):
                        is_in_badminton=True
                        break
                if(is_in_badminton==False):
                    crick_foot.append(i)
    
    print(f"Number of students who play cricket and football but not badminton:{crick_foot}")
    print("\nTOTAL NUMBER OF STUDENTS ARE ",len(crick_foot))

def onlyfootball():
    only=[]
    for i in football:
        is_in_cricket = False
        is_in_badminton = False
        for j in cricket:
            if(i==j):
                is_in_cricket=True
                break
        for k in badminton:
            if(i==k):
                is_in_badminton=True
                break
        if(is_in_badminton==False and is_in_badminton==False):
            only.append(i)
    
    print(f"Number of students who play neither cricket nor badminton:{only}")
    print("\nTOTAL NUMBER OF STUDENTS ARE ",len(only))

def main():
    while(1):
        print("""\n**********MENU***********
            \n1.INPUT DATA\n2.STUDENTS WHO LIKE CRICKET AND BADMINTON BOTH\n3.STUDENT WHO LIKE CRICKET OR BADMINTON NOT BOTH\n4:STUDENTS WHO LIKE CRICKET AND FOOTBALL NOT BADMINTON\n5:STUDENTS WHO NEITHER LIKE BADMINTON NOT CRICKET\n6:EXIT\n""")
        choice=int(input("ENTER YOUR CHOICE: "))
        if(choice==1):
            getdata()
        elif(choice==2):
            badminton_and_cricket()
        elif(choice==3):
            circket_or_badminton_not_both()
        elif(choice==4):
            cricket_and_football_not_badmiton()
        elif(choice==5):
            onlyfootball()
        elif(choice==6):
            print("EXITING.....................:)")
            break
        else:
            print("INAVLID CHOICE!!!")
main()
    