L = []
for i in range(10):
    L.append(eval(input()))

most_num = 0
for i in range(10):
    if L.count(L[i]) > most_num:
        most_num = L.count(L[i])
        M = L[i]
print(M)
print(most_num)