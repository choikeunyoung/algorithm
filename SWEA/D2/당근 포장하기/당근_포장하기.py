# 같은 크기의 당근은 같은 상자
# 비어있는 상자가 있으면 안된다.
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int,input().split()))
    carrots.sort()
    