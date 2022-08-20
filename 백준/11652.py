import sys
N=int(sys.stdin.readline())
dict = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

low_cnt = 0
max_val = max(dict.values())
for k,v in dict.items():
    if v == max_val:
        if low_cnt == 0:
            low_cnt = k
        else:
            if low_cnt < k:
                continue
            else:
                low_cnt = k
print(low_cnt)