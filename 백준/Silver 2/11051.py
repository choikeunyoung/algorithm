# 팩토리얼 계산 함수 (DP로 계산)
def fact(num):
    DP = [1]
    for i in range(2,num+1):
        DP.append((DP[-1]*i))
    return DP
# N, K 값받아옴
N, K = map(int,input().split())
# 함수 실행
DP_list = fact(N)
# N == K 혹은 K 값이 0 인경우 1 출력
if N == K or K == 0:
    print(1)
# 외의 경우 조합 계산
else:
    ans = ((DP_list[N-1])//(DP_list[N-K-1]*DP_list[K-1])%10007)
    print(ans)