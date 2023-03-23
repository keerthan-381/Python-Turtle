import turtle
t=turtle.Turtle()

t.penup()
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.pendown()
t.pensize(3)
t.pencolor('blue')
t.begin_fill()
t.fillcolor('blue')
t.circle(100)
t.end_fill()

t.penup()
t.back(200)
t.left(90)
t.forward(115)
t.right(90)
t.forward(30)
t.pendown()
t.pencolor('red')
t.begin_fill()
t.fillcolor('red')
t.circle(40)
t.end_fill()

t.left(90)
t.penup()
t.forward(110)
t.pendown()
t.left(90)
t.pencolor('gold')
t.fillcolor('gold')
t.begin_fill()
t.circle(-60)
t.end_fill()

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.forward(75)
t.pendown()
t.pencolor('green')
t.fillcolor('green')
t.begin_fill()
t.circle(-20)
t.end_fill()

t.penup()
t.forward(350)
t.right(90)
t.pendown()
t.pencolor('blue')
t.fillcolor('blue')
t.begin_fill()
t.forward(70)
t.circle(20,180)
t.forward(70)
t.circle(20,180)
t.end_fill()

t.forward(70)
t.penup()
t.right(90)
t.forward(30)
t.left(90)
t.pendown()
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.circle(50,180)
t.right(90)
t.forward(15)
t.right(90)
t.circle(-65,180)
t.right(90)
t.forward(15)
t.end_fill()

t.pencolor('yellow')
t.fillcolor('yellow')
t.right(90)
t.begin_fill()
t.circle(50,50)
t.right(90)
t.forward(15)
t.right(90)
t.circle(-75,45)
t.right(90)
t.forward(15)
t.end_fill()

t.penup()
t.right(90)
t.circle(50,85)
t.right(85)
t.forward(70)
t.left(90)
t.pendown()
t.pencolor('green')
t.fillcolor('green')
t.begin_fill()
t.forward(10)
t.left(90)
t.right(5)
t.forward(45)
t.left(90)
t.forward(20)
t.left(90)
t.forward(45)
t.left(90)
t.forward(10)
t.end_fill()

t.penup()
t.backward(1200)
t.left(90)
t.forward(50)
t.pendown()


def rectangle(l,color):
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.forward(l)
    t.circle(-20,180)
    t.forward(l)
    t.circle(-20,180)
    t.end_fill()
    t.right(90)
    t.penup()
    t.forward(80)
    t.left(90)
    

rectangle(100,'blue')
t.penup()
t.backward(35)
t.pendown()
rectangle(170,'red')
t.penup()
t.forward(30)
t.pendown()
rectangle(100,'yellow')
t.penup()
t.backward(20)
t.pendown()
rectangle(140,'green')

t.penup()
t.backward(300)
t.right(90)
t.forward(900)

t.pendown()
t.pencolor('black')
t.write('#NSK',font=("Bradley Hand ITC",'20',"bold"))








