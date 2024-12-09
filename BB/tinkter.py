from tkinter import *
def draw_rectangle(x,y,color):
    root=Tk()
    canvas=Canvas(root,width=300,height=300,bg="black")
    canvas.pack()
    canvas.create_rectangle(x,y,x+100,y+100,fill=color)
    root.mainloop()


def draw_point(x,y):
    root=Tk()
    canvas=Canvas(root,width=300,height=300)
    canvas.pack()
    canvas.create_oval(x,y,x,y,fill="black")
    root.mainloop()
    


class Cirle:
    def __init__(self,x,y,r,color):
        self.x=x
        self.y=y
        self.r=r
        self.color=color
    def draw_circle(self):
        root=Tk()
        canvas=Canvas(root,width=300,height=300,bg="black")
        canvas.pack()
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
        root.mainloop()

circle1=Cirle(100,100,50,"red")
circle1.draw_circle()

