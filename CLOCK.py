import turtle
import time

turtle.mode('logo')
h = turtle.Turtle()
h.color('blue')
h.shape('arrow')
h.shapesize(1,10)

m = turtle.Turtle()
m.color('black')
m.shape('arrow')
m.shapesize(1,14)

s = turtle.Turtle()
s.color('red')
s.shape('arrow')
s.shapesize(1,15)

def showHands():
    t=time.localtime()
    s.seth(t.tm_sec*6)
    m.seth(t.tm_min*6)
    h.seth(t.tm_hour*30 + t.tm_min*0.5)
    turtle.ontimer(showHands,1000)
def makeFace():
    b=turtle.Turtle()
    b.speed(0)
    b.hideturtle()
    b.penup()

    b.dot(350)
    b.pencolor('white')
    b.dot(340)

    b.pencolor('black')
    for a in range(0,360,6):
        b.goto(0,0)
        b.seth(a)
        b.fd(160)
        b.dot(5)

    for a in range(0,360,30):
        b.goto(0,0)
        b.seth(a)
        b.fd(160)
        b.dot(10)
makeFace()
showHands()