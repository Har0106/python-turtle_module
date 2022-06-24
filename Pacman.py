import turtle

screen = turtle.Screen()
screen.title('Pacman')

tur = turtle.Turtle()
tur.color('yellow')

tur.begin_fill()

tur.left(150)
tur.forward(200)
tur.setheading(60)
tur.circle(-200, 300)
tur.right(90)
tur.forward(200)

tur.end_fill()

turtle.done()