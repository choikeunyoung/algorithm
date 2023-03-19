import sys

N,M = map(int,input().split())

min_set = sys.maxsize
min_val = sys.maxsize

for _ in range(M):
    x,y = map(int,input().split())
    if x < min_set:
        min_set = x
    if y < min_val:
        min_val = y

cnt = (N//6)+1
cnt2 = cnt-1

print(min(cnt*min_set,N*min_val,(cnt2*min_set+((N-6*cnt2)*min_val))))