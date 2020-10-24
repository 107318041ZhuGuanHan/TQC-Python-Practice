n = int(input())

for i in range(1, n + 1):
    for sp in range(n - i):
        print(" ", end='')
    for star in range(i * 2 - 1):
        print("*", end='')
    print()