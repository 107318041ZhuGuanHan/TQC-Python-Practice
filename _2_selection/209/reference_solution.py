import math
x=eval(input())
y=eval(input())
Distance=(x-5)**2+(y-6)**2
if math.sqrt(Distance)<=15:
  print("Inside")
else:
  print("Outside")