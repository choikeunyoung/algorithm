import sys
from collections import deque
# BFS 통한 탐색
def BFS(start,target):
    # 초기값으로 시간, 시작점, 목표점
    q = deque([(0,start,target)])
    while q:
        time, current, target = q.popleft()
        # 현재 점수가 목표점수와 같은 경우
        if current == target:
            # 시간 출력
            print(time)
            break
        # 목표점수 + 3 의 값보다 현재값의 2배한 값이 작거나 같은경우
        if target + 3 >= current*2:
            # 점수가 한번도 횟수가 안나온 경우
            if graph[current*2] == -1:
                # queue 값에 현재 시간 +1, 현재점수 *2, 목표점수 +3 추가
                q.append((time+1, current*2, target+3))
        # 만약 현재 점수 +1 한 값이 나오지 않은 점수인 경우
        if graph[current+1] == -1:
            # queue 에 현재 시간 +1, 현재 값 +1, 목표값 저장
            q.append((time+1, current+1, target))

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    graph = [-1] * 100001
    me, enemy = map(int,input().split())
    if me == enemy:
        print(0)
        continue
    BFS(me,enemy)