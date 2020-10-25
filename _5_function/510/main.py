def fibo(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibo(number - 1) + fibo(number - 2) # ★遞迴:在function裡面會呼叫自己 -> 需要畫樹狀圖來分析程式如何進行

number_in = int(input("請輸入一個數字n，將為您顯示前n項的費式數列: "))

print("費式數列前面1~" + str(number_in) + "項: ")

for n in range(1, number_in + 1):
    print("%d " % fibo(n), end='')

# 這方式簡單，但是不實用，因為太慢了，在求每一個費氏數時，都會發生嚴重的重覆計算，
# 也就是遞迴該行 ( FIB(N-1) + FIB(N-2) )，最差的big-o可以到2的n/2次方，
# 畫張遞迴的樹狀圖就可以知道重覆計算的數有多少了。

# ----------------------------------------------------------------------
# 非遞迴的版本
def fibo(number):
    if (number == 0) or (number == 1):
        return n

    a = 0
    print("%d " % a, end='')
    b = 1
    print("%d " % b, end='')
    for i in range(1, number):
        temp = b
        b = a + b
        a = temp
        print("%d " % b, end='')

number_in = int(input("\n請輸入一個數字n，將為您顯示前n項的費式數列: "))

fibo(number_in)

# ----------------------------------------------------------------------

# 建list然後去追前面兩項之和感覺也是一個方法 ->★若考慮運算速度，這方法屌打遞迴

number_in = int(input("\n請輸入一個數字n，將為您顯示前n項的費式數列: "))

fibs = list(range(0, number_in + 1))
fibs[0] = 0
fibs[1] = 1

for i in range(2, number_in + 1):
    fibs[i] = fibs[i-1] + fibs[i-2]

for j in range(1, number_in + 1):
    print("%d " % fibs[j], end='')

print("\n第%d項 = %d" % (number_in, fibs[number_in]))

# ----------------------------------------------------------------------
# list的另一方式(複製的)
def fibonacci(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

for i in range(0, 20):
    print(fibonacci(i), end=' ')

# ----------------------------------------------------------------------
# 以空間換取時間
table = [0] * 3
table[0] = 0
table[1] = 1

for i in range(2, 11):
    table[2] = table[0] + table[1]
    table[0] = table[1]
    table[1] = table[2]

print(table[2])

# ----------------------------------------------------------------------
# 再練習一次(遞迴)
def room(num):

    if num == 0:
        return num

    elif num == 1:
        return num

    return (room(num - 1) + room(num - 2))


number = int(input("請輸入你想列出費式數列的前面幾項: "))

print("費式數列的前1~%d項為: " % number)
for n in range(1, number + 1):
    print("%d" % room(n), end=" ")

# ----------------------------------------------------------------------
# 再練習一次(list)

def face_numbers(num):

    room = []
    room.append(0)
    room.append(1)

    for n in range(2, num + 1): # 用list來做
        room.append(room[n-1] + room[n-2])

    return room


number = int(input("請輸入你想列出費式數列的前面幾項: "))

print("費式數列的前1~%d項為: " % number)

numbers = face_numbers(number)

for number in numbers[1:]:
    print("%d " % number, end='')
