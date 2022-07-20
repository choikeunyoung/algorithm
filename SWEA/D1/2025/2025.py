import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
s = 0
for i in range(1,T+1):
    s+=i
print(s)