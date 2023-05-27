N = int(input())
A = list(map(int,input().split()))
# 리스트 길이를 확인해서 정답 리스트 생성
A_length = len(A)
# 0으로 이루어진 길이 리스트 생성
P = [0]*A_length
# 정렬한 리스트 생성
sorted_A = sorted(A)
# 리스트 번호를 매겨줄 변수
cnt = 0

for i in range(N):
    # 오름차순 정렬된 작은 값부터 넣어서 비교
    check = sorted_A[i]
    for j in range(N):
        # 목표값과 A리스트 값이 같으면 A리스트 값을 -1로 변환 후 P리스트에 순서 저장 후 순서값 증가
        if A[j] == check:
            P[j] = cnt
            A[j] = -1
            cnt += 1
            break
print(*P)