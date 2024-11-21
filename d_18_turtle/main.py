from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
timmy = Turtle()
timmy.shape("circle")
timmy.color("HotPink")

def color_t():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
print(color_t)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)

# timmy.color('red')
# timmy.fillcolor('yellow')
# timmy.begin_fill()

# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break

# timmy.end_fill()

# for _ in range(10):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()
# sides = 2
# for _ in range(10):
#     sides += 1
#     n = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(n)
timmy.speed(0)
def color_circle(seperation):
    sides = int(360/seperation)
    for _ in range(sides):
        timmy.pencolor(color_t())
        timmy.circle(70)
        timmy.left(seperation)
color_circle(2)

screen = Screen()
screen.exitonclick()