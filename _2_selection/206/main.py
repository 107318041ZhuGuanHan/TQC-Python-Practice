number = int(input("請輸入一個分數(整數)，我將為您判斷等級: "))

if number >= 80: # 這邊如果分數超過100就還是會輸出A，參考答案的雖不會但是它下面的判斷都沒善用if elif else結構的功能
    print("A")

elif number >= 70:
    print("B")

elif number >= 60:
    print("C")

elif number <= 59:
    print("F")