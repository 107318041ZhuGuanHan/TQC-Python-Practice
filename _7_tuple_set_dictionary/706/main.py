english = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', # 小心不要打錯，錯在這裡很難找
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

time = int(input("請輸入您要測試幾筆資料: "))

for i in range(0, time):
    string = input("第%d筆資料: " % (i+1))

    string_set = set()  # 宣告空的集合

    for s in string:
        string_set.add(s.lower()) # ★要轉成全部小寫才能比較，
        # 不然就算是全字母句也會因為大寫而回傳False

    if ' ' in string_set:
        string_set.remove(' ')  # 把空格去掉 -> set不會有重複的東西所以去掉一次即可
                                # list就會需要寫迴圈一個一個慢慢殺了
    state = (string_set == english)

    print("全字母句: " + str(state))

# string = "The quick brown fox jumps over the lazy dog"
# for s in string:
#     print(s) -> 會一個一個字元印出來



# ----------------------------------------------------------------------
# ★參考答案是直接把一段字串給直接轉成set

english = set("abcdefghijklmnopqrstuvwxyz") # ★直接輸入a~z，set()會幫你切成set的格式
time = int(input("請輸入您要測試幾筆資料: "))

for i in range(0, time):
    string = set(input("第%d筆資料: " % (i+1)).lower())
    # 把輸入的字串全部轉成小寫，然後全部變成字母集合

    if ' ' in string: #把空格殺掉
        string.remove(' ')

    state = string == english
    print("全字母句: " + str(state))


