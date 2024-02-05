class Shape:
    def Area(self, area = 0):
        print(f"The area of the shape: {area}")

class Square(Shape):

    def __init__(self, length):
        self.length = length
        super().__init__()
        self.squares_area = self.length  ** 2    

fig = Square(int(input("Square length: ")))

fig.Area(fig.squares_area)

