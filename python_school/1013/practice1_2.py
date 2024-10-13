def f(n):
    if n == 1:
        return 10
    else:
        return f(n-1)*2
def sum(n):
    if n == 1:
        return f(1)
    else:
        return f(n) + sum(n-1)
print(f"第10天應存入 {f(10)}")
print(f"共存入 {sum(10)}")