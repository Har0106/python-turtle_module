import turtle

screen = turtle.Screen()
screen.bgcolor('maroon')
screen.title('Star')

tur = turtle.Turtle()

tur.penup()
tur.setpos(90, 30)
tur.pensize(20)
colors = ['blue', 'red', 'green', 'orange', 'purple']

tur.pendown()
for i in range(5):
    tur.color(colors[i])
    tur.right(144)
    tur.forward(200)

turtle.done()