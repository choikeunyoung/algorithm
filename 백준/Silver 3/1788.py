def fibonacci(num):
    # 양수일때 피보나치 리스트
    dp = [0, 1]
    # 음수일 경우 피보나치 리스트
    dp_ma = [0, 1, -1]
    # 음수에서 절대값 구하기 위해서 사용되는 변수
    check = 0
    # n 값이 1000000을 넘지 않는다 했으므로 범위를 미리 설정하여 값을 다 구해둔다
    for _ in range(2,1000001):
        # 양수인 경우 기존의 피보나치 구하는 방식대로 구한다.
        answer_dp = dp[-1] + dp[-2]
        # 음수의 경우 기존에서 구하는 방식과는 다르게 -2 값에서 -1을 빼는 식으로 값을 구한다.
        answer_ma = dp_ma[-2]-dp_ma[-1]
        # 양수의 경우 그냥 나머지를 나눠서 값으로 넣어준다.
        answer_dp %= 1000000000
        # 만약 결과값이 음수인 경우 check 라는 변수에 1을 넣어주고 answer_ma에 -를 붙여서 양수로 변경해준다.
        if answer_ma < 0:
            answer_ma = -answer_ma
            check = 1
        # 똑같이 1000000000을 나눠준다
        answer_ma %= 1000000000
        # 만약 앞에서 check를 통해서 음수에서 양수로 변경되었다면 다시 음수로 바꿔준 후 check를 다시 0으로 바꾼다.
        if check == 1:
            answer_ma = -answer_ma
            check = 0
        dp.append(answer_dp)
        dp_ma.append(answer_ma)
    # 들어온 input 값에 따라서 반환해주는 리스트를 다르게 해준다.
    if num < 0:
        return dp_ma[abs(num)]
    else:
        return dp[num]

num = int(input())
ans = fibonacci(num)
# 반한된 결과값에 따라서 음수면 -1 양수면 1 0이면 0을 출력해준다.
if ans < 0:
    print(-1)
    print(abs(ans))
elif ans > 0:
    print(1)
    print(ans)
else:
    print(0)
    print(ans)