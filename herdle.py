import turtle


scn = turtle.Screen()
mouthy = turtle.Turtle()
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
    eyey1.penup()
    eyey1.color("white")
    eyey1.goto(-600, 100)

def eye2():
    eyey2.penup()
    eyey2.goto(60, 100)
    eyey2.pendown()
    eyey2.begin_fill()
    eyey2.circle(10)
    eyey2.end_fill()
    eyey2.penup()
    eyey2.color("white")
    eyey2.goto(-600, 100)

def mouth():
    mouthy.penup()
    mouthy.goto(-60, 80)
    mouthy.pendown()
    mouthy.begin_fill()
    mouthy.forward(115)
    mouthy.right(90)
    for i in range(180):
        mouthy.right(1)
        mouthy.forward(1)
    mouthy.end_fill()
    mouthy.penup()
    mouthy.color("white")
    mouthy.goto(-600, 100)

face()
eye1()
eye2()
mouth()


turtle.exitonclick()