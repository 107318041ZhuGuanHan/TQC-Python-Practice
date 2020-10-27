L = set()
while True:
    N = eval(input())
    if N == -9999:
        break
    L.add(N)

print('Length:', len(L))
print('Max:', max(L))
print('Min:', min(L))
print('Sum:', sum(L))