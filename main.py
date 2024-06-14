from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveForwads():
  tim.forward(10)

def moveBackwards():
  tim.backward(10)

def turnLeft():
  new_heading = tim.heading() + 10
  tim.setheading(new_heading)

def turnRight():
  new_heading = tim.heading() - 10
  tim.setheading(new_heading)

def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()

screen.listen()
screen.onkey(key = "w", fun = moveForwads)
screen.onkey(key = "s", fun = moveBackwards)
screen.onkey(key = "a", fun = turnLeft)
screen.onkey(key = "d", fun = turnRight)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()