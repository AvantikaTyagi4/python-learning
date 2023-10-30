class Point:
    def draw(self):
        print("Draw")
    
    def move(self):
        print("Move")


# to create object
point1 = Point()
point1.draw() # to call class method


# to define class variable
point2 = Point()
point2.x = 10
point2.y = 20
print(point2.x)

# If we don't define variable of class's object and try to use it 
# we get error AttributeError: 'Point' object has no attribute 'x'
# point3 = Point()
# print(point3.x)
