numbers = []

message = "請輸入整數: "
message += "\n(輸入'-9999'以離開程序)"

while True: # 參考答案用條件式來退出
    number = int(input(message))

    if number == -9999:
        break

    numbers.append(number)

numbers = tuple(numbers) # 直接用沒有副作用的function將list暫時轉換成tuple
# 暫時轉換完成後賦值給自己 -> 變成真正的轉換(有副作用)
# 參考答案是直接用另外一個變數來接這個tuple

print(numbers)
print("Length: " + str(len(numbers)))
print("Max: " + str(max(numbers)))
print("Min: " + str(min(numbers)))
print("Sum: " + str(sum(numbers)))