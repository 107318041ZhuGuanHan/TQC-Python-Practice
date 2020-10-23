number_1 = int(input("請輸入第一個整數: "))

number_2 = int(input("請輸入第二個整數: "))

math_processing = input("請輸入算術運算子 (+, -, *, /, //, %): ")

if math_processing == "+":
    print(number_1 + number_2)

elif math_processing == "-":
    print(number_1 - number_2)

elif math_processing == "*":
    print(number_1 * number_2)

elif math_processing == "/":
    print(number_1 / number_2)

elif math_processing == "//":
    print(number_1 // number_2)

elif math_processing == "%":
    print(number_1 % number_2)