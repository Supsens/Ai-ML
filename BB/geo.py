import math
class Rectangle:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y
    

class circle:
    r=0
    def __init__(self,r):
        self.r=r    
        
    def area(self):
        return math.pi*self.r*self.r