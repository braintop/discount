class Point:
    #phase 1 - constructor
    def __init__(self,x, y):
        self.x = x 
        self.y = y
    
    def move_by_x_and_y(self, dx, dy):
        self.x = self.x +  dx
        self.y = self.y + dy
    

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1.x)
p1.move_by_x_and_y(3, 4)
print(p1.x)
print(p1.y)
if p1.x > p2.x:
    print("p1 is greater than p2")
else:
    print("p2 is greater than p1")