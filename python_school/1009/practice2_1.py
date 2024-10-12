max = 0
min = 100
fn = 0
for i in range(10):
    g = eval(input(f"第{i+1}位同學的成績:"))
    if g > max: max = g
    if g < min: min = g
    if g < 60 : fn += 1
print("最高分:", max)
print("最低分:", min)
print("不及格人數:",fn)
