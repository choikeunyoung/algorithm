import sys

input = sys.stdin.readline
# 테스트 케이스
T = int(input())
for _ in range(T):
    # 들어오는 인원 수
    N = int(input())
    # 총 등수를 카운팅할 리스트
    total_list = []
    # 사람들 등수 추가
    for __ in range(N):
        person_list = list(map(int, input().split()))
        total_list.append(person_list)
    # 서류심사 성적 순위로 정렬
    total_list.sort(key=lambda x: x[0])
    answer_list = []
    # 면접 순위를 정답 리스트에 저장
    answer_list.append(total_list[0][1])
    # 초기 최대값과 최소값 선언
    max_value = answer_list[-1]
    min_value = answer_list[-1]
    # 사람들 성적을 반복문을 순회하며 조건 비교
    for i in total_list[1:]:
        # 앞선 사람의 서류 성적은 높기때문에 면접 순위만 비교
        if i[1] < max_value:
            # 이미 최저로 등록된 점수보다 높아야 하기 때문에 비교 후 높을 경우 순위 갱신
            if i[1] < min_value:
                min_value = i[1]
                answer_list.append(i[1])
    print(len(answer_list))
