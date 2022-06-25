import turtle
import time

n = int(input('Set Timer: '))

screen = turtle.Screen()

user = turtle.Turtle()
timer = turtle.Turtle()
timer.color('red')
timer.setpos(-30, 0)
start = time.time()

while time.time() - start < n:
    user.penup()
    user.hideturtle()
    user.forward(1)
    user.left(1)
    timer.hideturtle()
    timer.clear()
    timer.write(int(time.time() - start), font=('Courier', 50, 'bold'))
    screen.update()

print('Time is Over')