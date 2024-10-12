for i in range(5):
    print(f"-----{i+1}-----")
    if i == 0:
        s = 0
        for j in range(2,31,2):
            s += j
        print("S =",s)
    if i == 1:
        s = 1
        for j in range(1,8,2):
            s *= j*3
        print("S =",s)
    if i == 2:
        s = 0
        for j in range(3,12,2):
            s += 1/j
        print("S =",s)
    if i == 3:
        s = 0
        for j in range(1,14,3):
            s += j * (j+4)
        print("S =",s)
    if i == 4:
        s = 0
        p = 7
        for j in range(-10,0,3):
            s += j**p
            p -= 2
        print("S =",s)
    print()