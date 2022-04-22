import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Enter a color: ")
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for each in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[each])
    new_turtle.penup()
    new_turtle.goto(-225, y_positions[each])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 200:
            is_race_on = False
            winner = turtle.pencolor()
            print(f"The winner is {winner}!")
            if winner == user_bet:
                print("You win!")
            else:
                print("You lose.")


# if turtle.xcor() == 200 and turtle.color() == user_bet:
#     print("You win!")
# else:
#     print("You lose.")


screen.exitonclick()





