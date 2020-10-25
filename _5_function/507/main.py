def compute(number):

    prime = True  # 預設它是質數

    # 參考答案與我差不多思路，不過它是切成 <= 1 與 > 2
    if number > 2: # 是大於2的數才繼續進行計算

        for n in range(2, number):  # 從第1個質數(2)開始，一直到輸入的數的前一個。
            # range忘記打，就會很麻煩 -> for n in (2, number) 會變成只有 2 跟 number

            if number % n == 0:  # 抓到這個數的其他因數時
                prime = False  # 把質數判斷改為否

        if prime:
            print("Prime")
        else:
            print("Not Prime")

    elif number == 2:  # 2是質數
        print("Prime")

    elif number == 1:  # 1不是質數
        print("Not Prime")

    elif number <= 0:  # 0或負數都不會是質數
        print("Not Prime")


while True:

    number_in = int(input("請輸入一個數字，我將為您判斷此數字是否為質數: "))

    compute(number_in)
