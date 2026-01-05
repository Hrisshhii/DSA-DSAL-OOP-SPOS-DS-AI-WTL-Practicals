
def accept(arr):
    num=int(input("ENTER THE NUMBER OF ELEMENTS: "))
    for i in range(num):
        n=int(input("ENTER THE ELEMENT: "))
        arr.append(n)

def display(arr):
    print(f"{arr}")

def bubble(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(f"{arr}")


def selection(arr):
    min=0
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[min]>arr[j]):
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp
    print(f"SORTED ARRAY: {arr}")

def insertion(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0) and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    print(f"SORTED MARKS: {arr}")

def shell(arr):
    gap=len(arr)//2
    while(gap>0):
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=gap//2
    print(f"SORTED MARKS: {arr}")

def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    left=merge(left)
    right=merge(right)

    return mer(left,right)

def mer(left,right):
    sorted=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

def top5(arr,n):
    print(arr[:n-6:-1])

def main():
    arr=[]
    while(1):
        print("""\n**********MENU***********
            1.INPUT ELEMENTS
            2.DISPLAY
            3.SELECTION SORT
            4.BUBBLE SORT
            5.INSERTION SORT
            6.SHELL SORT
            7.MERGE SORT
            8.TOP 5
            9.EXIT """)
        choice=int(input("ENTER YOUR CHOICE: "))
        if(choice==1):
            accept(arr)
        elif(choice==2):
            display(arr)
        elif(choice==3):
            selection(arr)
        elif(choice==4):
            bubble(arr)
        elif(choice==5):
            insertion(arr)
        elif(choice==6):
            shell(arr)
        elif(choice==7):
            p=merge(arr)
            print(f"{p}")
        elif(choice==8):
            top5(arr,len(arr))
        elif(choice==9):
            print("EXITING............:)")
            break
        else:
            print("INVALID CHOICE: ")

main()