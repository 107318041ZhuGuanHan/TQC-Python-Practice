SSN = list(input().split("-"))
b=0
for i in range(len(SSN)):
  if SSN[i].isdigit()==False:
    print("Invalid SSN")
    b+=1
    break
if b==0:
  print("Valid SSN")