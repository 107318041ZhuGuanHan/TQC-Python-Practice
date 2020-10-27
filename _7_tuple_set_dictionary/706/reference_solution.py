k=int(input())
str1 = set('abcdefghijklmnopqrstuvwxyz')
for i in range(k):
  str2=input()
  str2=set(str2.lower()) #將輸入的字串轉成小寫，並設成集合
  str2.discard(" ") #如果集合中，有空格，那麼就刪掉，以免影響判斷
  print(str1==str2) #將輸入的字串，與a~z做比對