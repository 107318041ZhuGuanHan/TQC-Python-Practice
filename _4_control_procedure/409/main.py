# 思路:for迴圈5次，裡面要叫使用者輸入，計算票數，印出來

v_nami = 0
v_chopper = 0
v_none = 0
#宣告初始值

for v in range(1, 6):
    voting = input("請輸入你要投給幾號候選人: ")

    if voting == '1':
        v_nami += 1  # 計算票數

    elif voting == '2':
        v_chopper += 1

    else:
        v_none += 1

    print("Total votes of No.1: Nami =  " + str(v_nami))
    print("Total votes of No.2: Chopper =  " + str(v_chopper))
    print("Total null votes =  " + str(v_none))

if v_nami > v_chopper:  # 不是Nami贏
    print("No.1 Nami won the election.")

elif v_chopper > v_nami:  # 就是Chopper贏
    print("No.2 Chopper won the election.")

elif v_nami == v_chopper:  # 要不然其實就是平手
    print("No one won the election.")
