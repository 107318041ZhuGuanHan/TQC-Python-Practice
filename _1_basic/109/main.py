from math import pow, tan, pi

s = float(input("請輸入正五邊形的邊長: "))

area = (5 * (s ** 2)) / (4 * tan(pi / 5))

print("Area = %.4f" % area)