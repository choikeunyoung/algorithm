import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    c = 1
    a, b = map(int, input().split())
    for _ in range(b):
        c *= a
        c %= 10
        if c == 0:
            print(10)
            break
    else:
        print(c)
