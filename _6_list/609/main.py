# matrix_1 = [[1, 2], [3, 4]]
# matrix_2 = [[5, 6], [7, 8]]
# matrix_3 = matrix_1 + matrix_2
# -> ★不能這樣搞，這樣會變成 matrix_3 = [[1, 2], [3, 4], [5, 6], [7, 8]]
# ★要用元素相加的方式
# 1.建3個 2*2 的矩陣 2. 可以試著把那3個 2*2 的矩陣放在同一個list裡面

matrix_1 = [[0 for column in range(0, 2)] for row in range(0, 2)]
matrix_2 = [[0 for column in range(0, 2)] for row in range(0, 2)]
matrix_3 = [[0 for column in range(0, 2)] for row in range(0, 2)]

print("Enter matrix 1: ")  # 矩陣1的輸入
for row in range(0, 2):
    for column in range(0, 2):
        matrix_1[row][column] = int(input("[%d, %d]: "
                                          % (row + 1, column + 1)))

print("Enter matrix 2: ")  # 矩陣2的輸入
for row in range(0, 2):
    for column in range(0, 2):
        matrix_2[row][column] = int(input("[%d, %d]: "
                                          % (row + 1, column + 1)))

for row in range(0, 2):  # 矩陣3的元素計算
    for column in range(0, 2):
        matrix_3[row][column] = matrix_1[row][column] + matrix_2[row][
            column]

print("Matrix 1: ")
print("**%d %d**" % (matrix_1[0][0], matrix_1[0][1]))
print("**%d %d**" % (matrix_1[1][0], matrix_1[1][1]))
print("Matrix 2: ")
print("**%d %d**" % (matrix_2[0][0], matrix_2[0][1]))
print("**%d %d**" % (matrix_2[1][0], matrix_2[1][1]))
print("Sum of 2 matrices:")
print("**%d %d**" % (matrix_3[0][0], matrix_3[0][1]))
print("**%d %d**" % (matrix_3[1][0], matrix_3[1][1]))



# 參考答案在print這邊就是寫3個雙重for迴圈，可以不用那麼麻煩用格式化輸出
# ----------------------------------------------------------------------
# 自己練習參考答案的思路

matrix_1 = [[0 for column in range(0, 2)] for row in range(0, 2)]
matrix_2 = [[0 for column in range(0, 2)] for row in range(0, 2)]

print("Enter matrix 1: ")
for row in range(0, 2):
    for column in range(0, 2):
        matrix_1[row][column] = int(input("[%d, %d]: "
                                          % (row + 1, column + 1)))

print("Enter matrix 2: ")
for row in range(0, 2):
    for column in range(0, 2):
        matrix_2[row][column] = int(input("[%d, %d]: "
                                         % (row+1, column+1)))

print("Matrix 1: ")
for row in range(0, 2):
    print("**", end='')

    for column in range(0, 2):
        print(matrix_1[row][column], end=' ')

    print("**")

print("Matrix 2: ")
for row in range(0, 2):
    print("**", end='')

    for column in range(0, 2):
        print(matrix_2[row][column], end=' ')

    print("**")

print("Sum of 2 matrices: ")
for row in range(0, 2):
    print("**", end='')

    for column in range(0, 2):
        print((matrix_1[row][column] + matrix_2[row][column]), end=' ')

    print("**")
