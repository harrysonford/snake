from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Roboto", 20, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Очки: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("ВСЁ, ДО СВИДАНИЯ", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()