N = ["1st", "2nd", "3rd"] # 先建立字串的list等等拿來print出來
L1 = [[0 for j in range(5)] for i in range(3)] # 列表解析裡面還有列表解析，初始值都給0
for i in range(3):
    print("The {} student:".format(N[i]))
    for j in range(5):
        L1[i][j] = int(input()) # 有list跟處使值以後，就可以不用花費心思來建立list，可以直接輸入分數來改裡面的元素

for i in range(3):
    print("Student %d" % (i + 1))
    print("#Sum %d" % (sum(L1[i])))
    print("#Average %.2f" % (sum(L1[i]) / 5))