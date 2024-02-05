from c2_task import Shape

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def Rectangle_area(self):
        self.Rectangle_area = self.l * self.w


rec = Rectangle(int(input("Rectandle length: ")), int(input("Rectangle width: ")))

rec.Rectangle_area()

rec.Area(rec.Rectangle_area)