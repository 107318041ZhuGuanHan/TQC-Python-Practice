numbers_string = []

message = "請輸入整數: "
message += "\n(如要離開請輸入'-9999')"

while True:
    number = int(input(message))

    if number == -9999:

        if len(numbers_string) < 1:
            print("請輸入至少1個整數，要不然會有很多麻煩")
            continue

        elif len(numbers_string) >= 1:
            break

    numbers_string.append(number)

numbers_set = set(numbers_string)
# 如果輸入重複的數字，會被set剔除
# -> ex.輸入: 1, 2, 3, 4, 5, 5會變成只有1, 2, 3, 4, 5 -> 然後直接進行計算會少1個 5

# 這題沒有重複的數字
print("Set: " + str(numbers_set))
print("Length: " + str(len(numbers_set)))
print("Max: " + str(max(numbers_set)))
print("Min: " + str(min(numbers_set)))
print("Sum: " + str(sum(numbers_set)))




# numbers_set = set()
# numbers_set.append(0) ->★ 會報錯，因為set不能用append
# numbers_set.add(0) -> ★ 沒問題，set後面可以接.add() -> 參考答案的方式

# ----------------------------------------------------------------------
# 自己練習一次參考答案的方式

numbers_set = set()

message = "請輸入整數: "
message += "\n(若要離開/結束程序請輸入'-9999')"

while True:
    number = int(input(message))

    if number == -9999:

        if len(numbers_set) < 1:
            print("請輸入至少1個整數，要不然我們會很麻煩！")
            continue

        elif len(numbers_set) >= 1:
            break

    numbers_set.add(number)

print("Set: " + str(numbers_set))
print("Length: " + str(len(numbers_set)))
print("Max: " + str(max(numbers_set)))
print("Min: " + str(min(numbers_set)))
print("Sum: " + str(sum(numbers_set)))
