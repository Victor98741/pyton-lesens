import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

class DrawShape:
    def draw(self, color = 'red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()       

class Rect(DrawShape):
    def __init__(self, size, fill = False) :
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill = fill
        
        
rect = Rect(80, fill = True)
rect.draw()
t.goto(0, 80)
rect.draw('yellow')
t.goto(0, 160)
rect.draw('green')
# t.left(70)
# for i in range(45):
#  t.forward(150)
#  t.right(170)

screen.mainloop()
