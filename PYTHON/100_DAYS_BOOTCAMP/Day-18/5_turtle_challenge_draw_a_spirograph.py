# CHALLENGE:
'''
STEPS:
1. Import CLASSES - Turtle, Screen from PACKAGE - 'turtle'
2. Create OBJECTS from CLASSES
3. Calling METHODS
4. Using LOOPS
'''

from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.color("Green")
tim.shape("turtle")
tim.speed("fastest")
screen = Screen()
screen.colormode(255)

for _ in range(200):
    # Circle
    tim.circle(120, 360)  # circle(radius, degrees)

    # Change Position
    current_heading = tim.heading()
    print(tim.heading)
    tim.setheading(current_heading + 2)

    # Change Color
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    tim.color(a, b, c)
    tim.pencolor(a, b, c)


screen.exitonclick()
