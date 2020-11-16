# ----------------------------------------------------------------------
# 205
char = input("請輸入一個字元: ")

if char.isupper():
    print("%s is an upper alphabet." % char)

elif char.islower():
    print("%s is a lower alphabet." % char)

elif char.isnumeric():
    print("%s is a number." % char)

elif char.isspace():
    print("%s is a space." % char)

else:
    print("%s is other symbol." % char)
# ----------------------------------------------------------------------
# 206
grade = int(input("請輸入分數: "))

if grade in range(80, 101):
    print("A")

elif grade in range(70, 80):
    print("B")

elif grade in range(60, 70):
    print("C")

elif grade in range(0, 60):
    print("F")

else:
    print("請輸入0~100之間的分數!")
# ----------------------------------------------------------------------
# 208
number = int(input("輸入一個十進位整數num(0 ≤ num ≤ 15): "))
if number >= 10:
    number_16 = hex(number)
    print(str(number_16).lstrip("0x").upper())

else:
    print(number)
# ----------------------------------------------------------------------
# 303
number = int(input("請輸入一個整數: "))

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print("%4d" % (row * column), end='')

    print("")
# ----------------------------------------------------------------------
# 305
number = input("請輸入一個正整數，等等為您反轉: ")

for n in range(1, len(number)+1):
    print(number[-n], end='')
# ----------------------------------------------------------------------
# 308
time = int(input("請輸入要判斷的資料筆數: "))

for t in range(0, time):
    number = input("請輸入第%d筆資料" % (t + 1))
    total = 0
    for n in range(0, len(number)):
        total += int(number[n])
    print("Sum of all digits of %s is %d" % (number, total))
# ----------------------------------------------------------------------
# 310
number = int(input("請輸入一正整數: "))

total = 0
for n in range(1, number):
    total += 1 / ((n ** 0.5) + ((n + 1) ** 0.5))

print("%.4f" % total)
# ----------------------------------------------------------------------
# 401
numbers = []
for n in range(0, 10):
    numbers.append(int(input("請輸入第%d個數字" % (n + 1))))

print("最小值: %d" % min(numbers))
# ----------------------------------------------------------------------
# 402
numbers = []
while True:
    number_in = int(input("請輸入數字: "))
    if number_in == 9999:
        break
    else:
        numbers.append(number_in)

print("最小值: %d" % min(numbers))
# ----------------------------------------------------------------------
# 403
numbers = []
number_min = int(input("請輸入最小值: "))
number_max = int(input("請輸入最大值: "))
total = 0
count = 0
for n in range(number_min, number_max+1):
    if n % 4 == 0 and n % 9 == 0:
        total += n
        count += 1
        numbers.append(n)

    elif n % 4 == 0:
        total += n
        count += 1
        numbers.append(n)

    elif n % 9 == 0:
        total += n
        count += 1
        numbers.append(n)

print("倍數個數(變數):", count)
print("倍數個數(list):", len(numbers))
print("倍數總和(變數):", total)
print("倍數總和(list):", sum(numbers))
# ----------------------------------------------------------------------
# 404
number = input("輸入一個正整數，此正整數將以反轉的順序輸出: ")

for n in range(1, len(number) + 1):
    print(number[-n], end='')
# ----------------------------------------------------------------------
# 405
while True:
    score = int(input("請輸入分數: "))

    if score == -9999:
        break

    if score in range(90, 101):
        print("GPA: A")

    elif score in range(80, 90):
        print("GPA: B")

    elif score in range(70, 80):
        print("GPA: C")

    elif score in range(60, 70):
        print("GPA: D")

    elif score in range(0, 60):
        print("GPA: E")

    else:
        print("請輸入個正常的分數！")

# ----------------------------------------------------------------------
# 410
height = int(input("請輸入一正整數n，表示等腰三角形的高: "))

space = " "
star = "*"
for h in range(1, height+1):
    message = (height-h) * space + (2 * h - 1) * star
    print(message)
# ----------------------------------------------------------------------
# 410下半部
for h in range(1, height):
    message = h * space + (2 * height - 1 - 2 * h) * star
    print(message)
# ----------------------------------------------------------------------
# 菱形
height = int(input("請輸入菱形的高: "))
width = int(input("請輸入菱形的寬: "))

space = " "
star = "*"

height_up_tri = height // 2 + 1
height_low_tri = height // 2


add_rate = (width - 1) // (height_up_tri - 1)

for w in range(1, width + add_rate, add_rate):
    message = w * star
    print(message.center(width))

for w in range(add_rate, width, add_rate):
    message = (width - w) * star
    print(message.center(width))
# ----------------------------------------------------------------------
# 503
def compute(number_1, number_2):
    total = 0
    for n in range(number_1, number_2+1):
        total += n

    return total

a = int(input("請輸入最小值: "))
b = int(input("請輸入最大值: "))

ans = compute(number_1=a, number_2=b)
print(ans)
# ----------------------------------------------------------------------
# 505
def compute(char, col, row):

    for r in range(0, row):
        for c in range(0, col):
            print(char, end=' ')
        print("")

character = input("請輸入一個字元: ")
column = int(input("請輸入每行印出的個數(行數): "))
row = int(input("請輸入要印出幾列: "))

compute(char=character, col=column, row=row)
# ----------------------------------------------------------------------
# 508
# ----------------------------------------------------------------------
# 509
# ----------------------------------------------------------------------
# 510


























