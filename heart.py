from turtle import *

#curve function
def curve(lines):
    while(lines > 0):
        left(10)
        forward(10)
        lines = lines - 1

#setup
width(6)
begin_fill()
color("red")
penup()
speed(2)
right(90)
forward(100)
pendown()

#firstline
left(150)
forward(200)

#curveLeft
curve(20)

#adjustment
right(170)

#curveLeft
curve(22)
right(6)

#forward
forward(190)

#fill with color red
end_fill()


#adjust
color("black")

#goto
penup()
goto(-250,-220)
setheading(270)
pendown()

#L
forward(100)
left(90)
forward(60)

#goto
penup()
forward(30)
pendown()

#O
forward(60)
left(90)
forward(100)
left(90)
forward(60)
left(90)
forward(100)

#goto
penup()
left(90)
forward(115)
pendown()

#V
left(70)
forward(110)
backward(110)
left(40)
forward(110)
backward(110)

#goto
setheading(0)
penup()
forward(65)
pendown()

#E
forward(60)
backward(60)
left(90)
forward(50)
right(90)
forward(60)
backward(60)
left(90)
forward(50)
right(90)
forward(60)
backward(60)
left(90)
backward(100)
right(90)

#goto 
penup()
forward(180)
pendown()

#U
left(90)
forward(100)
backward(100)
right(90)
forward(60)
left(90)
forward(100)

#hide cursor
hideturtle()

mainloop()