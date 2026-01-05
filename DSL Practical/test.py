'''
Problem Statement: In second year computer engineering class, group A student's play cricket, group B students play badminton and group C students play football.
Write a Python program using functions to compute following:
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realising the group, duplicate entries should be avoided, Do not use SET built-in functions)

Code from Data Structure Lab (SPPU - Second Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-se-comp-codes/DSL
'''

# BEGINNING OF CODE
# List to store players
cricketPlayers = []
badmintonPlayers = []
footballPlayers = []

# Input cricket
def cricketInput():
    total = int(input("Total number of CRICKET players:\t"))
    for i in range(total):
        players = int(input(f"Roll number of player {i+1}:\t"))
        cricketPlayers.append(players)
    print(f"\n----------\nStudents playing cricket:\t {cricketPlayers}\n----------\n")

# Input badminton
def badmintonInput():
    total = int(input("Total number of BADMINTON players:\t"))
    for i in range(total):
        players = int(input(f"Roll number of player {i+1}:\t"))
        badmintonPlayers.append(players)
    print(f"\n----------\nStudents playing badminton:\t {badmintonPlayers}\n----------\n")

# Input football
def footballInput():
    total = int(input("Total number of FOOTBALL players:\t"))
    for i in range(total):
        players = int(input(f"Roll number of player {i+1}:\t"))
        footballPlayers.append(players)
    print(f"\n----------\nStudents playing football:\t {footballPlayers}\n----------\n")

# Playing both cricket and badminton
def CricketAndBadminton():
    listCricketAndBadminton = []
    for i in cricketPlayers:
        if i in badmintonPlayers:
            listCricketAndBadminton.append(i)
    print(f"\n----------\nStudents playing cricket and badminton:\t {listCricketAndBadminton}\n----------\n")

# Either cricket or badminton but not both
def CricketOrBadminton():
    listCricketOrBadminton = []
    for i in cricketPlayers:
        if i not in badmintonPlayers:
            listCricketOrBadminton.append(i)
    for i in badmintonPlayers:
        if i not in cricketPlayers:
            listCricketOrBadminton.append(i)
    print(f"\n----------\nStudents playing cricket or badminton (but not both):\t {listCricketOrBadminton}\n----------\n")

# Neither cricket nor badminton, i.e. football only
def FootballOnly():
    listCricketAndBadminton = []
    listFootballOnly = []
    for i in cricketPlayers:
        listCricketAndBadminton.append(i)
    for i in badmintonPlayers:
        if i not in cricketPlayers:
            listCricketAndBadminton.append(i)
    for i in footballPlayers:
        if i not in listCricketAndBadminton:
            listFootballOnly.append(i)
    print(f"\n----------\nTotal students playing football only are:\t{len(listFootballOnly)}\nList:\t{listFootballOnly}\n----------\n")

# Cricket and football but not badminton
def notBadminton():
    listNotBadminton = []
    for i in cricketPlayers:
        if i in footballPlayers:
            if i not in badmintonPlayers:
                listNotBadminton.append(i)
    print(f"\n----------\nTotal students not playing badminton (but do play cricket and football):\t{len(listNotBadminton)}\nList:\t{listNotBadminton}\n----------\n")

# Main function with options
def main():    
    print("----- ENTER ROLL NUMBERS IN LIST -----")
    cricketInput()
    badmintonInput()
    footballInput()
    print("----- ROLL NUMBERS SAVED -----\n")
    while (1):
        print("\n----- MAIN MENU -----")
        print("1 -> Students playing both cricket and badminton")
        print("2 -> Students playing either cricket or badminton, but not both")
        print("3 -> Students playing neither cricket nor badminton (i.e. football only)")
        print("4 -> Students playing cricket and football, but not badminton")
        print("5 -> Exit")
        
        optn = int(input("Choose an option (1-5):\t"))
        
        if (optn == 1):
            CricketAndBadminton()
        elif (optn == 2):
            CricketOrBadminton()
        elif (optn == 3):
            FootballOnly()
        elif (optn == 4):
            notBadminton()
        elif (optn ==5):
            print("\n\n## END OF CODE\n\n")
            quit()
        else:
            print("\n\nPlease choose a valid option (1-5)\n\n")

main()
# END OF CODE
