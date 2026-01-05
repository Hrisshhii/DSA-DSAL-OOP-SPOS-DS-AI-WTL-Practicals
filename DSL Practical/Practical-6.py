def insertion(marks,n):
    for i in range(0,len(marks)):
        temp=marks[i]
        j=i-1
        while(j>=0 and marks[j]>temp):
            marks[j+1]=marks[j]
            j=j-1
        marks[j+1]=temp
    print(f"SORTED MARKS: {marks}")

def shell(marks):
    gap=len(marks)//2
    while (gap>0):
        for i in range(gap,len(marks)):
            temp=marks[i]
            j=i
            while(j>=gap and marks[j-gap]>temp):
                marks[j]=marks[j-gap]
                j=j-gap
            marks[j]=temp
        gap=gap//2
    print(f"SORTED MARKS: {marks}")

def top5(marks,n):
    print(marks[:n-66
                :-1])

def main():
    marks=[]
    num=int(input("ENTER THE NUMBER OF STUDENTS: "))
    for i in range(0,num):
        no=int(input("ENTER THE NUMBER: "))
        marks.append(no)
    while True:
        print("**************MENU**************\n1.Insertion sort\n2.Shell Sort\n3.TOP 5\n4.EXIT")
        choice=int(input("ENTER THE CHOICE: "))
        if choice==1:
            insertion(marks,len(marks))
        elif choice==2:
            shell(marks)
        elif choice==3:
            top5(marks,len(marks))
        elif choice==4:
            print("EXIT")
            break
        else:
            print("INVALID INPUT!!!!!")
main()