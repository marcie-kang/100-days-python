from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
X_POSITIONS = -230
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(X_POSITIONS, Y_POSITIONS[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost! The {winning_color} is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()