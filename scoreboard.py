from turtle import Turtle
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.ht()
        self.pu()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGHSCORE:{self.highscore}", align= ALIGNMENT
                   , font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT
    #                , font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()


