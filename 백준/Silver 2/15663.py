# 중복된 수 제거한 순열 생성
def N_and_M(num):
    # ans 리스트 길이가 M 과 같으면
    if len(ans) == M:
        # set 에 tuple 형태로 저장
        answer.add(tuple(ans))
        return
    else:
        # 그 외의 경우
        for i in range(N):
            # i 값이 num으로 들어온 index 값과 다를 경우
            if i != num:
                # num_list[i] 값이 카운트 갯수가 0개가 아닌 경우
                if num_dict[num_list[i]] > 0:
                    # num_dict 에서 num_list[i] 의 갯수를 -1 해줌
                    num_dict[num_list[i]] -= 1
                    # ans 에 값 저장
                    ans.append(num_list[i])
                    # 재귀 실행
                    N_and_M(i)
                    # 조건 탈출시 ans 값 뽑아옴
                    ans.pop()
                    # num_dict 의 value 값 다시 1 증가
                    num_dict[num_list[i]] += 1


N, M = map(int,input().split())
num_list = list((map(int,input().split())))
# 리스트 정렬
num_list.sort()
# 리스트 갯수가 몇개인지 체크할 딕셔너리
num_dict = {}
for i in num_list:
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1
# 값을 임시 저장할 리스트
ans = []
# 정답을 출력할 set
answer = set()
# 초기 값 -1로 실행
N_and_M(-1)
# set을 list로 다시 변환
answer = list(answer)
# 정렬 후 출력
answer.sort()
for i in answer:
    print(*i)