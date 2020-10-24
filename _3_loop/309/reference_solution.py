money = eval(input())
SS = eval(input())
month = eval(input())

print('%s \t  %s' % ('Month', 'Amount'))
for i in range(month):
    money = money + (money * SS / 1200)
    print('%3d \t %.2f' % (i + 1, money))