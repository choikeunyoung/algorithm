import sys

sys.stdin = open("input.txt", "r")

# (int(sys.stdin.readline()))
t = (int(sys.stdin.readline()))
for i in range(1, t+1):
    x, y = map(int,sys.stdin.readline().split())
    print(f"#{i}", x//y, x%y)

# T = int(input())

# for i in range(1, T+1):
#     x, y = map(int,input().split())
#     print(f"#{i}", x//y, x%y)