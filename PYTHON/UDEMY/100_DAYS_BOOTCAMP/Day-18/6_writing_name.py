# CHALLENGE:


'''
STEPS:
1. Import CLASSES - Turtle, Screen from PACKAGE - 'turtle'
2. Create OBJECTS from CLASSES
3. Calling METHODS
4. Using Loops
'''

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
screen = Screen()
screen.colormode(255)
random_num = random.randint(0, 255)
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for _ in range(500):
    # Random Colour
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a, b, c)

    # M
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(-45)
    tim.forward(30)
    tim.setheading(45)
    tim.forward(30)
    tim.setheading(-90)
    tim.forward(30)

    # SPACE
    tim.setheading(0)
    tim.forward(30)
    # Random Colour
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a, b, c)

    # A
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(0)
    tim.forward(30)
    tim.setheading(-90)
    tim.forward(15)
    tim.setheading(180)
    tim.forward(30)
    tim.backward(30)
    tim.setheading(270)
    tim.forward(15)

    # SPACE
    tim.setheading(0)
    tim.forward(30)
    # Random Colour
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a, b, c)

    # N
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(-45)
    tim.forward(42.426)
    tim.setheading(90)
    tim.forward(30)
    tim.backward(30)

    # SPACE
    tim.setheading(0)
    tim.forward(30)
    # Random Colour
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a, b, c)

    # A
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(0)
    tim.forward(30)
    tim.setheading(-90)
    tim.forward(15)
    tim.setheading(180)
    tim.forward(30)
    tim.backward(30)
    tim.setheading(270)
    tim.forward(15)

    # SPACE
    tim.setheading(0)
    tim.forward(30)
    # Random Colour
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.pencolor(a, b, c)

    # R
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(0)
    tim.forward(30)
    tim.setheading(-90)
    tim.forward(15)
    tim.setheading(180)
    tim.forward(30)
    tim.setheading(330)
    tim.forward(30)

    # SPACE
    tim.setheading(0)
    tim.forward(30)

    # SPACE
    tim.setheading(0)
    tim.forward(30)






screen.exitonclick()
