sn = 0
bn = 0
g = eval(input(f"第1個數:"))
max = g
min = g
if g < 0: sn += 1
if g > 10: bn += 1

for i in range(2,11):
    g = eval(input(f"第{i}個數:"))
    if g > max: max = g
    if g < min: min = g
    if g < 0 : sn += 1
    if g > 10: bn += 1
print("最高:", max)
print("最低:", min)
print("<0 個數:",sn," ,>10 個數:",bn)
