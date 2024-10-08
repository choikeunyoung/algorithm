import sys
# 재귀 제한 해제
sys.setrecursionlimit(10000)
# 백트래킹
def backtracking(cnt):
    # 리스트 2배의 길이가 됐을때 종료
    if cnt == N*2:
        print(*answer)
        exit()
        return
    # 리스트 안의 값 순회
    for value in num_list:
        # 딕셔너리 값이 존재할 경우
        if num_dict[value] > 0:
            # 딕셔너리 값이 2인 경우 백트래킹
            if num_dict[value] == 2:
                answer.append(value)
                num_dict[value] -= 1
                backtracking(cnt+1)
                answer.pop()
                num_dict[value] += 1
            # 이미 한번 나온 경우
            elif num_dict[value] == 1:
                # 현재 값의 인덱스 위치 찾기
                idx = answer.index(value)
                # 현재 cnt 값에서 idx + 1 한 값이 현재 값과 같은경우 같은수이므로 백트래킹
                if cnt - (idx + 1) == value:
                    answer.append(value)
                    num_dict[value] -= 1
                    backtracking(cnt+1)
                    answer.pop()
                    num_dict[value] += 1


N = int(input())
num_list = list(map(int, input().split()))
# 사전 순 먼저 나온것이므로 숫자 정렬
num_list.sort()
num_dict = {}
# 초기 딕셔너리 2로 고정
for i in num_list:
    num_dict[i] = 2

answer = []
# num_list 내부 순회 백트래킹
for i in num_list:
    answer = [i]
    num_dict[i] -= 1
    backtracking(1)
    num_dict[i] += 1
else:
    print(-1)