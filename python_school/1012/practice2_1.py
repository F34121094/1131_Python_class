x = eval(input("請輸入電度數:"))
price = 0

if x > 300:
    price += (x-300)*4.4 + 200*3.3 + 100*2.2
elif x > 100:
    price += (x-100)*3.3 + 100*2.2
else: price += x * 2.2

print("您的電費總共為",format(price,".2f"),"元")
