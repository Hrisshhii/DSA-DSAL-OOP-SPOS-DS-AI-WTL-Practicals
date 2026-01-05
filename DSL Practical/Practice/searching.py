arr=[]

def accept(arr):
    num=int(input("ENTER THE NUMBER OF ELEMENTS: "))
    for i in range(num):
        n=int(input("ENTER THE ELEMENT: "))
        arr.append(n)

def display(arr):
    print(f"{arr}")

def linear(arr):
    key=int(input("ENTER THE KEY: "))
    flag=0
    for i in range(len(arr)):
        if(arr[i]==key):
             print("ELEMENT FOUND AT ",i+1," POSITION")
             flag=1
             break
    if(flag!=1):
        print("ELEMENT NOT FOUND")

def sentinel(arr):
    key=int(input("ENTER THE KEY: "))
    last=arr[len(arr)-1]
    arr[len(arr)-1]=key
    i=0
    flag=0
    while(arr[i]!=key):
        i+=1
    arr[len(arr)-1]=last
    if(i<len(arr)-1):
        print("ELEMENT FOUND AT ",i," INDEX")
    elif i==len(arr)-1 and key==arr[i]:
        print("ELEMENT FOUND AT ",len(arr)-1," INDEX")
    else:
        print("ELEMENT NOT FOUND")

def binary(arr,l,h,key):
    if(h>=l):
        mid=l+(h-l)//2
        if arr[mid]==key:
            print("ELEMENT FOUND AT ",mid)
        elif arr[mid]<key:
            binary(arr,mid+1,h,key)
        elif arr[mid]>key:
            binary(arr,l,mid-1,key)
    else:
        print("ELEMENT NOT FOUND")
            
def fib(arr,n,key):
    offset=-1
    fm2=0
    fm1=1
    fm=fm1+fm2
    while(fm<n):
        fm2=fm1
        fm1=fm
        fm=fm1+fm2
    while fm>1:
        mid=min(offset+fm2,n-1)
        if(arr[mid]<key):
            fm=fm1
            fm1=fm2
            fm2=fm-fm1
            offset=mid
        elif(arr[mid]>key):
            fm=fm2
            fm1=fm1-fm2
            fm2=fm-fm1
        else:
            return mid
    if fm1 and arr[offset+1]==key:
        return offset+1
    return -1
    

def main():
    while(1):
        print("""\n**********MENU***********
            1.INPUT ELEMENTS
            2.DISPLAY
            3.LINEAR SEARCH
            4.SENTINEL SEARCH
            5.BINARY SEARCH
            6.FIBONNACI SEARCH
            7.EXIT""")
        choice=int(input("ENTER YOUR CHOICE: "))
        if(choice==1):
            accept(arr)
        elif(choice==2):
            display(arr)
        elif(choice==3):
            linear(arr)
        elif(choice==4):
            sentinel(arr)
        elif(choice==5):
            print("NOTE:BINARY SEARCH NEEDS SORDED DATA!!")
            key=int(input("ELEMENT TO BE SEARCHED: "))
            binary(arr,0,len(arr),key)
        elif(choice==6):
            key=int(input("ELEMENT TO BE SEARCHED: "))
            index=fib(arr,len(arr),key)
            if(index>=0):
                print("FOUNT AT: ",index+1)
            else:
                print("UNSUCCESSFULL SEARCH!!!!")
        elif(choice==7):
            print("EXITING............:)")
            break
        else:
            print("INVALID CHOICE: ")
main()