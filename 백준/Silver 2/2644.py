import sys
# 많은 인풋 처리
input = sys.stdin.readline
# DFS 함수
def DFS(start):
    # 시작 위치 1로 방문처리
    visited[start] = 1
    global cnt
    global end
    # matrix로 접근
    for i in range(N+1):
        # matrix 값이 1인 경우
        if matrix[start][i] == 1:
            # 방문하지 않았다면
            if visited[i] == 0:
                # i 값이 목표값과 같은 경우
                if i == end:
                    # cnt 출력 후 실행 종료
                    print(cnt)
                    exit()
                # 외의 경우
                else:
                    # cnt 값 증가(촌수 계산)
                    cnt += 1
                    # 방문처리에 이전값 + 1
                    visited[i] = visited[start] + 1
                    # 재귀 실행
                    DFS(i)
                    # 방문처리 취소
                    visited[i] = 0
                    # cnt 값 다시 감소
                    cnt -= 1

N = int(input())
start, end = map(int,input().split())
# 부모 자식간의 관계 수
m = int(input())
# martix 생성
matrix = [ [0]*(N+1) for _ in range(N+1) ]
# visited 생성
visited = [0] * (N+1)
for _ in range(m):
    # A,B 인풋 값 추가
    A,B = map(int,input().split())
    matrix[A][B] = 1
    matrix[B][A] = 1
# 촌수 계산 변수
cnt = 1
# 값이 없는걸 체크할 리스트
ans = []
DFS(start)
# DFS 함수를 통해서 값을 못찾았을 경우 -1 출력
if len(ans) == 0:
    print(-1)