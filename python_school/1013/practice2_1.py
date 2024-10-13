score = [[0 for _ in range(2)]for _ in range(5)]
c_max = 0
e_fail = 0
for i in range(5):
    print("請輸入第",i+1,"位同學的")
    for j in range(2):
        if j == 0:
            c = int(input("國文成績:"))
            score[i][j] = c
            if i == 0 or score[i][j] > c_max: c_max= score[i][j]
        else:
            e = int(input("英文成績:"))
            score[i][j] = e
            if score[i][j] < 60 : e_fail += 1
print()
print("全班國文分數最高為:",c_max)
print("全班英文不及格人數:",e_fail)
