import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    words = input().strip()
    ans = deque()
    last_ope = ""
    for word in words:
        if word == "<":
            ans.rotate(-1)
        elif word == ">":
            ans.rotate(1)
        elif word == "-":
            if ans != "":
                ans.pop()
        else:
            ans.append(word)
    print(ans)