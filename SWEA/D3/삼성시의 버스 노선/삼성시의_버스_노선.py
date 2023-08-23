T = int(input())


for tc in range(1, T+1):
    buses = [0] * 5001
    N = int(input())
    for i in range(1, N+1):
        A,B = map(int,input().split())
        for j in range(A,B+1):
            buses[j] += 1
    
    P = int(input())
    answer = []
    for k in range(P):
        C = int(input())
        answer.append(buses[C])
    print(f"#{tc}",*answer)