import copy

N = int(input())

word_list = []
answer = 0
# 단어들을 리스트에 저장
for _ in range(N):
    word_list.append(input())
# 첫번째 단어의 갯수를 세기위한 딕셔너리
word_dict = {}
# 단어의 길이
word_length = len(word_list[0])
# 첫번째 단어를 딕셔너리에 갯수 저장
for i in word_list[0]:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
# 첫번째 이후 단어들 반복
for j in word_list[1:]:
    # 각 단어를 반복할때마다 deepcopy를 이용해 딕셔너리 복사
    check_dict = copy.deepcopy(word_dict)
    # 각 단어의 길이
    check_length = len(j)
    # 딕셔너리랑 단어가 몇개나 다른지 확인
    check_cnt = 0
    # value 값에서 단어가 있으면 몇개가 남았는지 혹은 더 많은지 체크하기 위한 변수
    check_num = 0
    # 단어의 갯수 합
    total = 0
    # 최대 1개까지 많거나 적어야 하지만 1개가 넘어가면 체크해줄 변수
    flag = False
    # 각 단어의 값들을 반복하며 딕셔너리에 존재하면 -1 아니면 check_cnt 증가
    for k in j:
        if k in check_dict:
            check_dict[k] -= 1
        else:
            check_cnt += 1
    # 계산이 끝난 딕셔너리의 value 값들을 반복하며 v 값이 0 미만 초과 인 경우 체크
    # 또 -1 미만 1 초과인 경우 flag 를 True로 변경
    # 그리고 계산하며 total 값을 구해준다.
    for v in check_dict.values():
        if v < 0 or v > 0:
            check_num += 1
        if v < -1 or v > 1:
            flag = True
        total += v
    # 기준 단어와 순회하는 단어의 길이가 같은 경우 1개 작은 경우 1개 많은 경우 각각 나눠서 조건식
    if check_length == word_length:
        # 같은 경우는 조건이 많이 붙는데 단어를 바꿀 수 있기 때문에 조건을 많이 설정했다.
        # 길이가 같으므로 모든 값이 딕셔너리에 존재하는 경우, 딕셔너리에 모든 값이 존재하지만 한개가 다른 경우, 딕셔너리에 값이 있지만 1개의 값만 없는 경우로 나눠서 조건을 설정했다.
        if (check_num == 1 and check_cnt == 1) or (check_num == 0 and check_cnt == 0) or (check_num == 2 and check_cnt == 0 and total == 0 and flag == False):
            answer += 1
    # 반복하는 단어의 길이가 기준이 되는 단어보다 한개 더 긴 경우
    elif check_length - 1 == word_length:
        # 딕셔너리 값을 모두 0으로 만들고 딕셔너리에 없는 단어가 1개 존재하는 경우와 딕셔너리에 값이 모두 존재하여 value 값이 -1이 되고 딕셔너리 외의 값이 존재하지 않는 경우 두개 이다.
        if (check_num == 0 and check_cnt == 1) or (check_num == 1 and check_cnt == 0):
            answer += 1
    # 반복하는 단어의 길이가 기준이 되는 단어보다 한개 더 작은 경우
    elif check_length + 1 == word_length:
        # 딕셔너리에 모든 단어가 존재하고 딕셔너리 값이 남아있는 경우 
        if check_num == 1 and check_cnt == 0:
            answer += 1
print(answer)