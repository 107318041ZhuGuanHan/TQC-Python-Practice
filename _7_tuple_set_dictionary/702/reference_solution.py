N = 0
N2 = 0
L1, L2 = [], []
print('Create tuple1:')
while (N != -9999):
    N = eval(input())
    if N != -9999:
        L1.append(N)
T1 = tuple(L1)

print('Create tuple2:')
while (N2 != -9999):
    N2 = eval(input())
    if N2 != -9999:
        L2.append(N2)

T2 = tuple(L2)

print('Combined tuple before sorting:', T1 + T2)
print('Combined list after sorting:', sorted(T1 + T2))