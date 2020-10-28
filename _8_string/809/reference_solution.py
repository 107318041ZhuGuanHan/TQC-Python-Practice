PW = input()
b=0
for i in range(len(PW)):
  if PW[i].isupper():
    b=1
if b==1 and len(PW)>=8 and PW.isalnum():
  print("Valid password")
else:
  print("Invalid password")