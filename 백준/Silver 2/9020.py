import sys

input = sys.stdin.readline

T = int(input())
# 에라토스테네스의 체
prime = [False,False] + [True] * 9999
for i in range(2,100):
    if prime[i]:
        for j in range(2*i,10001,i):
            prime[j] = False

# 테스트 케이스만큼 반복
for _ in range(T):
    N = int(input())
    # 3, 5 를 구하나 5, 3 을구하는건 같기때문에 N의 절반까지만 실행
    for j in range(2,(N//2)+1):
        # 에라토스테네스의 체를 통하여 구한 소수들로 N-j 한 값도 소수인 경우 정답값에 추가
        if prime[j] and prime[N-j]:
            # 변수로 선언한 이유는 결국 제일 마지막 값이 두 수사이의 차가 젤 적을 것이기 때문에
            ans = (j,N-j)
    print(ans[0],ans[1])