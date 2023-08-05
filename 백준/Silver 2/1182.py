from itertools import combinations
# 리스트 길이와 목표 값
N, S = map(int,input().split())
# num_list 를 리스트 형태로 받아옴
num_list = list(map(int,input().split()))
# 리스트 길이 담을 변수
num_length = len(num_list)
# 총 몇번 원하는 값이 존재하는지 체크
cnt = 0
# 1~N 까지 반복
for i in range(1,N+1):
    # i개의 조합을 만들어 반환
    comb_list = combinations(num_list,i)
    # 반환된 조합들의 합을 통해서 조건이 같으면 cnt 증가
    for j in comb_list:
        if sum(j) == S:
            cnt += 1
print(cnt)