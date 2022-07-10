from turtle import Screen
from pong import Pong
from pad import Pad
from score import ScoreBoard
from time import sleep


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)
# bet = screen.textinput(title="BET", prompt="Place your Bet:")
pong = Pong()
pad1 = Pad(1)
pad2 = Pad(-1)
screen.update()
# screen.tracer(1)
# pong direction range : (-36, 36)
screen.onkeypress(pad1.move_up, "Up")
screen.onkeypress(pad2.move_up, "w")
screen.onkeypress(pad1.move_down, "Down")
screen.onkeypress(pad2.move_down, "s")
screen.onkeypress(pong.start, "space")

score1 = ScoreBoard(1)
score2 = ScoreBoard(-1)

game_over = False


def end():
    global game_over
    game_over = True
    score2.clear()
    score1.clear()
    score1.home()
    pong.hideturtle()
    if score1.score > score2.score:
        score1.write("Game Over! Player 1 wins!", False, "center", ("Times New Roman", 20, "normal"))
    elif score1.score < score2.score:
        score1.write("Game Over! Player 2 wins!", False, "center", ("Times New Roman", 20, "normal"))
    else:
        score1.write("Game Over! Draw", False, "center", ("Times New Roman", 20, "normal"))


while not game_over:
    screen.onkey(end, "z")
    screen.update()
    sleep(0.0001)
    pong.move()
    pong_pos = pong.position()

    if abs(370 - pong_pos[0]) <= pong.motion:
        if abs(pad1.ycor() - pong_pos[1]) <= 50:
            pong.bounce_x()
        else:
            pong.reposition(1)
            score2.add()
    elif abs(-370 - pong_pos[0]) <= pong.motion:
        if abs(pad2.ycor() - pong_pos[1]) <= 50:
            pong.bounce_x()
        else:
            pong.reposition(0)
            score1.add()

    if abs(pong_pos[1] - 290) <= 1 or abs(pong_pos[1] + 290) <= 1:
        pong.bounce_y()

screen.exitonclick()
