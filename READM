



Created by:  Ahmad alfisal
Student ID: 201289481

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Moudel summary:

This file includes the number of 10 agents, an environment has been created and special codes have been created so that the agents they
can move in this environment and eat and share with the neighbor within a distance of 20.

The model includes several files to be run as required which is it:
- "GUI_Web_scraping.py"  It is the main file of the model and it contains all command or script.
- "agentframework4.py" provides framework file to run the model  which containe the required algorithms and to reduce operating burden of the main model.
- "in.txt" this file contain the environment data where the program pulls data from it and adds it after analyzing it by the operator and adding it 
to the environment file.
-"stores.txt" the mian of this file to save storage for each agent.
- "http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html" it web data which contain the y,x and z values in this project 

 

The aim of the model is :

to create environmental and agents, and the agents interact with each othe and eating and share as well
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
***********************************************************************************************************************************************************************
***********************************************************************************************************************************************************************
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                               the GUI file
                                                      **###  GUI_Web_scraping.py  ###**


import random                            ### library for producing random numbers ### 
import matplotlib.pyplot                 ### library for creating charts ### 
import matplotlib
matplotlib.use ("TkAgg")                 ### Windows Library ### 
import agentframework4                   ### framework file ### 
import sys                               ### a library that helps run the data from Pormpt screen ### 
import matplotlib.animation              ### Animation Library ### 
import tkinter                           ### Windows Library Menus Library ### 
import requests                          ### library to retrieve data from the internet ### 
import bs4                               ### internet data analysis ### 


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

agents = []      ### agents list ### 
enviroment = []  ### enviroment list ### 

def load_data_from_web ():  ### Define the function that gets data from the web ### 
    r = requests.get ('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')

    content = r.text                                   ### page content and we define it as a content ### 
    soup = bs4.BeautifulSoup (content, 'html.parser')  ### specifies the type of content before the analysis process and is defined as sup ### 
    td_ys = soup.find_all (attrs = {"class": "y"})     ### Collect all the information that classifies (Y) and place it in the TD_YS variable ### 
    td_xs = soup.find_all (attrs = {"class": "x"})     ### Collect all the information that classifies (x) and put it in the td_xs variable ### 
 
    
    for i in range (num_of_agents):                                       ### Agent production ### 
        y = int (td_ys [i] .text)                                         ### call the value of y from the variable td_ws ### 
        x = int (td_xs [i] .text)                                         ### call the x value from the td_xs variable ### 
        agents.append (agentframework4.Agent (x, y, enviroment, agents))  ### to create agents and add them to the list ### 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

fig = matplotlib.pyplot.figure () ###  Create a blank graphic ### 
carry_on = True                   ### is a variable that specifies the continuation or stopping of animation ### 
def update (F):                   ### defines the function of the animation ### 
    global carry_on               ### Indicating and linking a variable outside the function ### 
    fig.clear ()                  ### command each time a graphic is created, it is deleted ### 



                                                  ** ###  Move the agents ### **

    for j in range (num_of_iterations):                       ###  for Move Agents ### 
        random.shuffle (agents)                               ### shake agents for every time we run the model and reorder them ### 
        for i in range (num_of_agents):                       ### Every agents has an order like this ### 
            agents [i] .move ()                               ### call the moving function ### 
            agents [i] .eat ()                                ### call the eating function ### 
            agents [i] .share_with_neighbours (neighborhood)  ### call the share function ### 

### And all of these calls and functions are found in Agent FrameWork4 file ### 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    for i in range (num_of_agents):                                                ### Every agents has an order like this ### 
        matplotlib.pyplot.scatter (agents [i] .y, agents [i] .x, color = "yellow") ### command to draw and color each point for each customer ### 
    matplotlib.pyplot.imshow (enviroment)                                          ### Show the background graphic ### 
    
    for agent in agents:         ### stop motion condition ### 
        if agent.store <3000:    ### If the agents has is less than 3000 means Keep moving ### 
            return         
        
    carry_on = False            ### If return does not apply this means stopping ### 
    
def gen_function ():            ### number of iterations ### 
    while carry_on:             ### As long as there is continuity ### 
        yield 1                 ###  gives a repeat order once ### 
        
    with open ("out.txt", "w") as file:   ### save the result after the animation stops ### 
        for row in enviroment:            ### for each line in the environment ### 
            for value in row:             ### for each part in a line ### 
                file.write (f "{value},") ### Write this vertex in this file ### 
            file.write ("\ n")            ### If all values ​​on the line end, create a new line ### 

    with open ("stores.txt", "a") as file:     ### Create  a stores file ### 
        for agent in agents:                   ### for each agent in agents do the following ### 
            file.write (f "{agent.store},")    ### records the agents inventory in this file ### 
        file.write ("\ n")                     ### If all agents end up on the line, create a new line ### 


----------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

                     **### the following make the model run in spider or any python operator and in the Pormpt screen ###**    
 
try: try it
    num_of_agents = int (sys.argv [1])     ### Read the first value from the Pormpt screen ### 
except:
    num_of_agents = 10                     ### if there is no value to use this number 10 ### 

try:
    num_of_iterations = int (sys.argv [2]) ### Read the second value from the Pormpt screen ### 
except:
    num_of_iterations = 100                ### if there is no value using this number 100 ### 

try:
    neighborhood = int (sys.argv [3])      ### Read the third value from the Pormpt screen ### 
except:
    neighborhood = 20                      ### if there is no value use this number 20 ### 


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


with open ("in.txt") as file:     ### to read the environment ### 
    for line in file:             ### for each line of the file ### 
        row = list (eval (line))  ###  creates a row ### 
        enviroment.append (row)   ### Adds the row in the environment variable ### 


def run ():                ###  to  command the run function ### 
    load_data_from_web ()  ### Call the function to fetch data from the net ### 
    animation = matplotlib.animation.FuncAnimation (fig, update, frames = gen_function, repeat = False) 
    ### to Call the move function until the stop function orders it stop ### 

    canvas.draw () ### Show the graph inside the window ### 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                         **### to create a window  ###**

  
root = tkinter.Tk ()                                        ###  Create a window ### 
root.wm_title ("GUI")                                       ###  Give a title to the window ### 
menu_bar = tkinter.Menu (root)                              ###  Create a menu bar ### 
root.config (menu = menu_bar)                               ### Install the menu bar inside the window ### 
model_menu = tkinter.Menu (menu_bar)                        ### Create a menu ### 
menu_bar.add_cascade (label = "Run", menu = model_menu)     ### Install the menu inside the menu bar and it is named Run ### 
model_menu.add_command (label = "Run Model", command = run) ###  Add a command inside the menu ### 

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg (fig, master = root)
canvas._tkcanvas.pack (side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)
mainloop ()                                                                     ### Keep window open until closed ### 


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
***********************************************************************************************************************************************************************
***********************************************************************************************************************************************************************
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                                     the framework File

                                                                 **### agentframework4.py ###**

                                                            **### the agents creation function ###**
    
    def __init __ (self, x0, y0, enviroment, agents): 
        self.x = x0                                   ### Determine the value of the x ###
        self.y = y0                                   ### Determine the value of y ###
        self.enviroment = enviroment                  ### Determine the value of the environment ###
        self.store = 0                                ### Give the store an initial value of zero ###
        self.agents = agents                          ### agents List ### 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                               
                                                    **### the agnets description function ###**

    def __str __ (self):                            
        return "x =" + str (self.x) + ", y =" + str (self.y) + "store" + str (self.store)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                          **### agent movement function ###**    
    def move (self): 

        if random.random () <0.5:                        ###  Gives a movement condition to the left or right if the value is less than or more than ### 
            self.x = (self.x + 1)% len (self.enviroment) ### right movement ### 
        else:
            self.x = (self.x - 1)% len (self.enviroment) ### left movement ### 
        if random.random () <0.5:                        ### Gives a condition to move up or down if the value is less than or more than ### 
            self.y = (self.y + 1)% len (self.enviroment) ### Move down ###    
        else:
            self.y = (self.y - 1)% len (self.enviroment) ### Move up ### 
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

							 **### the eating  function ###** 
    def eat (self):                                     
            if self.enviroment [self.y] [self.x]> 10:    ### Eats if the agents is standing in an area if the area hane valuet more than 10 ### 
                self.enviroment [self.y] [self.x] - = 10 ### The place where it eat is less then 10 ### 
                self.store + = 10                        ### The store within the agent increases by 10 ### 
            else: or
                self.store + = self.enviroment [self.y] [self.x] ###  eats all the rest of the place ### 
                self.enviroment [self.y] [self.x] = 0            ### and the value after eating will be 10 ### 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

   							**### share function ###**            
    def share_with_neighbours (self, neighborhood): 
        for agent in self.agents:                           ### for each agent ### 
            distance = self.distance_between (agent)        ### call the distance function ### 
            if distance <= neighborhood:                        ### if the  distance between every agents allowed to shear ### 
                average_store = (self.store + agent.store) / 2  ### Calculate the sum and divide it by two ### 
                self.store = average_store                      ### Give the average to the first agent ### 
                agent.store = average_store                     ### Give the average to the second agent ### 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                               **### distance calculation function ###**              
    def distance_between (self, agent): 
        return ((self.y-agent.y) ** 2 + (self.x - agent.x) ** 2) ** 0.5

***********************************************************************************************************************************************************************

                                                                	** THE END **


