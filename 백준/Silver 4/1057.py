N,jimin,hansoo = map(int,input().split())
# 라운드 체크
round = 1
# N을 계속해서 나눠가기때문에 0이아닌경우 까지
while N != 0:
    # 지민이가 큰지 한수가 큰지 모르기 때문에 이런 조건 설정함
    if jimin > hansoo:
        # 한수가 홀수이고 지민이가 짝수인 경우 한수 +1 이 지민이인 경우
        if hansoo%2 == 1 and jimin%2 == 0:
            if hansoo+1 == jimin:
                print(round)
                break
    elif jimin < hansoo:
        # 지민이가 홀수이고 한수가 짝수인 경우 지민 +1 이 한수인 경우
        if jimin%2 == 1 and hansoo%2 == 0:
            if jimin+1 == hansoo:
                print(round)
                break
    else:
        # 둘다 같은경우 -1
        print(-1)
    # 만약 N이 홀수인 경우
    if N%2 == 1:
        # 나눈값에 +1 을해준다 맨마지막 인원은 계속 올라가기 때문에
        N = N//2 + 1
    else:
        N //= 2
    # 지민이가 홀수인 경우
    if jimin%2 == 1:
        # 나눈값에 +1을 해줘야한다.
        jimin = jimin//2 + 1
    elif jimin%2 == 0:
        jimin //= 2
    # 한수가 홀수인 경우
    if hansoo%2 == 1:
        # 나눈값에 +1을 해준다
        hansoo = hansoo//2 + 1
    elif hansoo%2 == 0:
        hansoo //= 2
    # 매 대결이 끝나면 라운드 +1 해준다.
    round += 1