import sys

input = sys.stdin.readline
# 숫자의 길이
N = int(input())
# 숫자 리스트
num_list = list(map(int,input().split()))
# 반복문 횟수
M = int(input())
# 각 숫자들 인덱스별 팰린드롬 체크 배열
ans_list = [ [0] * N for _ in range(N)]
# 1~1 2~2 등 자기자신은 팰린드롬 이므로 1 대입
for i in range(N):
    ans_list[i][i] = 1
# 2 까지는 i와 i+1 만 비교해도됨
for i in range(N-1):
    j = i + 1
    if num_list[i] == num_list[j]:
        ans_list[i][j] = 1
# 2 이상부터 반복문
if N > 2:
    # 3이 초기값이므로 3부터 반복문
    for i in range(3,N+1):
        # 0부터 N에서 i 를 뺸 길이만큼 반복
        for j in range(N-i+1):
            # index 라는 변수를 통해서 0 부터 몇번 인덱스까지 비교할지 대입
            index = j + i - 1
            # num_list의 index 와 j 값이 같은 값이고 팰린드롬 체크하는 ans_list에 index 와 j 값을 각각 +-1한 인덱스가 팰린드롬인 경우
            if num_list[index] == num_list[j] and ans_list[j+1][index-1] == 1:
                # ans_list[j][index] 도 팰린드롬 이므로 1 넣어줌
                ans_list[j][index] = 1

for _ in range(M):
    start, end = map(int,input().split())
    start -= 1
    end -= 1
    print(ans_list[start][end])