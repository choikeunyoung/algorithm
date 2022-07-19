import sys

sys.stdin = open("input.txt", "r")

t = int(sys.stdin.readline())

for i in range(1,t+1):
    x = list(map(int,sys.stdin.readline().split()))
    print(f'#{i}', round(sum(x)/len(x)))