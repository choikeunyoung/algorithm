# 과일 갯수와 뱀의 길이
N, M = map(int, input().split())
# 과일 길이를 리스트로 받아옴
fruit_length = list(map(int, input().split()))
# 과일 길이를 정렬한다.
fruit_length.sort()

# 과일 리스트를 순회하며 M보다 작거나 같으면 M의 길이가 1증가
for i in fruit_length:
    if i <= M:
        M += 1
    else:
        break
print(M)
