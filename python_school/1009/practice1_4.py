total = 0
total_5 = 0
for i in range(20,51):
    total += i
    if i % 5 ==0:
        print(i,end = " ")
        total_5 += i
print()
print("total (5) :",total_5)
print("total (ALL) :",total)