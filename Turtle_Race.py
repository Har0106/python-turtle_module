import turtle
import random

width, length = 400, 400

def number():
    n = input('How many racers do you want? ')
    while True:
        if n.isdigit():
            return int(n)
        else:
            print('Invalid number try again: ')

def ready(n):
    for i in range(int(n)):
        har = turtle.Turtle()
        har.shape('turtle')
        har.setheading(90)
        har.color(['red', 'blue', 'yellow', 'black', 'green'][i])
        har.penup()
        x = -width + ((width*2 // (int(n)+1))*(i+1))
        har.setpos(x, -250)

ready(number())
turtle.Screen().screensize(400, 400)

turtle.mainloop()