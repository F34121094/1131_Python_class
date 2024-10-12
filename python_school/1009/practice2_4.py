num = eval(input("請輸入全班的總人數:"))
max = 0
gg = 0
sg = 0
total = 0
for i in range(num):
    g= int(input(f"第{i+1}個同學:"))
    if g > max: max = g
    if g >= 900: gg += 1
    if g <= 700 and g >= 600: sg += 1
    total += g
print("最高:", max)
print("900分以上:",gg)
print("600~700:",sg)
print("平均",format(total/num,".2f"))