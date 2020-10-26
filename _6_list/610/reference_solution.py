L = []
for w in range(1, 4 + 1):
    print("Week %d:" % w)
    for D in range(1, 3 + 1):
        x = eval(input("Day %d:" % D))
        L.append(x)

A = sum(L) / len(L)
print("Average: %.2f" % A)
print("Highest:", max(L))
print("Lowest:", min(L))