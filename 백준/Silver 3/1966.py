import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, search = map(int, input().split())
    # 중요도 순위 리스트 생성
    priority_list = list(map(int, input().split()))
    # 중요도 리스트 index 번호와 매칭
    for i, v in enumerate(priority_list):
        priority_list[i] = (v, i)
    # deque 로 변환
    priority_list = deque(priority_list)
    # max_value 에 max 값 추출
    max_value = max(priority_list)[0]
    # 초기 cnt 값 1 선언
    cnt = 1
    while True:
        # max_value 와 중요도의 max 값이 같은 경우
        if max_value == priority_list[0][0]:
            # 중요도 리스트 0번 인덱스의 인덱스가 search와 같으면
            if priority_list.popleft()[-1] == search:
                # cnt 값 출력 후 break
                print(cnt)
                break
            # 그 외의 경우 max_value 값 갱신
            else:
                max_value = max(priority_list)[0]
            # 값을 뽑으면 cnt 증가
            cnt += 1
        else:
            priority_list.rotate(-1)
