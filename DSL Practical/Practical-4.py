def input_data(arr):
    num=int(input("ENTER THE NUMBER OF STUDENTS: "))
    for i in range(0,num):
        char=int(input("ENTER THE ROLL NUMBER: "))
        arr.append(char)

def linear(arr):
    key=int(input("ENTER THE KEY: "))
    flag=0
    for i in range(0,len(arr)):
        if arr[i]==key:
            print("NUMBER FOUND AT INDEX: ",i)
            flag=1
            break
    if flag==0:
        print("NOT FOUND!!!")

def sentinal(arr):
    key=int(input("ENTER THE KEY: "))
    last=arr[len(arr)-1]
    arr[len(arr)-1]=key
    i=0
    while arr[i]!=key:
        i+=1
    arr[len(arr)-1]=last
    if i<len(arr)-1:
        print("FOUND AT ",i)
    elif key==arr[i] and i==len(arr)-1:
        print("FOUND AT: ",len(arr)-1)
    else:
        print("NOT FOUND!!!")

def binary(arr,l,h,key):
    if h>l:
        mid=l+(h-l)//2
        if arr[mid]==key:
            print("FOUND AT ",mid)
        elif key>arr[mid]:
            binary(arr,mid+1,h,key)
        elif key<arr[mid]:
            binary(arr,l,mid-1,key)
    else:
        print("NOT FOUND")

def fibonacci(arr,key,n):
    offset=-1
    f2=0
    f1=1
    fm=f1+f2
    while fm<n:
        f2=f1
        f1=fm
        fm=f1+f2
    while fm>1:
        mid=min(offset+f2,n-1)
        if(arr[mid]<key):
            fm=f1
            f1=f2
            f2=fm-f1
            offset=mid
        elif (arr[mid]>key):
            fm=f2
            f1=f1-f2
            f2=fm-f1
        else:
            return mid
        
    if f1 and arr[offset+1]==key:
        return offset+1
    return -1


def main():
    arr=[]
    print("**********************MENU**********************\n1.INPUT DATA\n2.LINEAR SEARCH\n3.SENTINAL SEARCH\n4.BINARY SEARCH\n5.FIBONACCI SEARCH\n6.EXIT\n")
    while True:
        choice=int(input("ENTER THE CHOICE: "))
        if choice==1:
            input_data(arr)
        elif choice==2:
            linear(arr)
        elif choice==3:
            sentinal(arr)
        elif choice==4:
            key=int(input("ENTER THE KEY TO BE SEARCH: "))
            n=0
            binary(arr,n,len(arr)-1,key)
        elif choice==5:
            key=int(input("ENTER THE KEY TO BE SEARCH: "))
            index=fibonacci(arr,key,len(arr))
            if(index>=0):
                print("FOUNT AT: ",index+1)
            else:
                print("UNSUCCESSFULL SEARCH!!!!")
        elif choice==6:
            print("EXIT")
            break
        else:
            print("INVALID CHOICE!!!!!!!")
main()