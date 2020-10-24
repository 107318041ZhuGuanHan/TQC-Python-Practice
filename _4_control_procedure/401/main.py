# 自己的寫法
number_1 = int(input("請輸入第1個整數: "))
number_2 = int(input("請輸入第2個整數: "))
number_3 = int(input("請輸入第3個整數: "))
number_4 = int(input("請輸入第4個整數: "))
number_5 = int(input("請輸入第5個整數: "))
number_6 = int(input("請輸入第6個整數: "))
number_7 = int(input("請輸入第7個整數: "))
number_8 = int(input("請輸入第8個整數: "))
number_9 = int(input("請輸入第9個整數: "))
number_10 = int(input("請輸入第10個整數: "))
# 這邊太多input -> 參考答案將input寫在迴圈裏面，就不會那麼麻煩

min_value = min(number_1, number_2, number_3, number_4, number_5,
                number_6, number_7, number_8, number_9, number_10)

print("您輸入的10個數字中，最小值為 " + str(min_value) + " 。")

# ----------------------------------------------------------------------
# 參考答案的寫法

numbers = []

for n in range(1, 11):
    number = int(input("請輸入第%d個整數: " % n))
    numbers.append(number) # ★建list來處理比較容易，但如果是要加總可能是設定變數來寫比較精簡

min_value = min(numbers)

print("您輸入的10個數字中，最小值為 " + str(min_value) + " 。")