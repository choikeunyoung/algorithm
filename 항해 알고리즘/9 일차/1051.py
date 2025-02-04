N, M = map(int,input().split())

matrix = [ list(map(int,input())) for _ in range(N)]
# 최대 결과값이 1이 될 수 있으므로 1을 베이스로 시작
result = [1]
# 브루트포스 시작
for i in range(N):
    for j in range(M):
        # 꼭지점 계산을 위한 초기값 선언
        current = 1
        # 범위 내에 존재하면 계속 반복문 진행
        while i+current < N and j+current <M:
            # 각 꼭지점 값 비교
            if matrix[i][j] == matrix[i][j+current] and matrix[i][j] == matrix[i+current][j] and matrix[i][j] == matrix[i+current][j+current]:
                # 모두 같은경우 길이를 추가
                result.append(current+1)
            # 계속해서 범위를 늘려나감
            current += 1

# 최대 길이 도출
answer = max(result)
# 길이값 추가
print(answer**2)