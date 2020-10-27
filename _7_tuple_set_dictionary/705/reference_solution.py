S1, S2, S3 = set(), set(), set()
print('Input to set1:')
for i in range(5):
    S1.add(eval(input()))

print('Input to set2:')
for i in range(3):
    S2.add(eval(input()))

print('Input to set3:')
for i in range(9):
    S3.add(eval(input()))

print('set2 is subset of set1: ', end="")
if S2.issubset(S1) == True:
    print("True")
else:
    print("False")

print('set3 is superset of set1: ', end="")
if S3.issuperset(S1) == True:
    print("True")
else:
    print("False")