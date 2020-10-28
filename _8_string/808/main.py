# 會用到.isdight()

ssn_list = input("請輸入社會安全碼: ").split('-')

ssn = True  # 宣告旗標來判斷是否初步符合格式，賦值預設值為True
for number in ssn_list:

    if not number.isdigit():  # 如果每段密碼不是一段正常的數字
        # ★ not number.isdigit() 會比 number.isdigit() == False 更好看

        print("Invalid SSN")
        ssn = False # 抓到不是以後，旗標要改 -> 初步不符合
        break  # 抓到不是就結束了


length_1 = len(ssn_list[0]) == 3
length_2 = len(ssn_list[1]) == 2
length_3 = len(ssn_list[2]) == 4

if ssn: # 先判斷是否初步符合

    if length_1 and length_2 and length_3:  # 初步看完是不是數字以後，接著看數字長度正不正確

        print("Valid SSN")
    else:                                   # 只要任何一個長度不正確就是格式錯誤
        print("Invalid SSN")


