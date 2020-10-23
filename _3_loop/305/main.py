number = input("請輸入一個多位數的正整數，我將為您將此整數反轉:")

for n in range(1, len(number)+1):
    print(str(number[-n]), end='')
# 上面幾乎等於參考答案

# a = "123456"
# b = sorted(a, reverse=True) ★ 在這裡會變成顛倒過來的list
# print(b)