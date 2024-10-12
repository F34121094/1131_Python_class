n = eval(input("n:"))

for i in range(1,n+1):
    s = ' ' * (n - i)
    h = '#' * (2 * i - 1)
    print(s + h)
