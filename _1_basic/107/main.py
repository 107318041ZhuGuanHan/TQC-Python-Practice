number_1 = float(input("請輸入第一個數字: "))
number_2 = float(input("請輸入第二個數字: "))
number_3 = float(input("請輸入第三個數字: "))
number_4 = float(input("請輸入第四個數字: "))
number_5 = float(input("請輸入第五個數字: "))
# 使用者輸入


number_sum = number_1 + number_2 + number_3 + number_4 + number_5
number_avg = number_sum / 5.0
# 內部計算


print("%d %d %d %d %d" % (number_1, number_2, number_3
                          , number_4, number_5))
print("Sum = %.1f" % number_sum)
print("Average = %.1f" % number_avg)
# 顯示結果