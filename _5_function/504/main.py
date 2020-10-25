def compute(a, b):
    result = a ** b
    return int(result)


number_1 = int(input("請輸入底數: "))
number_2 = int(input("請輸入指數(次方): "))

number_result = compute(number_1, number_2)

print("%d 的 %d 次方 = %d" % (number_1, number_2, number_result))
