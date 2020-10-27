N = 0
L = []
while (N != -9999):
    N = eval(input())
    if N != -9999:
        L.append(N)

T = tuple(L)
print(T)
print("Length:", len(T))
print("Max:", max(T))
print("Min:", min(T))
print("Sum:", sum(T))