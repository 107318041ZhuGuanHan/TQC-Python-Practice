# 思路:2個雙重for迴圈然後使用判斷，1個來建立3 * 3的list，1個抓最大值跟最小值的索引

numbers = []
for in_row in range(0, 3):
    numbers.append([]) # 建立空list給下面的for迴圈使用

    for in_column in range(0, 3):
        number_in = int(input("請輸入numbers[%d][%d]之中的元素(整數): "
                        % (in_row, in_column)))
        numbers[in_row].append(number_in)

row_max = 0
column_max = 0

row_min = 0
column_min = 0


max_item = max(max(row) for row in numbers)
# ★求出2維list的最大值 -> 不能直接用 max(numbers)因為會回傳一個list，裡面還不一定包含最大值

min_item = min(min(row) for row in numbers)
# ★求出2維list的最小值 -> 不能直接用 min(numbers)因為會回傳一個list，裡面還不一定包含最小值

for row in range(0, len(numbers)): # 用雙重迴圈

    for column in range(0, len(numbers[row])): # 來看numbers這個list

        if numbers[row][column] == max_item: # 遇到最大值
            row_max = row                       # 就把他的索引值存到變數裡面
            column_max = column

        elif numbers[row][column] == min_item: # 遇到最小值
            row_min = row                       # 也把他的索引值存到變數裡面
            column_min = column

print("Index of the largest number %d is: (%d, %d)"
      % (max_item, row_max, column_max))

print("Index of the smallest number %d is: (%d, %d)"
      % (min_item, row_min, column_min))

# ----------------------------------------------------------------------
# 參考答案直接用1D的list

numbers = []

for i in range(1, 10): # 一樣輸入9次，只是要顯示出來數字正常而已
    number_in = int(input("請輸入第%d個元素(整數): " % i))
    numbers.append(number_in)

max_value = max(numbers)
max_index = numbers.index(max_value) # ★要認識index這個function怎麼用!
print("Index of the largest number %d is: (%d, %d)"
      % (max_value, max_index // 3, max_index % 3))  # ★直接在這裡計算index數值(它偷吃步or我自己太老實)

min_value = min(numbers)
min_index = numbers.index(min_value) # ★要認識index這個function怎麼用!
print("Index of the smallest number %d is: (%d, %d)"
      % (min_value, min_index // 3, min_index % 3))

# ----------------------------------------------------------------------
# 試著在2d list裡面直接抓index
numbers = []
for in_row in range(0, 3):
    numbers.append([]) # 建立空list給下面的for迴圈使用

    for in_column in range(0, 3):
        number_in = int(input("請輸入numbers[%d][%d]之中的元素(整數): "
                        % (in_row, in_column)))
        numbers[in_row].append(number_in)

max_item = max(max(row) for row in numbers)
min_item = min(min(row) for row in numbers)

for row in numbers:
    if max_value in row:
        print(numbers.index(row)) # 印出max_value在第幾個row
        print(row.index(max_value)) # 印出max_value在第幾個column
        print("Index of the largest number %d is: (%d, %d)"
              % (max_value, numbers.index(row), row.index(max_value)))
        # index 使用格式: list_name.index(元素)
        # 不能直接numbers.index(max_value)
        # ★只要變成多維度list就會很難處理

print("") # 換行
for row in numbers:
    if min_value in row:
        print(numbers.index(row))
        print(row.index(min_value))
        print("Index of the smallest number %d is: (%d, %d)"
              % (min_value, numbers.index(row), row.index(min_value)))
        # 跟上面差不多，看上面註解





