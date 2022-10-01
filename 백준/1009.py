import sys

T = int(sys.stdin.readline())

for i in range(T):
    c = 1
    a,b = map(int,sys.stdin.readline().split())
    for _ in range(b):
        c *= a
        c %= 10
    print(c)
