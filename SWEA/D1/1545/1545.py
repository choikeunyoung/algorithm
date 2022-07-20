import sys

sys.stdin = open("input.txt", "r")

t = int(sys.stdin.readline())
for i in range(t,-1,-1):
    print(i, end=" ")