from math import pow, pi, tan

n = int(input("請輸入他是正幾邊形(邊數、邊的各數): "))
s = float(input("請輸入這個正n邊形的邊常: "))

area = (n * (s ** 2)) / (4 * tan(pi / n))

print("Area = %.4f" % area)