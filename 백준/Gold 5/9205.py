import sys
from collections import deque
# 많은 인풋 처리를 위해 sys 사용
input = sys.stdin.readline

T = int(input())
# 테스트 케이스 만큼 반복
for tc in range(T):
    store_cnt = int(input())
    # 편의점 위치 담을 리스트
    stores = []
    # 현재 시작 위치
    home = list(map(int,input().split()))
    # 편의점 위치 추가
    for _ in range(store_cnt):
        stores.append(list(map(int,input().split())))
    # 도착 지점 설정
    rock_festival = list(map(int,input().split()))
    # 갈 수 있는 지점 deque 를 이용한 queue 사용
    can_go = deque([])
    # 편의점 방문 체크
    visited = [0] * store_cnt
    # 집과 맥주 페스티벌의 거리가 1000 이하일 경우 바로 갈 수 있음
    if max(rock_festival[0],home[0]) - min(rock_festival[0],home[0]) + max(rock_festival[1],home[1]) - min(rock_festival[1],home[1]) <= 1000:
        print("happy")
    # 외의 경우
    else:
        # 현재 집에서 갈 수 있는 편의점 리스트 추가 후 방문여부 체크
        for index, store in enumerate(stores):
            if max(store[0],home[0]) - min(store[0],home[0]) + max(store[1],home[1]) - min(store[1],home[1]) <= 1000:
                can_go.append(store)
                visited[index] = 1
        # 갈 수 있는 편의점 리스트 순회
        while can_go:
            check = can_go.popleft()
            # 편의점에서 맥주 페스티벌까지 갈 수 있으면 정답 출력 후 반복문 종료
            if max(rock_festival[0],check[0]) - min(rock_festival[0],check[0]) + max(rock_festival[1],check[1]) - min(rock_festival[1],check[1]) <= 1000:
                print("happy")
                break
            # 편의점리스트 순회하며
            for index, store in enumerate(stores):
                # 현재 편의점에서 다음 편의점에 갈 수 있고 방문하지 않았으면 방문처리 후 갈 수 있는 리스트에 추가
                if max(store[0],check[0]) - min(store[0],check[0]) + max(store[1],check[1]) - min(store[1],check[1]) <= 1000:
                    if visited[index] == 0:
                        can_go.append(store)
                        visited[index] = 1
        # 반복문이 break로 탈출하지 못했을 경우 답 출력
        else:
            print("sad")
