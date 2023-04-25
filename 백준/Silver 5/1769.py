N = input()
# 각 자리수의 합을 구해야 하기때문에 초기값이 10보다 큰지 작은지 판단
if int(N) >= 10:
    cnt = 0
    # 무한루프를 통해서 각 자리 수의 합을 N 으로 갱신
    while True:
        # 변수 선언
        total = 0
        # 각 자리수를 정수형으로 변화하며 total 에 값을 더해 나감
        for i in N:
            total += int(i)
        # 총합을 문자로 변형하여 N에 대입
        N = str(total)
        cnt += 1
        # N의 길이가 1이면 종료
        if len(N) == 1:
            break
    # 반복문이 끝나면 횟수를 출력
    print(cnt)
    # 3으로 나눠지면 YES 안나눠지면 NO
    if int(N) % 3 == 0:
        print("YES")
    else:
        print("NO")
else:
    if int(N) % 3 == 0:
        print(0)
        print("YES")
    else:
        print(0)
        print("NO")