A = int(input())
B = int(input())
C = int(input())

total = A*B*C
total = str(total)
dict = {}
for j in range(0,10):
    dict[str(j)] = 0
for i in total:
    if i in dict:
        dict[i] += 1

for k in dict:
    print(dict[k])