"""# 在迴圈中要判斷它是誰的倍數
# 用多個if的方式，遇到公倍數用set刪掉(因為重複了)， -> 不行
# 要不然就是使用 if elif else的特性，公倍數在前面被抓走即可

number_1 = int(input("輸入第一個正整數(最小值): "))
number_2 = int(input("輸入第二個正整數(最大值): "))

numbers = []
total = 0 # 在這裡沒用到，在下面會用到

for n in range(number_1, number_2+1):

    if n % 4 == 0:
        numbers.append(n)

    if n % 9 == 0:
        numbers.append(n)

# ★ set不能接.sort()，要list才能接
no_repeat_numbers_set = set(numbers) # 把 重複的數字(公倍數) 剔除，剔除後順序會亂掉，才能用set剔除重複的數字(公倍數) 因為
no_repeat_numbers_list = list(no_repeat_numbers_set).sort() # 需要先把set轉回list再把順序排好
# ★一下子要set一下子要sort是完全不行的
# 這裡太天真了做不到

end_n = 0

print("所有倍數如下: ")

for number in no_repeat_numbers_list:

    print("%-4d" % number, end='')
    end_n += 1 # 用來計算換行的時機

    if end_n == 10: # 要換行了
        end_n = 0 # 換行時要歸零(reset)
        print("")

print("\n倍數個數: " + str(len(no_repeat_numbers_list)))
print("倍數總和: " + str(sum(no_repeat_numbers_list)))

"""
# ----------------------------------------------------------------------
# ★這邊的寫法比較好

number_1 = int(input("輸入第一個正整數(最小值): "))
number_2 = int(input("輸入第二個正整數(最大值): "))

numbers = []
total = 0

for n in range(number_1, number_2+1):

    if n % 4 == 0: # ★運用if elif的結構特性可以處理掉公倍數(重複)的問題。之後甚至可以把最上面的if改成是否為公倍數，就很好處理了。
        total += n # 參考答案用 or 的方式來判斷
        numbers.append(n)

    elif n % 9 == 0:
        total += n
        numbers.append(n)

end_n = 0 # 用來判斷換行

for number in numbers:

    print("%-4d" % number, end='')
    end_n += 1

    if end_n == 10:
        end_n = 0
        print("")

print("\n倍數個數: " + str(len(numbers)))
print("倍數總和: " + str(total))
print("倍數總和(list): " + str(sum(numbers)))