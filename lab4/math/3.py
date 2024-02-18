import math
print("Num of sides: ")
n = int(input())
print("Length of side: ")
a = float(input())
area = (n / 4) * a * a * (1 / math.tan(math.pi / n))
ap_area = int(area) 
print("The area of the polygon is:", ap_area)
