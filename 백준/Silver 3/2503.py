from itertools import permutations

N = int(input())
# 들어온 숫자 값들을 저장할 리스트
num_list = []
# 숫자값과 스트라이크 볼을 저장할 리스트
base_list = []
# 없는 숫자를 체크할 리스트
no_list = []
# 1~9의 숫자조합을 만들기 위한 리스트
check_list = [1,2,3,4,5,6,7,8,9]
# N의 갯수만큼 반복문 시행
for _ in range(N):
    # input 으로 외친 숫자, 스트라이크 갯수, 볼의 갯수
    baseball = list(map(int,input().split()))
    # input 으로 들어온 숫자를 문자열로 치환
    baseball[0] = str(baseball[0])
    # 볼과 스트라이크가 둘다 0이 아닌 경우 인풋 형태 그대로 리스트한개에 저장
    # 숫자만 따로 별도의 리스트에 저장
    if baseball[1] != 0 or baseball[2] != 0:
        num_list.append(baseball[0])
        base_list.append(baseball)
    # 만약 스트라이크 갯수가 0 이고 볼의 갯수가 0 인 경우 no_list에 없는 값들 추가
    elif baseball[1] == 0 and baseball[2] == 0:
        for l in baseball[0]:
            if l not in no_list:
                # 정수형으로 다시 변환
                no_list.append(int(l))
# 만약 num_list 에 값이 존재할 경우
if num_list:
    # check_list에 존재하는 값들로 가능한 모든 경우의 수를 생성
    perm_list = list(permutations(check_list,3))
    # 변환한 값들을 세 자리 수로 바꿔서 담을 리스트 생성
    answer = []
    # perm_list의 값들에 대해서
    for i in perm_list:
        # check 라는 문자열 변수를 생성하여 리스트에 값을 추가해줄 예정
        check = ""
        # i 값 한개씩 문자열로 변환하여 check 라는 변수에 더해줌
        for j in i:
            check += str(j)
        # 합쳐진 문자열을 answer 리스트에 추가
        answer.append(check)
    # 정답을 출력할 리스트생성
    answer_list = []
    # num_list 의 갯수가 실제 N으로 들어온 것보다 적을 수 있기 때문에 길이 측정
    num_length = len(num_list)
    # 모든 가능한 경우의 수를 만들어 둔 리스트를 순회함
    for i in answer:
        # 실제 배열의 길이만큼 반복문 시행
        for j in range(num_length):
            # 값들의 스트라이크 갯수와 볼 갯수를 체크하는 변수
            check_s = 0
            check_b = 0
            # 첫째자리 ~ 셋째자리 까지 반복문 시행
            for k in range(3):
                # 만약 i의 자리가 num_list(실제로 물어본 값)의 자리와 같은 경우 check_s 스트라이크 갯수 증가
                if i[k] == num_list[j][k]:
                    check_s += 1
                # 만약 자리의 값이 다를 경우
                elif i[k] != num_list[j][k]:
                    # 볼인지 확인하기 위해 리스트에 존재하는지 체크하고 있을 경우 볼의 갯수 증가
                    if i[k] in num_list[j]:
                        check_b +=1
            # 이렇게 반복문이 끝난 후 체크 된 스트라이크 갯수와 실제 입력으로 들어온 스트라이크 갯수 비교
            # 체크 된 볼의 갯수와 실제 볼의 갯수 비교
            # 둘다 같은 경우 넘어가고 아닌 경우 break를 통해서 쓸데없는 반복문을 안돌게함.
            if check_s == base_list[j][1] and check_b == base_list[j][2]:
               pass
            else:
                break
        # 반복문이 break로 끝나지 않았을 경우 (모두 탐색을 하고 조건에 부합할 경우)
        else:
            # 정답 리스트에 값을 추가
            answer_list.append(i)
    # 이렇게 추가된 값들의 갯수를 출력
    print(len(answer_list))
# num_list 에 값이 저장되지 않았을 경우
else:
    # no_list 에 값들을 순회하며 check_list 에 저장된 값을 지워나감
    for i in no_list:
        check_list.remove(i)
    # 지워진 값들을 가지고 가능한 모든 경우의 수를 생성
    perm_list = list(permutations(check_list,3))
    # perm_list의 길이를 출력
    print(len(perm_list))