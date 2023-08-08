# A,B = map(int,input().split())
# cnt = 0
# num_list = ['4','7']
# for i in range(A,B+1):
#     for j in str(i):

## 보류
# import sys
# input = sys.stdin.readline

def dfs(k):
    global cnt
    if len(str(k)) > y:
        return
    if x <= len(str(k)) <= y:
        if a <= k <= b:
            cnt += 1
    for i in 4, 7:
        num = k * 10 + i
        print(num)
        dfs(num)
a, b = map(int, input().split())
x = len(str(a))
y = len(str(b))
cnt = 0
dfs(4)
dfs(7)
print(cnt)