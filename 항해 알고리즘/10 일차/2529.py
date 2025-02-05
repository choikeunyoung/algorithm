# 백트래킹
def backtracking(index, check):
    # 인덱스가 끝값에 도달할 경우
    if index == K + 1:
        answer.append("".join(map(str, check)))
        return
    # 0 ~ 9 까지 값 반복하며 방문헀는지 안했는지 및 부등호에 따른 연산자 처리
    for num in range(10):
        if not visited[num]:
            if index == 0 or (operator[index - 1] == "<" and check[-1] < num) or (operator[index - 1] == ">" and check[-1] > num):
                visited[num] = True
                backtracking(index + 1, check + [num])
                visited[num] = False


K = int(input())
operator = input().split()

visited = [False] * 10
answer = []
# 방문처리 및 리스트 정리
for num in range(10):
    visited[num] = True
    backtracking(1, [num])
    visited[num] = False

print(answer[-1])
print(answer[0])