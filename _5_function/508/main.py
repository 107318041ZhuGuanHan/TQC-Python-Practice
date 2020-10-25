def compute(x, y):

    max_common_factor = 0
    for n in range(1, min(x, y) + 1): # 從1開始，一直到兩數之間較小的數為止
        if (x % n == 0) and (y % n == 0):
            max_common_factor = n  # 用1個變數來儲存可能的最大公因數即可，因為只要有更大的公因數就會一直更新
            # 其實也可以建立list，再利用max()來抓出最大公因數 -> 參考答案的思路

    return int(max_common_factor)


number_1, number_2 = eval(input("請輸入兩個數字並以半形逗點分隔: ")) # 不能直接把輸入內容用int()包起來
# input("請輸入兩個數字並以半形逗點分隔: ").split(', ') -> 這樣會變成一個str list -> 也還是不能用int()包起來
# ★一行input()要多個輸入很麻煩

result = compute(number_1, number_2)

print("最大公因數 = " + str(result))
