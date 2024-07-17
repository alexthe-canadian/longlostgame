import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print('Long Lost . . .')
input('Press enter to play')
clear()

def computer():
    selection = input('What would you like to do? 1. Open the ship control application 2. Log off\n')
    if(selection == "2"):
        print('You log off the computer')
        re()
    else:
        selection = input('What would you like to do?\n 1.Attempt To Redirect Spaceship\n 2. Open Command Prompt\n 3. Log off\n')
        if(selection == "3"):
            print('You log off the computer')
            re()
        elif(selection == "1"):
            print('Access Denied. You do not have the required Priveliges. Task Needs: \"Administrator\"')
            computer()
        elif(selection == "2"):
            print('What would you like to do \n 1. Attempt to hack system\n 2. Log off')
            selection = input('\n')
            if(selection == "2"):
                print('You log off the computer')
            elif(selection == "1"):
                print('You begin typing away, attempting to hijack the system')
                print('. . .')
                time.sleep(5)
                print('Access Granted, Administrator')
                selection = input('What Would you like to do? \n 1. Attempt to redirect the course of the ship \n 2. Log off\n')
                if(selection == "1"):
                    print('The ship has been sucessfully redirected to \"EARTH\"')
                    print('You begin feeling sleepy, and head down to your bed')
                    time.sleep(3)
                    clear()
                    print('. . .')
                    time.sleep(5)
                    print('AGENT: Welp, it seems like youre the last left\n AGENT: It\'s understandable though. You were up there for 20 years')
                    time.sleep(5)
                    print('PRESIDENT: Somehow this person was able to land the long lost space craft, and get it back to earth.\n To all families that lost their family members when they were in the craft. \n President: At least you can rest knowning that their bodies are back on earth. And that they were honorable men.')
                    time.sleep(5)
                    clear()
                    print('Hey, thank you for playing my game. I made this within an hour or two and it is at least half decent, in my opinion, at least.')
                    print('Thanks, AlexTheCanadien')
                    print('Good Ending')
                if(selection == "2"):
                    print('You feel yourself getting sleepy')
                    time.sleep(5)
                    clear()
                    print('You wake up to some alarms blaring \"CRITICAL ALERT: LOW OXYGEN IN BACKUP TANKS\"')
                    time.sleep(3)
                    print('You know that you are screwed as the only place to refill them is earth')
                    time.sleep(3)
                    print('At this point you send your last message to your family\n And accept your death')
                    time.sleep(5)
                    clear()
                    print('Hey, thank you for playing my game. I made this within an hour or two and it is at least half decent, in my opinion, at least.')
                    print('Thanks, AlexTheCanadien')
                    print('Bad Ending')

print('You awake in a room, surrrounded by the stars, You wonder how you got here, all you know is you must get out')
print('Last you remember you were with your wife and kids')
def re():
    selection = input('What would you like to do:\n 1.Stare at the stars \n 2. Interact with your computer\n')
    if(selection == "1"):
        print('You stare at the stars, before coming to your senses')
        re()
    if(selection == "2"):
        computer()
    

re()
