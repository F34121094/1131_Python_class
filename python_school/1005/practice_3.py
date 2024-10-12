score = [700,800,850]
total = 0
for i in score:
    total += i
avg = total/len(score)
print("Average =",avg)
print(score[2] - avg)