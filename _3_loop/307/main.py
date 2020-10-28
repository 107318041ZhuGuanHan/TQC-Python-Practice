number = int(input("請輸入一個正整數n，我將為您顯示出 n * n 的乘法表: "))

for n_right in range(1, number+1): # 直的下去的(顯示右邊的數字)
    for n_left in range(1, number+1): # 橫的往右邊過去的(顯示左邊的數字)
        print("%-2d* %-2d= %-4d "
              % (n_left, n_right, n_left * n_right), # 注意格式化的輸出要求
              end='') # 在這裡都沒有換行
    print("") # ，所以這個迴圈外面要有換行