import turtle
import pandas
from writing import Writing

# creating the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# reading my csv data
data = pandas.read_csv("50_states.csv")

# Variable for series of states from the csv data
states = data["state"]

# list created to add string of state written from the input box
states_written = []

game_is_on = True
while game_is_on:
    # statement put "Guess the State" at the first title of the input box and start tracking the answer gotten when the user enters
    if len(states_written) == 0:
        good = "Guess the State"
    else:
        good = f"{len(states_written)}/50 States Correct"

    # Variable that stores the text input
    answer_state = screen.textinput(title=good, prompt="What's another state's name?").title()

    #so for each state in the states series from the csv  file, if the answer state input is equal to any of the state, cont....
    for state in states:
        if answer_state == state:

            #element is variable for that row(answer state) in the table
            element = data[data.state == answer_state]

            # so below sets the x and y variable to be equal to the int(x element and y element respectively)
            x = int(element.x)
            y = int(element.y)

            #then an object is created using these x & y with the answer state
            write_object = Writing(x, y, answer_state)

            #then answer state is appended to the state_written_list to track it
            states_written.append(answer_state)

    #if answer state is Exit(user enters exit), all state list is created and is it gotten from changing the state series to a list
    if answer_state == "Exit":
        all_state_list = data["state"].to_list()

        #missed list is created and all element in all state list not in state written, it is appended to the missed list
        missed_list = []
        for element in all_state_list:
            if element not in states_written:
                missed_list.append(element)

        #missed list dataframe is created
        missed_list_dataframe = pandas.DataFrame(missed_list)

        #missed_list_datafram is converts and creates a csv file
        missed_list_dataframe.to_csv("states_to_learn.csv")

        #game is off
        game_is_on = False


        #game also ends of all states are guessed by tracking when the length of state written becomes 50
        if len(states_written) == 50:
            game_is_on = False

turtle.exitonclick()
