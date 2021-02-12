from turtle import *
from random import randint

title('My Turtle Race')
bgcolor('black')
pencolor('white')

speed(10)
penup()
goto(-140, 140)

for step in range(16):
    write(step, align='center', )
    right(90)
    for num in range(12):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(240)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 105)
ada.pendown()
ada.right(360)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 75)
bob.pendown()
bob.left(360)

tim = Turtle()
tim.color('orange')
tim.shape('turtle')
tim.penup()
tim.goto(-160, 45)
tim.pendown()
tim.right(360)

sam = Turtle()
sam.color('yellow')
sam.shape('turtle')
sam.penup()
sam.goto(-160, 15)
sam.pendown()
sam.left(360)

tom = Turtle()
tom.color('purple')
tom.shape('turtle')
tom.penup()
tom.goto(-160, -15)
tom.pendown()
tom.right(360)

ben = Turtle()
ben.color('turquoise')
ben.shape('turtle')
ben.penup()
ben.goto(-160, -45)
ben.pendown()
ben.left(360)

joe = Turtle()
joe.color('magenta')
joe.shape('turtle')
joe.penup()
joe.goto(-160, -75)
joe.pendown()
joe.right(360)


for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    tim.forward(randint(1,5))
    sam.forward(randint(1,5))
    tom.forward(randint(1,5))
    ben.forward(randint(1,5))
    joe.forward(randint(1,5))