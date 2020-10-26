grades = []
for i in range(1, 11):
    score = int(input("請輸入第%d個分數: " % i))
    grades.append(score)

grades.sort() # 先排好(由小到大)，等等要剔掉最大最小值

max_score = grades.pop()   # 剔掉最大值(list裡面最後面的數字)
min_score = grades.pop(0)  # 剔掉最小值(list裡面最前面的數字)

total_score = sum(grades)  # 剩下的數字作加總
mean_score = total_score / len(grades)  # 剩下的數字取平均

print("總分 = " + str(total_score))
print("平均 = %.2f" % mean_score)



# 參考答案是直接不改變list的內容，用function來處理
# ----------------------------------------------------------------------

grades = []
for i in range(1, 11):
    score = int(input("請輸入第%d個分數: " % i))
    grades.append(score)

total_score = sum(grades) - max(grades) - min(grades)  # 直接扣掉不要的
mean_score = total_score / (len(grades)-2) # 砍掉兩個東西 所以長度 -2

print("總分 = " + str(total_score))
print("平均 = %.2f" % mean_score)