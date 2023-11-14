class circle(object): 
    def __init__(self, radius):
        self.radius = radius
        
    def __str__(self):
        return 'A circle of radius {0}'.format(self.radius)
    
    def __repr__(self): 
        return 'circle({0})'.format(self.radius)
        
    def area(self): 
        import numpy as np
        return round(np.pi * self.radius**2, 2)
    
    def circumfrence(self):
        import numpy as np 
        return round(2 * np.pi * self.radius, 2)
    
    def diameter(self):
        return 2 * self.radius
    
    def arcLength(self, degrees): 
        import numpy as np 
        radians = degrees/180 * (np.pi)
        return round(self.radius * radians , 2) 
    
    def pieArea(self, degrees): 
        tArea = self.area()
        return round((degrees/360)*tArea , 2)
       
a = circle(5)
a
print(a)
a.area()
a.circumfrence()
a.diameter()
a.arcLength(30)
a.pieArea(30)

a.radius = 6
print(a.radius)
