message = "請輸入您的購物金額，我將為您顯示折扣優惠後的實付金額: "
message += "\n(購物金額需要超過8,000元(含)才有打折) "

price = int(input(message))

if price >= 38000:
    print("打七折，共 " + str(price * 0.7) + " 元")

elif price >= 28000:
    print("打八折，共 " + str(price * 0.8) + " 元")

elif price >= 18000:
    print("打九折，共 " + str(price * 0.9) + " 元")

elif price >= 8000:
    print("打九五折，共 " + str(price * 0.95) + " 元")

elif price < 8000:
    print("沒打折，原價共 " + str(price) + " 元")