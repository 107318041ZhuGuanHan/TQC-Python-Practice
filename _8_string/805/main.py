# 跟101差不多，只是處理數字變成處理字串 (%d -> %s)
# 這一題很快

while True:
    string = input("請輸入一個長度為6的字串: ")

    if len(string) == 6: # 防止user輸入長度不是6的字串
        break

print("|%-10s|" % string)   # -10 ->佔10格，負數:靠左對其
print("|  %s  |" % string)  # 沒有置中的符號，只好自己來 -> ★參考答案用.center(10)
print("|%10s|" % string)    # 10 -> 佔10格，正數:靠右對其



string = input("請輸入一個長度為6的字串: ")
print("|%s|" % string.center(10))  # ★參考答案用.center(10)