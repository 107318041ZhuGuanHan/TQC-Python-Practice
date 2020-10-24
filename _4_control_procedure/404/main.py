number = input("請輸入一數字，我將為您輸出將每一位數反轉後的數字: ")

for n in range(1, len(number)+1): # ★ 用一個變數n來抓number的index，而不是用一班的list操作方式
    print("%s" % number[-n],  end="") # ★ 在這裡需要用到n
    #在這邊0不需要別判斷也正常運作

# 參考答案這裡也沒有特別去判斷0
