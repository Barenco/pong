import turtle
import os
import time


# Set players name
while True:
    player_a = input('Player one name: ')
    player_b = input('Player two name: ')

    if len(player_a) < 15 and len(player_b) < 15:
        break

    print("Names must have less than 15 charactheres")

# Load screen
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4.5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4.5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.06
ball.dy = -0.06


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{player_a}: {score_a}  {player_b}: {score_b}", align="center", font=("Courier", 24, "normal"))


# Movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y > 240:
        return
    y += 20    
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y < -240:
        return
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y > 240:
        return
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y < -240:
        return
    y -= 20
    paddle_b.sety(y)


# Keybord binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")


    if ball.xcor() > 410:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f"{player_a}: {score_a}  {player_b}: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.dx = 0.08
        ball.dy = -0.08
        time.sleep(0.5)
    
    if ball.xcor() < -410:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write(f"{player_a}: {score_a}  {player_b}: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.dx = 0.08
        ball.dy = -0.08
        time.sleep(0.5)


    # Paddle and ball collisions
    if (ball.xcor() > 335 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(335)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

        if ball.dx > 0:
            ball.dx += 0.005
        else:
            ball.dx -= 0.005

        if ball.dy > 0:
            ball.dy += 0.005
        else:
            ball.dy -= 0.005

    if (ball.xcor() < -335 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-335)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

        if ball.dx > 0:
            ball.dx += 0.005
        else:
            ball.dx -= 0.005

        if ball.dy > 0:
            ball.dy += 0.005
        else:
            ball.dy -= 0.005
