class cuboid(object): 
    def __init__(self, length, width, height):
        self.length = length
        self.width = width 
        self.height = height 
        
    def __str__(self): 
        return 'A cuboid of length {0}, width {1} and height {2}'.format(self.length, self.width, self.height)
    
    def __repr__(self):
        return 'cuboid({0},{1},{2})'.format(self.length, self.width, self.height)
    
    def calcVol(self): 
        return self.length * self.width * self.height
    
    def calcSurfaceArea(self):
        total = 2 * self.length * self.width
        total = total + 2 * self.length * self.height
        total = total + 2 * self.width * self.height
        return total
        
    def volToSufRatio(self): 
        vol = self.calcVol()
        suf = self.calcSurfaceArea()
        return round(vol/suf, 2)
    
    def isCube(self): 
        return (self.length == self.width == self.height)
        
        
# A Cube 
a = cuboid(3, 3, 3)
a
print(a)
a.calcSurfaceArea()
a.calcVol()
a.volToSufRatio()
a.isCube()

# A Cuboid
b = cuboid(3, 4, 5)
b
print(b)
b.calcSurfaceArea()
b.calcVol()
b.volToSufRatio()
b.isCube()
