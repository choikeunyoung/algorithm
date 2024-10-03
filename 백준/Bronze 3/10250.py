T = int(input())
H,W,N = map(int,input().split())

div = N//H
other = N%H
last = 1 + other
start = 10
if div != 0 :
    start = H * div
