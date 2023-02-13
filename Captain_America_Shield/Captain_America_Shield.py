import turtle
import math
t=turtle.Turtle()
t.speed(10)


t.penup()
t.goto(-3.0,-373.0)
t.pendown()
t.begin_fill()
t.fillcolor('crimson')
t.circle(375)
t.end_fill()

t.penup()
t.goto(-3.0,-278.0)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.circle(275)
t.end_fill()


t.penup()
t.goto(-3.0,-171.0)
t.pendown()
t.begin_fill()
t.fillcolor('crimson')
t.circle(175)
t.end_fill()

t.penup()
t.goto(-3.0,-73.0)
t.pendown()
t.begin_fill()
t.fillcolor('blue')
t.circle(75)
t.end_fill()


   
t.penup()
t.goto(-3.0,1.0)
t.pendown()
def paanch(r, color):
       t.speed(10)
       t.pencolor(color)
       t.setheading(162)
       t.forward(r)
       t.setheading(0)
       t.fillcolor(color)
       t.begin_fill()

       for i in range(5):
                t.forward(math.cos(math.radians(18)) * 2 * r) 
                t.right(144)
       t.end_fill()
paanch(74,'white')


t.penup()
t.goto(453.0,-267.0)
t.pendown()
t.pencolor('red')
t.write('#NSK',font=("Bradley Hand ITC", 30, "bold"))









