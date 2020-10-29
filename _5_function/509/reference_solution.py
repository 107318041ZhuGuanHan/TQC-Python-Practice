def compute(a, b):  # 一開始a跟b誰大誰小沒關係，如果一開始a < b，那第1次呼叫自己的時候就會顛倒過來
    if b == 0: return a
    else: return compute(b, a % b)


x, y = map(int, input().split(', '))
m, n = map(int, input().split(', '))

p, q = (x * n) + (m * y), y * n
num = compute(p, q)
print('{}/{} + {}/{} = {}/{}'.format(x, y, m, n, int(p / num), int(q / num)))