d1 = {}
d2 = {}
print('Create dict1:')
while True:
    Key1 = input('Key: ')
    if Key1 == "end":
        break
    d1[Key1] = input('Value: ')

print('Create dict2:')
while True:
    Key2 = input('Key: ')
    if Key2 == "end":
        break
    d2[Key2] = input('Value: ')

d1.update(d2)
for i in sorted(d1.keys()):
    print(i, ": ", d1[i], sep="")