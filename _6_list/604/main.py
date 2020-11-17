numbers = []
for i in range(1, 11):
    number_in = int(input("請輸入第%d個數字: " % i))
    numbers.append(number_in)

number_counts = {} # 用字典來建立key: value 對
for n in numbers:
    count = numbers.count(n) # ★用.count()來計算特定元素在列表中出現的次數
    number_counts[n] = count #  把元素跟次數 整理成 元素:次數

for key, value in number_counts.items():

    if value == max(number_counts.values()): # 在這邊先不考慮沒有眾數或是多個眾數的問題
        print("眾數 = " + str(key))
        print(str(key) + " 出現 " + str(value) + " 次。")

# 參考答案是直接用變數來接
# ----------------------------------------------------------------------
numbers = []
for i in range(1, 11):
    number_in = int(input("請輸入第%d個數字" % i))
    numbers.append(number_in)


max_count = 0 # 用來儲存眾數的數量
much_number = 0 # 給定初始值，不給的話其實也沒關係，只是下面會有橘色的線
for number in numbers:

    if max_count < numbers.count(number): # 判斷每個元素的數量是否大於目前的眾數數量
        max_count = numbers.count(number) # ★更新現在眾數的數量(只要此變數看到更大的數就會一直更新到跟他看到的數字一樣)
        much_number = number # 更新眾數
        # 有些時候不能用變數來儲存，這邊可以是因為index的數值都 >= 0(初始值)
        # 遇到要儲存任意數的list就很容易讓初始值變成不是最大或最小值了


print("眾數 = " + str(much_number))
print(str(much_number) + " 出現 " + str(max_count) + " 次。")