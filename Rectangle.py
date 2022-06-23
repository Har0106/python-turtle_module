import turtle

screen = turtle.Screen()
screen.title('Rectangle')

tur = turtle.Turtle()

for i in range(2):
    tur.forward(200)
    tur.left(90)
    tur.forward(100)
    tur.left(90)

turtle.done()