up90 = 0
c_high = 0
m_low = 0
e_fail = 0
total = 0
for i in range(10):
    u = 0
    print(f"請輸入第 {i+1} 位同學的")
    for j in range(3):
        if j == 0:
            s = eval(input("國文成績:"))
            if s >= 90: u += 1
            if i == 0 or s > c_high: c_high = s
            total += s
        elif j == 1:
            s = eval(input("英文成績:"))
            if s >= 90: u += 1
            if s < 60: e_fail += 1
            total += s
        else:
            s = eval(input("數學成績:"))
            if s >= 90: u += 1
            if i == 0 or s < m_low: m_low = s
            total += s
    if u == 3: up90 += 1
av = total / 30
print()
print(f"三科皆90以上的人數{up90}")
print(f"全班國文最高分{c_high}")
print(f"全班數學最低分{m_low}")
print(f"英文不及格人數{e_fail}")
print(f"平均{av}")



