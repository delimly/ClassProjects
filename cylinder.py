class cylinder(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height 
        
    def __str__(self):
        return 'A Cylinder of radius {0} and height {1}'.format(self.radius , self.height)
    
    def __repr__(self):
        return 'cylinder({0},{1})'.format(self.radius, self.height)
    
    def volume(self):
        import numpy as np 
        return  round(np.pi * (self.radius)**2 * self.height, 2)
    
    def lateralSurfaceArea(self):
        import numpy as np
        return round(2 * np.pi * self.radius * self.height, 2)
    
    def baseArea(self):
        import numpy as np 
        return round(np.pi * (self.radius)**2, 2) 
    
    def surfaceArea(self): 
        return self.lateralSurfaceArea() + 2 * self.baseArea()
    
    
a = cylinder(3, 4)
a
print(a)
a.volume()
a.lateralSurfaceArea()
a.baseArea()
a.surfaceArea()
