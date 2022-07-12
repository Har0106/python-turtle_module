import turtle

screen = turtle.Screen()
screen.title('Flower')

tur = turtle.Turtle()
tur.color('red', 'yellow')

tur.begin_fill()
for i in range(36):
    tur.forward(200)
    tur.left(170)
tur.end_fill()

turtle.done()