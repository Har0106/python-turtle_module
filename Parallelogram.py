import turtle

screen = turtle.Screen()
screen.title('Parallelogram')

tur = turtle.Turtle()

for i in range(2):
    tur.forward(200)
    tur.left(60)
    tur.forward(100)
    tur.left(120)

turtle.done()