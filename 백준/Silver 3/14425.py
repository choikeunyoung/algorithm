import sys

input = sys.stdin.readline

N,M = map(int,input().split())
# 갯수 세는 변수
cnt = 0
# 체크할 리스트
check_list = []
# 단어 저장리스트
word_list= []
for _ in range(N):
    word_list.append(input())

for __ in range(M):
    check_list.append(input())

# 반복문 돌면서 word_list 안에 있으면 cnt + 1
for i in check_list:
    if i in word_list:
        cnt += 1
print(cnt)