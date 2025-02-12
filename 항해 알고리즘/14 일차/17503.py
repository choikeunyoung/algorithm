import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(k):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[1])

l, r = 0, k - 1
ans = -1

while l <= r:
    mid = (l + r) // 2
    beers = [arr[i][0] for i in range(mid + 1)]
    beers.sort(reverse=True)
    lm = min(mid, n - 1)
    total_sum = sum(beers[i] for i in range(lm + 1))

    if total_sum >= m and mid >= n - 1:
        ans = arr[mid][1]
        r = mid - 1
    else:
        l = mid + 1

print(ans)
