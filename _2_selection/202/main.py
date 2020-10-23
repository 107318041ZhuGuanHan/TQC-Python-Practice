x = int(input("請輸入一個正整數: "))

if x % 5 == 0:

    if x % 3 == 0: # 上面判斷x是否為5的倍數，這裡再進一步判斷是否為3的倍數
        print(str(x) + " is a multiple of 3 and 5.")
    else:
        print(str(x) + " is a multiple of 5.")

elif x % 3 == 0: # 最上面判斷x是否為5的倍數為否，在這裡已不需要再判斷一次了，不然就不會在這個elif了
    print(str(x) + " is a multiple of 3.")

else:
    print(str(x) + " is not a multiple of 3 or 5.")

# ----------------------------------------------------------------------

if (x % 5 == 0) and (x % 3 == 0):
    print(str(x) + " is a multiple of 3 and 5.")

elif x % 5 == 0:
    print(str(x) + " is a multiple of 5.")

elif x % 3 == 0:
    print(str(x) + " is a multiple of 3.")

else:
    print(str(x) + " is not a multiple of 3 or 5.")