from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        with open("my_score.txt", 'r') as file:
            self.high_score = int(file.read())  # get highscore from previous playthrough

        self.score = 0
        self.hideturtle()
        self.color("white")
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"SCORE: {self.score} | HIGHSCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_score.txt", 'w') as file:
                file.write(str(self.high_score))  # write the new highscore to the file to save

        self.score = 0
        self.update_board()
