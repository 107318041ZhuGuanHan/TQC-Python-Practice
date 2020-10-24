A=0
B=0
for i in range(10):
  N=int(input())
  if N%2==0:
    A+=1
  if N%2!=0:
    B+=1
print("Even numbers: %d"%A)
print("Odd numbers: %d"%B)