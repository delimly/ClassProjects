class sphere(object):
    def __init__(self, radius):
        self.radius = radius
        
    def __str__(self):
        return 'A Sphere of radius {0}'.format(self.radius)
    
    def __repr__(self):
        return 'sphere({0})'.format(self.radius)
    
    def volume(self): 
        import numpy as np 
        return round((4/3) * np.pi * (self.radius ** 3) ,2)
    
    def area(self): 
        import numpy as np 
        return round(4 * np.pi * (self.radius ** 2), 2)
    
    def diameter(self): 
        return 2 * self.radius
    
a = sphere(3)
a
print(a)
a.volume()
a.area()
a.diameter()

a.radius
a.radius =4 
a.radius

a.volume()
a.area()
a.diameter()
