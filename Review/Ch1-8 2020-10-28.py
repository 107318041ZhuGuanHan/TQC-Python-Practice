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
for row in range(1, n + 1):
    for column in range(1, row + 1):
        print("%4d" % (row * column), end='')
    print("")
# ----------------------------------------------------------------------
# 305
number = input("請輸入一串數字，我將為您反轉: ")
for n in range(1, len(number) + 1):
    print(number[-n], end='')
# ----------------------------------------------------------------------
# 307
n = int(input("請輸入一個數字n，我將為您輸出一個n * n的乘法表:"))

for n_right in range(1, n + 1):

    for n_left in range(1, n + 1):
        print(
            "%-2d* %-2d= %-4d" % (n_left, n_right, (n_left * n_right)),
            end='')

    print("")
# ----------------------------------------------------------------------
# 308

num_of_data = int(input("請輸入您欲輸入的資料筆數: "))

for n_data in range(0, num_of_data):

    data = input("請輸入第%d筆資料: " % (n_data + 1))
    total = 0
    for number in data:
        total += int(number)

    print("Sum of all digits of %s is %d" % (data, total))

# ----------------------------------------------------------------------
# 401

numbers = []
print("請輸入10個數字，我將為您輸出10個數字中的最小值: ")
for t in range(1, 11):
    numbers.append(int(input("請輸入第%d個數字: " % t)))

min_value = min(numbers)

print("Min: " + str(min_value))

# ----------------------------------------------------------------------
# 403
print("請輸入兩個正整數: ")
a = int(input("請輸入第1個正整數a(最小值): "))
b = int(input("請輸入第2個正整數b(最大值): "))

total = 0
times = 0
numbers = []

for n in range(a, b + 1):

    if (n % 4 == 0) and (n % 9 == 0):
        times += 1
        total += n
        numbers.append(n)

    elif n % 4 == 0:
        times += 1
        total += n
        numbers.append(n)

    elif n % 9 == 0:
        times += 1
        total += n
        numbers.append(n)

line = 0  # 換行
for number in numbers:
    print("%-4d" % number, end='')

    line += 1
    if line % 10 == 0:
        print("")

print("\n倍數個數(變數): " + str(times))
print("倍數總和(變數): " + str(total))
print("倍數個數(list): " + str(len(numbers)))
print("倍數總和(list): " + str(sum(numbers)))

# ----------------------------------------------------------------------
# 404
number = input("請輸入一串數字，我將為您將這串數字反轉: ")

for n in range(1, len(number) + 1):
    print(number[-n], end='')

print("")

# ----------------------------------------------------------------------
# 405
while True:
    score = int(input("請輸入一個正整數(代表分數)，我將為您輸出所對應的GPA: "))

    if score == -9999:
        break

    if score in range(90, 101):  # ★用range的方式
        print("A")

    elif score in range(80, 90):
        print("B")

    elif score in range(70, 80):
        print("C")

    elif score in range(60, 70):
        print("D")

    elif score in range(0, 60):
        print('E')

    else:
        print("請輸入一個0~100的正常分數！")
# ----------------------------------------------------------------------
# 410
# (等腰三角形上半部)
height = int(input("請輸入等腰三角形的高: "))

width = 2 * height - 1

space = " "
star = "*"
for h in range(1, height + 1):
    line = (height - h) * space + (2 * h - 1) * star
    print(line)

# (等腰三角形下半部)

for h in range(1, height):
    line = h * space + (width - 2 * h) * star
    print(line)

# (菱形)
height = int(input("請輸入菱形的高度: "))
height_up_tri = height // 2 + 1
height_low_tri = height // 2

width = int(input("請輸入菱形的寬度: "))
width_up_tri = width

adding_rate = (width_up_tri - 1) // (height_up_tri - 1)

width_low_tri = width - adding_rate

star = "*"
for n in range(1, width_up_tri + adding_rate, adding_rate):
    line = star * n
    print("%s" % line.center(width))

for n in range(adding_rate, width_up_tri + adding_rate, adding_rate):
    line = (width - n) * star
    print("%s" % line.center(width))


# ----------------------------------------------------------------------
# 503
def compute(min_number, max_number):
    number_total = 0
    for n in range(min_number, max_number + 1):
        number_total += n

    return number_total


a = int(input("請輸入一個整數a(最小值): "))
b = int(input("請輸入一個整數b(最大值): "))

total = compute(min_number=a, max_number=b)
print("從 %d 連加到 %d 的總和 = %d" % (a, b, total))


# ----------------------------------------------------------------------
# 505-1

def compute(char, column, row):
    for y in range(1, row + 1):
        line = (char + " ") * column
        print(line)


a = input("請輸入一個字元: ")
x = int(input("請輸入每列要印出幾個字元: "))
y = int(input("請輸入要印出多少列: "))

compute(char=a, column=x, row=y)
# ----------------------------------------------------------------------
# 505-2
def compute(char, column, row):
    for r in range(1, row+1):

        for c in range(1, column + 1):
            print("%s" % char, end=" ")

        print("")


a = input("請輸入一個字元: ")
x = int(input("請輸入每列要印出幾個字元: "))
y = int(input("請輸入要印出多少列: "))

compute(char=a, column=x, row=y)
# ----------------------------------------------------------------------
# 507
def compute(number):

    if number > 2:

        prime = True  # 預設number是質數，如果遇到1以外的其他因數在改成False
        for n in range(2, number):
            if number % n == 0:
                prime = False

        if prime:
            print("Prime")

        else:
            print("Not Prime")

    elif number == 2:  # 2是質數
        print("Prime")

    elif number == 1:  # 1不是質數
        print("Not Prime")

    elif number <= 0:  # 0跟負數都不是質數
        print("Not Prime")

x = int(input("請輸入一個整數，我將為您判斷是否為質數: "))

compute(x)
# ----------------------------------------------------------------------
# 508
def compute(x, y):

    max_common_factor = 0  # 1.用變數來儲存
    common_factors = []           # 2.用list來做
    for n in range(1, min(x, y)):
        if (x % n == 0) and (y % n == 0):  # 抓到公因數以後
            max_common_factor = n          # 1.就更新最大公因數的數值
            common_factors.append(n)       # 2.就把公因數加入list

    return max_common_factor, max(common_factors)


number_1, number_2 = eval(input("請輸入兩個正整數(以半形逗號分隔): "))

ans_var, ans_list = compute(x=number_1, y=number_2)

print("Answer from var = %d" % ans_var)
print("Answer from list = %d" % ans_list)
# ----------------------------------------------------------------------
# 510-遞迴

def face_numbers(number):
    if number == 0:
        return number
    elif number == 1:
        return number
    return face_numbers(number - 1) + face_numbers(number - 2)

n = int(input("請輸入一個正整數: "))

print("費氏數列的前1~%d項為: " % n)
for i in range(1, n+1):
    print(face_numbers(i), end=' ')

# ----------------------------------------------------------------------
# 510-list
def face_list(number):
    face_numbers = []
    face_numbers.append(0)
    face_numbers.append(1)
    for n in range(2, number+1):
        face_numbers.append(face_numbers[n-1] + face_numbers[n-2])

    print("費氏數列的前1~%d項為: " % number)
    for i in range(1, len(face_numbers)):
        print(face_numbers[i], end=' ')

num = int(input("請輸入一個正整數: "))

face_list(num)