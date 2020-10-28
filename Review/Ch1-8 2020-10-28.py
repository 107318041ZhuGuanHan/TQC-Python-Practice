# ----------------------------------------------------------------------
# 205
string = input("請輸入一個字元，我將為您判斷他是什麼: ")

if string.isupper():
    print(string + " is upper-alphabet.")

elif string.islower():
    print(string + " is lower-alphabet.")

elif string.isdigit():
    print(string + " is number.")

elif string.isspace():
    print(string + " is space.")

else:
    print(string + " is other symbol.")
# ----------------------------------------------------------------------
# 206 ★ 想到用range的方式
score = int(input("請輸入成績，我將為您判斷等級: "))

if score in range(80, 101):
    print("A")

elif score in range(70, 80):
    print("B")

elif score in range(60, 70):
    print("C")

elif score in range(0, 60):
    print("F")

else:
    print("分數請不要亂打")

# ----------------------------------------------------------------------
# 208

number = int(input("請輸入1個0~15的數字: "))

if number >= 10:
    print((str(hex(number))).lstrip("0x").upper())

else:
    print(str(number))

# ----------------------------------------------------------------------
# 303
n = int(input("請輸入一個正整數: "))
for row in range(1, n+1):
    for column in range(1, row+1):
        print("%4d" % (row * column), end='')
    print("")
# ----------------------------------------------------------------------
# 305
number = input("請輸入一串數字，我將為您反轉: ")
for n in range(1, len(number)+1):
    print(number[-n], end='')
# ----------------------------------------------------------------------
# 307
n = int(input("請輸入一個數字n，我將為您輸出一個n * n的乘法表:"))

for n_right in range(1, n + 1):

    for n_left in range(1, n+1):
        print("%-2d* %-2d= %-4d" % (n_left, n_right, (n_left * n_right)), end='')

    print("")
# ----------------------------------------------------------------------
# 308

num_of_data = int(input("請輸入您欲輸入的資料筆數: "))

for n_data in range(0, num_of_data):

    data = input("請輸入第%d筆資料: "% (n_data+1))
    total = 0
    for number in data:
        total += int(number)

    print("Sum of all digits of %s is %d" % (data, total))