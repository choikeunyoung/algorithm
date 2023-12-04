N = int(input())
# 값 리스트
num_list = list(map(int,input().split()))
# 정답을 출력할 리스트
ans_list = [0]*N
# enumerate 사용하여 index와 value 같이 받아옴
for i,v in enumerate(num_list):
    index = 0
    cnt = 0
    # cnt 로 0의 개수를 체크하면서 앞의 빈숫자가 몇개인지 체크
    while cnt != v:
        # 만약 ans_list 의 index 가 0인 경우 0의 개수 증가
        if ans_list[index] == 0:
            cnt += 1
        # 반복하며 index 값 1씩 증가
        index += 1
    # 만약 0의 개수는 충족하지만 index에 값이 있는 경우
    if ans_list[index] != 0:
        # index에 값이 없을때까지 index 증가
        while ans_list[index] != 0:
            index += 1
    # 0인 ans_list에 index + 1 값 넣어줌
    ans_list[index] = i + 1
print(*ans_list)