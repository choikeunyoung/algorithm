def gop(num):
    if num * 2 <= 100000:
        return num*2
    else:
        return num

def div(num):
    if num // 2 >= 0:
        return num // 2
    else:
        return num

def plus(num):
    if num + 1<= 100000:
        return num + 1
    else:
        return num

def minous(num):
    if num - 1 >= 0:
        return num -1
    else:
        return num


def BFS(start):
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        check = queue.pop(0)
        g = gop(check)
        d = div(check)
        p = plus(check)
        m = minous(check)
        
        if visited[g] == 0:
            queue.append(g)
            visited[g] = visited[check] + 1
        if visited[d] == 0:
            queue.append(d)
            visited[d] = visited[check] + 1
        if visited[p] == 0:
            queue.append(p)
            visited[p] = visited[check] + 1
        if  visited[m] == 0:
            queue.append(m)
            visited[m] = visited[check] + 1
        
        if g == D:
            return visited[g]
        elif d == D:
            return visited[d]
        elif p == D:
            return visited[p]
        elif m == D:
            return visited[m]

S = int(input())
D = int(input())

visited = [0]*100001

print(BFS(S)-1)