import math

class FiguraGeometrica:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        
    def area(self):
        return FiguraGeometrica(math.py * self.x * self.x)
        
area1 = FiguraGeometrica(1)
print(area1)
