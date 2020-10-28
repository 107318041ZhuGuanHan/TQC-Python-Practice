S = list(input().split(" "))
ALL = 0
for i in range(len(S)):
    ALL += int(S[i])

print("Total =", ALL)
print("Average =", ALL / len(S))