# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:18:49 2019

@author: ml18a22a
"""

# blur ---------------------------------------
import matplotlib.pyplot
import random
import operator

import matplotlib.pyplot
import agentframework
import matplotlib.pyplot
data = []
processed_data = []

# Fill with random data.
for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
datarow.append(random.randint(0,255))
    datarow.append(datarow)

# Blur.
for i in (range(0,99)):
    datarow = []
    for j in (range(0,99)):
        sum = data[i][j]
        sum += data[i-1][j]
        sum += data[i+1][j]
        sum += data[i][j+1]
        sum += data[i][j-1]
        sum /= 5
    datarow.append(sum)
    processed_data.append(datarow)

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
matplotlib.pyplot.imshow(processed_data)
matplotlib.pyplot.show()

# End ---------------------------------------