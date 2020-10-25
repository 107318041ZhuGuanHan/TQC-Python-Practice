def compute(a, x, y):
    for i in range(y):
        for i in range(x):
            print(a, end=" ")
        print()


a = input()
x = eval(input())
y = eval(input())

compute(a, x, y)