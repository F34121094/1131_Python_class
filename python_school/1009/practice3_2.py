print("-----A-----")
total_a = 0
for i in range(4,23,3):
    total_a += i
print("A :",total_a)

print("-----B-----")
total_b = 0
for i in range(1,10,2):
    total_b += i*(i+3)
print("B :",total_b)

print("-----C-----")
total_c = 0
for i in range(7,0,-2):
    total_c += -(i+3)**i
print("C :",total_c)

print("-----D-----")
total_d = 0
for i in range(1,8,2):
    total_d += i*(i+2)*(i+6)
print("D :",total_d)

print("-----E-----")
total_e = 0
for i in range(1,8,2):
    total_e += i/(i*2+1)
print("E :",total_e)

print("-----F-----")
total_f = 0
for i in range(2,5):
    a = 3
    for j in range(i):
        total_f += a
        a += 2
print("F :",total_f)