set_1 = set() # set的宣告方式
set_2 = set() # ★雖然跟字典一樣都是被大括號{}包著，但是宣告的「空物件」的方式大不相同
set_3 = set()

message = "請輸入整數: "

print("Input to set1:")
for i in range(0, 5):
    number = int(input(message))
    set_1.add(number)

print("Input to set2:")
for i in range(0, 3):
    number = int(input(message))
    set_2.add(number)

print("Input to set3:")
for i in range(0, 9):
    number = int(input(message))
    set_3.add(number)


state_2_in_1 = set_2.issubset(set_1)
# ★用issubset()來判斷set_2是否為set_1的子集合
# 後面要被拿來判斷的物件擺前面，比較的基準擺後面

state_3_super_1 = set_3.issuperset(set_1)
# ★用issuperset()來判斷set_3是否為set_1的子集合
# 後面要被拿來判斷的物件擺前面，比較的基準擺後面

print("Set1: " + str(set_1))
print("Set2: " + str(set_2))
print("Set3: " + str(set_3))

print("Set2 is subset of Set1: " + str(state_2_in_1))
print("Set3 is superset of Set1: " + str(state_3_super_1))
# 參考答案後面在print出來時候的判斷其時感覺有點多餘


