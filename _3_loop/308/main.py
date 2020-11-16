# 自己的方法
num_of_data = int(input("請輸入你等等總共會輸入幾筆資料: "))

for n_data in range(1, num_of_data+1):
    str_data = input("請輸入你要的數字資料，我將為您將每一位的數字進行加總: ") # 使用者先輸入數字，並賦值儲存在一個字串變數中
    str_list_data = list(str_data) # 將字串變數轉換為list，目前是一個str list
    int_list_data = [] # 宣告一個空的int list之後要拿來用
    for n in str_list_data[:]: # 為str_list_data建立一個副本，並且開始使用來將其所有字串元素轉換為int元素
        int_list_data.append(int(n)) # 將轉換出來的int元素賦值/儲存在int list中

    total = sum(int_list_data) # 有int list，才可以用sum對於這個list使用sum這個函式
    print("Sum of all digits of " + str_data + " is " + str(total))
    # 最後就是印出來

# ----------------------------------------------------------------------
#答案的方法(不需要建立list) -> 約等於305的方法、知識

num_of_data = int(input("請輸入你等等總共會輸入幾筆資料: "))

for n_data in range(1, num_of_data+1):
    str_data = input("請輸入你要的數字資料，我將為您將每一位的數字進行加總: ")
    total = 0 # 用一個變數來計算加總的過程
    for n in range(0, len(str_data)):
        total += int(str_data[n]) # ★在這裡進行加總，就不用建立一堆list只為了要使用sum()的function了

    print("Sum of all digits of " + str_data + " is " + str(total))