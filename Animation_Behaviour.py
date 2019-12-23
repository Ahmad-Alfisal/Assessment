
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:31:45 2019

@author: a7md_

"""
import random
import operator
import matplotlib.pyplot
import agentframework3
import sys
import matplotlib.animation 

#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.y - agents_row_b.y)**2) +
#        ((agents_row_a.x - agents_row_b.x)**2))**0.5

fig = matplotlib.pyplot.figure()
carry_on = True
def update(F):
    global carry_on
    fig.clear()   
    # Move the agents.
    for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x, color="yellow")
    matplotlib.pyplot.imshow(enviroment)    
    
    for agent in agents:
        if agent.store < 3000:
            return
        
    carry_on=False
    
def gen_function():
    while carry_on:
        yield 1
        
try:
    num_of_agents = int(sys.argv[1])
except:
    num_of_agents = 10 

try:
    num_of_iterations = int(sys.argv[2]) #100
except:
    num_of_iterations = 100

try:
    neighbourhood = int(sys.argv[3]) #20
except:
    neighbourhood = 20

#try:   
#    visual_on = eval(sys.argv[4].title())
#except: 
#     visual_on = True
" as above we add how many agents we want and how many steps they move "
agents = []
enviroment = []

with open("in.txt") as file:
    for line in file:
        row = list(eval(line))
        enviroment.append(row)
        
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework3.Agent(random.randint(0,len(enviroment)-1),random.randint(0,len(enviroment)-1), enviroment, agents))

    
"as above the agent shoud move and eat and shering(change) ever time we run it."


matplotlib.pyplot.xlim(0, len(enviroment)-1)
matplotlib.pyplot.ylim(0, len(enviroment)-1) 
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()

#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b)
#        "print (distance)"
        
with open ("out.txt", "w") as file:
    for row in enviroment:
        for value in row:
            file.write(f"{value},")
        file.write("\n")

with open("stores.txt", "a") as file:
    for agent in agents:
        file.write(f"{agent.store},")
    file.write("\n")

