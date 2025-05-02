# THE 5 ROOM DUNGEON 2!
import random
import tkinter as tk
roomsExplored = 0
score = 0
reward = 50
bosstreasre = 200

# This dictonary is where the game gets room names, desciptions and events that have to happen when a room is used
events = [ 
    {"Name":"Bathroom","Description":"You found the dungeon's bathroom... someone didn't flush.","Fight":False,"Treasure":False},
    {"Name":"Storage Room","Description":"You found a storage room... There is a box of treasure!","Fight":False,"Treasure":True},
    {"Name":"Kitchen","Description":"You found a kitchen... nothing but old bread in here.","Fight":False, "Treasure":False},
    {"Name":"Closit","Description":"You found a closit... as you opened the door a broom fell out and starteled you.","Fight":False,"Treasure":False},
    {"Name":"Library","Description":"You found a room full of books... with an angry librarian inside!","Fight":True,"Treasure":False},
    {"Name":"Barracks","Description":"You found the barracks full of goblins! Defend yourself!","Fight":True, "Treasure":False},
    {"Name":"The Dog House","Description":"You found where the boss keeps his pet Cerberus, and it wants to eat you now!","Fight":True, "Treasure":False},
    {"Name":"Living Room","Description":"You found a living room... and a pile of gold on a table!","Fight":False, "Treasure":True},
    {"Name":"Snake Pit","Description":"You found the snake pit... fight the snakes.","Fight":True, "Treasure":False},
    {"Name":"Hallway","Description":"You found a hallway... it has guards!","Fight":True, "Treasure":False}
    ]

def BossRoom():
    # This opens a window just describing that you met the boss
    boss_window = tk.Toplevel()
    boss_window.title("You entered the boss' lair...")
    label = tk.Label(boss_window, text="Prepare to fight the Boss!", fg="black", padx=150, pady=20)
    label.pack()
    button = tk.Button(boss_window, text="Fight The Boss", command=bossfight)
    button.pack(pady=10)

def bossfight():
    # This window is similar to fightEvent except winning doesnt proceed, it ends the game.
    global score
    battle_window = tk.Toplevel()
    battle_window.title("BOSS BATTLE!")
    label = tk.Label(battle_window, text="Pick your weapon!", fg="black", padx=150, pady=20)
    label.grid(row=0,column = 1)

    def play(choice):
        # Rock Paper Scissors...
        global score
        global bosstreasre
        enemy_choice = random.choice(["Rock", "Paper", "Scissors"])
        if choice == enemy_choice:
            result = f"You have tied! The steaks are raised..."
            bosstreasre += 50
        elif (choice == "Rock" and enemy_choice == "Scissors") or (choice == "Paper" and enemy_choice == "Rock") or (choice == "Scissors" and enemy_choice == "Paper"):
            score += bosstreasre
            result = f"You have defeated the boss of the dungeon! Final Score: {score}"
            button1.config(text="Win",command=gamescreen.destroy)
            button2.config(text="Win",command=gamescreen.destroy)
            button3.config(text="Win",command=gamescreen.destroy)
        else:
            result = f"You were defeated and your corpse now decorates the dungeon. Final Score: {score}"
            button1.config(text="Quit",command=gamescreen.destroy)
            button2.config(text="Quit",command=gamescreen.destroy)
            button3.config(text="Quit",command=gamescreen.destroy)
        label.config(text=result)

    button1 = tk.Button(battle_window, text="Rock", command=lambda: play("Rock"))
    button2 = tk.Button(battle_window, text="Paper", command=lambda: play("Paper"))
    button3 = tk.Button(battle_window, text="Scissors", command=lambda: play("Scissors"))
    button1.grid(row=1, column=0, padx=50, pady=10)
    button2.grid(row=1, column=1, padx=50, pady=10)
    button3.grid(row=1, column=2, padx=50, pady=10)

def fightEvent(special_window):
    # Plays rock paper scissors with enemies
    global score
    battle_window = tk.Toplevel()
    battle_window.title("Fight Time!")
    label = tk.Label(battle_window, text="Pick your weapon!", fg="black", padx=150, pady=20)
    label.grid(row=0,column = 1)

    def play(choice):
        # Rock Paper Scissors
        global score
        global reward
        enemy_choice = random.choice(["Rock", "Paper", "Scissors"])

        def closewindows():
            # Needed to proceed the game
            special_window.destroy()
            battle_window.destroy()

        if choice == enemy_choice:
            result = f"You have tied! The steaks are raised..."
            reward += 50
        elif (choice == "Rock" and enemy_choice == "Scissors") or (choice == "Paper" and enemy_choice == "Rock") or (choice == "Scissors" and enemy_choice == "Paper"):
            result = f"You win! You collect your reward and proceed."
            score += reward
            button1.config(text="Proceed",command=closewindows)
            button2.config(text="Proceed",command=closewindows)
            button3.config(text="Proceed",command=closewindows)
        else:
            result = f"You were defeated and your corpse now decorates the dungeon. Final Score: {score}"
            button1.config(text="Quit",command=gamescreen.destroy)
            button2.config(text="Quit",command=gamescreen.destroy)
            button3.config(text="Quit",command=gamescreen.destroy)
        label.config(text=result)

    button1 = tk.Button(battle_window, text="Rock", command=lambda: play("Rock"))
    button2 = tk.Button(battle_window, text="Paper", command=lambda: play("Paper"))
    button3 = tk.Button(battle_window, text="Scissors", command=lambda: play("Scissors"))
    button1.grid(row=1, column=0, padx=50, pady=10)
    button2.grid(row=1, column=1, padx=50, pady=10)
    button3.grid(row=1, column=2, padx=50, pady=10)

def openDoor():
    # Sorts out what room you enter and what happens in that room
    global roomsExplored
    global score
    if roomsExplored == 5:
       BossRoom()
    else:
        roomsExplored += 1
        event = random.choice(events)
        room_window = tk.Toplevel()
        room_window.title(event["Name"])
        label = tk.Label(room_window, text=event["Description"], fg="black", padx=150, pady=20)
        label.pack()
        closebutton = tk.Button(room_window, text="Close", command=room_window.destroy)
        closebutton.pack(pady=10)
        if event["Fight"] == True:
            closebutton.config(text="Begin Combat", command=lambda: fightEvent(room_window))
        if event["Treasure"] == True:
            score += 50
    

# Define the main game menu
gamescreen = tk.Tk()
gamescreen.title("The Five Room Dungeon!")
Label = tk.Label(gamescreen, text="Choose an Action.", fg="black")
Label.pack(pady=20,padx=150)
Roombutton = tk.Button(gamescreen, text="Enter Room", command=openDoor)
Roombutton.pack(pady=20,padx=150)
closebutton = tk.Button(gamescreen, text="Quit Game", command=gamescreen.destroy)
closebutton.pack(pady=10)
gamescreen.mainloop()