from turtle import *

dove = Turtle()
clove = Turtle()

dove.color("red")
dove.pensize(5)
dove.speed(9)
dove.shape("turtle")

clove.color("green")
clove.pensize(5)
clove.speed(9)
clove.shape("turtle")

for x in range(3):
	dove.forward(300)
	dove.left(120)

clove.circle(100)

mainloop()