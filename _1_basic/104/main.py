import math
radius = float(input("請輸入圓形的半徑: "))

pi = math.pi

perimeter = 2 * pi * radius

area = pi * radius ** 2

print("Radius = %.2f" % radius)
print("Perimeter = %.2f" % perimeter)
print("Area = %.2f" % area)
