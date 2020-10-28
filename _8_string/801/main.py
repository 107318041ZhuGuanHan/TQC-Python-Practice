# 1.用迴圈裡面的i 2.用.index()

# ----------------------------------------------------------------------
# 1. -> 跟參考答案差不多

string = input("請輸入一個字串: ")

for i in range(0, len(string)):
    print("Index of '%s': %d" % (string[i], i))

# ----------------------------------------------------------------------
# 2.

string = input("請輸入一個字串: ")

for s in string:
    print("Index of '%s': %d" % (s, string.index(s)))
    # ★index()使用格式: list / string .index(裡面的元素)
