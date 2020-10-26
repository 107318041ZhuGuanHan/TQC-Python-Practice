# 1.先建一個list，之後慢慢加入空list 2.先建一個[[], [], []] 都可以

grades = []

for student in range(1, 4): # 從第1位學生~第3位學生
    grades.append([])

    if student == 1:
        print("The 1st student: ")

    elif student == 2:
        print("The 2nd student: ")

    elif student >= 3:
        print("The 3rd student: ")

    elif student >= 4: # 所以這裡不會用到，但日後較容易擴充
        print("The %dth student: " % student)

    for s in range(1, 6):
        score = int(input("請輸入第%d個分數: " % s))
        grades[student-1].append(score) # 因為student是從1開始，到3結束，
        # 而index需要從0開始，顧index值需要 -1

for g in range(0, len(grades)): #從0開始，一直到len(grades)-1結束
    print("Student %d" % (g+1))

    total_score = sum(grades[g])
    print("# Sum = " + str(total_score))

    mean_score = total_score / len(grades[g])
    print("# Average = %.2f" % mean_score)




# ★參考答案有用到列表解析裡面還有列表解析(設定初始值為0)
# ----------------------------------------------------------------------
# 自己練習參考答案的思路

students = ['1st', '2nd', '3rd']
grades = [[0 for score in range(0, 5)] for student in range(0, 3)]

for student in range(0, 3):
    print("The %s student: " % (students[student])) # 這邊變數建議不要用帶向不然很容易錯誤
    for score in range(0, 5):
        grades[student][score] = int(input("請輸入第%d個分數" % (score+1)))
        # 最後面要 +1 顯示出來才會正常，因為index與常理差1

for g in range(0, len(grades)):
    print("Student %d" % (g+1))

    total_score = sum(grades[g])
    print("# Sum = " + str(total_score))

    mean_score = total_score / len(grades[g])
    print("# Average = %.2f" % mean_score)