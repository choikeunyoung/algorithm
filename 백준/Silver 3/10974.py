from itertools import permutations
# N의 갯수
N = int(input())
# 1~N 까지 수를 담을 리스트
num_list = []

for i in range(1,N+1):
    num_list.append(i)
# N개의 갯수만큼 순열 생성
answer = list(permutations(num_list,N))

for j in answer:
    print(*j)