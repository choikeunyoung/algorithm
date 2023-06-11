import sys
# 파일의 갯수
N = int(input())
# 각 파일별 길이
file_lengths = []
for _ in range(N):
    # 파일을 리스트 형태로 받아옴
    num_list = list(map(int, input().split()))
    file_lengths.append(num_list)
# 파일의 길이중 최대값을 max_length 에 저장
max_length = max(map(len, file_lengths))
# 파일에서 최소가 되는 값을 저장할 변수
min_value = sys.maxsize
# 1~최대 길이 까지 반복문 시행
for K in range(1, max_length + 1):
    # set 형태로 리스트를 받아올 변수
    unique = set()
    # 파일들이 담긴 리스트에서 파일들을 순회
    for file in file_lengths:
        # 만약 K 값보다 파일의 길이가 작은 경우
        if len(file) < K:
            # 튜플 형태로 파일 리스트에 부족한 0 추가
            file[-1] = 0
            unique.add(tuple(file + [0] * (K - len(file) - 1)))
            file[-1] = -1
        else:
            # 튜플형태로 0~K 까지 파일 리스트 추가
            unique.add(tuple(file[:K]))
    # 만약 리스트 갯수가 N 의 갯수와 같으면 min_value 값에 K 넣고 출력
    if len(unique) == N:
        min_value = K
        break

print(min_value)