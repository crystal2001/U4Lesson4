from turtle import *

dove = Turtle()

dove.color("green")
dove.pensize(5)
dove.speed(9)
dove.shape("turtle")

for x in range(4):
	dove.forward(200)
	dove.left(90)

mainloop()