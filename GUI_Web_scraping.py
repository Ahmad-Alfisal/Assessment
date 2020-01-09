
import random
import matplotlib.pyplot
import matplotlib
matplotlib.use("TkAgg")
import agentframework4
import matplotlib.animation 
import tkinter
import requests
import bs4


agents = []
enviroment = []

def load_data_from_web():
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    
    for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        agents.append(agentframework4.Agent(x,y, enviroment, agents))



fig = matplotlib.pyplot.figure()
carry_on = True
def update(F):
    global carry_on
    fig.clear()   

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
        
    with open ("out.txt", "w") as file:
        for row in enviroment:
            for value in row:
                file.write(f"{value},")
            file.write("\n")

    with open("stores.txt", "a") as file:
        for agent in agents:
            file.write(f"{agent.store},")
        file.write("\n")
        

num_of_agents = 10 
num_of_iterations = 100
neighbourhood = 20


with open("in.txt") as file:
    for line in file:
        row = list(eval(line))
        enviroment.append(row)
        

def run():
    load_data_from_web()
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    
root = tkinter.Tk() 
root.wm_title("GUI")


menu_bar=tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Run", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

tkinter.mainloop()
