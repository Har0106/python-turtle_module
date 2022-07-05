import turtle

screen = turtle.Screen()
screen.title('Circles inside circles')

tur = turtle.Turtle()

for i in range(5):
    tur.circle((i+1)*25)

turtle.done()