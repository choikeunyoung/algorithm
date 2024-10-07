N, M = map(int,input().split())

matrix = list(map(int,input().split()))

left = matrix[0]
min_index = 0
answer = 0

for i in range(1,M):
    if matrix[i] >= left:
        left = matrix[i]
        min_index = i
    elif matrix[i] < left:
        answer += left - matrix[i]
