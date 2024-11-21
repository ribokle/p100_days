import colorgram
import random
import turtle as t 
from turtle import Turtle, Screen, screensize

color_list = [(236, 144, 89), (225, 236, 243), (68, 97, 166), (247, 223, 53), (160, 70, 26), (74, 166, 67), (238, 87, 122), (106, 197, 223), (251, 143, 163), (86, 206, 193), (236, 69, 39), (237, 121, 149), (21, 29, 73),
              (61, 145, 42), (41, 51, 21), (4, 171, 191), (238, 208, 4), (116, 218, 201), (239, 172, 153), (205, 22, 13), (165, 195, 221), (144, 57, 73), (151, 27, 35), (46, 54, 102), (23, 35, 14), (135, 212, 229), (82, 121, 180)]

def hirst_painting(num_dot, size_dot, spacing):
    width = 20 + (num_dot * ( spacing))
    t.colormode(255)
    t.setup(width, width)
    hirst = Turtle()
    hirst.hideturtle()
    hirst.up()
    hirst.speed(0)
    locx = width/2 - 20
    locy = width/2 - 20
    hirst.setpos((-locx,-locy))
    hirst.down()
    hirst.shape("circle")
    hirst.shapesize(size_dot/20)
    for _ in range(num_dot):
        hirst.up()
        hirst.setpos((-locx,-locy))
        locy -= spacing
        for _ in range(num_dot):
            hirst.down()
            hirst.color(random.choice(color_list))
            hirst.stamp()
            hirst.up()
            hirst.forward(spacing)
            hirst.down()

hirst_painting(15, 15, 40)

i = Screen()
i.exitonclick()




# colors = colorgram.extract('image.jpg', 30)
# list = []
# for _ in range(len(colors)):
#     rgb = colors[_].rgb
#     r = rgb.r 
#     g = rgb.g 
#     b = rgb.b 
#     list.append((r , g, b))
# print(list)

