import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(725, 491)


guessed_states = []

data = pandas.read_csv("50_states.csv")
states_list = data['state'].tolist()

while len(guessed_states) < 50:
    answer = (screen.textinput(f"Guess a state {len(guessed_states)}/50", "What's another state name ?")).title()

    if answer in guessed_states:
        continue

    if answer == "Exit":
        break

    if answer in states_list:
        guessed_states.append(answer)
        row = data[data.state == answer]
        s = turtle.Turtle()
        s.penup()
        s.hideturtle()
        s.goto(int(row.x), int(row.y))
        s.write(answer)

missed_states = [p for p in states_list if p not in guessed_states]

print(missed_states)

data2 = pandas.DataFrame(missed_states)
data2.to_csv("missed states")










