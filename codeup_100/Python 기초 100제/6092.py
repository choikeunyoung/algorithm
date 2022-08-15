n = int(input())
list = list(map(int,input().split()))
dict = {}
for i in range(1,24):
    if i not in dict:
        dict[i] = 0

for k in list:
    if k in dict:
        dict[k] += 1

for v in dict.values():
    print(v, end=' ')
