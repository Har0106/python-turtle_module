import turtle
import random
import time

width, length = 400, 400
colors = ['red', 'blue', 'yellow', 'black', 'green']

n = input('How many racers do you want? ')
while True:
    if n.isdigit():
        n = int(n)
        break
    else:
        n = input('Invalid number try again: ')

racers = []

for i in range(n):
    har = turtle.Turtle()
    har.shape('turtle')
    har.setheading(90)
    har.color(['red', 'blue', 'yellow', 'black', 'green'][i])
    har.penup()
    x = -width + ((width*2 // (int(n)+1))*(i+1))
    har.setpos(x, -250)
    racers.append(har)

winner = ''
found = False

while True:
    for i in racers:
        x,y = i.pos()
        if y >= 255:
            winner = colors[racers.index(i)]
            found = True
        i.pendown()
        i.forward(random.randrange(1, 20))
    if found:
        break

print(f'The Winner is {winner.capitalize()} Turtle')
time.sleep(5)