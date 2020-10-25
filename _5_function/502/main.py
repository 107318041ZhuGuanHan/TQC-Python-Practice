def compute(x, y):
    return int(x * y) # 回傳兩數相乘 的數值


number_1 = int(input("請輸入第一個整數: "))
number_2 = int(input("請輸入第二個整數: "))

number_multiple = compute(number_1, number_2) # 將回傳值 賦值給 number_multiple

print("兩數相乘 = " + str(number_multiple))

