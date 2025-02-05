# I PICK LIST AND SET.
# Also playing with how classes opperate.
import random
class datastructs:
    def __init__(self,list,set):
        # Creating the list and set
        self.list = list
        self.set = set
    
    def GetThirdElements(self):
        # PRINT THE THIRD ELEMENT OF THE SET AND LIST (IF YOU CAN!!!)
        print("Sets are unordered. They dont even have a So Called Third Element!")
        print("The third element of the list is " + self.list[2])

    def GetRandomElements(self):
        # PRINT A RANDOMIZED LIST AND SET (SET IS ALREADY RANDOM)
        print("Here are random elements from the List,")
        x = len(self.list)
        # making a dupe list so I dont pop all the elements of my main list
        templist = []
        for i in range(len(self.list)):
            templist.append(self.list[i])
        randomizedlist = []
        for i in range(x):
            rando = random.randrange(0,len(templist))
            randomizedlist.append(templist.pop(rando))
        print(randomizedlist)
        print("Here are random elements from the set, ")
        print(self.set)
    
    def AddNewElements(self, listelement, setelement):
        # ADD A NEW ELEMENT TO THE END OF THE STRUCTURES
        # Sets arent ordered so there is no "end" but ill just add the element in anyway.
        self.list.append(listelement)
        print("The new list is,")
        print(self.list)
        self.set.add(setelement)
        print("The new set is, ")
        print(self.set)
    
    def RemoveFirstElement(self):
        # REMOVE THE FIRST ELEMENT OF EACH STRUCTURE
        # there is no first element of a set, so ill just remove a random one
        self.list.pop(0)
        print("The new list is, ")
        print(self.list)
        self.set.pop()
        print("Your new set is, ")
        print(self.set)

    def RemoveSameElement(self, element):
        # REMOVE THE SAME ELEMENT FROM BOTH STRUCTURES
        # Will raise an error if the element isnt in the list.
        self.set.discard(element)
        self.list.remove(element)
        print("The Specified element has been removed")
        print("Your new list is, ")
        print(self.list)
        print("The Specified element has been removed")
        print("Your new set is, ")
        print(self.set)

        


listoffoods = ["Starfruit", "Fish", "Steak", "Melon", "Cantelope", "Bannana", "Apple", "Pear", "Orange", "Grapefruit"]
setoffoods = {"Grapefruit", "Orange", "Pear", "Apple", "Bannana", "Cantelope", "Melon", "Steak", "Fish", "Starfruit"}
DataStructures = datastructs(listoffoods,setoffoods)
DataStructures.GetThirdElements()
DataStructures.GetRandomElements()
DataStructures.AddNewElements("Carrot", "Carrot")
DataStructures.RemoveFirstElement()
DataStructures.RemoveSameElement("Carrot")