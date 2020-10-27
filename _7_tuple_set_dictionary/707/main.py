subject_x = set()
subject_y = set()

message = "請輸入科目: "
message += "\n輸入'end'以停止輸入\n"

print("Enter group X's subjects: ")
while True:  # X組的科目
    subject = input(message)

    if subject == 'end':
        break

    subject_x.add(subject)


print("Enter group Y's subjects: ")
while True:  # Y組的科目
    subject = input(message)

    if subject == 'end':
        break

    subject_y.add(subject)

print("X組: " + str(subject_x))
print("Y組: " + str(subject_y))

# ★
union_set = subject_x.union(subject_y)
# 聯集 -> 也可以寫成: subject_x | subject_y

intersection_set = subject_x.intersection(subject_y)
# 交集 -> 也可以寫成: subject_x & subject_y

difference_set = subject_y.difference(subject_x) # 誰 - 誰 就是誰前誰後
# 差集 -> 也可以寫成: subject_y - subject_x

symmetric_difference_ser = subject_x.symmetric_difference(subject_y)
# 對稱差集 -> 也可以寫成: subject_x ^ subject_y
# 就是兩集合之中獨有的項目

# sorted()把要顯示出來的給排好


print("X組 和 Y組的所有科目: " + str(sorted(union_set)))  # 聯集
print("X組 和 Y組的共同科目: " + str(sorted(intersection_set))) # 交集
print("Y組有但X組沒有的科目: " + str(sorted(difference_set))) # 差集
print("X組和Y組彼此沒有的科目(不包含相同科目): "
      + str(sorted(symmetric_difference_ser))) # 對稱差集


# ----------------------------------------------------------------------
# 練習參考答案的方式(簡單的寫法)

subject_x = set()
subject_y = set()

message = "請輸入科目: "
message += "\n要離開請輸入'end'\n"

print("Enter group X's subjects:\n")
while True:
    subject = input(message)

    if subject == 'end':
        break

    subject_x.add(subject)


print("Enter group Y's subjects:\n")
while True:
    subject = input(message)

    if subject == 'end':
        break

    subject_y.add(subject)

print("X: " + str(subject_x))
print("Y: " + str(subject_y))

print("所有科目: " + str(sorted(subject_x | subject_y)))
print("共同科目: " + str(sorted(subject_x & subject_y)))
print("Y組有但X組沒有的科目: " + str(sorted(subject_y - subject_x)))
print("X組和Y組彼此沒有的科目（不包含相同科目）: "
      + str(sorted(subject_x ^ subject_y)))