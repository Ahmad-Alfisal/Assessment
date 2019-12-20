# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:31:36 2019

@author: ml18a22a
"""
import random

class Agent:
    
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y)
    
    def move(self):
        #print("move")
        #print("from ", self.x, self.y)
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
            #print("+ x")
        else:
            self.x = (self.x - 1) % 100
            #print("- x")
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
            #print("+ y")
        else:
            self.y = (self.y - 1) % 100
            #print("- y")
        #print("to ", self.x, self.y)
