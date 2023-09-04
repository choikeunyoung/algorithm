N = int(input())

num_list = list(map(int, input().split()))
# 정렬된 리스트
answer = sorted(num_list)
# 인덱스 번호매칭
cnt = 0
# 딕셔너리 활용
ans_dict = {}
# 정렬된 리스트에서
for i in answer:
    # 딕셔너리에 값이 없으면
    if i not in ans_dict:
        # 값과 인덱스 번호를 넣어줌
        ans_dict[i] = cnt
        # 인덱스 번호 1 증가
        cnt += 1
# num_list 에서 대칭되는 key 값 출력
for j in num_list:
    print(ans_dict[j], end=" ")