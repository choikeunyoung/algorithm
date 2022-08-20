import sys
N=int(sys.stdin.readline())
dict = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
low_val = 0
for k,v in dict.items():
    if max(dict.values()) == v:
        if low_val == 0:
            low_val = k
        else:
            if low_val < k:
                continue
            else:
                low_val = k

print(low_val)