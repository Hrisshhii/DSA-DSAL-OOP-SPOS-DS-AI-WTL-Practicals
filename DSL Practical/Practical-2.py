def input_marks(marks):
    n=int(input("ENTER THE NO OF STUDENTS: "))
    for i in range(0,n):
        k=int(input("ENTER MARKS: (IF ABSENT ENTER -1) "))
        marks.append(k)

def avg(marks):
    total=0
    for i in marks:
        if i!=-1:
            total+=i
    print("AVERAGE IS ",total/len(marks))

def absent(marks):
    count=0
    for i in marks:
        if i==-1:
            count+=1
    print("ABSENT STUDENTS ARE ",count)

def minimum(marks):
    low=100
    for i in marks:
        if i!=-1 and i<low:
            low=i
    print("MINIMUM MARKS IS ",low)

def maximum(marks):
    high=0
    for i in marks:
        if i>high:
            high=i
    print("MAXIMUM MARKS IS ",high)

def freq(marks):
    fr=0
    for i in range(len(marks)):
        count=0
        if marks[i]!=-1:
            for j in range(len(marks)):
                if marks[i]==marks[j]:
                    count=count+1
        if(fr<count):
            mark=marks[i]
            fr=count
    print("MARKS WITH HIGHEST FREQUENCY IS ",mark)
    print("FREQUENCY COUNT IS ",fr)



def main():
    marks=[]
    print("\nMENU:\n1.INPUT DATA\n2.AVERAGE OF CLASS\n3.COUNT ABSENT STUDENTS\n4.MINIMUM MARKS\n5.MAXIMUM MARKS\n6.FREQUENCY OF HIGHEST MARKS\n7.EXIT")
    while True:
        choice=int(input("ENTER A CHOICE: "))
        if choice==1:
            input_marks(marks)
        elif choice==2:
            avg(marks)
        elif choice==3:
            absent(marks)
        elif choice==4:
            minimum(marks)
        elif choice==5:
            maximum(marks)
        elif choice==6:
            freq(marks)
        elif choice==7:
            print("EXIT")
            break
        else:
            print("INVALID CHOICE!!!!!")
main()