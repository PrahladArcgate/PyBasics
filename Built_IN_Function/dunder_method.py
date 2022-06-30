# This is a method you must have already used if you have worked with classes. 
# The init method is used to create an instance of the class.


class point:
    x = None
    y = None
    
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def __str__(self):
        s = f'({self.x},{self.y})'
        return s
    
    def __add__(self,p2):
        print("In add")
        x = self.x + p2.x
        y = self.y + p2.y
        return point(x,y)
    
    def __iadd__(self,p2):
        self.x += p2.x
        self.y += p2.y
        return self
    
    def __isub__(self,p2):
        self.x -= p2.x
        self.y -= p2.y
        return self
    
    def __imul__(self,p2):
        self.x *= p2.x
        self.y *= p2.y
        return self
    
    def __itruediv__(self,p2):
        self.x /= p2.x
        self.y /= p2.y
        return self
    
    def __ifloordiv__(self,p2):
        self.x //= p2.x
        self.y //= p2.y
        return self
    
    def __call__(self):
        print(f"Called Point {self.x},{self.y}")