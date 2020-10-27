# tuple_string = ()
# tuple_string[0] = '1' 會報錯 -> 因為tuple宣告賦值之後就不能再改了，
# 所以建議先建list，都輸入完之後再改成tuple -> 參考答案也是像我下面那樣子搞

list_string = []

message = "請輸入字串: "
message += "\n(若要離開請輸入'end')"

while True:
    string = input(message)

    if string == 'end':

        if len(list_string) < 5: # 讓user至少輸入5個字串
            print("請至少輸入5個字串")
            continue # 輸入不到5個，會從迴圈的最上面開始執行

        elif len(list_string) >= 5:
            break

    list_string.append(string)

tuple_string = tuple(list_string)

print(tuple_string)
print(tuple_string[:3])   # 從最前面開始，一直到3號(第4個)以前 -> 包含到2號(第3個)
print(tuple_string[-3:])  # 從倒數第3個開始，一直到最後1個(包含最後1個)
