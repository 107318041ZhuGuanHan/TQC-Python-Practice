string = str(input("請輸入一個字元，我將為您判斷它是甚麼(如大小寫英文字母、數字、符號): "))

if string.isupper(): # 判斷是否為英文大寫
    print(string + " is an alphabet(upper).英文大寫")

elif string.islower(): # 判斷是否為英文小寫
    print(string + " is an alphabet(lower).英文小寫")

elif string.isdigit(): # 判斷是否為數字格式
    print(string + " is a number.數字")

elif string.isspace(): # 判斷是否為空格
    print(string + " is a space.空格")

else:
    print(string + " is a symbol.其他符號")