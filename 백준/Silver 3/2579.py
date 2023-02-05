N = int(input())
# 계단의 값 리스트 배열 생성
work_list = [0]
# 각 계단의 최대값 저장 배열 생성
max_list = [0]*301
# 계단의 값 추가
for _ in range(N):
    work_list.append(int(input()))

# 계단의 최대 칸 수만큼 반복문 시행
for i in range(1,N+1):
# 계단이 1개일 경우 최대값은 그 계단의 값
    if i == 1:
        max_list[i] = work_list[i]
# 계단이 2개일 경우 최대값은 그 계단과 직전의 계단을 더한 값
    elif i == 2:
        max_list[i] = max_list[1] + work_list[i]
# 계단이 3개 이상일 경우 그 계단에 도달하는 값이 정해져있다.
# 1번 : 바로 직전계단을 밟은것이 아닌 처음과 두번째 계단을 밟고 도착하는 방법
# 2번 : 처음 계단을 밟고 두번째를 건너뛰고 직전계단을 밟고 도착하는 방법
    else:
        max_list[i] = max(work_list[i] + max_list[i-3] + work_list[i-1], work_list[i] + max_list[i-2])
print(max_list[N])