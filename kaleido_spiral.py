import turtle as t

from itertools import cycle
colors = cycle(['gold','red','green','yellow','blue','maroon','silver'])

def draw_circle(size):
    t.pencolor(next(colors))
    t.circle(size)
    draw_circle(size+5)

t.bgcolor('black')
t.speed('fast')
t.pensize(5)
draw_circle(30)
