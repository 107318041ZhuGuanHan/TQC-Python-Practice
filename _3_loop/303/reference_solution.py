a=eval(input())
c=0
for i in range(1,a+1):
  for j in range(1,i+1):
    c=i*j
    print("%4d"%(c),end='')
  print()