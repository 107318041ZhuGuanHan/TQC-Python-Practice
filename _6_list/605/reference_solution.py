L = []
for s in range(10):
    x = eval(input())
    L.append(x)

S = sum(L) - max(L) - min(L)
print(S)
print("%.2f" % (S / (10 - 2)))