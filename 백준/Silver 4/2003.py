N,M = map(int,input().split())

num_list = list(map(int,input().split()))
# M과 같은 값이있을 때 체크하는 변수
cnt = 0
# 합을 나타낼 변수
answer = 0
# 인덱스를 체크할 변수
index = 0
# N 의 길이까지 반복문 반복
for i in range(N):
    # 정답 변수에 num_list 의 값을 더해나감
    answer += num_list[i]
    # 만약 정답이 M 보다 큰 경우
    if answer > M:
        # M보다 작아질 때까지 answer에서 index 값들을 빼준다.
        while answer > M:
            # index가 초기에는 0에 위치해 있고 클 경우 1씩 증가해가며 값들을 빼나간다
            answer -= num_list[index]
            index += 1
        # 만약 값이 같은 경우 cnt 증가
        if answer == M:
            cnt += 1
    # 처음부터 같았을 경우 값 추가
    elif answer == M:
        cnt += 1
print(cnt)