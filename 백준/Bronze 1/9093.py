T = int(input())

for _ in range(T):
    sentents = list(map(str,input().split()))
    for i in sentents:
        print(i[::-1], end=" ")
    print()