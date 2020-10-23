number = int(input("請輸入一個0~15的數字，我將為您轉換成16進位: "))

if number >= 10:
    number = hex(number)
    print(str(number).lstrip("0x").upper()) # 先轉成字串，
    # 再把字串左邊的0x去掉，然後改成大寫

else:
    print(str(number))
# ----------------------------------------------------------------------
# 沒有判斷直接來:

number = int(input("請輸入一個0~15的數字，我將為您轉換成16進位: "))
number = hex(number)
print(str(number).lstrip("0x").upper())



