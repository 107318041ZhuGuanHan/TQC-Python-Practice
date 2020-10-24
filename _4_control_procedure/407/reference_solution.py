Y=0
while(Y!=-9999):
  Y=eval(input())
  if Y!=-9999:
    if Y%4==0 and Y%100!=0:
      print(Y,"is a leap year.")
    elif Y%400==0:
      print(Y,"is a leap year.")
    else:
      print(Y,"is not a leap year.")