import heapq

N,M = map(int,input().split())

matrix = [ list(map(int,input())) for _ in range(M) ]
# 방향배열 탐색
direction = [(0,-1), (-1,0), (0,1), (1,0)]
# 거리 값 갱신
distance = [ [10**9]*N for _ in range(M) ]

def dijkstra():
    # 시작 노드 설정
    queue = [(1, (0,0))]
    # 시작 거리 1로 설정
    distance[0][0] = 1
    # queue 리스트 탐색
    while queue:
        # 거리와 현재 노드 추출
        dist, now = heapq.heappop(queue)
        # 거리가 현재 추출한 노드의 cost 값보다 작으면 반복문 다음걸로
        if distance[now[0]][now[1]] < dist:
            continue
        # 방향배열 탐색
        for k in range(4):  
            ny = now[0] + direction[k][0]
            nx = now[1] + direction[k][1]
            # 범위안에 있으면
            if 0 <= ny < M and 0 <= nx < N:
                # 벽이 아닌경우
                if matrix[ny][nx] == 0:
                    # 시작 값이 아니면
                    if distance[ny][nx] == 10**9:
                        # 값 갱신 후 queue에 추가
                        distance[ny][nx] = dist
                        heapq.heappush(queue,(dist,(ny,nx)))
                    # 이미 값이 있으면
                    else:
                        # 거리값 갱신 후 queue 에 cost, 노드 추가
                        if distance[ny][nx] > dist:
                            distance[ny][nx] = dist
                            heapq.heappush(queue,(dist,(ny,nx)))
                # 벽인 경우
                else:
                    # 벽을 부시면 기존의 cost에서 +1 한 값을 갱신
                    if distance[ny][nx] == 10**9:
                        distance[ny][nx] = dist + 1
                        heapq.heappush(queue,(dist+1,(ny,nx)))

dijkstra()
print(distance[M-1][N-1]-1)