import turtle
import random

screen = turtle.Screen()

snake = turtle.Turtle()
snake.shape('square')
snake.penup()

class Move():
    def __init__(self):
        self.dis = (0, 0)
    def up(self):
        snake.setheading(90)
        snake.forward(20)
        self.dis = snake.pos()
    def down(self):
        snake.setheading(270)
        snake.forward(20)
        self.dis = snake.pos()
    def left(self):
        snake.setheading(180)
        snake.forward(20)
        self.dis = snake.pos()
    def right(self):
        snake.setheading(0)
        snake.forward(20)
        self.dis = snake.pos()

food = turtle.Turtle()
food.shape('circle')
food.penup()
food.shapesize(0.5)
food.setpos(random.randrange(-200,200, step=20), random.randrange(-200,200, step=20))

move = Move()
turtle.listen()
turtle.onkey(move.up, 'Up')
turtle.onkey(move.down, 'Down')
turtle.onkey(move.left, 'Left')
turtle.onkey(move.right, 'Right')

while True:
    screen.update()
    print(move.dis, food.pos())
    if move.dis == food.pos():
        food.hideturtle()
        food.setpos(random.randrange(-200,200, step=20), random.randrange(-200,200, step=20))
        food.showturtle()
    elif move.dis == (300,300):
        break

turtle.done()