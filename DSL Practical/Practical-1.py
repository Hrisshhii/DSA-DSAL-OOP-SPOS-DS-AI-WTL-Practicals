#Getting all the students!!!!!!
cricket=[]
football=[]
badminton=[]

def accept_cricket():
    n=int(input("ENTER NO OF STUDENTS WHO PLAY CRICKET: "))
    for i in range(n):
        num=int(input("ENTER ROLL NO: "))
        cricket.append(num)
accept_cricket()

def accept_football():
    n=int(input("ENTER NO OF STUDENTS WHO PLAY FOOTBALL: "))
    for i in range(n):
        num=int(input("ENTER ROLL NO: "))
        football.append(num)
accept_football()

def accept_badminton():
    n=int(input("ENTER NO OF STUDENTS WHO PLAY BADMINTON: "))
    for i in range(n):
        num=int(input("ENTER ROLL NO: "))
        badminton.append(num)
accept_badminton()

#STUDENTS WHO PLAY BOTH CRICKET AND BADMINTON
def crickbat():
    both=[]
    for i in cricket:
        if i in badminton:
            both.append(i)
    print(f"\n----------\nStudents playing cricket and badminton:\t {both}\n----------\n")
crickbat()

#STUDENTS WHO PLAY EITHER CRICKET OR BADMINTON NOT BOTH
def criorbad():
    cricketorbadminton=[]
    for i in cricket:
        if i not in badminton:
            cricketorbadminton.append(i)
    for j in badminton:
        if j not in cricket:
            cricketorbadminton.append(j)
    print(f"\n----------\nStudents playing cricket or badminton not both:\t{cricketorbadminton}\n----------\n")
criorbad()

#STUDENTS WHO PLAY NEITHER CRICKET NOT BADMINTON 
def notcricketnorbadminton():
    count=0
    footballonly=[]
    for i in football:
        if i not in cricket and i not in badminton:
            footballonly.append(i)
    print(f"\n----------\nStudents playing neither cricket nor badminton:\t{footballonly}\n----------\n")
    for k in footballonly:
        count=count+1
    print("Total player are ",count)
notcricketnorbadminton()

#STUDENTS WHO PLAY CRICKET AND FOOTBALL NOT BADMINTON
def onlycricketandfootball():
    crickfoot=[]
    count=0
    for i in cricket:
        if i in football and i not in badminton:
            if i not in badminton:
                crickfoot.append(i)
    print(f"\n----------\nStudents playing Cricket and Football not badminton:\t{crickfoot}\n----------\n")
    for k in crickfoot:
        count=count+1
    print("Total player are ",count)
onlycricketandfootball()

