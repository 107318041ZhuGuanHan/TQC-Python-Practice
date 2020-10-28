# ★使用function ord() ->ex.  ord('a') = 65

string = input("請輸入一個字串: ")

total_value = 0

for s in string:
    print("ASCII code for '%s' is %d" % (s, ord(s)))
    total_value += ord(s)

print("Sum of ASCII code = " + str(total_value))