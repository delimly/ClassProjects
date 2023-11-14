class rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self. width = width
        
    def calculate_area(self): 
        return self.length * self.width 
    
    def LWRatio(self): 
        return round(self.length / self.width, 2)
    
    def __str__(self):
        return 'The Rectangle of length {0} and width {1}'.format(self.length , self.width)
    def __repr__(self): 
        return 'rectangle({0},{1})'.format(self.length, self.width)

a = rectangle(3, 4)
a
print(a)
a.LWRatio()
a.calculate_area()


