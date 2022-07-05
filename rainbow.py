import turtle

screen = turtle.Screen()
screen.screensize(300, 300)

tur = turtle.Turtle()
tur.setheading(90)
tur.width(25)
colors = ['#9400D3', '#4B0082', '#0000FF', '#00FF00', '#FFFF00', '#FF7F00', '#FF0000']

for i in range(7):
    tur.penup()
    tur.setpos(100+(i*20), -50)
    tur.pendown()
    tur.color(colors[i])
    tur.setheading(90)
    tur.circle(100+(i*20), 180)

turtle.done()