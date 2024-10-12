n = eval(input("請輸入數字:"))

for i in range(n):
    for j in range(i+1):
        print("X",end = '')
    print()