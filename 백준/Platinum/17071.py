from collections import deque

def BFS(start):
    global K
    cnt = 0
    queue = deque([(start,0)])
    y_check = 0
    while queue:
        next = queue.popleft()
        if y_check != next[1]:
            cnt += 1
            K += cnt
        if K >= 500000:
            return -1

        if dp[K][0] == True:
            return dp[:30],cnt,K

        if 0 <= next[0]-1 <= 500000 and dp[next[0]-1][0] == False:
            dp[next[0]-1] = [True,next[1]+1]
            queue.append((next[0]-1,next[1]+1))
        if 0 <= next[0]+1 <= 500000 and dp[next[0]+1][0] == False:
            dp[next[0]+1] = [True,next[1]+1]
            queue.append((next[0]+1,next[1]+1))
        if 0 <= next[0]*2 <= 500000 and dp[next[0]*2][0] == False:
            dp[next[0]*2] = [True,next[1]+1]
            queue.append((next[0]*2,next[1]+1))
        y_check = next[1]

N, K = map(int,input().split())

if N == K:
    print(0)
else:
    dp = [[False,0]] * 500001
    dp[N] = [True,0]
    temp = BFS(N)
    if temp == -1:
        print(-1)
    else:
        print(temp)