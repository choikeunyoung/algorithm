def search_num(current, value):
    global cnt
    if current > 10:
        print(-1)
        exit()
    if cnt == N:
        print(start)
        exit()
    else:
        


N = int(input())
cnt = 0
ans = []
search_num(1,0)