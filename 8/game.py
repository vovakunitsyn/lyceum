###Game Rock,Paper,Scissors#####


from sys import exit
from random import randint

print "Welcome to the Rock,Paper,Scissors!"
print "What is your name?"
user = raw_input('> ')

#asks the user for an entry and prints what he has chosen
def start(): 
    print "%s, choose one of the options: " % user

    print """
    1. Rock
    2. Paper
    3. Scissors
    """

    choice = 0
    cpu_choice = randint(1,3)

    while choice <= 0 or choice >= 4:

        choice = int(raw_input('> '))
        if choice == 1:
            print "You chose ROCK!"
        elif choice == 2:
            print "You chose PAPER"
        elif choice == 3:
            print "You chose SCISSORS"
        else:
            print "What is your problem? Try again, this time choose a number between 1 and 3!"
    cpu_decision(cpu_choice)
    result(choice, cpu_choice)


def cpu_decision(cpu):
    if cpu == 1:
        print "Computer chose ROCK!"
    elif cpu == 2:
        print "Computer chose PAPER!"
    else:
        print "Computer chose SCISSORS"


def lose():
    print "Sorry, you lose the round. But you can won in next round. Never give up!"


def win():
    print "Congratulations! You beat computer!!"


def result(user, comp):
    if user == comp:
        print "kek ^^ It's draw. But you can won in next round. Never give up!"
        
    elif user == 1 and comp == 2:
        lose()
    elif user == 1 and comp == 3:
        win()
    elif user == 2 and comp == 1:
        win()
    elif user == 2 and comp == 3:
        lose()
    elif user == 3 and comp == 1:
        lose()
    elif user == 3 and comp == 2:
        win()

    again()


def again():
    print """
    Wanna play again?
    1.YES, I like your game so much! 
    Anything else to quit
    """

    again1 = int(raw_input('> '))

    if again1 == 1:
        start()
    else:
        exit()

start()
