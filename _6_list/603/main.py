numbers = []
for i in range(1, 11):
    number_in = int(input("請輸入第%d個數字: " % i))
    numbers.append(number_in)


numbers.sort(reverse=True) # sort(): 將元素由小到大排序，reverse=True表示順序顛倒(變成最大排到最小)

print("您輸入的數字中，最大的3個數字由大到小依序為: ")
for number in numbers[:3]: # 從最前面開始，一直到index3(第4個)以前(前3個不包含第4個) -> 最大的3個數字由大到小印出來
    print("%d " % number, end='')

# 與參考答案做法差不多，只有最後print的方式不太一樣而已
