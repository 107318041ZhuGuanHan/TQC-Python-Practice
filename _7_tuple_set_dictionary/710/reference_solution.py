d1 = {}
while True:
    K = input("Key: ")
    if K == "end":
        break
    d1[K] = input("Value: ")

sc = input("Search key: ")
print(sc in d1.keys())