def selection(marks,n):
    k=0
    for i in range(0,n):
        k=i
        for j in range(i+1,n):
            if marks[k] > marks[j]:
                k=j
        marks[i], marks[k] = marks[k], marks[i]
    print(f"SORTED ARRAY: {marks}")

def bubble(marks):
    n=len(marks)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    print(f"SORTED ARRAY: {marks}")

def top5(marks,n):
    print(marks[:n-6:-1])

def main():
    marks=[]
    num=int(input("ENTER THE NUMBER OF STUDENTS: "))
    for i in range(1,num):
        no=int(input("ENTER THE NUMBER: "))
        marks.append(no)
    while True:
        print("**************MENU**************\n1.Selection sort\n2.Bubble Sort\n3.TOP 5\n4.EXIT")
        choice=int(input("ENTER THE CHOICE: "))
        if choice==1:
            selection(marks,len(marks))
        elif choice==2:
            bubble(marks)
        elif choice==3:
            top5(marks,len(marks))
        elif choice==4:
            print("EXIT")
            break
        else:
            print("INVALID INPUT!!!!!")
main()