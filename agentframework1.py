# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 19:31:00 2019

@author: a7md_
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:31:36 2019

@author: ml18a22a
"""
import random

class Agent:
    
    def __init__(self, x0, y0, enviroment):
        self.x = x0
        self.y = y0
        self.enviroment = enviroment
        self.store = 0
        
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y) + "store" + str(self.store)  
    
    def move(self):
        #print("move")
        #print("from ", self.x, self.y)
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.enviroment)
            #print("+ x")
        else:
            self.x = (self.x - 1) % len(self.enviroment)
            #print("- x")
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.enviroment)
            #print("+ y")
        else:
            self.y = (self.y - 1) % len(self.enviroment)
            #print("- y")
        #print("to ", self.x, self.y)
    def eat(self):
            if self.enviroment[self.y][self.x] >10:
                self.enviroment[self.y][self.x]-= 10
                self.store+= 10
            else:
                self.store +=   self.enviroment[self.y][self.x]
                self.enviroment[self.y][self.x]=0
            if self.store > 100:
                 self.enviroment[self.y][self.x]+= self.store
                 self.store = 0
                
            