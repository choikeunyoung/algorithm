import sys
# 인풋값이 많으므로 선언
input = sys.stdin.readline

N = int(input())
# 시간 리스트 생성
time_list = []

for _ in range(N):
    time_list.append(list(map(int,input().split())))
# 시간 리스트 정렬
time_list.sort()
# 값을 체크해줄 변수들
x = -1
y = -1
# 갯수 체크
cnt = 1
# 리스트를 순회하며
for i in range(N-1):
    # 초기값 선언
    if x == -1 and y == -1:
        x = time_list[i][0]
        y = time_list[i][1]
    # 만약 저장된 x, y 변수의 값의 사이에 있으면 그 값들로 x,y 값 갱신
    if x <= time_list[i+1][0] and y > time_list[i+1][1]:
        x = time_list[i+1][0]
        y = time_list[i+1][1]
    # y값보다 다음 값의 x 값이 큰 경우
    elif y <= time_list[i+1][0]:
        # 회의가 끝났으므로 +1 해준 후 새로운 회의 시간으로 갱신
        cnt += 1
        x = time_list[i+1][0]
        y = time_list[i+1][1]
# 총 갯수
print(cnt)