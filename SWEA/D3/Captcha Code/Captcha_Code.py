T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    sample = list(map(int,input().split()))
    passcode = list(map(int,input().split()))
    pass_length = len(passcode)
    cnt = 0
    check_index = 0
    flag = 0
    for i in passcode:
        for j in range(check_index,N):
            if i == sample[j]:
                check_index = j
                cnt += 1
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            print(f"#{tc} 0")
            break
    else:
        if cnt == pass_length:
            print(f"#{tc} 1")
        else:
            print(f"#{tc} 0")