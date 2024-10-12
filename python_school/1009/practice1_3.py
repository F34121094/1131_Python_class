total = 0
for i in range(1,100):
    if i <= 50 and i >= 21 and i % 2 == 1:
        print(i,end = ' ')
        total += i
print()
print("Total =",total)