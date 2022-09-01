import turtle
import time
t=turtle.Turtle()

t.penup()
t.backward(500)
t.left(90)
t.forward(300)
t.pendown()
time.sleep(15)

t.pensize(3)
t.backward(650)
t.forward(630)
t.right(90)
t.begin_fill()
t.fillcolor('black')
t.circle(10)
t.end_fill()


t.begin_fill()
t.fillcolor('orange')  
t.forward(400)
t.right(90)
t.forward(88.888)
t.right(90)
t.forward(400)
t.right(90)
t.forward(88.888)
t.end_fill()

t.penup()
t.backward(88.888)
t.pendown()
t.right(90)
t.forward(400)
t.right(90)
t.forward(88.888)
t.right(90)
t.forward(400)
t.right(90)
t.forward(88.888)

t.penup()
t.backward(88.888)
t.pendown()
t.right(90)
t.begin_fill()
t.fillcolor('green')
t.forward(400)
t.right(90)
t.forward(88.888)
t.right(90)
t.forward(400)
t.right(90)
t.forward(88.888)
t.end_fill()


def spokes():
    for i in range(24):
        t.pencolor('blue')
        t.forward(40)
        t.backward(40)
        t.left(15)
    

    



t.penup()
t.forward(44.444)
t.right(90)
t.forward(200)
t.pendown()
spokes()
t.right(90)
t.forward(40)
t.left(90)
t.circle(40)

t.penup()
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(496.67)
t.pendown()

t.pencolor('black')
t.left(90)
t.forward(200)
t.right(90)
t.forward(30)
t.right(90)
t.forward(400)
t.right(90)
t.forward(30)
t.right(90)
t.forward(200)



t.left(90)
t.begin_fill()
t.fillcolor('black')
t.forward(630)
t.left(90)
t.forward(10)
t.left(90)
t.forward(630)
t.left(90)
t.forward(10)
t.end_fill()



t.penup()
t.goto(-10,50)
t.pendown()
t.pencolor('orange')
t.write('HAPPY',font=("Bradley Hand ITC",60,"bold"))

t.penup()
t.goto(40,-50)
t.pendown()
t.pencolor('blue')
t.write('INDEPENDENCE',font=("Bradley Hand ITC",60,"bold"))

t.penup()
t.goto(550,-150)
t.pendown()
t.pencolor('green')
t.write('DAY',font=("Bradley Hand ITC",60,"bold"))

t.penup()
t.goto(455.0,-319.0)
t.pendown()
t.pencolor('black')
t.write('#NSK',font=("Bradley Hand ITC",30,"italic"))





