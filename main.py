import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup()

score = 0
list_states_answered = []
list_state_not_answered = []

while len(list_states_answered) < 50:
    answer_state = screen.textinput(title=f"{len(list_states_answered)}/50: Guess the State", prompt="What state do you know ?").title()
    states = pandas.read_csv("50_states.csv")
    states_frame = states.state.to_list()
    if answer_state == "Exit":
        list_state_not_answered = [state for state in states_frame if state not in list_states_answered]
        states_not_answered_dic = {
            "states to review": list_state_not_answered
        }
        states_to_review = pandas.DataFrame(states_not_answered_dic)
        states_to_review.to_csv("states_to_review.csv")
        break

    if answer_state in states_frame:
            state_attributes = states[states.state == answer_state]
            state_matched_x = int(state_attributes.x)
            state_matched_y = int(state_attributes.y)

            cursor_state = turtle.Turtle()
            cursor_state.hideturtle()
            cursor_state.penup()
            cursor_state.goto(state_matched_x, state_matched_y)
            cursor_state.write(f"{answer_state}", font=("Arial", 8, "normal"))

            score += 1

            list_states_answered.append(answer_state)

