# 1.for迴圈公差

print("及將為您算出1~n中，所有5的倍數的總和")
number = int(input("請輸入一個正整數: "))

max_five = number - number % 5 # 把number變成1~number之間最大的5的倍數，
# 賦值給max_five，為了後面的for迴圈

total = 0 # 給定初始值頗重要的

for n in range(5, number+1, 5): # 從5開始，修改後的number為止(含)
    total += n

print(total)




# ----------------------------------------------------------------------
# 用判斷的方式

print("及將為您算出1~n中，所有5的倍數的總和")
number = int(input("請輸入一個正整數: "))

total = 0

for n in range(1, number+1):
    if n % 5 == 0: # 碰到5的倍數的時候才進行計算
        total += n

print(total)
