def Dqueue(num):
    global front
    if num == M:
        return front
    else:
        front = (front+1) % N
        return Dqueue(num+1)

T = int(input())
for tc in range(1, T+1):
    front = 0
    N, M = map(int,input().split())
    queue = list(map(int,input().split()))
    print(f"#{tc} {queue[Dqueue(0)]}")