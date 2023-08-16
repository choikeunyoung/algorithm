def superSum(start,end):
    global total
    if start == end:
        return total + start
    else:
        total += start
        return superSum(start+1, end)

while True:
    try:
        N,M = map(int,input().split())
        total = 0
        print(superSum(N,M))
    except EOFError:
        break