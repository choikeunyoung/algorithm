def recur(num,total,cnt):
    if cnt >= N:
        ans.add(total)
        return
    for i in range(num,4):
        recur(i, total+numbers[i], cnt+1)

N = int(input())

numbers = [1, 5, 10, 50]

ans = set()
recur(0,0,0)
print(len(ans))