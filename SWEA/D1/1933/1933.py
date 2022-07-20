import sys

sys.stdin = open('input.txt', 'r')

t = int(sys.stdin.readline())

for i in range(1,t+1):
    if t % i == 0:
        print(i, end=" ")

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for i in range(1, T + 1):
#     if T % i == 0:
#         print(i, end=" ")
