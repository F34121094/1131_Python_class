n = eval(input("n:"))
time = 0
ans = 0
while 1:
    n -= 1
    time += 1
    ans += 1
    if time == 5:
        time = 0
        n += 1
    if n == 0: break
print(ans)