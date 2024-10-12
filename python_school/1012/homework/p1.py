time = 0
sign = 0
while time < 4:
    st = input("密碼:")
    if st != "ncku":
        print("密碼錯誤")
        time += 1
        if time == 4: break
        print(f"剩下 {4-time} 次機會")

    else:
        sign = 1
        break

if sign == 1: print("成功登入")
else: print("登入失敗")