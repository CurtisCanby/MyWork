# THE 5 ROOM DUNGEON!
import random
events = [ 
    {"Name":"Hallway","Description":"long and poorly lit, thankfully its safe.","Fight":False},
    {"Name":"Storage Room","Description":"a dusty room full of barrels and boxes.","Fight":False},
    {"Name":"Kitchen","Description":"a poorly stocked and abandoned kitchen, it smells of moldy bread.","Fight":False},
    {"Name":"Closit","Description":"a closit. As you opened the door a broom fell out a starteled you.","Fight":False},
    {"Name":"Library","Description":"a room full of books... with an angry librarian inside!","Fight":True},
    {"Name":"Barracks","Description":"a room where a table full of goblins stare at you!","Fight":True}
    {"Name":"Boss Room","You meet the boss of the dungeon! HE IS NOT HAPPY TO SEE YOU!","Fight":True}
          ]

eventsize = len(events) - 1
def generateDungeon():
    #This fills out a list with various events that will act as the dungeon!
    dungeon = []
    for i in range(0,5):
        random_integer = random.randint(0, eventsize)
        dungeon.append(events[random_integer])
    return dungeon

def getvalidroom(valid):
    #This gets user input and checks its valid, then passes the valid input.
    print("Please Pick A Room")
    while True:
        try:
            chosenroom = int(input())
            if chosenroom <= valid and chosenroom > 0:
                break
            else:
                print("Invalid Room. Pick again.")
        except ValueError:
            print("Thats not even a number, choose again.")
    return chosenroom

def getMonsterWeapon():
    monsterweapon = None
    random_integer = random.randint(0, 2)
    match random_integer:
        case 0:
            monsterweapon = "Rock"
            return monsterweapon
        case 1:
            monsterweapon = "Paper"
            return monsterweapon
        case 2:
            monsterweapon = "Scissors"
            return monsterweapon

def fightmechanic(life):
    print("What is your weapon?")
    # MONSTER PICKS WEAPON
    monsterweapon = getMonsterWeapon()
    yourweapon = None
    while True:
        try:
            chosenweapon = str(input())
            if chosenweapon == "Rock":
                yourweapon = chosenweapon
                break
            elif chosenweapon == "Paper":
                yourweapon = chosenweapon
                break
            elif chosenweapon == "Scissors":
                yourweapon = chosenweapon
                break
            else:
                print("That is not a weapon. Again!")
        except ValueError:
            print("Not valid")
    print("You chose " + yourweapon)
    print("The Monster Chose " + monsterweapon)
    if (yourweapon == "Rock" and monsterweapon == "Scissors") or (yourweapon == "Paper" and monsterweapon == "Rock") or (yourweapon == "Scissors" and monsterweapon == "Paper"):
        print("You Won! The monster bows before your might.")
    elif (yourweapon == "Rock" and monsterweapon == "Rock") or (yourweapon == "Paper" and monsterweapon == "Paper") or (yourweapon == "Scissors" and monsterweapon == "Scissors"):
        print("YOU TIED! GO AGAIN!")
        fightmechanic(life)
    else:
        if life > 0:
            print("You lost and the monster took your shoes. Move along.")
            life -= 1
            return life
        else:
            print("You had no shoes to take, the monster kills you. GAME OVER!")
            life -= 1
            return life

def Explore(dungeon):
    #This is the engine of the game, calling necessary functions to traverse the dungeon!
    lifeforce = 1
    for i in range(0,5):
        length = len(dungeon)
        print("There are "+str(length)+" rooms to explore.")
        # STEP 1: PICK ROOM
        uip = getvalidroom(length)
        desiredroom = uip - 1
        # STEP 2: INTERACT WITH ROOM
        chosenroom = dungeon[desiredroom]
        dungeon.pop(desiredroom)
        print("You enter the ")
        print(chosenroom["Name"])
        print("The room is " + chosenroom["Description"] )
        # ROCK PAPER SCISSORS FIGHT MECHANIC IF FIGHT IS TRUE FOR THE ROOM
        if chosenroom["Fight"] == True:
            print("The monster challenges you to Rock Paper Scissors!")
            lifeforce = fightmechanic(lifeforce)
            if lifeforce  == -1:
                break
    # STEP 3: AFTER ROOMS EXPLORED CHALLENGE BOSS OR LEAVE?
    print("The Dungeon has been Explored...")

fiverooms = generateDungeon()
Explore(fiverooms)

