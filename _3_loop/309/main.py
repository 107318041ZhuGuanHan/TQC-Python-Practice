money = float(input("請輸入你想存入的金額: "))
benefit_rate = float(input("請輸入收益率(%): "))
month = int(input("請輸入你想存幾個月: "))

print("Month  Amount")

for mon in range(1, month+1):
    money = money + money * benefit_rate / 1200 # %數 / 100 -> 1年12個月 -> %數 / 1200
    # 上面也可以打成: money += money * benefit_rate / 1200
    print("%3d    %.2f" % (mon, money))
