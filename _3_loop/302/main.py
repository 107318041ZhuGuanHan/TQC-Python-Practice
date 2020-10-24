print("將為您計算a~b之間所有偶數的總和")

number_a = int(input("請輸入一個正整數(最小值): "))
number_b = int(input("請輸入一個正整數(最大值): "))
number = 0 # 給定初始值

if number_a % 2 != 0: # 怕有人給我輸入奇數
    number_a = number_a + 1 # 變成在範圍內的最小偶數

if number_b % 2 != 0: # 怕有人給我輸入奇數
    number_b = number_b - 1 # 變成在範圍內的最大偶數

# 參考答案在這裡是直接在迴圈裡面判斷是不是2的倍數，是的話才進行加總

for n in range(number_a, number_b+1, 2):
    number += n

print(number)