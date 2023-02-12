import sys
input = sys.stdin.readline

n=int(input())
answer = 1
for i in range(n):
    answer += int(input()) -1
    
print(answer)