CM=eval(input())
while(CM!=-9999):
  KG=eval(input())
  M=CM/100
  BMI=KG/M**2
  print("BMI: {:.2f}".format(BMI))
  if BMI<18.5:
    print("State: under weight")
  if 18.5<=BMI<25:
    print("State: normal")
  if 25.0<=BMI<30:
    print("State: over weight")
  if 30<=BMI:
    print("State: fat")
  CM=eval(input())