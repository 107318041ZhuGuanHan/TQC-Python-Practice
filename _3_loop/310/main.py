number = int(input("輸入一個大於1的正整數，我將為您計算很複雜的東西: "))
total = 0 # 宣告初始值等等比較好用
for n in range(1, number): # 範圍只到number，因為下面最後:(number-1) + 1 = number
    total = total + ((1/(n ** 0.5 + (n+1) ** 0.5)))
    # 參考答案的index與我不同，另外答案使用函式庫math.sqrt來開根號

print(total)
print("%.4f" % total)