# 재귀 제한 풀기
import sys
sys.setrecursionlimit(10000)
# DFS 함수
def backtracking(total, cnt):
    # 횟수가 N과 같으면
    if cnt == N:
        # 값 출력 후 리턴
        print(total)
        return
    # 2째 자리부터는 1, 3, 7, 9 홀수만 뒤에 붙을 수 있음
    for num in num_list:
        # 만들어진 값의 절반정도까지 2씩 증가해가며 소수인지 판단
        for i in range(3, int(total + num)//2,2):
            # 소수가 아닌 경우 반복문 탈출
            if int(total+num) % i == 0:
                break
        # 소수인 경우 DFS 실행
        else:
            backtracking(total+num, cnt + 1)

N = int(input())

num_list = ["1","3","7","9"]
ans_list = ["2","3","5","7"]

if N == 1:
    for ans in ans_list:
        print(ans)
else:
    for ans in ans_list:
        answer = ans
        backtracking(answer, 1)