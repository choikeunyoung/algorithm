import sys

sys.stdin = open("input.txt", "r")

t = int(sys.stdin.readline())

for i in range(1,t+1):
    x, y = map(int,sys.stdin.readline().split())
    if x>y:
        print(f"#{i} >")
    elif x==y:
        print(f'#{i} =')
    else:
        print(f'#{i} <')