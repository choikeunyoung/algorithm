N = int(input())
# 10 보다 작은 경우 한자릿 수
if N < 10:
    print(N)
else:
    # 자리수를 세기 위한 변수
    cnt = 0
    # 10의 배수자릿 수를 세기위한 변수
    N_length = 1
    # 초기값 1
    base = 1
    # 길이가 N과 같을때 까지 반복
    while N_length < len(str(N)):
        # num 이라는 변수로 10, 100 등을 나타냄
        num = 10**N_length
        # 갯수에는 num 이라는 변수에서 초기값 base 라는 변수를 뺀 값에 N_length를 곱해준다.
        cnt += (num-base)*N_length
        # base값에 10을 곱해나감
        base *= 10
        # 10의 배수 자릿수를 더해나간다.
        N_length += 1
    # 반복문을 탈출한 후 맨 마지막 값을 계산하기 위해 따로 설정
    answer = N - num
    answer += 1
    cnt += (answer*N_length)
    print(cnt%1234567)