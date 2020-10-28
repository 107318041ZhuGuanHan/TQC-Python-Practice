n=0
while(n<1 or n>100):
  n=int(input())
for i in range(n):
    line=input().split(' ') #先將所有數字分割成串列
    data=[] #再新增1個串列，用eval將原串列中的字串轉為文字
    for j in range(len(line)):
      data.append(eval(line[j]))
    print("{:.2f}".format(max(data)-min(data)))