while True:

    tall = int(input("請輸入身高(cm): ")) # 這兩個需要拿進來不然會變成無限迴圈
    weight = int(input("請輸入體重(kg): ")) # 這兩個需要拿進來不然會變成無限迴圈

    if (tall == -9999) or (weight == -9999):
        break # 先判斷要不要跳出去

    bmi = weight / ((tall / 100) ** 2) # 計算BMI

    # 開始印出訊息
    print("\nBMI: %.2f" % bmi)
    if bmi >= 30:
        print("State: fat")

    elif bmi >= 25:
        print("State: over weight")

    elif bmi >= 18.5:
        print("State: normal")

    elif bmi < 18.5:
        print("State: under weight")