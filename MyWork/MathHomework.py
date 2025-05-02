from pulp import*
assignment = LpProblem("Assignment_of_Swimmers_to_Styles", LpMinimize)

swimmers = ["Gary", "Mark", "Jim","Chet"] 
styles = ["Free", "Breast", "Fly","Back"] 

supply = {"Gary":1, "Mark":1, "Jim":1, "Chet":1} 
demand = {"Gary":1, "Mark":1, "Jim":1, "Chet":1}

# change 2. complete tcost
tcost= {"Gary":{"Free":54, "Breast":54, "Fly":51, "Back":53},
        "Mark":{"Free":51, "Breast":57, "Fly":52, "Back":52},
        "Jim":{"Free":50, "Breast":53, "Fly":54, "Back":56},
        "Chet":{"Free":56, "Breast":55, "Fly":56, "Back":54},}

# change 3. Write the second key for the variables
#Define the decision variables
x = LpVariable.dicts("ass", (swimmers, styles), lowBound=0) 

# Define the objective function
assignment += lpSum([tcost[i][j]*x[i][j] for i in swimmers for j in styles]) 

# Write the supply constraints:
for i in swimmers:
    assignment+=lpSum(x[i][j] for j in styles)<=supply[i]

#change 4. Write the demand constraints
for j in styles:
    assignment += lpSum(x[i][j] for i in swimmers) == 1

assignment.solve(PULP_CBC_CMD(msg=0))

print("Status= ", LpStatus[assignment.status])
print("Total Cost= ", value(assignment.objective))

for v in assignment.variables():
    if v.value()>0:
        print(v.name, " = ", v.value())

print("\n\n LP model:\n ")
print(assignment)