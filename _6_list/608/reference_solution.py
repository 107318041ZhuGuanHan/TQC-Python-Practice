L = []
for i in range(9):
    L.append(int(input()))

max_n = max(L)
max_n_index = L.index(max_n)

print("Index of the largest number {} is: ({}, {})"
      .format(max_n, max_n_index // 3, max_n_index % 3))

min_n = min(L)
min_n_index = L.index(min_n)

print("Index of the smallest number {} is: ({}, {})"
      .format(min_n, min_n_index // 3, min_n_index % 3))