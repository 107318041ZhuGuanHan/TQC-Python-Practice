def compute(a, b, c):
    y = (b**2) - (4 * a * c)

    if y > 0:
        x1, x2 = (-b + (y ** 0.5)) / (2 * a), (-b - (y ** 0.5)) / (2 * a)
        # 可以一口氣賦值給兩個變數
        return x1, x2

    else:
        return 'Your equation has no root', None


a = eval(input())
b = eval(input())
c = eval(input())
m, n = compute(a, b, c)

if n == None:
    print(m)
else:
    print('{}, {}'.format(m, n))