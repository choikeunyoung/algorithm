import sys

input = sys.stdin.readline
# 몇명을 확인할지 받아오는 변수
N = int(input())
# 학생들이 각각 누구를 가리키는지 넣을 리스트
students = []
# 리스트에 각각 누구를 가리키는지 저장
for _ in range(N):
    students.append(int(input()))

# 각 학생별로 몇명을 거치는지 N 만큼 리스크 길이 생성
answer = [0]*N

for i in range(N):
    # 몇명을 거쳤는지 체크하는 변수
    cnt = 1
    # 그 사람을 방문 했는지 안했는지
    visited = [False]*N
    # 초기 사람은 방문하고 시작
    visited[i] = True
    # stack 리스트에 처음 사람이 누굴 가리키는지 추가
    stack = [students[i]]
    # stack 값이 들어있을 경우 계속 반복
    while stack:
        # stack 값을 뽑아서 check 변수에 담아줌
        check = stack.pop()
        # check-1 번 인덱스가 방문하지 않았을 경우
        if not visited[check-1]:
            # check-1 인덱스에 True 로 방문했다고 변경
            visited[check-1] = True
            # stack에 다음은 누굴 가리키는지 추가
            stack.append(students[check-1])
            # 한 사람을 거쳤으니 cnt 값 증가
            cnt += 1
    # 각 해당 인덱스별로 몇명을 거쳤는지 cnt 값 대입
    answer[i] = cnt
# 제일 많이 방문한 사람이 몇명을 방문했는지 값을 추출
max_value = max(answer)
# 반복문을 진행하며 max_value 와 값이 동일할 경우 index 출력 후 break
for i in range(N):
    if max_value == answer[i]:
        print(i+1)
        break