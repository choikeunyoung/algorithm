# 게임기 크기, 바구니 크기
N, M = map(int, input().split())
# 몇 개의 사과가 들어오는 지
T = int(input())
# 사과들의 위치 리스트
apples = []
# 사과 추가
for _ in range(T):
    apples.append(int(input()))
# 가장 먼 길이의 사과 위치
max_value = max(apples)
# 게임기 길이보다 제일 먼 사과의 위치가 작은 경우 N 값을 먼 길이 사과로 갱신
if max_value < N:
    N = max_value
# 몇번 움직였는지 갯수파악
cnt = 0
# index 값 증가
index = 0
# 현재 바구니 왼쪽끝의 위치
pos = 0
# T번 시행
while index < T:
    # base_value 값을 사과 리스트의 한개씩 순차적으로 넣어줌
    base_value = apples[index]
    # 만약 바구니 안에 값이 있을 경우 무시
    if base_value > pos and base_value <= pos+M:
        pass
    # 그 외의 경우
    else:
        # 만약 바구니 오른쪽 끝이 사과의 위치보다 작은 경우
        if (pos+M) < base_value:
            # 갯수 파악해주는 변수에 사과의 위치 - 끝의 위치
            cnt += (base_value-(pos+M))
            # 이후 왼쪽 끝을 사과의 위치에서 M 만큼 빼줌(바구니 길이)
            pos = base_value-M
        # 왼쪽 끝의 값이 현재 사과의 위치보다 크거나 같은 경우
        elif pos >= base_value:
            # 갯수 파악하는 변수에 현재 바구니 왼쪽끝의 위치에서 현재 사과위치 -1을 더해줌
            # 앞선 조건에서 pos > 으로 설정했기 때문에 -1을 해줌
            cnt += (pos-(base_value-1))
            # 이 또한 위 주식과 마찬가지
            pos = base_value-1
            # 0보다 작아졌을 경우 0으로 초기화
            if pos < 0:
                pos = 0
    index += 1
print(cnt)