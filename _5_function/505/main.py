def compute(a, x, y): # a: 字元character, x: 每列印出來的個數, y: 共有幾列

    for n in range(1, y+1): # 列的部分
        string = (a + ' ') * x # 用字串來定義 每一列 要印出來的內容 -> ★用字串來串接 的方法
        # 參考答案是寫雙重迴圈
        print(string) # 每一次的print都會自動換行，有印我要的東西出來它就會自動換了


s = input("請輸入您想要印出來的字元/字串: ") # input預設的type就是字串string，所以不用強制型轉
column = int(input("請輸入您想在每一列印出多少個字元/字串: "))
raw = int(input("請輸入您想要印出多少列: "))

compute(s, column, raw)
