year=eval(input(""))
if (year%4)==0 and (year%100)!=0:
    print('%d is a leap year.'%(year))
elif (year%400)==0: # 這絕對有問題，1900年明明也是閏年，但輸出卻不是
    print('%d is a leap year.'%(year))
else:
    print('%d is not a leap year.'%(year))