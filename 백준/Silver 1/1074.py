N, r, c = map(int,input().split())

matrix = [ [0] * 2**N for _ in range(2**N)]

cnt = 0

def searching(N):
    for i in range(0,2**N,2**N//4):
        print(i*(2**N))

searching(N)