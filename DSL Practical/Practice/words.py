def longest(sen):
    words=sen.split()
    l=0
    longer=""
    for word in words:
        if(len(word)>l):
            l=len(word)
            longer=word
    print("WORD WITH LONGEST LENGTH IS ",longer," OF LENGTH ",l)

def char_occurance(sen):
    char=(input("THE CHARACTER TO CHECK OCCURANCE OF IN STRING: "))
    count=0
    for i in range(len(sen)):
        if(sen[i]==char):
            count+=1
    print("THE CHARACTER OCCURED ",count," TIMES IN THE STRING")

def word_occurance(sen):
    w=(input("THE CHARACTER TO CHECK OCCURANCE OF IN STRING: "))
    count=0
    str=sen.split()
    for i in str:
        if(i==w):
            count+=1
    print("THE WORD OCCURED ",count," TIMES IN THE STRING")

def palindrome(sen):
    word=input("ENTER THE WORD TO CHECK IF PALINDROME: ")
    if(word==word[::-1]):
        print("WORD IS PALINDROME")
    else:
        print("NOT A PALINDROME!!")
    print("CHECKING THE SENTENCE PALINDROME OR NOT!")
    if(sen==sen[::-1]):
        print("SENTENCE IS PALINDROME")
    else:
        print("SENTENCE IS NOT A PALINDROME!!")

def first_occ(sen):
    check=input("WORD TO CHECK FIRST OCCURANCE OF: ")
    found=sen.index(check)
    if(found!=-1):
        print("WORD FOUND AT ",found)
    else:
        print("WORD NOT FOUND!")

def word_occ(sen):
    frq={}
    s=sen.split()
    for word in s:
        if word in frq:
            frq[word]+=1
        else:
            frq[word]=1
    for word,count in frq.items():
        print(f"WORD:{word} OCCURES {count} TIMES")

def cpy(sen):
    new=sen
    print("STRING COPIED!!!")
    print("PRINTING USING COPYED LOCATION: ",new)


def main():
    sen=input("ENTER THE STRING: ")
    while(1):
        print("""\n**********MENU***********
              1.FIND THE LONGEST WORD IN STRING
              2.FREQENCY OF OCCURANCE OF A CHARACTER IN STRING
              3.FREQENCY OF OCCURANCE OF A WORD IN STRING
              4.PALINDROME CHECK
              5.FIRST APPERANCE
              6.OCCURANCE OF EACH WORD
              7.COPY THE STRING
              8.EXIT""")
        choice=int(input("ENTER YOUR CHOICE: "))
        if(choice==1):
            longest(sen)
        elif(choice==2):
            char_occurance(sen)
        elif(choice==3):
            word_occurance(sen)
        elif(choice==4):
            palindrome(sen)
        elif(choice==5):
            first_occ(sen)
        elif(choice==6):
            word_occ(sen)
        elif(choice==7):
            cpy(sen)
        elif(choice==8):
            print("EXITING............:)")
            break
        else:
            print("INVALID CHOICE: ")
main()