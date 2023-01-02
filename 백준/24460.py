# 특별상을 받을 수 있는 사람이 한 명이라면, 그 사람이 뽑힌다.
# 그렇지 않은 경우, 대회장을 같은 크기의 정사각형 네 개로 나누어 각 구역에서 이 규칙을 재귀적으로 적용해서 구역마다 한 명씩 총 네 명을 뽑는다.
# 뽑힌 네 명 중 의자에 적힌 추첨번호가 두 번째로 작은 사람이 뽑힌다.

N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]
print(matrix)

def dfs(matrix):
    if len(matrix)