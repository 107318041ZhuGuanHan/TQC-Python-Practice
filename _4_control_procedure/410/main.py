# 思路:
# 1.%s總共要占幾格欄位，跟左半邊靠右、右半邊靠左的方式 -> 不行 因為欄位都是未定
# 2.字串拼接的方式 -> 可行
# 3.迴圈裏面還有迴圈(參考答案) -> 也可以

# ----------------------------------------------------------------------
# 思路3
height = int(input("請輸入等腰三角形的高度: "))
weight = 2 * height - 1
# 最後一層的寬度 = 2 * height - 1
# 左半邊靠右對齊，占height格欄位
# 右半邊靠左對齊，占height - 1格欄位

dot = "*"
space = " "

for h in range(1, height+1): # 直的下去的
    for s in range(1, height - h + 1):
        print("%s" % space, end="")

    for d in range(1, 2 * h - 1 + 1):
        print("%s" % dot, end="")
    print("")

# ----------------------------------------------------------------------
#思路2 ★ 自己想的

height = int(input("請輸入等腰三角形的高度: "))
weight = 2 * height - 1
# 最後一層的寬度 = 2 * height - 1
# 左半邊靠右對齊，占height格欄位
# 右半邊靠左對齊，占height - 1格欄位

dot = "*"
space = " "

for h in range(1, height+1): # 直的下去的
    string = (height - h) * space + dot * (2 * h - 1) # 直接在字串這邊開刀 -> 跟上面比起來較不容易出錯，因為上面有index需要+1
    print(string)

# ----------------------------------------------------------------------
# 思路2畫菱形

height = int(input("請輸入等腰三角形的高度: "))
weight = 2 * height - 1
# 最後一層的寬度 = 2 * height - 1
# 左半邊靠右對齊，占height格欄位
# 右半邊靠左對齊，占height - 1格欄位

dot = "*"
space = " "

for h in range(1, height+1): # 直的下去的
    string = (height - h) * space + dot * (2 * h - 1) # 直接在字串這邊開刀
    print(string)

for h in range(1, height):
    string = h * space + dot * (2 * height - 1 - 2 * h)
    print(string)