#Imports and Inputs

from turtle import * 
import pandas as pd, pygal, random

Excel_Name = str(input("What is your files name? (Have this in the same directory): "))
List_Amount = int(input("How many lists would you like to do: "))
Excel_Data = pd.read_csv(Excel_Name)
Data_Names = []

#List and column maker for the excel document and turtle graphing

List_of_lists = []

def List_Creator(temp_list, temp_column):
    temp_list = Excel_Data[temp_column].tolist()
    List_of_lists.append(temp_list)
    
for i in range(List_Amount):
    list_name = str(input("What would you like the list to be named?: "))
    Data_Names.append(list_name)
    column_name = str(input("What is the name of the column you want the data from?: "))
    List_Creator(list_name, column_name)
    
#Excel Creator
Excel_Graph_Counter = 0
Line_Name_Counter = 0

Excel_Graph = pygal.Line()
Excel_Graph.title = str(input("What would you like your CSV Graph to be named"))
for i in range(List_Amount):
    Graph_Name = Data_Names[Line_Name_Counter]
    Excel_Graph.add(Graph_Name, List_of_lists[Excel_Graph_Counter])
    Excel_Graph_Counter += 1
    Line_Name_Counter += 1
Excel_Graph.render_to_file("Your Graph.svg")



#Turtle Grapher function and lists ----------------------------------------------------------------------------------------------------------------

color_list = ["Blue", "Red", "Green", "cyan", "purple"]
turtle_degrees = [0, 90]
turtle_distance = [800, 300]
dud_list = []

def plot_graph(turtle_degrees, turtle_distance, temp_list) :
    tturtle = Turtle()
    tturtle.speed(0)
    tturtle.color(random.choice(color_list))
    tturtle.hideturtle()
    tturtle.penup()               
    tturtle.goto(-450, -150)           
    tturtle.pendown()
    ax = 0
    
    if len(temp_list) > 2 :
        for item in temp_list:
            tturtle.goto(ax - 450, (item * 10) - 150 )
            ax += 1.5
    elif len(temp_list) == 0:
        tturtle.color("black")
        tturtle.left(turtle_degrees)
        tturtle.forward(turtle_distance)

plot_graph(turtle_degrees[1], turtle_distance[1], dud_list)
plot_graph(turtle_degrees[0], turtle_distance[0], dud_list)

List_counter = 0
for i in range(List_Amount):
    plot_graph(None, None, List_of_lists[List_counter])
    List_counter += 1
