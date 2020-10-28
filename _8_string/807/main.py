# 先把字串切成都是數字字串的list，再用迴圈一個一個轉換成整數加總存到一個變數 -> 跟參考答案相同

numbers_list = input("請輸入五個數字，以空白隔開: ").split(' ')

total = 0

for number in numbers_list:
    total += int(number)

avg = total / len(numbers_list)

print("Total = " + str(total))
print("Average = " + str(avg))


# ----------------------------------------------------------------------
# 不需要建立變數來儲存，直接用迴圈把字串list轉換成整數list

numbers_list = input("請輸入五個數字，以空白隔開: ").split(' ')

for i in range(0, len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])  # 把每個字串元素轉換成整數元素

total = sum(numbers_list)
avg = total / len(numbers_list)

print("Total = " + str(total))
print("Average = " + str(avg))