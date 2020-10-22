number = int(input("請輸入一個正整數，我將告訴你該數字是奇數或偶數: "))

if number % 2 == 0:
    print("數字 " + str(number) + " 是偶數(even)。")
    print(str(str(number) + " is an even number.\n"))

else:
    print("數字 " + str(number) + " 是奇數(odd)。")
    print(str(number) + " is not an even number.\n")
