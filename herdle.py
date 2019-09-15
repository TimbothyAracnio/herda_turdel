import turtle


scn = turtle.Screen()
glassy = turtle.Turtle()
eyey1 = turtle.Turtle()
eyey2 = turtle.Turtle()
facey = turtle.Turtle()

def face():
    facey.color("yellow")
    facey.begin_fill()
    facey.circle(80)
    facey.end_fill()


def eye1():
    eyey1.penup()
    eyey1.goto(-60, 100)
    eyey1.pendown()
    eyey1.begin_fill()
    eyey1.circle(10)
    eyey1.end_fill()

def eye2():
    eyey2.penup()
    eyey2.goto(60, 100)
    eyey2.pendown()
    eyey2.begin_fill()
    eyey2.circle(10)
    eyey2.end_fill()

face()
eye1()
eye2()


turtle.exitonclick()