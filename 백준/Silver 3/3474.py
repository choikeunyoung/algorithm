import sys

input = sys.stdin.readline

T = int(input())
# Test Case 만큼 반복
for _ in range(T):
    # input 값으로 들어온 N이 5보다 작은경우 0의 갯수는 0 개다
    N = int(input())
    if N < 5:
        print(0)
    else:
        # 5라는 변수를 받고 cnt 값에 N을 5로 나눈 몫을 더해준다
        five_num = 5
        cnt = N//five_num
        # N보다 작은 5의 제곱 수를 가지고 cnt 값을 측정한다.
        while five_num <= N:
            # 이미 5로 구했기 떄문에 5를 곱해준다
            five_num *= 5
            # N이 만약 25보다 작으면 몫에 0이 들어가기 떄문에 cnt 값은 변화가 없다.
            cnt += (N//five_num)
        print(cnt)