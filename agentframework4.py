


# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:31:36 2019

@author: ml18a22a
"""
import random

class Agent:
    
    def __init__(self, x0, y0, enviroment, agents):
        self.x = x0
        self.y = y0
        self.enviroment = enviroment
        self.store = 0
        self.agents = agents
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y) + "store" + str(self.store)  
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.enviroment)
        else:
            self.x = (self.x - 1) % len(self.enviroment)
    
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.enviroment)
        else:
            self.y = (self.y - 1) % len(self.enviroment)

    def eat(self):
            if self.enviroment[self.y][self.x] >10:
                self.enviroment[self.y][self.x]-= 10
                self.store+= 10
            else:
                self.store +=   self.enviroment[self.y][self.x]
                self.enviroment[self.y][self.x]=0

              
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average_store = (self.store + agent.store)/ 2
                self.store = average_store
                agent.store = average_store

                
    def distance_between(self, agent):
        return ((self.y- agent.y)**2 +(self.x - agent.x)**2)**0.5
