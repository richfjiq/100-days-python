import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_on = True

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 Guess the State",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state in guessed_states:
                pass
            else:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # t.goto(int(state_data.iloc[0, 1]), int(state_data.iloc[0, 2]))
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        # t.write(state_data.iloc[0, 0])
        # t.write(state_data.state.item())
        t.write(answer_state)
