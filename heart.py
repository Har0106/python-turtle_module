import turtle

screen = turtle.Screen()
screen.title('Heart')
screen.bgcolor('pink')

tur = turtle.Turtle()
tur.color('maroon', 'red')
tur.pensize(20)

tur.begin_fill()

tur.penup()
tur.setpos(0, -150)
tur.left(140)
tur.pendown()
tur.forward(200)
tur.circle(-100, 200)
tur.setheading(60)
tur.circle(-100, 200)
tur.forward(200)

tur.end_fill()

turtle.done()