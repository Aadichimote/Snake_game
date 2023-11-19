from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
OVER = ("Courier", 18, "normal")
# create a score board
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
# read csv data to operate as a high score
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            # If the file does not exist, create it and set the default high score
            with open("data.txt", "w") as file:
                file.write("0")
            self.high_score = 0  # Set the high score to 0
#properrties of score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
#update scoreboard after collision
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}           HIGH SCORE : {self.high_score}", align=ALIGNMENT, font=FONT)
#reset the score 
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=OVER)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
