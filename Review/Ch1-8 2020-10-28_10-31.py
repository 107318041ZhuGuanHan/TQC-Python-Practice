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
# ----------------------------------------------------------------------
# 604
numbers = []

print("請輸入10個整數，我將為您輸出這10個整數之中的眾數: ")
for n in range(1, 11):
    numbers.append(int(input("請輸入第%d個整數: " % n)))

max_number = 0  # 眾數數值
max_time = 0    # 眾數的出現次數
for number in numbers:

    if max_time < numbers.count(number):
        max_time = numbers.count(number)
        max_number = number

print("眾數: " + str(max_number))
print("總共出現了 " + str(max_time) + " 次。")
# ----------------------------------------------------------------------
# 606-2維list
def compute(num_list):

    for rows in num_list:

        for cols in rows:
            print("%4d" % cols, end='')

        print("")


row = int(input("請輸入您要的二維list有多少列: "))
column = int(input("請輸入您要的二維list有多少行: "))

numbers = []

for r in range(0, row):

    numbers.append([])
    for c in range(0, column):
        numbers[r].append(c-r)  # numbers[r]的[r]記得要打，不然裡面是1D list

compute(num_list=numbers)

# ----------------------------------------------------------------------
# 606-列表解析裡面還有列表解析

def compute(num_list):
    for rows in num_list:

        for cols in rows:
            print("%4d" % cols, end='')

        print("")

row = int(input("請輸入您要的二維list有多少列: "))
column = int(input("請輸入您要的二維list有多少行: "))

numbers = [[c-r for c in range(0, column)] for r in range(0, row)]

compute(num_list=numbers)
# ----------------------------------------------------------------------
# 607
students = ["1st", "2nd", "3rd"]
grades = [[0 for score in range(0, 5)] for student in range(0, 3)]

for stu in range(0, 3):
    print("The %s student: " % students[stu])
    for score in range(0, 5):
        grades[stu][score] = int(input("請輸入第%d個分數: " % (score + 1)))

for student in range(0, len(grades)):
    print("Student %d" % (student + 1))
    print("#個人總分Sum = %d" % sum(grades[student]))
    print("#個人平均Average = %.2f"
          % (sum(grades[student]) / len(grades[student])))
# ----------------------------------------------------------------------
# 608
numbers = []
for n in range(0, 9):
    numbers.append(int(input("請輸入(%d, %d)" % (n // 3, n % 3))))  #★

max_number = max(numbers)
print("Index of the largest number %d is: (%d, %d)"
      % (max_number,
         numbers.index(max_number) // 3,
         numbers.index(max_number) % 3))

min_number = min(numbers)
min_index = numbers.index(min_number)
print("Index of the smallest number %d is: (%d, %d)"
      % (min_number, min_index // 3, min_index % 3))  # 這比上面優雅



# ----------------------------------------------------------------------
# 609
matrix_1 = [[0 for column in range(0, 2)] for row in range(0, 2)]
matrix_2 = [[0 for column in range(0, 2)] for row in range(0, 2)]
matrix_3 = [[0 for column in range(0, 2)] for row in range(0, 2)]

print("Enter matrix 1: ")
for row in range(0, 2):

    for column in range(0, 2):
        matrix_1[row][column] = int(input("[%d, %d]"
                                          % (row + 1, column + 1)))

print("Enter matrix 2: ")
for row in range(0, 2):

    for column in range(0, 2):
        matrix_2[row][column] = int(input("[%d, %d]"
                                          % (row + 1, column + 1)))

for row in range(0, 2):  # 計算matrix_3

    for column in range(0, 2):
        matrix_3[row][column] = matrix_1[row][column] + matrix_2[row][column]

print("Matrix 1: ")
for row in range(0, len(matrix_1)):

    print("**", end='')
    for column in range(0, len(matrix_1[row])):
        print(matrix_1[row][column], end=' ')
    print("**")

print("Matrix 2: ")
for row in range(0, len(matrix_2)):

    print("**", end='')
    for column in range(0, len(matrix_2[row])):
        print(matrix_2[row][column], end=' ')
    print("**")

print("Sum of 2 matrices: ")
for row in range(0, len(matrix_3)):

    print("**", end='')
    for column in range(0, len(matrix_3[row])):
        print(matrix_3[row][column], end=' ')
    print("**")


# ----------------------------------------------------------------------
# 610
temperatures = []

for week in range(1, 5):
    print("Week %d: " % week)
    for day in range(1, 4):
        temperatures.append(float(input("Day %d: " % day)))

avg = sum(temperatures) / len(temperatures)
highest_value = max(temperatures)
lowest_value = min(temperatures)

print("Average: %.2f" % avg)
print("Highest: %.1f" % highest_value)
print("Lowest: %.1f" % lowest_value)
# ----------------------------------------------------------------------
# 701 -> 實驗轉成tuple再轉回list
numbers = []
message = "請輸入整數: "
message += "\n若要離開請輸入'-9999'"

while True:
    number_in = int(input(message))

    if number_in == -9999:
        break

    numbers.append(number_in)

numbers = tuple(numbers)

# numbers = list(numbers)  # -> 直接用本來的變數這樣轉回去也可以 -> ★可以互轉

# numbers_test = list(numbers) -> 用一個新的變數來接OK
# numbers_test == [-4, 0, 37, 19, 26, -43, 9]

print("Tuple: " + str(numbers))
print("Length: %d" % len(numbers))
print("Max: %d" % max(numbers))
print("Min: %d" % min(numbers))
print("Sum: %d" % sum(numbers))
# ----------------------------------------------------------------------
# 702
list_1 = []
list_2 = []
message = "請輸入數字(整數): "
message += "\n若要結束這個部分請輸入'-9999'"

print("Create tuple1: ")
while True:
    number_in = int(input(message))

    if number_in == -9999:
        break

    list_1.append(number_in)
tuple_1 = tuple(list_1)

print("Create tuple2: ")
while True:
    number_in = int(input(message))

    if number_in == -9999:
        break

    list_2.append(number_in)
tuple_2 = tuple(list_2)

tuple_combine = tuple_1 + tuple_2

print("Combined tuple before sorting: " + str(tuple_combine))
print("Combined list after sorting: " + str(sorted(tuple_combine)))

# ----------------------------------------------------------------------
# 704  測試set與list互轉 -> 也沒問題
numbers = set()

message = "請輸入整數: "
message += "\n若要離開請輸入'-9999'"

while True:
    number_in = int(input(message))

    if number_in == -9999:

        if len(numbers) == 0:
            print("請輸入至少一個數字，不然我們會很麻煩！")
            continue

        else:
            break

    numbers.add(number_in)

# numbers = list(numbers)  #也是可以這樣子直接互轉
# numbers = set(numbers)   # -> ★可以互轉
#
# number_test = list(numbers)
# number_test = set(numbers)

print("Length: %d" % len(numbers))
print("Max: %d" % max(numbers))
print("Min: %d" % min(numbers))
print("Sum: %d" % sum(numbers))
# ----------------------------------------------------------------------
# 705
set_1 = set()
set_2 = set()
set_3 = set()

print("Input to set1: ")
for n in range(0, 5):
    set_1.add(int(input("請輸入第%d個整數: " % (n + 1))))

print("Input to set2: ")
for n in range(0, 3):
    set_2.add(int(input("請輸入第%d個整數: " % (n + 1))))

print("Input to set3: ")
for n in range(0, 9):
    set_3.add(int(input("請輸入第%d個整數: " % (n + 1))))

print("Set1: " + str(set_1))
print("Set2: " + str(set_2))
print("Set3: " + str(set_3))

print("set2 is subset of set1: " + str(set_2.issubset(set_1)))
print("set3 is superset of set1: " + str(set_3.issuperset(set_1)))
# ----------------------------------------------------------------------
# 706
alphabet = set("abcdefghijklmnopqrstuvwxyz")

time = int(input("請輸入您欲測試幾筆資料: "))
for t in range(0, time):
    string_set = set(input("請輸入第%d筆資料: " % (t + 1)).lower())

    if ' ' in string_set:
        string_set.remove(' ')

    true_false = string_set == alphabet
    print("全字母句: " + str(true_false))

# ----------------------------------------------------------------------
# 707
subject_x = set()
subject_y = set()

message = "請輸入科目: "
message += "\n若要離開此部分程序請輸入'end'"

print("Enter group X's subjects: ")
while True:
    string_in = input(message)

    if string_in == 'end':
        break

    subject_x.add(string_in)

print("Enter group Y's subjects: ")
while True:
    string_in = input(message)

    if string_in == 'end':
        break

    subject_y.add(string_in)

print("Group X: " + str(sorted(subject_x)))
print("Group Y: " + str(sorted(subject_y)))

print("X組和Y組的所有科目: " + str(sorted((subject_x | subject_y))))
print("共同科目: " + str(sorted(subject_x & subject_y)))
print("Y組有但X組沒有的科目: " + str(sorted(subject_y - subject_x)))
print("X組和Y組彼此沒有的科目（不包含相同科目）" + str(sorted(subject_x ^ subject_y)))

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


# for key, value in sorted(dict_combine).items(): -> ★不是這樣寫喔!
for key, value in sorted(dict_combine.items()):
    print(key + ": " + value)

# ----------------------------------------------------------------------
# 801 - i
string = input("請輸入1個字串: ")
for i in range(0, len(string)):
    print("Index of '%s': %d" % (string[i], i))
# ----------------------------------------------------------------------
# 801 - .index()
string = input("請輸入1個字串: ")
for s in string:
    print("Index of '%s': %d" % (s, string.index(s)))
# ----------------------------------------------------------------------
# 802
string = input("請輸入字串: ")

total = 0
for s in string:
    print("ASCII code for '%s' is %d" % (s, ord(s)))
    total += ord(s)

print("所有字元的ASCII碼總合 = " + str(total))
# ----------------------------------------------------------------------
# 803
string_list = input("請輸入一個句子(至少有五個詞，以空白隔開): ").split(' ')
for string in string_list[-3:]:
    print(string, end=' ')
# ----------------------------------------------------------------------
# 805
string = input("請輸入一個長度為6的字串: ")

print("|%-10s|" % string)
print("|%s|" % string.center(10))
print("|%10s|" % string)
# ----------------------------------------------------------------------
# 806 - 不要用function的寫法
string = input("請輸入一個字串: ")
char = input("請輸入一個字元: ")

print("%s occurs %d time(s)" % (char, string.count(char)))
# ----------------------------------------------------------------------
# 806 - 用function的寫法
def compute(string, char):

    return string.count(char)


string = input("請輸入一個字串: ")
char = input("請輸入一個字元: ")

times = compute(string=string, char=char)
print("%s occurs %d time(s)" % (char, times))

# ----------------------------------------------------------------------
# 807 - 用變數來儲存
numbers = (input("請輸入一字串，字串內容為五個數字，以空白隔開: ")).split(' ')

total = 0
for number in numbers:
    total += int(number)

avg = total / len(numbers)

print("Total = %d" % total)
print("Average = %.1f" % avg)
# ----------------------------------------------------------------------
# 807 - 用修改list的方式
numbers = input("請輸入一字串，字串內容為五個數字，以空白隔開: ").split(' ')

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

total = sum(numbers)
avg = total / len(numbers)

print("Total = %d" % total)
print("Average = %.1f" % avg)
# ----------------------------------------------------------------------
# 808
ssn_list = input("請輸入社會安全碼SSN: ").split('-')

ssn = True  # 假設初步判斷格式會是正確的

for number in ssn_list:

    if not number.isdigit():  # 判斷到了不正確的格式

        ssn = False  # 就改成False

state_1 = len(ssn_list[0]) == 3
state_2 = len(ssn_list[1]) == 2
state_3 = len(ssn_list[2]) == 4

if ssn:  # 初步的判斷

    if state_1 and state_2 and state_3:  # 再更進一步的判斷
        print("Valid SSN")

    else:
        print("Invalid SSN")

else:
    print("Invalid SSN")
# ----------------------------------------------------------------------
# 809
password = input("請輸入密碼: ")

length = len(password) >= 8
eng_num_only = password.isalnum()  # ★直接一口氣看字串裡面的每一個字元
one_upper = False  # 預設是沒半個大寫，有的話才改成True

for s in password:

    if s.isupper():
        one_upper = True

if length and eng_num_only and one_upper:
    print("Valid password")

else:
    print("Invalid password")

# ----------------------------------------------------------------------
# 810

k = int(input("請輸入正整數k，代表有k筆測試資料: "))

for time in range(0, k):
    numbers = input("請輸入第%d串數字(以空白隔開): " % (time + 1)).split(' ')

    for n in range(0, len(numbers)):
        numbers[n] = float(numbers[n])

    ans = max(numbers) - min(numbers)

    print("Max = %.2f" % max(numbers))
    print("Min = %.2f" % min(numbers))
    print("Max - Min = %.2f" % ans)
    