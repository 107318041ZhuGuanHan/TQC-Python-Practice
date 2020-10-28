# ★字串.count(字元)

def compute(string_f, char_f):
    return string_f.count(char_f)  # 參考答案用迴圈在那邊慢慢算


string = input("請輸入您要檢查的長字串: ")
char = input("請輸入您要檢查的字元: ")

time = compute(string_f=string, char_f=char)

print(char + " occurs " + str(time) + " time(s)")


# ----------------------------------------------------------------------
# 寫一次參考答案

def compute(string_f, char_f):
    time_f = 0

    for s in string_f:

        if s == char_f: # 遇到指定的字元，數字就累加1
            time_f += 1

    return time_f


string = input("請輸入您要檢查的長字串: ")
char = input("請輸入您要檢查的字元: ")

time = compute(string_f=string, char_f=char)

print(str(char) + " occurs " + str(time) + " tims(s)")