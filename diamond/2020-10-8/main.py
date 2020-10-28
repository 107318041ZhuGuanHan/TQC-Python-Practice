# 這邊是用上半三角形 + 下半三角形 合成菱形
height = int(input("請輸入等腰三角形的高: "))
weight = 2 * height - 1

dot = '*'

for i in range(1, height + 1):
    message = (2 * i - 1) * dot
    print("%s" % message.center(weight))

for i in range(1, height):
    message = (weight - (2 * i)) * dot
    print("%s" % message.center(weight))

# ---------------------------------------------------------------------
height = int(input("請輸入菱形的高: "))  # ★

height_up_tri = (height // 2) + 1  # ★
height_low_tri = height // 2  # ★

weight = int(input("輸入菱形的寬: "))  # ★

weight_up_tri = weight  # ★
weight_low_tri = weight - ((weight_up_tri - 1) // (height_up_tri - 1))  # ★

adding_rate = (weight_up_tri - 1) // (height_up_tri - 1)  # ★

dot = '*'

for i in range(1, weight_up_tri + 1, adding_rate):  # ★

    message = i * dot
    print("%s" % message.center(weight))

for i in range(adding_rate, weight_low_tri + adding_rate, adding_rate):  # ★
    # 這邊的範圍比較難

    message = abs(weight - i) * dot
    print("%s" % message.center(weight))


# 上面的是用寬來做
# ------------------------------------------------------------------------------
# 下面的是用高來做
for i in range(1, height_up_tri+1):
    message = abs(adding_rate * i - 1) * dot
    print("%s" % message.center(weight))

for i in range(1, height_low_tri+1):
    message = abs(weight - adding_rate * i) * dot
    print("%s" % message.center(weight))
