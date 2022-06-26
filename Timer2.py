import turtle
import time

n = int(input('Set Timer: '))

screen = turtle.Screen()

user = turtle.Turtle()
timer = turtle.Turtle()
timer.color('red')
timer.setpos(-100, 0)
start = time.time()
sec = 0

while sec < n:
    user.penup()
    user.hideturtle()
    user.forward(1)
    user.left(1)
    timer.hideturtle()
    timer.clear()
    sec = time.time() - start
    timer.write('{:.2f}'.format(sec).replace('.', ':'), font=('Courier', 50, 'bold'))
    screen.update()

print('Time is Over')