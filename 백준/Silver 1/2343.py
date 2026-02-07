def backtracking(index, check):
    if index == K + 1:
        answer.append("".join(map(str, check)))
        return

    for num in range(10):
        if not visited[num]:
            if (
                index == 0
                or (operator[index - 1] == "<" and check[-1] < num)
                or (operator[index - 1] == ">" and check[-1] > num)
            ):
                visited[num] = True
                backtracking(index + 1, check + [num])
                visited[num] = False


K = int(input())
operator = input().split()

visited = [False] * 10
answer = []

for num in range(10):
    visited[num] = True
    backtracking(1, [num])
    visited[num] = False

print(answer)
print(answer[-1])
print(answer[0])
