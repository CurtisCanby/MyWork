import random
import secrets
import timeit

class rngandsorting:
    # Uses classes again because I like OOP :)
    def __init__(self):
        return None
    
    def randomfill(self, max):
        # FILL A DATASTRUCTURE WITH 100 RANDOM NUMBERS USING RANDOM
        randomlist = []
        for i in range(100):
            x = random.randrange(1,max+1)
            randomlist.append(x)
        return randomlist
    
    def randomfill100k(self, max):
        # FILL A DATASTRUCTURE WITH 100k RANDOM NUMBERS USING RANDOM
        randomlist = []
        for i in range(100000):
            x = random.randrange(1,max+1)
            randomlist.append(x)
        return randomlist
    
    def secretsfill(self, max):
        # FILL A DATASTRUCTURE WITH 100 RANDOM NUMBERS USING SECRETS
        secretlist = []
        for i in range(100):
            x = secrets.randbelow(max)+1 # randbelow includes 0, so I had to add 1
            secretlist.append(x)
        return secretlist
    
    def countrepeats(self, list):
        # GET A COUNT OF THE UNIQUE NUMBERS IN A DATASTRUCT
        count = {}
        for i in list:
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1
        sorteddict = {key: val for key, val in sorted(count.items(), key=lambda x: x[0])}
        print(sorteddict)
        # I was originally going to get the counts by using switch case, but I ended up using
        # this solution from stack overflow because it scales with part 2.
        # if the range was still just 1-16 then I woulda kept my switch case solution lol.
        # And copilot made this sorting function. I didn't even know dicts could be sorted so thats cool
    
    def getsmallest(self,list):
        # RETURN THE INDEX OF THE SMALLEST VALUE IN THE LIST
        smallest = 0
        for i in range(0,len(list)):
            if list[smallest] > list[i]:
                smallest = i
        return smallest
    
    def simpleSort(self,list):
        # POP ALL THE SMALLEST VALUES IN LIST UNTILL ITS EMPTY
        # PUT SMALLEST VALUES INTO NEW LIST THEN PRINT THE NEW LIST
        sortedlist = []
        for i in range(0,len(list)):
            svi  = self.getsmallest(list) #svi stands for "smallest value index" because im getting the index of smallest value from getsmallest()
            smallestvalue = list.pop(svi)
            sortedlist.append(smallestvalue)
        return sortedlist
   
        


# PART 1
assignment = rngandsorting()
randomlist = assignment.randomfill(16)
secretlist = assignment.secretsfill(16)
assignment.countrepeats(randomlist)
assignment.countrepeats(secretlist)
# I cant see any indication one is "more random". For my purposes here they are even.

# PART 2
bigrandomlist = assignment.randomfill(65535)
bigsecretlist = assignment.randomfill(65535)
assignment.countrepeats(bigrandomlist)
assignment.countrepeats(bigsecretlist)
# I ran it a few times and didn't get any repeats for either one.

# PART 3
unsortedlist = assignment.randomfill(16)
start1 = timeit.default_timer()
assignment.simpleSort(unsortedlist)
print("Time my sort spent sorting :", timeit.default_timer() - start1)

unsortedlist = assignment.randomfill(16)
start2 = timeit.default_timer()
unsortedlist.sort()
print("Time .sort spent sorting :", timeit.default_timer() - start2)

# .sort() is faster than mine.. obviously LOL

unsortedlist = assignment.randomfill(65535)
start3 = timeit.default_timer()
assignment.simpleSort(unsortedlist)
print("Time my sort spent sorting big numbers :", timeit.default_timer() - start3)

unsortedlist = assignment.randomfill(65535)
start4 = timeit.default_timer()
unsortedlist.sort()
print("Time .sort spent sorting big numbers :", timeit.default_timer() - start4)

# Neither of them seem effected by the size of values

unsortedlist = assignment.randomfill100k(65535)
start5 = timeit.default_timer()
assignment.simpleSort(unsortedlist)
print("Time my sort spent sorting big numbers and long list :", timeit.default_timer() - start5)

unsortedlist = assignment.randomfill100k(65535)
start6 = timeit.default_timer()
unsortedlist.sort()
print("Time .sort spent sorting big numbers and long list :", timeit.default_timer() - start6)

# They both got a little slower with a larger list. I think even 1k items is still not big enough to really effect a computer lol.
# oughta make a list of 100k and then see what happens >:)
# I DID IT! My sort took 2 minutes to do 100k items.. It only took .sort 0.01 seconds