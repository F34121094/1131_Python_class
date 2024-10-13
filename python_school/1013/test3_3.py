sum = 0
f= 0

s = []
fi = open("./score.txt","r")
for i in range(0,10,1):
    s.append(eval(fi.readline()))
fi.close()

for i in range(0,10,1):
    sum += s[i]
    if s[i] < 60:
        f += 1
avg = sum / 10
print("total =",sum)
print("average =",avg)
print("fail =",f)