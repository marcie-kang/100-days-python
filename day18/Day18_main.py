import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


direction = [0, 90, 180, 270]
tim.width(10)


for _ in range(100):
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(10)


screen = turtle.Screen()
screen.exitonclick()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("pink")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
