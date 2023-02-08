import turtle
import time

t = turtle.Turtle()
turtle.bgcolor('black')
time.sleep(2)

t.pencolor('white')
t.penup()
t.right(90)
t.forward(300)
t.pendown()
t.pensize(5)
t.left(90)
t.fillcolor('red')
t.begin_fill()
t.circle(300)
t.end_fill()

t.penup()
t.left(90)
t.forward(50)
t.right(90)
t.pendown()
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.circle(250)
t.end_fill()

t.penup()
t.left(90)
t.pencolor('white')
t.forward(100)
t.pendown()
t.right(90)
t.forward(50)
t.fillcolor('red')
t.begin_fill()
t.backward(100)

t.right(180)
t.left(70)
t.forward(220)

t.right(70)
t.forward(100)
t.right(110)
t.forward(750)

t.right(70)
t.forward(125)
t.right(90)
t.forward(540)
t.right(90)
t.forward(105)
t.right(90)
t.forward(42)
t.end_fill()

t.left(90)
t.forward(100)

t.right(110)
t.penup()
t.forward(100)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.forward(192)
t.right(160)
t.forward(180)
t.right(90)
t.forward(65)
t.end_fill()

t.penup()
t.right(180)
t.forward(60)
t.right(90)
t.forward(140)

t.left(135)
t.pendown()
t.pencolor('black')
t.pensize(20)
t.forward(150)
t.left(90)
t.forward(150)

t.penup()
t.goto(530.0,-316.0)
t.pendown()
t.pencolor('white')
t.write('#NSK',font=("Bradley Hand ITC",'30',"italic"))











