def compute(x, y):
    for i in range(1, little + 1):
        if x % i == 0 and y % i == 0:
            L1.append(i)
    return max(L1)


L1 = []
x, y = eval(input())
little = min(x, y)
print(compute(x, y))