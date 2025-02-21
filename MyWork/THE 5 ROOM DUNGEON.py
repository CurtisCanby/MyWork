# THE 5 ROOM DUNGEON
events = [ 
    {"Name":"Room Too Dark To See","Description":"Though the room is dark, you feel a presence watching you","Fight":False},
    {"Name":"Sleeping Quarters","Description":"You wake up a sleeping goblin!","Fight":True}
          ]

def generateDungeon():
    dungeon = []
    dungeon.append(events[1])

    return dungeon

def Explore(dungeon):
    for room in dungeon:
        print("You enter a " + room['Name'])
        print(room['Description'])
        if room['Fight'] == True:
            #Roll a combat event?
            print("You got into a fight and won!")
        else:
            print("You safely leave the room")

fiverooms = generateDungeon()
Explore(fiverooms)

