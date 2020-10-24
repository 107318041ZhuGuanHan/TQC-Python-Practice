L=[]
while True:
  n=eval(input())
  if n==9999:
      break
  L.append(n)
print(min(L))