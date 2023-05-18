N = int(input())

cnt = 0
first_value = N
# N 값이 5보다 작은 경우 2로 나눈 몫과 나머지 출력
if N < 5:
    cnt += N // 2
    N = N % 2
    if N == 0:
        print(cnt)
    else:
        print(-1)
else:
    # N 값이 5보다 큰 경우 cnt 에 5로 나눈 몫을 넣고 나머지를 N에 넣어줘서 2로 똑같은 작업 수행
    for i in [5, 2]:
        cnt += N // i
        N = N % i
    # 무한루프 통해서 N == 0 인 경우 그대로 출력 아닌 경우 조건 생각
    while True:
        if N == 0:
            print(cnt)
            break
        # 아닌경우 N 값이 초기 N 보다 커질때 -1 출력하고 break
        else:
            if N > first_value:
                print(-1)
                break
            # 그 전까지 N 에 5를 더해가며 cnt 값을 -1 씩해가고 나머지를 변수에 저장해서 0이 되는지 판단
            else:
                N += 5
                cnt -= 1
                nam = N % 2
                if nam == 0:
                    # 나머지가 0 이 될 경우 cnt 에 2로나눈 몫 값을 더해주고 출력
                    cnt += N // 2
                    print(cnt)
                    break
