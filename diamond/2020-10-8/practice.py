height = int(input("請輸入菱形的高: "))
height_up = (height // 2) + 1
height_low = height // 2

width = int(input("請輸入菱形的寬: "))

adding_rate = (width - 1) // (height_up-1)

width_up = width
width_low = width - adding_rate

star = '*'

for i in range(1, width_up+1, adding_rate):

    line = i * star
    print("%s" % line.center(width))

for i in range(adding_rate, width_low + adding_rate, adding_rate):

    line = abs(width - i) * star
    print("%s" % line.center(width))