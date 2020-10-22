x1 = float(input("請輸入第一個點的x座標: "))
y1 = float(input("請輸入第一個點的y座標: "))
x2 = float(input("請輸入第二個點的x座標: "))
y2 = float(input("請輸入第二個點的y座標: "))

distance = (((x1-x2) ** 2) + ((y1-y2) ** 2)) ** 0.5

print("第一個點： (%.f, %.f)" % (x1, y1))
print("第二個點： (%.1f, %.f)" % (x2, y2)) # 為了要跟題目有相同的輸出
print("Distance = %.4f" % distance) # 這邊輸出沒有疑慮