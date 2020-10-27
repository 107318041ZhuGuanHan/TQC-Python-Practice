personal_info = {}

while True:
    key = input("Key: ")

    if key == 'end':
        break

    value = input("Value: ")

    if value == 'end':
        break

    personal_info[key] = value

while True:
    search = input("Search key: ") # 最關鍵的這裡差不多
    ans = search in personal_info.keys()
    print(ans)
