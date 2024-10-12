n = eval(input("n:"))
total = 0
for i in range(1,n+1):
    total += i*i

if total > 1000:
    print("too large")
else: print(total)