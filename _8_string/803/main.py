# 用split(' ')
# ★用split()把字串切下去以後，會回傳一個list，裡面的元素就是被切開的每一個字串

string = input("請輸入一個至少5個單字的句子: ")

string_list = string.split(' ')
# 把string切開，看到空格' '就切一刀，切完回傳一個list -> 賦值給string_list

for s in string_list[-3:]:
    print(s, end=' ')


# 參考答案用兩行結束 -> 輸入跟切寫在一起
# ----------------------------------------------------------------------
# 自己練習一下參考答案的寫法

string_list = input("請輸入一個至少5個單字的句子: ").split(' ')
print(string_list[-3], string_list[-2], string_list[-1]) # ★ ,表示印出來的空格

# print(1, 2, 3) -> 會印出1, 2, 3

