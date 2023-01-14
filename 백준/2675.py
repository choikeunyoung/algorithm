T = int(input())

for _ in range(T):
    s,p = map(str,input().split())
    for i in p:
        print(i*int(s),end="")
    print()