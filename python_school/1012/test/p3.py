x= eval(input("x:"))
total = 0
x1 = 1
x2 = 1
now = 0
for i in range(x-1):
    now = x2
    x2 += x1
    x1 = now

print(x2)
