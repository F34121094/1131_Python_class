gap1 = 0
gap2 = 0
for i in range(5):
    g = eval(input(f"第 {i+1} 個數:"))
    if g >= 1 and g <= 30: gap1 += 1
    if g >= 10 and g <= 60: gap2 += 1
print(f"1~30:{gap1}, 10~60:{gap2}")