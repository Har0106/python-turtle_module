import turtle

screen = turtle.Screen()
screen.title('Triangle')

tur = turtle.Turtle()

for i in range(3):
    tur.forward(100)
    tur.left(120)

turtle.done()