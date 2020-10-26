def compute(num_list):

    for n in range(0, len(num_list)):

        for number in num_list[n]:
            print("%4d" % number, end='')

        print("")  # 上面印完一整列，就換行


row = int(input("請輸入欲建立的list有多少列(row): "))

column = int(input("請輸入欲建立的list有多少行(column): "))


numbers = []  # 宣告1維的空list


for r in range(0, row):
    numbers.append([])  # ★每次在裡面增加一個空list(直的下去) -> 把一維list變成二維list ->
                        # 也可以 列表解析裡面建立list / 列表解析裡面還有列表解析
    for c in range(0, column):  # 在剛剛增加的空list裡面開始加入元素(橫的過去)
        numbers[r].append(c-r)

compute(num_list=numbers)



# 參考答案是直接不使用list，給我直接用變數來處理
# ----------------------------------------------------------------------

def compute(row, col):

    for r in range(0, row):

        for c in range(0, col):
            print("%4d" % (c-r), end='')

        print("")



rows = int(input("請輸入欲建立的list有多少列(row): "))
cols = int(input("請輸入欲建立的list有多少行(column): "))

compute(row=rows, col=cols)



# 列表解析裡面建立list
# ----------------------------------------------------------------------
numbers = [list(range(1, 6)) for i in range(1, 11)]
print(numbers)


# 列表解析裡面還有列表解析
# ----------------------------------------------------------------------
numbers = [[0 for j in range(0, 5)] for i in range(0, 10)] # 設定0為初始值
print(numbers)

# 列表解析裡面建立list 來做做看這一題 -> 不行沒有一般式
# ----------------------------------------------------------------------
numbers = []

# ★列表解析裡面還有列表解析 來做做看
# ----------------------------------------------------------------------
row = int(input("請輸入欲建立的list有多少列(row): "))

column = int(input("請輸入欲建立的list有多少行(column): "))

numbers = [[c-r for c in range(0, column)] for r in range(0, row)]
# print(numbers) 想看它是甚麼就可以print出來

for r in range(0, len(numbers)):

    for number in numbers[r]:
        print("%4d" %number, end='')

    print("") # 換行