def prime_check(N):
    prime_visited = [False, False] + [True] * 2000000
    for i in range(2, int(2000000**0.5) + 1):
        for j in range(i + i, 2000002, i):
            if prime_visited[j]:
                prime_visited[j] = False

    for i in range(2000002):
        if prime_visited[i]:
            i = str(i)
            if i == i[::-1]:
                if int(i) >= N:
                    print(i)
                    break


N = int(input())

prime_check(N)
