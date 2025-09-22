import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

print(all_states)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        learn_states = [state for state in all_states if state not in guessed_states]
        final_state = pandas.DataFrame(learn_states)
        final_state.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# for state in guessed_states:
#     if state
# state_to_learn.

# if data[data["state"] == answer_state]:
#     state_data = data[data["state"] == answer_state]
#     x = int(state_data.iloc[0]["x"])
#     y = int(state_data.iloc[0]["y"])
#     answer_board.update_answer(answer_state, x, y)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
