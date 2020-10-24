# 思路:用while迴圈，遇到9999就break，每次輸入就存數字進去list變成一個元素
# 參考答案跟我的思路一模模一樣樣

numbers = [] # 宣告list

while True:
    number = int(input("請輸入數字(輸入9999即退出程序計算最小值): "))
    numbers.append(number)

    if number == 9999: # 判斷是否退出迴圈去計算最小值
        break

min_value = min(numbers)
print("在您輸入的所有數字中，最小值為 " + str(min_value))
