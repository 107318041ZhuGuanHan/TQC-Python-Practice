temperatures = [[0 for day in range(0, 3)] for week in range(0, 4)]

temperatures_total = 0

for week in range(0, 4):
    print("Week %d: " % (week+1))

    for day in range(0, 3):

        temperatures[week][day] = float(input("Day %d: " % (day+1)))
        temperatures_total += temperatures[week][day]


temperature_avg = temperatures_total / 12
max_temperature = max(max(day) for day in temperatures)
# ★把每一週的最大值都抓出來，再取一次最大值
min_temperature = min(min(day) for day in temperatures)
# ★把每一週的最小值都抓出來，再取一次最小值

# 在2D的list裡面計算最大最小溫度其實很辛苦 -> 建議一開始就直接宣告1D的list

print("Average: %.2f" % temperature_avg )
print("Highest: %.1f" % max_temperature)
print("Lowest: %.1f" % min_temperature)




# 參考答案直接建立1D的list，只有前面輸入是雙重迴圈，後面計算超快
# ----------------------------------------------------------------------
# 自己練習參考答案的思路

temperatures = []
for week in range(0, 4):
    print("Week %d" % (week + 1))
    for day in range(0, 3):
        temperature = float(input("Day %d: " % (day + 1)))
        temperatures.append(temperature)

temperatures_total = sum(temperatures)
temperature_avg = temperatures_total / len(temperatures)
max_temperature = max(temperatures)
min_temperature = min(temperatures)
# 直接用1D的list真的很好處理

print("Average: %.2f" % temperature_avg)
print("Highest: %.1f" % max_temperature)
print("Lowest: %.1f" % min_temperature)
