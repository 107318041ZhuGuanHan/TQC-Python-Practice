n=eval(input())
for i in range(n):
    sn=input()
    ALL=0
    for j in range(len(sn)):
        ALL+=int(sn[j])
    print("Sum of all digits of",sn,"is",ALL)