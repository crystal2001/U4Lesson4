from turtle import *

dove = Turtle()

dove.color("green")
dove.pensize(5)
dove.speed(9)
dove.shape("turtle")

for x in range(9):
	dove.forward(300)
	dove.left(60)

mainloop()