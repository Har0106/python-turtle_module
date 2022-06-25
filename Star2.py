import turtle

screen = turtle.Screen()
screen.title('Star')

tur = turtle.Turtle()

for i in range(8):
    tur.forward(250)
    tur.left(135)

turtle.done()