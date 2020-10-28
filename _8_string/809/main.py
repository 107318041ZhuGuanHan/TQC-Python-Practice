# 1.巢狀if:先判斷字串長度是否 >= 8，再去看後面 2.設置3個旗標:長度、英數字、至少一個大寫

string = input("請輸入一段密碼: ")

eng_num_only = True  # 預設是只有英數字
one_upper = False # 預設是沒有半個大寫
if len(string) >= 8:

    for s in string:

        if not (s.isdigit() or s.isalpha()):  # 檢查英數字，如果不是英數字 -> 至少要有一個不是英數字
            eng_num_only = False  # 這邊就把預設的True變成fFalse

        if s.isupper():  # 檢查大小寫，如果是大寫 -> 至少要有一個大寫
            one_upper = True  # 這邊就把預設的False變成True

    if eng_num_only and one_upper:
        print("Valid password")

    else:
        print("Invalid password")

else:
    print("Invalid password")

# ----------------------------------------------------------------------
# 單純用3個旗標分別修改指定，最後再合在一起判斷

string = input("請輸入一段密碼: ")

length = len(string) >= 8  # 一拿到字串就可以判斷賦值囉~
eng_num_only = True  # 預設是只有英數字
one_upper = False

for s in string:

    if not (s.isdigit() or s.isalpha()):  # ★這邊的話參考答案是直接用 .isalnum() ->判斷是否為 英數字
        eng_num_only = False

    if s.isupper():
        one_upper = True

if length and eng_num_only and one_upper:
    print("Valid password")

else:
    print("Invalid password")