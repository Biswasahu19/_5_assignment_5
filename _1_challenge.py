class Point:
    def __init__(self, x ,y, z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        return(self.x*self.x) + (self.y*self.y) + (self.z*self.z)

sq_object = Point(5, 8, 9)
print(sq_object.sqSum())