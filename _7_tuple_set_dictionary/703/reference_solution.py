L1 = []
while True:
    N = input()
    if N == "end":
        break
    L1.append(N)
T1 = tuple(L1)

print(T1)
print(T1[0:3])
print(T1[-3:])