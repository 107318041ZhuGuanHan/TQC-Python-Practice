def compute(a, b):
    ALL = 0
    for i in range(a, b + 1):
        ALL += i
    return ALL


a = eval(input())
b = eval(input())
print(compute(a, b))