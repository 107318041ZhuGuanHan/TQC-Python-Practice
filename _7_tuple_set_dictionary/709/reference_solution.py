color_dict={}
while True:
  K=input("Key: ")
  if K=="end":
    break
  color_dict[K]=input("Value: ")
for i in sorted(color_dict.keys()):
  print(i,": ",color_dict[i],sep="")