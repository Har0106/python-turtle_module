import turtle

screen = turtle.Screen()
screen.bgcolor('pink')
screen.title('Custom Design')

tur = turtle.Turtle()
tur.color('blue', 'cyan')
tur.pensize(10)

tur.begin_fill()
tur.circle(50)
tur.end_fill()

turtle.done()
