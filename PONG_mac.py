#PONG#

import turtle
import os

window = turtle.Screen()
window.title("PONG")
window.bgcolor("skyblue")
window.setup(width=800, height=600)
window.tracer(0)

# Score

score_a = 0
score_b = 0



# Paddle A

paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.shape("square")
paddle_A.color("yellow")
paddle_A.penup()
paddle_A.goto(-370, 0)


# Paddle B

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.shape("square")
paddle_B.color("red")
paddle_B.penup()
paddle_B.goto(370, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.04
ball.dy = -0.04

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Times New Roman", 24, "normal"))






# FUNCTION

def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y) 

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)       

# keyboard
window.listen()
window.onkeypress(paddle_A_up, "w")
window.onkeypress(paddle_A_down, "s")
window.onkeypress(paddle_B_up, "Up")
window.onkeypress(paddle_B_down, "Down")





#main loop"

while True:
    window.update()

    # Move the Ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay tik1.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay tik2.wav&")    

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1 
        os.system("afplay do1.wav&")       
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        os.system("afplay do2.wav&")       
        score_b += 1  
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))
 

    #paddle collision
    
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() -50):  
        ball.setx(360)
        ball.dx *= -1
        os.system("afplay ping1.wav&")    


    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() -50):  
        ball.setx(-360)
        ball.dx *= -1
        os.system("afplay ping2.wav&")    

        


