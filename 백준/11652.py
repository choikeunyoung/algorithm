from collections import deque
N=int(input())
dict = {}
for _ in range(N):
    num = int(input())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
low_list = deque([])

for k,v in sorted(dict.items()):
    if max(dict.values()) == v:
        low_list.append(k)

if len(low_list) >= 2:
    print(low_list.popleft())
else:
    print(low_list.popleft())