def compute(a, b):
    total = 0  # 設定總和的初始值
    for n in range(a, b + 1):  # 有含最後一項
        total += n
        # ★用一個變數total來儲存加總的數值
        # ★如果是要最大值或最小值建議用list，然後用min或是max function來抓

    return int(total)  # 回傳計算結果


number_1 = int(input("請輸入第一個整數(最小值): "))
number_2 = int(input("請輸入第二個整數(最大值): "))

number_total = compute(number_1, number_2)

print("從%d連加到%d的總和 = %d" % (number_1, number_2, number_total))
