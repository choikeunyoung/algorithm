from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
check = []
for i in range(1,T+1):
    str_ = input().strip()
    for i in str_:
        check.append(i)
    
    for j in range(0,len(check)-1):
        for k in range(i+1,len(check)):
            pass