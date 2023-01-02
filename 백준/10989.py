N = int(input())
num_dict = {}
for i in range(1, 10001):
    num_dict[i] = 0
for _ in range(N):
    i = int(input())
    if i in num_dict:
        num_dict[i] += 1

for k,v in num_dict.items():
    if v > 0:
        for j in range(v):
            print(k)