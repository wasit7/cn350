class Rectangle(object):
    def __init__ (self, w=0, h=0):
        self.w=w
        self.h=h
        
    def get_area(self):
        return self.w*self.h
    
    def __str__(self):
        return("width:{}, height:{}, area:{}".format(self.w, self.h, self.get_area() ))

class Square(Rectangle):
    def __init__(self, edge):
        self.w=edge
        self.h=edge
        