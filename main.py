import turtle

import colorgram
from turtle import *
import random

#20 in size, spaced by 50

def extract_colors(picture):


    colors = colorgram.extract(picture, 40)

    li =[tuple(c.rgb) for c in colors]

    return li

color_list = extract_colors("damien.jpeg")

screen = Screen()


turtle.colormode(255)
tim = Turtle()
tim.hideturtle()

tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed(0)

for i in range(10):
    for j in range(9):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.left(90)
    tim.forward(50)
    tim.left(90)
    for z in range(9):
        tim.forward(50)
    tim.right(180)
















screen.exitonclick()