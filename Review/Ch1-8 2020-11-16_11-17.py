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
def compute(x, y):
    common_factors = []
    for n in range(1, min(x, y) + 1):

        if x % n == 0 and y % n == 0:
            common_factors.append(n)

    return max(common_factors)

x, y = eval(input("輸入兩個正整數x、y（以半形逗號分隔）: "))

gcd = compute(x, y)
print(gcd)
# ----------------------------------------------------------------------
# 509
def compute(p, q):
    # return p if q == 0 else compute(q, p % q) ★可以用倒裝句
    if q == 0:
        return p
    else:
        return compute(q, p % q)  # ★這裡記得要打return，並不是直接呼叫就好了

x, y = eval(input("請輸入 x/y 中的x與y(以半形逗號分隔): "))
m, n = eval(input("請輸入 m/n 中的m與n(以半形逗號分隔): "))

p = x * n + y * m
q = y * n

gcd = compute(p=p, q=q)

p = p / gcd
q = q / gcd

print("%d/%d + %d/%d = %d/%d" % (x, y, m, n, p, q))
# ----------------------------------------------------------------------
# 510-1
def face_numbers(num):

    if num == 0 or num == 1:
        return  num

    return  face_numbers(num-1) + face_numbers(num-2)

number_in = int(input("請輸入您想要顯示費式數列的前面幾項: "))
print("費氏數列的前0~%d項為: " % number_in)
for n in range(0, number_in+1):
    print(face_numbers(n), end=" ")

# ----------------------------------------------------------------------
# 510-2
face_list = [0, 1]
number_in = int(input("請輸入您想要顯示費式數列的前面幾項: "))

for n in range(2, number_in+1):
    face_list.append(face_list[n-1] + face_list[n-2])
print("費氏數列的前0~%d項為: " % number_in)

for number in face_list:
    print(number, end=' ')
# ----------------------------------------------------------------------
# 601 不知不覺打了...
numbers = []
for n in range(0, 12):
    number = int(input("請輸入第%d個正整數: " % (n+1)))
    numbers.append(number)

total = 0
for n in range(0, len(numbers), 2):
    total += numbers[n]

for number in numbers:
    print("%3d" % number, end='')
    if (numbers.index(number) + 1) % 3 == 0:
        print("")

print("索引為偶數的數字相加總合: %d" % total)


# ----------------------------------------------------------------------
# 604-1
numbers = []

for n in range(0, 10):
    number = int(input("請輸入第%d個整數: " % (n+1)))
    numbers.append(number)

count_number = 0
much_number = 0
for number in numbers:
    if numbers.count(number) > count_number:
        much_number = number
        count_number = numbers.count(number)

print("眾數為%d, 有%d個" % (much_number, count_number))
# ----------------------------------------------------------------------
# 604-2
numbers = []

for n in range(0, 10):
    number = int(input("請輸入第%d個整數: " % (n+1)))
    numbers.append(number)

numbers_dict = {}
for number in numbers:
    numbers_dict[number] = numbers.count(number)

for key, value in numbers_dict.items():
    if value == max(numbers_dict.values()):
        print("眾數為%d, 出現次數為%d" % (key, value))
# ----------------------------------------------------------------------
# 606
rows = int(input("請輸入二維list的列數: "))
cols = int(input("請輸入二維list的行數: "))

num_list = [[ c-r for c in range(0, cols)] for r in range(0, rows)]
for row in num_list:

    for column in row:

        print("%4d" % column, end='')

    print("")
# ----------------------------------------------------------------------
# 607
students = ['Student 1', 'Student 2', 'Student 3']
grades = [[0 for score in range(0, 5)] for student in range(0, 3)]

for student in range(0, 3):
    print("請輸入第%d位學生的成績: " %(student+1))
    for grade in range(0, 5):
        score = int(input("請輸入第%d筆成績: " % (grade+1)))
        grades[student][grade] = score

for g in range(0, len(grades)):
    print(students[g])
    total_score = sum(grades[g])
    print("Sum = %d" % total_score)
    avg_score = total_score / len(grades[g])  # 建議先算完再印出來比較不會出錯
    print("Average = %.2f" % avg_score)
# ----------------------------------------------------------------------
# 608
numbers = []
for n in range(0, 9):
    number = int(input("請輸入numbers[%d][%d]" % (n // 3, n % 3)))
    numbers.append(number)

max_number = max(numbers)
min_number = min(numbers)

print("Index of the largest number %d is: (%d, %d)"
      % (max_number,
         numbers.index(max_number) // 3,
         numbers.index(max_number) % 3))
print("Index of the smallest number %d is: (%d, %d)"
      % (min_number,
         numbers.index(min_number) // 3,
         numbers.index(min_number) % 3))
# ----------------------------------------------------------------------
# 609
matrix_1 = []
matrix_2 = []
matrix_sum = []

print("Enter matrix 1:")
for m in range(0, 4):
    number = int(input("[%d, %d]" % (m // 2, m % 2)))
    matrix_1.append(number)

print("Enter matrix 2:")
for m in range(0, 4):
    number = int(input("[%d, %d]" % (m // 2, m % 2)))
    matrix_2.append(number)

for n in range(0, 4):
    matrix_sum.append(matrix_1[n] + matrix_2[n])

print("Matrix 1:")
for i in range(0, 2):
    print("**%-2d%-2d**" % (matrix_1[2 * i + 0], matrix_1[2 * i + 1]))

print("Matrix 2:")
for i in range(0, 2):
    print("**%-2d%-2d**" % (matrix_2[2 * i + 0], matrix_2[2 * i + 1]))

print("Sum of 2 matrices:")
for i in range(0, 2):
    print("**%-3d%-3d**" % (matrix_sum[2 * i + 0], matrix_sum[2 * i + 1]))

# ----------------------------------------------------------------------
# 610
temperatures = []

for week in range(0, 4):
    print("Week %d: " % (week+1))
    for day in range(0, 3):
        temperature = float(input("Day %d: " % (day + 1)))
        temperatures.append(temperature)

avg_temperature = sum(temperatures) / len(temperatures)
highest_temperature = max(temperatures)
lowest_temperature = min(temperatures)
print("Average: %.2f" % avg_temperature)
print("Highest: %.1f" % highest_temperature)
print("Lowest: %.1f" % lowest_temperature)
# ----------------------------------------------------------------------
# 702
list_1 = []
list_2 = []
print("Create tuple1:")
while True:
    number = int(input("請輸入數字: "))
    if number == -9999:
        break
    list_1.append(number)

print("Create tuple2:")
while True:
    number = int(input("請輸入數字: "))
    if number == -9999:
        break
    list_2.append(number)

numbers_list = list_1 + list_2
numbers_tuple = tuple(numbers_list)
numbers_list.sort()

print("Combined tuple before sorting:", numbers_tuple)
print("Combined list after sorting:", numbers_list)
# ----------------------------------------------------------------------
# 704
numbers = set()

while True:
    number = int(input("請輸入數字: \n(如要離開請輸入'-9999')"))

    if number == -9999:
        break

    numbers.add(number)

print("Length: %d" % len(numbers))
print("Max: %d" % max(numbers))
print("Min: %d" % min(numbers))
print("Sum: %d" % sum(numbers))
# ----------------------------------------------------------------------
# 705
set_1 = set()
set_2 = set()
set_3 = set()
print("Input to set1:")
for i in range(0, 5):
    number = int(input("請輸入第%d個整數: " % (i+1)))
    set_1.add(number)

print("Input to set2:")
for i in range(0, 3):
    number = int(input("請輸入第%d個整數: " % (i+1)))
    set_2.add(number)

print("Input to set3:")
for i in range(0, 9):
    number = int(input("請輸入第%d個整數: " % (i+1)))
    set_3.add(number)

print("set2 is subset of set1:", set_2.issubset(set_1))
print("set3 is superset of set1:", set_3.issuperset(set_1))
# ----------------------------------------------------------------------
# 706
alphabet = set('abcdefghijklmnopqrstuvwxyz')
time = int(input("輸入測試資料筆數: "))

for t in range(0, time):
    data = input("請輸入第%d筆資料: " % (t+1))
    data = data.lower()
    data = set(data)
    data.remove(' ')
    print(data == alphabet)
# ----------------------------------------------------------------------
# 707
subject_x = set()
subject_y = set()
message = "請輸入科目: "
message += "\n(若要退出請輸入'end')"

print("Enter group X's subjects: ")
while True:
    subject = input(message)

    if subject == 'end':
        break

    subject_x.add(subject)

print("Enter group Y's subjects: ")
while True:
    subject = input(message)

    if subject == 'end':
        break

    subject_y.add(subject)

print(sorted(subject_x))
print(sorted(subject_y))
print(sorted(subject_x | subject_y))
print(sorted(subject_x & subject_y))
print(sorted(subject_y - subject_x))
print(sorted(subject_x ^ subject_y))

# ----------------------------------------------------------------------
# 708
dict_1 = {}
dict_2 = {}

print("Create dict1: ")
while True:
    key = input("Key: ")
    if key == 'end':
        break

    value = input("Value: ")
    if value == 'end':
        break

    dict_1[key] = value

print("Create dict2: ")
while True:
    key = input("Key: ")
    if key == 'end':
        break

    value = input("Value: ")
    if value == 'end':
        break

    dict_2[key] = value

dict_combine = {**dict_1, **dict_2}

for key, value in sorted(dict_combine.items()):
    print(key + ": " + value)
# ----------------------------------------------------------------------
# 801
string = input("請輸入一個字串: ")

for s in string:
    print("Index of '%s': %d" % (s, string.index(s)))
# ----------------------------------------------------------------------
# 802
string = input("請輸入一個字串: ")

total_ascii = 0
for s in string:
    print("ASCII code for '%s' is %d" % (s, ord(s)))
    total_ascii += ord(s)

print("Sum of ASCII = ", total_ascii)
# ----------------------------------------------------------------------
# 803
string_list = input("輸入一個句子（至少有五個詞，以空白隔開）: ").split(' ')

for string in string_list[-3:]:
    print(string, end=' ')
# ----------------------------------------------------------------------
# 805
string = input("請輸入一個字串: ")

print("|%-10s|" % string)
print("|%s|" % string.center(10))
print("|%10s|" % string)
# ----------------------------------------------------------------------
# 806
def compute(string, char):
    return string.count(char)

string = input("請輸入一個句子: ")
char = input("請輸入您要計算出現次數的字元: ")

count = compute(string=string, char=char)
print("%s occur %d time(s)" % (char, count))
# ----------------------------------------------------------------------
# 808
while True:
    ssn = input("輸入一個社會安全碼SSN")
    ssn_list = ssn.split('-')
    valid_ssn = True  # 先假設格式是正確的

    for number in ssn_list:
        if not number.isnumeric():
            valid_ssn = False  # 遇到格式不正確就把它改成False

    len_1 = len(ssn_list[0]) == 3
    len_2 = len(ssn_list[1]) == 2
    len_3 = len(ssn_list[2]) == 4
    if not (len_1 and len_2 and len_3):
        valid_ssn = False

    if valid_ssn:
        print("Valid SSN")

    else:
        print("Invalid SSN")

# ----------------------------------------------------------------------
# 809
password = input("請輸入密碼: ")

if len(password) >= 8:
    condition_a = True
else:
    condition_a = False

if password.isalnum():
    condition_b = True
else:
    condition_b = False

condition_c = False
for p in password:
    if p.isupper():
        condition_c = True

condition = condition_a and condition_b and condition_c

if condition:
    print("Valid password")

else:
    print("Invalid password")
# ----------------------------------------------------------------------
# 810
k = int(input("請輸入資料筆數(測試次數): "))

for n in range(0, k):

    numbers = input("請輸入資料(以空格隔開): ").split(' ')

    for i in range(0, len(numbers)):
        numbers[i] = float(numbers[i])

    ans = max(numbers) - min(numbers)
    print("Max - Min = %.2f" % ans)


















