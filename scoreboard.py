from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-275, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align='center', font=FONT)
