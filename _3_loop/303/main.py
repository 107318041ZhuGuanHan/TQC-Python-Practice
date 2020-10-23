number = int(input("請輸入一個正整數: "))



for n_out in range(1, number + 1):

    message = "" # 需要在這個地方清空

    for n_in in range(1, n_out + 1):
        print("%4d" % (n_out * n_in), end='')
        # ★ print(...end='') 表示輸出(印出來)不要自動換行

    print("") # 印完一個長條就換行繼續供上面繼續印



# ----------------------------------------------------------------------
# 自己一開始的想法，但是寫不出4格的那個空格欄位

number = int(input("請輸入一個正整數: "))



for n_out in range(1, number + 1):

    message = "" # 需要在這個地方清空

    for n_in in range(1, n_out + 1):
        n = (str(n_out * n_in))
        message += " " + n

    print(message)