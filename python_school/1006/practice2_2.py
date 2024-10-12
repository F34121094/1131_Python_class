a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))
if a>b and a>c:
    print("100")
elif c>b and c>a:
    print("10")
elif b>a and b>c:
    print("1")
else:
    print("0")