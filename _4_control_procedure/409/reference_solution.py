N1=0
N2=0
Z=0
for i in range(5):
  N=int(input())
  if N==1:
    N1+=1
  if N==2:
    N2+=1
  if N!=1 and N!=2:
    Z+=1
  print("Total votes of No.1: Nami =  %d"%N1)
  print("Total votes of No.2: Chopper =  %d"%N2)
  print("Total null votes =  %d"%Z)
if N1>N2:
  print("=> No.1 Nami won the election.")
elif N1<N2: # 這邊本來還給我寫錯，我改正了
  print("=> No.2 Chopper won the election.")
else:
  print("=> No one won the election.")