numbers = []

for i in range(1, 13): # 讓user輸入12個數字

    number_in = int(input("請輸入第%d個數字: " % i))
    numbers.append(number_in)


ans = 0
for n in range(0, len(numbers), 2): # 從number[0]開始，一直到number的最後一項，n每次+2
    ans += numbers[n]               # list的index: 0 ~ len(numbers)-1
    # 計算index為偶數的元素總和
    # 參考答案是印出每個元素跟加總合在一個迴圈，這邊是分開


end = 0 # 拿來判斷換行(因為下面的迴圈沒有index可以用)
for number in numbers:
    print("%3d" % number, end='')
    end += 1
    if end % 3 == 0: # 每當end為3的倍數時，換行一次 -> 印出3個就要一次換行
        print("")

print("12個數字中，索引為偶數的數字相加總合 = " + str(ans))