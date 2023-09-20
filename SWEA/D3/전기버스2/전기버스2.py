T = int(input())

for tc in range(1, T+1):
    infos = list(map(int,input().split()))
    total = infos[0]
    battery = infos[1:]
    index = 0
    cnt = 0
    while True:
        if index >= total-1:
            break
        next = index + battery[index]
        max_charge = max(battery[index:next])
        index += max_charge
        cnt += 1
    print(f"#{tc} {cnt-1}")