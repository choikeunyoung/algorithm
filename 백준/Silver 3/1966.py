import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, search = map(int,input().split())
    priority_list = list(map(int,input().split()))
    max_value = max(priority_list)
    for i,v in enumerate(priority_list):
        priority_list[i] = (v,i)
    priority_list = deque(priority_list)
    