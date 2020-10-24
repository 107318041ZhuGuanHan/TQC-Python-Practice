x = float(input("請輸入一個點的x座標: "))
y = float(input("請輸入一個點的y座標: "))

distance = (((x - 5) ** 2) + ((y - 6) ** 2)) ** 0.5 # 這邊計算距離，參考答案直接call function
print("Distance from (5, 6) to (%f, %f) is %f" % (x, y, distance))

if distance <= 15:
    print("Inside")

elif distance > 15:
    print("Outside")