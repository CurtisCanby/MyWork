#This agent takes in the state of the floor and where it is at to decide action
def Vacuume_Cleaner_Robot(state, loc):
    if state == "Dirty":
        return "Suck the Dirt"
    elif state == "Clean" and loc == "Left":
        return "Go Right"
    elif state == "Clean" and loc == "Right":
        return "Go Left"
    
# Creating a senario where the robot is in the left room and the floor is dirty    
print(Vacuume_Cleaner_Robot("Dirty", "Left"))
# After the floor is vacuumed the agent will need to go to next room!
print(Vacuume_Cleaner_Robot("Clean", "Left"))
    