import turtle
import random

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'indigo', 'violet']
window = turtle.Screen().bgcolor('black')
har = turtle.Turtle()
har.width(5)

for i in range(20):
    har.penup()
    har.color(random.choice(colors), random.choice(colors))
    x = random.randrange(-325, 325)
    y = random.randrange(-325, 325)
    har.setpos((x, y))
    har.pendown()
    har.begin_fill()
    har.circle(random.randrange(10, 100))
    har.end_fill()

turtle.done()