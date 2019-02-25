from turtle import *

dove = Turtle()

dove.color("green")
dove.pensize(5)
dove.speed(9)
dove.shape("turtle")

for x in range(10):
	dove.forward(100)
	dove.left(36)

mainloop()