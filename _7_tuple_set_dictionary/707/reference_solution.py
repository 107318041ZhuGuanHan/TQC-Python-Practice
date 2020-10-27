x = set()
y = set()
print("Enter group X's subjects:")
while True:
    enter = input()
    if enter == "end":
        break
    x.add(enter)

print("Enter group Y's subjects:")
while True:
    enter = input()
    if enter == "end":
        break
    y.add(enter)

print(sorted(x | y))
print(sorted(x & y))
print(sorted(y - x))
print(sorted(x ^ y))