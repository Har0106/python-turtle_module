import turtle
import random
import time

width, length = 400, 400
colors = ['red', 'blue', 'yellow', 'black', 'green']

n = input('How many racers do you want (1-5)? ').strip()
while True:
    if n.isdigit() and n != '0':
        if int(n) <= 5:
            n = int(n)
            break
        else:
            n = input('Number out of range. Try again: ')
            continue
    else:
        n = input('Invalid number try again: ')

racers = []

for i in range(n):
    har = turtle.Turtle()
    har.shape('turtle')
    har.setheading(90)
    har.color(colors[i])
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

with open('scores.txt', 'r+') as file:
    content = ''
    for i in file.readlines():
        win, score = i.split(' : ')
        if win == winner:
            i = f'{win} : {int(score)+1}\n'
        content += i
    file.seek(0)
    file.write(content)

time.sleep(3)
