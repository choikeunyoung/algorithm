import sys

input = sys.stdin.readline

N = int(input())
ans = 0

for _ in range(N):
    words = input().strip()
    stack = []
    # 스택에 끝값이랑 같으면 뽑음
    for word in words:
        if stack:
            if stack[-1] == word:
                stack.pop()
            # 외의 경우 스택에 값 추가
            else:
                stack.append(word)
        else:
            stack.append(word)
    # 스택이 비어있으면 정답 +1
    if not stack:
        ans += 1
print(ans)