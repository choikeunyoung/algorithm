T = int(input())

for tc in range(1,T+1):
    ans = 0
    N = int(input())

    arr = list(map(int,input().split()))
    lst = [0]

    def calculate(lst):
        if not (lst[0] == 0 and lst[-1] == N-1):
            print(lst)
            f = (arr[lst[0]] + arr[lst[-1]]) ** 2
            l = (arr[lst[1]] + arr[lst[2]]) ** 2
            f2 = (arr[lst[0]] + arr[lst[1]]) ** 2
            l2 = (arr[lst[2]] + arr[lst[-1]]) ** 2
            if f + l > f2 + l2:
                return f+l
            else:
                return f2+ l2
        else:
            return ans

    def dfs(n,lst):
        global ans
        if n > N:
            return ans
        if len(lst) == 4:
            ans = max(ans, calculate(lst))
            return ans
        else:
            if (n+1) - lst[-1] == 1:
                n += 1
                dfs(n,lst)
            else:  
                lst.append(n+1)
                n += 1
                dfs(n+1, lst)
                lst.pop()
                dfs(n,lst)

    dfs(0,lst)

    print(f'#{tc} {ans}')