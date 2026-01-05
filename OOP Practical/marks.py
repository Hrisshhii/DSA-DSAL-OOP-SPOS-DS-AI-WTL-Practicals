marks=[]

def accept():
    n=int(input("ENTER TOTAL NUMBER OF STUDENTS: "))
    for i in range(n):
        prn=int(input("ENTER THE MARKS OF STUDENT (if absent marks -1): "))
        marks.append(prn)

def avg(marks,n):
    total=0
    for i in range(n):
        if(marks[i]!=-1):
            total=total+marks[i]

    print("AVERAGE OF CLASS IS ",total/len(marks))

def max_min(marks):
    min=100
    max=0
    for i in marks:
        if(i>max):
            max=i
        
        if(i!=-1 and i<min):
            min=i
    print("MAXIMUM MARKS: ",max,"\nMINIMUM MARKS: ",min)

def absent(marks):
    count=0
    for i in marks:
        if i==-1:
            count=count+1
    print("TOTAL ABSENT STUDENTS: ",count)

def most_freq(marks):
    fr={}
    max_freq=0
    result=-1
    for mark in marks:
        if mark!=1:
            if mark in fr:
                fr[mark]+=1
            else:
                fr[mark]=1
    for mark, count in fr.items():
        if(count>max_freq):
            max_freq=count
            result=mark
        elif count==max_freq:
            if mark>result:
                result=mark


    print("MARKS WITH HIGHEST FREQUENCY IS ",result)
    print("FREQUENCY COUNT IS ",max_freq)

def most(marks):
   unique=[]
   frq=[]
   for m in marks:
       if m!=-1:
            if m in unique:
               index=unique.index(m)
               frq[index]+=1
            else:
               unique.append(m)
               frq.append(1)
   max_freq=0
   resut=-1
   for i in range(len(unique)):
       if(frq[i]>max_freq):
           max_freq=frq[i]
           result=unique[i]
       elif frq[i]==max_freq:
           if unique[i]>result:
               result=unique[i]
   print("Mark with highest frequency:", result)
   print("Frequency count:", max_freq)


def main():
    while(1):
        print("""\n************MENU************
              1.INPUT DATA
              2.AVERAGE
              3.MAXIMUM AND MINIMUM MARKS
              4.ABSENT STUDENTS COUNT
              5.HIGEST FREQUENT MARKS
              6.EXIT\n""")
        choice=int(input("ENTER YOUR CHOICE: "))
        if(choice==1):
            accept()
        elif(choice==2):
            avg(marks,len(marks))
        elif(choice==3):
            max_min(marks)
        elif(choice==4):
            absent(marks)
        elif(choice==5):
            most_freq(marks)
            most(marks)
        elif(choice==6):
            print("EXITING......................:)")
            break
        else:
            print("INALID CHOICE!!!")
main()