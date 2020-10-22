import math
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
Distance=(x1-x2)**2+(y1-y2)**2
print("(" , x1 , ",", y1 , ")")
print("(" , x2 , ",", y2 , ")")
print("Distance = %.4f"%(math.sqrt(Distance)))