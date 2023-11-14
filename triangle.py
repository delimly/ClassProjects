class triangle(object): 
    def __init__(self, base, height): 
        self.base = base
        self.height = height 

    def __str__(self):
        return 'A triangle of base length {0} and height length {1}'.format(self.base, self.height)
    
    def __repr__(self):
        return 'triange({0},{1})'.format(self.base, self.height)
    
    def calcArea(self):
        ans = (self.height * self.base)/2
        return round(ans,2)
    
    def calcSideA(self, gamma): 
        if not (0 < gamma < 180):
            return 'Cannot do this action'
        import numpy as np 
        gamma = (gamma/180)*np.pi 
        area = self.calcArea()
        calc = 2 * area * (1/(self.base * np.sin(gamma)))
        return calc 
    
    def calcSideC(self, perimeter, gamma):
        sideA = self.calcSideA(gamma)
        sideC = perimeter - sideA - self.base 
        return sideC
    
    def typeTriangle(self, perimeter, gamma): 
        a = self.calcSideA(gamma)
        c = self.calcSideC(perimeter, gamma)
        if (a == self.base == c):
            return 'Equilateral'
        elif (a == c) or (c == self.base) or (self.base == a):
            return 'Isoceles'
        else: 
            return 'Scalene'
        
a = triangle(3, 4)     
a
print(a)    
a.calcArea()
a.calcSideA(30)
a.calcSideC(15, 30)
a.typeTriangle(15, 30)
