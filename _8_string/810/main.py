# ★一次就要最大最小值，而且輸入的數值沒有限定範圍 -> 不適合用變數先賦值初始值，再去儲存極值的方式
# ★感覺先把list裡面的元素全部轉成float再去取 max(list)-min(list) 比較好


k = int(input("請輸入預測式的資料筆數: "))

for time in range(0, k):

    number_list = input("請輸入第%d筆測試資料: " % (time+1)).split(' ')
    # ★ 只有輸出印出來的話，可以寫在迴圈裏面
    # ★ 如果是不同的物件如 list_1、list_2就不能在迴圈裡面了 ->因為是不同物件

    for i in range(0, len(number_list)):
        number_list[i] = float(number_list[i])  # list可以直接改
        # 參考答案是直接再宣告一個新的list，然後再用append(float(number_list[i]))
        # 如果是這樣就會不需要i了，可以直接抓number_list的元素

    ans = max(number_list) - min(number_list)

    print("Max: %.2f" % max(number_list))
    print("Min: %.2f" % min(number_list))
    print("Max - Min = %.2f" % ans)
