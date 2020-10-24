# 思路: 1.用list再抓長度 2.設置變數來計算

# 思路1

number_odd = []
number_even = []

for n in range(1, 11):
    number = int(input("請輸入第 %d 個數字:" % n))

    if number % 2 == 0:
        number_even.append(number)

    else:
        number_odd.append(number)

print("Even numbers: " + str(len(number_even)))
print("Odd numbers: " + str(len(number_odd)))


# 思路2

number_odd = 0
number_even = 0

for n in range(1, 11):
    number = int(input("請輸入第 %d 個數字:" % n))

    if number % 2 == 0:
        number_even += 1

    else:
        number_odd += 1

print("Even numbers: " + str(number_even))
print("Odd numbers: " + str(number_odd))
