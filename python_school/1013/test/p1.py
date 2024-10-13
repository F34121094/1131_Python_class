def f(n):
    if n == 1:return 12
    elif n == 2: return 35
    else: return f(n-2)*2 + f(n-1)

n = eval(input("n:"))
total = 0
time = 0
for i in range(1,10000):
    total += f(i)
    if total >= n:
        time = i
        break
print(time)
