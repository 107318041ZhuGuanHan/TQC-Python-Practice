while True:
    number = int(input("請輸入一個正整數(代表分數): "))

    if number == -9999:
        break

    # 這邊判斷分數等級
    if (number >= 90) and (number <= 100):
        print(str(number) + " -> A")

    elif number >= 80: # 輸入123，會輸出B，★因為上面if沒過這邊判斷還是會過 -> 是bug -> 最好還是每個都指定範圍比較好 -> 要不然在多一層if else在外層
        print(str(number) + " -> B")

    elif number >= 70:
        print(str(number) + " -> C")

    elif number >= 60:
        print(str(number) + " -> D")

    elif (number >= 0) and (number <= 59):
        print(str(number) + " -> E")

    else:
        print("請輸入一個正常的分數")



