import sys

sys.stdin = open('input.txt', 'r')

p,k = map(int,sys.stdin.readline().split())
cnt = 1

while p!=k:
    cnt+=1
    k+=1

print(cnt)