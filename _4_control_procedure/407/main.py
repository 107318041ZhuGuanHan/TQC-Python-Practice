while True:
    year = int(input("請輸入西元年分，我將為您判斷是否為閏年: "))

    if year == -9999:
        break

    if year > 0: # 判斷是否有人亂打
        if year % 4 == 0:
            print(str(year) + " is a leap year.")

        else:
            print(str(year) + " is not a leap year.")

    else:
        print("請正常輸入!")