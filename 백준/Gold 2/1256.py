def searching(N, M, K):
    result = []
    total = N + M
    # 총 길이가 0보다 클때까지
    while total > 0:
        # a의 개수가 0보다 큰 경우 만들 수 있는 조합 식 계산
        if N > 0:
            count = comb(N + M - 1, M)
        else:
            count = 0
        # K번 째 수가 위에서 계산산 조합식 count 값보다 작거나 같은 경우 a 로 시작 혹은 끝
        if K <= count:
            result.append('a')
            N -= 1
        # K번 째 수가 조합식 count 보다 큰 경우 z 로 접근됨
        else:
            result.append('z')
            K -= count
            M -= 1
        # 길이 1개 감소
        print(result,N,M,K)
        total -= 1

    return ''.join(result)
# combnation 개수 체크
from math import comb

N, M, K = map(int, input().split())

if K > comb(N + M, M):
    print(-1)
else:
    print(searching(N, M, K))
