print("將為您計算a連加到b的總和")
number_1 = int(input("請輸入一個正整數(最小值): "))
number_2 = int(input("請輸入一個正整數(最大值): "))
# 輸入假設user很乖會按照我的指示去輸入

number = 0 # 宣告、設定初始值(把0賦值給number)

for n in range(number_1, number_2 + 1): # n從number_1開始，到number_2結束
    number += n


print(number)
