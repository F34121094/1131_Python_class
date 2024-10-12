i = 0
s_max = 0
s_fail = 0
while i < 10:
    s = eval(input(f"請輸入第 {i+1} 個同學的成績:"))
    if s < 0 or s > 100:
        print("輸入錯誤!!")
        continue
    if i == 0 or s > s_max: s_max = s
    if s < 60 : s_fail += 1
    i += 1
print(f"全班的最高分是 : {s_max}")
print(f"不及格的人數是 : {s_fail}")