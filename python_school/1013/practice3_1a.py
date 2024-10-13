fi = open("./practice3_1a","r")
content = fi.read()
fi.close()
a,b,c = map(int,content.split(","))
total = 0
for i in range(a,b,c):
    total += i
print(total)