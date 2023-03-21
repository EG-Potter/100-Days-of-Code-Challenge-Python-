import turtle
import pandas

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Finds co-ordinates on click.
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


# Finds all states not guessed by user.
# def get_states(all_states, guessed_states):
#     to_learn = set(all_states) - set(guessed_states)
#     to_learn_result = list(to_learn)
#     to_learn_result = pandas.DataFrame(to_learn_result)
#     to_learn_result.to_csv("states_to_learn.csv")


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    # Exits game for user.
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        to_learn_result = pandas.DataFrame(missing_states)
        to_learn_result.to_csv("states_to_learn.csv")
        break
    # generates name of states onto the map.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        details = states[states.state == answer_state]
        t.goto(int(details.x), int(details.y))
        t.write(details.state.item())


# states_to_learn.csv

# turtle.mainloop()

