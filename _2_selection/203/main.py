year = int(input("請輸入西元年份，我將為您判斷是否為閏年: "))

if year % 4 == 0:
    print(str(year) + " is a leap year.(是閏年喲^^)")

else:
    print(str(year) + " is not a leap year.(不是閏年喲^_^)")