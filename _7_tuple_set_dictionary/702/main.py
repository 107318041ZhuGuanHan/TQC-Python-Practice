# ★因為tuple不能直接用sort function修改順序，所以需要先轉回list再用sort()

numbers_1 = []
numbers_2 = []

message = "請輸入整數: "
message += "\n(輸入'-9999'以離開程序)"

print("Create tuple1: ")
while True:
    number = int(input(message))

    if number == -9999:
        break

    numbers_1.append(number)

print("Create tuple2: ")
while True:
    number = int(input(message))

    if number == -9999:
        break

    numbers_2.append(number)

number_total_list = numbers_1 + numbers_2  # 把兩個list相加，賦值給number_total_list
number_total_list.sort()

numbers_total_tuple = tuple(
    numbers_1 + numbers_2)  # 在還是list的時候就加起來再轉成tuple

print("Combined tuple before sorting: " + str(numbers_total_tuple))
print("Combined list after sorting: " + str(number_total_list))

# numbers_total = tuple(numbers_1 + numbers_2)
# numbers_total = list(numbers_total).sort()
# ★把前面已經轉過去的tuple再轉回來是無效的，會變成None(不能同一個物件型轉兩次)


# ----------------------------------------------------------------------
# 參考答案真的生出兩個tuple在做
list_1 = []
list_2 = []

message = "請輸入整數: "
message += "\n(輸入'-9999'以離開程序)"

print("Create tuple1: ")
while True:
    number = int(input(message))

    if number == -9999:
        break

    list_1.append(number)

tuple_1 = tuple(list_1)


print("Create tuple2: ")
while True:
    number = int(input(message))

    if number == -9999:
        break

    list_2.append(number)

tuple_2 = tuple(list_2)

print("Combined tuple before sorting: " + str(tuple_1 + tuple_2))
print("Combined list after sorting: " + str(sorted(tuple_1 + tuple_2)))
# 印出來的時候可以直接加起來還

# ----------------------------------------------------------------------
# 驗證自己想法

tuple_3 = tuple_1 + tuple_2 # 在這裡也可以直接用 +號 串起來
print(tuple_3)

tuple_3.sort() # ★tuple後面不能接.sort()這個有副作用的function，所以會報錯

sorted(tuple_3) # ★用這種沒副作用的function，就可以把tuple自動形轉成list並且用function排序
