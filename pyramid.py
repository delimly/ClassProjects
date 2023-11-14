class pyramid(object):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height 
    
    def __str__(self): 
        return 'A pyramid of length {0}, width {1}, and height {2}'.format(self.length, self.width , self.height)
    
    def __repr__(self): 
        return 'pyramid({0}, {1}, {2})'.format(self.length, self.width, self.height)
    
    def volume(self): 
        ans = (self.length * self.width * self.height)/3
        return round(ans, 2)
    
    def baseArea(self): 
        return self.length * self.width

    def lateralSurfaceArea(self): 
        l = self.length
        w = self.width
        h = self.height
        
        a = l*((w/2)**2 + h**2)**(0.5)
        b = w*((l/2)**2 + h**2)**(0.5)
        
        return round(a + b,2)
    
    def surfaceArea(self):
        return self.lateralSurfaceArea() + self.baseArea()
    
a = pyramid(3,4,5)
a
print(a)
a.volume() 
a.baseArea()
a.lateralSurfaceArea()
a.surfaceArea()
