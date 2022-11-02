from turtle import *

width(3)
color("red")
speed(100)

def fracTree(size, levels, angle):
    if(levels == 0):
        return

    forward(size)
    left(angle)

    fracTree(size * 0.8, levels - 1, angle)

    right(angle*2)

    fracTree(size * 0.8, levels - 1, angle)

    left(angle)
    backward(size)

i = 0
while(i < 4):
    left(90)
    fracTree(90, 6, 20)
    i = i + 1

color("blue")
left(45)

i = 0
while(i < 4):
    left(90)
    fracTree(90, 6, 20)
    i = i + 1

mainloop()