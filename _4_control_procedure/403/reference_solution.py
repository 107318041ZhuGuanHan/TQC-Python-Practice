a=eval(input())
b=eval(input())
c=0
ALL=0
for i in range(a,b+1):
    if i%4==0 or i%9==0:
        c+=1
        ALL+=i
        print("%-4d"%i,end="")
        if c%10==0:
            print()
print("\n%d"%c)
print(ALL)