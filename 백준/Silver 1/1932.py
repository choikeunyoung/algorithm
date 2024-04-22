import sys
# 많은 인풋 처리
input = sys.stdin.readline

N = int(input())
# 숫자 저장할 리스트
num_list = []
# 숫자 저장
for _ in range(N):
    num_list.append(list(map(int,input().split())))
# 1 ~ N 까지 반복
for i in range(1,N):
    # i+1 까지 반복
    for j in range(i+1):
        # 양 끝점일 경우 한 경우의 수만 더함
        if j == 0:
            num_list[i][j] += num_list[i-1][j]
        elif j == i:
            num_list[i][j] += num_list[i-1][j-1]
        # 외의 경우 이전값 대각선 중 max 값 선택
        else:
            num_list[i][j] += max(num_list[i-1][j-1], num_list[i-1][j])
# 최종 계산된 결과에서 max 값 추출
print(max(num_list[-1]))