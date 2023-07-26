N = int(input())
# 정답 리스트 생성
answer_list = list(map(str,input().split()))
# 제출 리스트 생성
check_list = list(map(str,input().split()))
# 정답 갯수 체크
cnt = 0
# 시간 절약을 위해 딕셔너리 선언
answer_dict = {}
# enumerate를 통해 index 와 value를 가져옴
for i,j in enumerate(answer_list):
    # 딕셔너리에 값 추가
    answer_dict[j] = i
# N까지 반복
for i in range(N):
    # 처음 뽑을 값
    first_answer = check_list[i]
    # 이후 뽑을 값들 i+1부터 N 까지
    for j in range(i+1,N):
        second_answer = check_list[j]
        # 딕셔너리에 처음 값의 인덱스와 이후 값의 인덱스의 대소를 비교하여 cnt 증가
        if answer_dict[first_answer] < answer_dict[second_answer]:
            cnt += 1

total = (N*(N-1))//2

print(f"{cnt}/{total}")