from collections import deque

def ValueCheck(value,nextNumber):
    if 0 <= value <= 500000:
        if dp[value][0] == False:
            dp[value][0] = True
            if (nextNumber[0] + 1) % 2 == 0:
                dp[value][1][0] = nextNumber[0] + 1
            else:
                dp[value][1][1] = nextNumber[0] + 1

            return (nextNumber[0]+1,value)
        else:
            if (nextNumber[0] + 1) % 2 == 0:
                if dp[value][1][0] == 0:
                    dp[value][1][0] = nextNumber[0] + 1
                else:
                    if dp[value][1][0] > nextNumber[0] + 1:
                        dp[value][1][0] = nextNumber[0] + 1
            else:
                if dp[value][1][1] == 0:
                    dp[value][1][1] = nextNumber[0] + 1
                else:
                    if dp[value][1][1] > nextNumber[0] + 1:
                        dp[value][1][1] = nextNumber[0] + 1

def BFS(start):
    global K
    cnt = 0
    queue = deque([(0,start)])
    y_check = 0
    while queue:
        next = queue.popleft()
        if y_check != next[0]:
            cnt += 1
            K += cnt

        if K > 500000:
            return -1
        
        if dp[K] == True or K == next[1]:
            return dp[:K+1]

        minous_value = next[1] - 1
        plus_value = next[1] + 1
        double_value = next[1] * 2

        next_value = ValueCheck(minous_value,next)
        if next_value != None:
            queue.append(next_value)
        next_value = ValueCheck(plus_value,next)

        if next_value != None:
            queue.append(next_value)
        next_value = ValueCheck(double_value,next)
        if next_value != None:
            queue.append(next_value)

        y_check = next[0]

N, K = map(int,input().split())

if N == K:
    print(0)
else:
    dp = [[False, [0,0]] for _ in range(500001)]
    dp[N][0] = True
    check = BFS(N)