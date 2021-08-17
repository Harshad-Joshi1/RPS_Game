import random

def playersPoint():
    if(userCount>0 or compCount>0):
        print("User Points:",userCount)
        print("Comp Points:",compCount)
    else:
        print("User Points:",userCount)
        print("Comp Points:",compCount)

def roundResult():
    if userCount == compCount:
        print("                  ROUND DRAW               ")
    elif userCount>compCount:
        print("             USER WON THE ROUND            ")
    else:
        print("           COMPUTER WON THE ROUND        \n")

def mainResult():
    if userCount == compCount:
        print("                  MATCH DRAW               ")
    elif userCount>compCount:
        print("             USER WON THE MATCH            ")
    else:
        print("           COMPUTER WON THE MATCH        \n")

def playAgain(): 
    print("\n************************ THANKS FOR PLAYING GAME ********************")
    print()
    

choice = "y"
userCount = 0
compCount = 0
while choice == "y":
    list = ["r", "p", "s"]
    compChoice = random.choice(list)    
    print("******************************************* CODED BY HARSHAD JOSHI *******************************************", end = "\n\n")
    print("**************************************** STONE | PAPER | SCISSOR GAME ****************************************", end = "\n\n")

    userChoise = input("OPTIONS:\n  1. Rock as (r)\n  2. Paper as (p)\n  3. Scissor as (s)\n\nChoose any one among three: ")
    print("\n")

    if userChoise=="s" or userChoise=="p" or userChoise=="r":
        print(f"User has choosen: {userChoise}")
        print(f"Computer has choosen: {compChoice}", end = "\n\n")

        if compChoice == "s" and userChoise == "p":
            compCount += 2
        elif compChoice == "p" and userChoise == "s":
            userCount += 2
        elif compChoice == "r" and userChoise == "p":
            userCount += 2
        elif compChoice == "p" and userChoise == "r":
            compCount += 2
        elif compChoice == "r" and userChoise == "s":
            compCount += 2
        elif compChoice == "s" and userChoise == "r":
            userCount += 2
        elif((compChoice == "s" and userChoise == "s") or (compChoice == "p" and userChoise == "p") or (compChoice == "r" and userChoise == "r")):
            userCount += 1
            compCount += 1

        roundResult()
        print()
        playersPoint()
        print()
        choice = input('''To play again press "y" otherwise press any key: ''')
        print()
        mainResult()
        playAgain()        
    else:
        print("Choose correct option as given above!\n")
        choice = input('''To play again press "y" otherwise press any key: ''') 
        print()
        mainResult()
        playAgain() 