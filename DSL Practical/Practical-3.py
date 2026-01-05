def char_occurance(s):
    occur=0
    ch=input("Enter character to check occurance: ")
    for i in s:
        if i==ch:
            occur+=1
    print(ch," occurs ",occur," times")

def longest_word(s):
    str=s.split()
    l=0
    for i in str:
        if len(i)>l:
            l=len(i)
    print("WORD WITH LONGEST LENGTH IS ",i," with length",l)

def occurance_word(s):
    occ=input("Enter the word to find occurance of: ")
    str=s.split()
    count=0
    for i in str:
        if i==occ:
            count=count+1
    print("Word ",occ," occurs ",count," times.")

def first_occurance(s):
    sub=input("ENTER THE SUBSTRING: ")
    a=s.find(sub)
    if a!=-1:
        print("FOUND WORD AT INDEX ",a)
    else:
        print("NOT FOUND!!")
    

def palindrome(s):
    s2=input("ENTER TO FIND IF THE STING IS PALINDROME: ")
    if s2==s2[::-1]:
        print("PALINDROME!!!!")
    else:
        print("NOT A PALINDROME!!!")

def upper_case(s):
    up=s.upper()
    print("UPPER CASE: ",up)

def lower_case(s):
    lo=s.lower()
    print("LOWER CASE: ",lo)

def swap_case(s):
    sw=s.swapcase()
    print("SWAP CASE: ",sw)

def main():
    s=input("ENTER THE STRING: ")
    print("\n------------------------MENU------------------------\n1.Character Occurance\n2.Longest Word\n3.Occurance of word\n4.First Appereance of word\n5.Is string palindrome\n6.Convert to uppercase\n7.Convert to lowercase\n8.Swapcase\n9.Exit")
    while True:
        choice=int(input("ENTER THE CHOICE: "))
        if choice==1:
            char_occurance(s)
        elif choice==2:
            longest_word(s)
        elif choice==3:
            occurance_word(s)
        elif choice==4:
            first_occurance(s)
        elif choice==5:
            palindrome(s)
        elif choice==6:
            upper_case(s)
        elif choice==7:
            lower_case(s)
        elif choice==8:
            swap_case(s)
        elif choice==9:
            print("EXIT")
            break
        else:
            print("INVALID CHOICE!!!!!")        
main()