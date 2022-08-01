import sys

input = sys.stdin.readline

N,M = map(int,input().split())

cnt = 0
for i in range(M):
    bookcnt = int(input()) # 책의 갯수
    bookpos = (list(map(int,input().split()))) # 책 번호의 위치

    if bookpos != sorted(bookpos,reverse=True):
        cnt +=1

if cnt == 0:
    print("Yes")
else:
    print("No")