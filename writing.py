from turtle import Turtle
# A writing class to write on the map with x, y coordinates input and text input for state


class Writing(Turtle):
    def __init__(self, x, y, text):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x, y)
        self.write(text)


