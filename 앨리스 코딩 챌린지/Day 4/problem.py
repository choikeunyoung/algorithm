import sys
import collections

input = sys.stdin.read
sys.setrecursionlimit(200000)

def main():
    data = input().split()
    N = int(data[0])
    
    edges = []
    for i in range(1, len(data) - 1, 2):
        u = int(data[i])
        v = int(data[i+1])
        edges.append((u, v))
    
    tree = collections.defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    depth = [-1] * (N + 1)
    
    def dfs(node, d):
        depth[node] = d
        for neighbor in tree[node]:
            if depth[neighbor] == -1:
                dfs(neighbor, d + 1)
    
    dfs(1, 0)
    
    result = []
    for i in range(1, N + 1):
        if depth[i] % 2 == 0:
            result.append(1)  # 선공이 이김
        else:
            result.append(0)  # 후공이 이김
    
    print("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
