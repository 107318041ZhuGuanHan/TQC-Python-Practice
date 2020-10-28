L=input()
S=0
for i in range(len(L)):
  print("ASCII code for '%s' is "%(L[i]),end='')
  print(ord(L[i]))
  S+=ord(L[i])
print(S)