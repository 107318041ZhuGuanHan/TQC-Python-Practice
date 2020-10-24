length_1 = float(input("請輸入三角形的第一個邊長: "))
length_2 = float(input("請輸入三角形的第二個邊長: "))
length_3 = float(input("請輸入三角形的第三個邊長: "))

state_3 = length_1 + length_2 > length_3
state_2 = length_1 + length_3 > length_2
state_1 = length_2 + length_3 > length_1
# 儲存3個判斷解果(布林代數)

if state_1 and state_2 and state_3: # 在這裡把上面3個布林變數拿來用的話至少不會像參考答案那麼冗長
    perimeter = length_1 + length_2 + length_3
    print("Perimeter = " + str(perimeter))

else:
    print("Invalid")

