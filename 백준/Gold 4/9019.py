from collections import deque
import sys

input = sys.stdin.readline
# 2배 해주는 함수
def Double(num):
    return (num * 2) % 10000
# -1 해주는 함수
def Subtrack(num):
    return (num - 1) if num > 0 else 9999
# 너비우선탐색
def BFS(start, target):
    # 방문처리 체크
    visited = [False] * 10000
    # queue 에 값과 어떤 결과를 시행했는지 자정
    queue = deque([(start, "")])
    # 시작값 방문처리
    visited[start] = True
    # queue가 존재할 경우 계속 반복
    while queue:
        current, path = queue.popleft()
        # 2배 한 함수와 -1 한 함수 시행한 결과값 변수에 저장
        dobule_num = Double(current)
        subtrack_num = Subtrack(current)
        # left 로 움직이는 방법과 right로 움직이는 방법 변수에 저장
        left_num = (current % 1000) * 10 + (current // 1000)
        right_num = (current % 10) * 1000 + (current // 10)
        # 목표값과 같으면 현재 path + 각 연산을 결과를 출력
        if dobule_num == target:
            print(path + "D")
            return
        elif subtrack_num == target:
            print(path + "S")
            return
        elif left_num == target:
            print(path + "L")
            return
        elif right_num == target:
            print(path + "R")
            return
        # 저장된 숫자를 방문하지 않았을 경우 저장된 숫자 + 연산자를 queue에 추가해줌
        if not visited[dobule_num]:
            visited[dobule_num] = True
            queue.append((dobule_num, path + "D"))
        if not visited[subtrack_num]:
            visited[subtrack_num] = True
            queue.append((subtrack_num, path + "S"))
        if not visited[left_num]:
            visited[left_num] = True
            queue.append((left_num, path + "L"))
        if not visited[right_num]:
            visited[right_num] = True
            queue.append((right_num, path + "R"))

N = int(input())

for _ in range(N):
    problem, answer = map(int, input().split())
    BFS(problem, answer)
