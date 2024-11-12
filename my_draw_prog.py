from shelve import Shelf
from tkinter import*
root = Tk()

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

canvas.create_rectangle(100, 100, 300, 300) 
canvas.create_rectangle(200, 200, 400, 400)
canvas.create_line(100, 100, 200, 200)
canvas.create_line(300, 300, 400, 400)
canvas.create_line(100, 400, 200, 300)
canvas.create_line(200, 100, 200, 200)
canvas.create_polygon(10, 10, 100, 10, 100, 110, fill = 'blue')
canvas.create_text(200, 200, text = 'Hello world', fill = 'red', activefill = 'green', font = 'Arial 40')
from time import sleep

circle_1 = canvas.create_oval(10,10,50,50, fill='red')
circle_2 = canvas.create_oval(10,10,50,50)

for i in range(100):
    canvas.move(circle_1,1,1)
    root.update()
    sleep(0.05)
    
class Circle:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.size = 50
        self.speed_x = 3
        self.speed_y = 2
        self.canvas_size = 600
        self.object = canvas.create_oval (self.x, self.y, self.size, self.size, fill='red')

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()
    
    def check_collision(self):
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        if pos[1] <=0:
            self.speed_y *= -1
        if pos[2] >= self.canvas_size:
            self.speed_x *= -1
        if pos[3] >= self.canvas_size:
            self.speed_y *= -1
        
c1 = Circle()

while True:
    c1.move()
    root.update()
    sleep(0.005)    
    
root.mainloop()
