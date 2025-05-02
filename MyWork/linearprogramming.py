from pulp import *
production = LpProblem("Production Schedule",LpMinimize)

time = [1,2,3,4,5]
products = ["pr1","pr2","pr3"]

x = LpVariable.dicts("Quantity",[(i,t) for i in products for t in time], 0)

# Parameters and Data 
upc = {1:7, 2:8, 3:8 , 4:8, 5:7}    # unit production cost 
demand = {"pr1":{1:100, 2:100, 3:150 , 4:200, 5:150},
          "pr2":{1:60, 2:1000, 3:300 , 4:6, 5:150},
          "pr3":{1:1000, 2:10, 3:15 , 4:2000, 5:500}}  # demand data
ulabor = {"pr1":0.5,"pr2":0.6,"pr3":0.8}   # man-hours of labor used per unit of product
Tlabor = {1:600, 2:600, 3:800 , 4:1500, 5:1000} # available man-hours labor

# Objective function
production += lpSum(upc[t] * x[(i, t)] for i in products for t in time)

# Constraints (Capacity and Demand) for each time period
for t in time:
    production += lpSum(ulabor[i] * x[(i, t)] for i in products) <= Tlabor[t]
    for i in products:
        production += lpSum(x[(i, t)] for i in products) >= demand[i][t]

# solve the problem
production.solve()
print("Solution Status = ", LpStatus[production.status])

# Print the solution of the Decision Variables
for v in production.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)

# Print the optimal objective function
print("Total Cost = ", value(production.objective))