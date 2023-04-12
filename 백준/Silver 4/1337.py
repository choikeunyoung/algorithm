import sys

input = sys.stdin.readline

N = int(input())
# 인풋값을 저장할 리스트
num_list = []
# 각 인풋값 별 +4 를 저장할 리스트
check_list = []

for _ in range(N):
    # 인풋값을 변수로 받는다
    number = int(input())
    # 기본 리스트 초기값으로 인풋값을 넣어준다
    base_list = [number]
    # +4 까지 숫자를 바로 위의 리스트에 넣어준다
    for i in range(1,5):
        base_list.append(number+i)
    # 넣은 리스트를 check_list 라는 곳에 넣어준다
    check_list.append(base_list)
    # 인풋값을 num_list 에 넣어준다
    num_list.append(number)
# 리스트를 정렬
num_list.sort()
# 정답 리스트 생성
answer_list = []
# +5값을 한 리스트를 반복문 순회한다.
for i in check_list:
    # 몇개가 들어있는지 체크하는 변수
    cnt = 0
    # num_list 순회하며 리스트에 존재하면 cnt 값 추가
    for j in num_list:
        if j in i:
            cnt += 1
    # 5개의 값중 들어있는 갯수를 빼준 것을 리스트에 추가
    answer_list.append(5-cnt)
# 모든 값들 중 최솟값을 출력
print(min(answer_list))