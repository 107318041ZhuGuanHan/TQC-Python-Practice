dict_1 = {}
dict_2 = {}

message_key = "請輸入關鍵字(key): "
message_value = "請輸入所對應之數值(value): "


print("Create dict1: ")
while True:
    key = input(message_key)

    if key == 'end':
        break

    value = input(message_value)

    if value == 'end':
        break

    dict_1[key] = value


print("Create dict2: ")
while True:
    key = input(message_key)

    if key == 'end':
        break

    value = input(message_value)

    if value == 'end':
        break

    dict_2[key] = value

dict_combine = {**dict_1, **dict_2}  # ★合併字典的方式 這樣最精簡因為1行結束
# 也可以用以下的方式:
# dict_combine = dict_1.copy()
# dict_combine.update(dict_2) -> 參考答案是這樣子搞，只是直接就更新再dict_1

for key, value in sorted(dict_combine.items()): # ★可以直接這樣子，輸出的key就是按照字母排好的了
    print(key + ": " + value)
