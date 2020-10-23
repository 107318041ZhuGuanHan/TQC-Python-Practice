number = int(input("請輸入一正整數，我將為您算出它的階乘結果: "))

total = 1 # 給定一個不是0的初始值，賦值給total(因為等一下是乘法)

for n in range(1, number+1):
    total *= n # 從1開始一直乘到number -> 1 * 2 * 3 * ... * number

print(total)