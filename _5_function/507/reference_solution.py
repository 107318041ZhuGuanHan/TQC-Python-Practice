def compute(x):
    if x <= 1:
        return 'Not Prime'
    for i in range(2, x):
        if x % i == 0:  # 感覺輸入2就會跳說它不是質數
            return 'Not Prime'
        else:
            return 'Prime'


x = eval(input())
# 根本沒有call function