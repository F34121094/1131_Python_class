n = int(input("n:"))

def cal(n):
    if n == 1:
        return 1
    else:
        return cal(n-1)*2 + 3

print("f(n) =",cal(n))