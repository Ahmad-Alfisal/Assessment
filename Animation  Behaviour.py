# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:57:16 2019

@author: a7md_
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:31:45 2019

@author: a7md_

"""
import random
import operator
import matplotlib.pyplot
import agentframework2


#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.y - agents_row_b.y)**2) +
#        ((agents_row_a.x - agents_row_b.x)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
" as above we add how many agents we want and how many steps they move "
agents = []
enviroment = []

with open("in.txt") as file:
    for line in file:
        row = list(eval(line))
        enviroment.append(row)
        
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework2.Agent(random.randint(0,len(enviroment)-1),random.randint(0,len(enviroment)-1), enviroment, agents))

# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
"as above the agent shoud move and eat(change) ever time we run it."

matplotlib.pyplot.xlim(0, len(enviroment)-1)
matplotlib.pyplot.ylim(0, len(enviroment)-1)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].y,agents[i].x, color="yellow")
matplotlib.pyplot.imshow(enviroment)    
matplotlib.pyplot.show()
#
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

