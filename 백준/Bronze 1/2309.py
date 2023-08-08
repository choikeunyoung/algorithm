tall = []
for i in range(9):
    tall.append(int(input()))

total = sum(tall)

for j in range(len(tall)-1):
    for k in range(j+1,len(tall)):
        total_2 = total - (tall[j] + tall[k])
        if total_2 == 100:
            tall.remove(tall[k])
            tall.remove(tall[j])
            break
    if len(tall) == 7:
        break
for l in sorted(tall):
    print(l)