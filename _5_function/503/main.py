def compute(a, b):
    total = 0  # 設定總和的初始值
    for n in range(a, b + 1):  # 有含最後一項
        total += n
        # ★用一個變數total來儲存加總的數值
        # ★如果是要最大值或最小值建議用list，然後用min或是max function來抓
        # ★如果取極值用變數的方式，會有無法去限制人家輸入甚麼數值的問題
        # ★可能會讓初始值在所有輸入數值的中間，使得輸出只是初始值以上/以下的最小/最大值
        # ★如果是一開始就知道輸入數值有個區間範圍才能用儲存變數來做

    return int(total)  # 回傳計算結果


number_1 = int(input("請輸入第一個整數(最小值): "))
number_2 = int(input("請輸入第二個整數(最大值): "))

number_total = compute(number_1, number_2)

print("從%d連加到%d的總和 = %d" % (number_1, number_2, number_total))
