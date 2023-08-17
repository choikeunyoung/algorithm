from collections import deque
   

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    cheeses = list(map(int,input().split()))
    for i,v in enumerate(cheeses):
        cheeses[i] = [v,i]
    current_pos = N
    hwa_duck = deque()
    for i in range(N):
        hwa_duck.append(cheeses.pop(0))
    while len(hwa_duck) > 1:
        hwa_duck[0][0] //= 2
        if hwa_duck[0][0] == 0:
            if cheeses:
                hwa_duck.append(cheeses.pop(0))
            hwa_duck.popleft()
        else:
            hwa_duck.rotate(-1)
    print(f"#{tc} {hwa_duck[0][-1]+1}")