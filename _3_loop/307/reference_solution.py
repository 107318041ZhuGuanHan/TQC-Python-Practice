N=int(input())
for i in range(1,N+1):
  for j in range(1,N+1):
    print('{} * {} = {:<4}'.format(j,i,(j*i)),end='')
  print()