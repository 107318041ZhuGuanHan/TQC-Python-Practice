L = []
S = 0

for i in range(12):
    L.append(int(input()))

for j in range(12):
    if j % 2 == 0:
        S += L[j]
    print("{:3d}".format(L[j]), end='')
    if j % 3 == 2:
        print()

print(S)