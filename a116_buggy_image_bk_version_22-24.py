#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
painter.pensize(8)
painter.left(90)
painter.forward(20)
painter.right(40)
painter.forward(100)
painter.right(180)
painter.forward(100)
painter.right(210)
painter.forward(100)
painter.right(180)
painter.forward(100)
painter.right(220)
painter.forward(100)
painter.right(180)
painter.forward(100)
painter.right(210)
painter.forward(100)
painter.right(180)
painter.forward(200)
painter.right(180)
painter.forward(100)
painter.right(150)
painter.forward(100)
painter.right(180)
painter.forward(100)
painter.right(140)
painter.forward(100)
painter.right(180)
painter.forward(100)
painter.right(150)
painter.forward(100)
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
