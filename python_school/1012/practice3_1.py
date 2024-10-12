while 1:
    x = eval(input("請輸入電度數(1~950之間):"))
    if x < 1 or x > 950:
        break
    price = 0

    if x > 300:
        price += (x-300)*4.4 + 200*3.3 + 100*2.2
    elif x > 100:
        price += (x-100)*3.3 + 100*2.2
    else: price += x * 2.2

    print("您的電費總共為",format(price,".2f"),"元\n")

print("你輸入錯了 所以你不能用了")
