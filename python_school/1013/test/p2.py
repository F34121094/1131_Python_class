
while 1:
    type = input("function:")

    if type == "0": print("hello")

    elif type == "1":
        st = input("number:")
        print("reversed number: ",end = "")
        for i in range(-1,-(len(st)+1),-1):
            print(st[i],end = '')
        print()
    elif type == "2":
        a = eval(input("A:"))
        b = eval(input("B:"))
        c = eval(input("C:"))
        print("max:",max(a,b,c))
        print("min:",min(a,b,c))

    elif type == "3":
        n = eval(input("n:"))
        total = 1
        for i in range(n,0,-1):
            total *= i
        print("n!:",total)
    elif type == "q":
        print("quit")
        break
    else:print("invalid")