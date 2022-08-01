from collections import deque

N = int(input())
supple_list=[]
for i in range(1,N+1):
    supple_list.append(i)
supple_list = deque(supple_list)
drop_list = []

while True:
    drop_list.append(supple_list.popleft())
    if not supple_list:
        break
    supple_list.append(supple_list.popleft())

for j in drop_list:
    print(j, end=" ")