import turtle
import time
t = turtle.Turtle()
t.speed(100)
i = 0
while i < 10:
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.left(90)
  i += 1

time.sleep(5)
t.hideturtle()
t.clear()