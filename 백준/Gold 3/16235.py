import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int,input().split())
# 방향배열
direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
# 양분 초기값
matrix = [[5] * N for _ in range(N)]
# 겨울 양분 값
winter = []
# 양분 추가
for _ in range(N):
    winter.append(list(map(int,input().split())))
# 각각 나무에 영양분이 얼마인지 저장
trees = [[[] for _ in range(N)] for _ in range(N)]
# 초기 영양분 위치 저장
middle = set([])
# 나무 위치 저장 및 영양분 위치 저장
for _ in range(M):
    x, y, k = map(int,input().split())
    middle.add((x-1,y-1))
    trees[x-1][y-1].append(k)
# 나무 위치 정렬
for item in middle:
    trees[item[0]][item[1]].sort()
# K 년 만큼 반복문 진행
for _ in range(K):
    # 가을 리스트 생성
    fall = []
    # 여름 봄 기간 동안 처리할 양분과 나무
    for i in range(N):
        for j in range(N):
            # 죽은 나무 영양분 체크
            dead = 0
            # 새로 양분을 받은 나무 리스트
            current_trees = deque()
            # 각 나무 위치에 저장된 값
            for value in trees[i][j]:
                # 양분이 충분할 경우
                if value <= matrix[i][j]:
                    # 양분 주고 남은값 저장
                    matrix[i][j] -= value
                    # 나무의 나이 1 증가
                    value += 1
                    # 나무가 5의 배수인 경우 가을 리스트에 저장
                    if value % 5 == 0:
                        fall.append((i,j))
                    # 현재 나무위치의 값 저장
                    current_trees.append(value)
                else:
                    # 양분이 충분하지 않는 경우 죽기 떄문에 2로 나눈 몫 저장
                    dead += value//2
            # 반복문 종료시 영양분으로 죽은 나무 저장
            matrix[i][j] += dead
            #  현재 나무 리스트를 새롭게 갱신
            trees[i][j] = current_trees
    # 가을 리스트가 있는경우
    while fall:
        # 8방향 1의 영양분 나무 추가
        x, y = fall.pop()
        for k in range(8):
            nx = direction[k][0] + x
            ny = direction[k][1] + y
            if 0 <= nx < N and 0 <= ny < N:
                trees[nx][ny].appendleft(1)
    # 겨울에 각 땅에 영양분 저장
    for i in range(N):
        for j in range(N):
            matrix[i][j] += winter[i][j]
answer = 0
# 나무의 길이만큼 개수 추가
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            answer += len(trees[i][j])
print(answer)
