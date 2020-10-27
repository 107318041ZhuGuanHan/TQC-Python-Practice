color_dict = {}

while True:
    key = input("Key: ")

    if key == 'end':
        break

    value = input("Value: ")

    if value == 'end':
        break

    color_dict[key] = value

for key, value in sorted(color_dict.items()):
    # 這裡可以用沒副作用的function來排序key的輸出 -> 參考答案也是這樣
    print(key + ": " + value)