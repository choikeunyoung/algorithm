N, M = map(int, input().split())

T = int(input())

apples = []

for _ in range(T):
    apples.append(int(input()))

cnt = 0
base_value = apples[0]
flag = 0
index = 0
pos = 0
check = 0
while True:
    if flag == 1:
        if base_value > pos and base_value <= pos+M:
            cnt += ((pos+M)-base_value)
            pos = base_value-M
            index += 1
            if index == T:
                break
            else:
                base_value = apples[index]
        else:
            cnt += 1
            pos -= 1
        if pos < 0:
            flag = 0
            pos = 0
    else:
        if base_value > pos and base_value <= pos+M:
            cnt += (base_value - pos)
            pos = base_value
            index += 1
            if index == T:
                break
            else:
                base_value = apples[index]
        else:
            cnt += 1
            pos += 1
        if pos+M >= N:
            flag = 1
            pos = N - M + 1
    print(index,base_value,pos,cnt)
print(cnt)