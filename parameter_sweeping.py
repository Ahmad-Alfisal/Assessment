# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:30:28 2019

@author: a7md_
"""
import sys
import subprocess

num_of_agents = int(sys.argv[1]) #10
num_of_iterations = int(sys.argv[2]) #100
neighbourhood = int(sys.argv[3]) #20
visual_on = eval(sys.argv[4].title())

for i in range(5):
    subprocess.call(["python", "Communicating.py", str(num_of_agents), str(num_of_iterations), str(neighbourhood), str(visual_on)])
    num_of_agents += 10
    