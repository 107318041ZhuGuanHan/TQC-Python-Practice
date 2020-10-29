def compute(a, b, c):
    discriminant = (b ** 2) - 4 * (a * c)  # 判別式 = b平方 - 4ac

    if discriminant > 0:

        root_1 = (-b + (discriminant ** 0.5)) / (2 * a)
        root_2 = (-b - (discriminant ** 0.5)) / (2 * a)
        print("2個相異實根: ")
        print("%.1f, %.1f" % (root_1, root_2))

    elif discriminant == 0:
        root = (-b) / (2 * a)
        print("重根: ")
        print("%.1f" % root)

    elif discriminant < 0:
        print("Your equation has no root(無解)")


print("方程式: a * x^2 + b * x + c = 0")
a = int(input("請輸入方程式中a的數值(整數): "))
b = int(input("請輸入方程式中b的數值(整數): "))
c = int(input("請輸入方程式中c的數值(整數): "))

compute(a=a, b=b, c=c)
