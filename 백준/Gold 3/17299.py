N = int(input())

num_list = list(map(int,input().split()))

stack = [0]*N

ans = [0]*N
# 각 숫자가 몇개 나왔는지 체크해줄 딕셔너리
num_dict = {}
for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
# 딕셔너리에서 제일 많이 나온 숫자 체크
max_cnt = max(num_dict.values())
# stack에 리스트와 대칭되도록 cnt 값 갯수 넣어줌
for i in range(N):
    stack[i] = num_dict[num_list[i]]
# stack 사용할 리스트
stack_second = []
# 리스트 오른쪽 부터 순회
for i in range(N-1,-1,-1):
    # stack에 값이 있으면
    if stack_second:
        # stack 에는 오른쪽에서 시작해서 제일 큰 횟수와 인덱스가 저장됨
        # 그 갯수보다 작은 경우
        if stack[-1] < stack_second[-1][0]:
            # ans 라는 정답을 출력할 리스트 인덱스 번호에 stack에 저장된 인덱스 번호의 숫자를 넣어줌
            ans[i] = num_list[stack_second[-1][1]]
            # stack_second 에 stack 의 값을 뽑아 (횟수, 인덱스)로 저장
            stack_second.append((stack.pop(),i))
        # stack의 끝값이 stack_second 에 저장된 값보다 큰 경우
        else:
            # 그 값이 max_cnt 값이랑 같으면
            if stack[-1] == max_cnt:
                # 그 인덱스 자리에 -1 로 변환
                ans[i] = -1
                # stack_second 리스트 초기화
                stack_second = []
                # stack_second 에 stack 의 값 뽑아 (횟수, 인덱스) 생성
                stack_second.append((stack.pop(),i))
            else:
                # stack_second 에 저장된 값이 빌때까지
                while stack_second:
                    # 값을 뽑아냄 위에서 이미 비교를 했기 때문에
                    stack_second.pop()
                    # 뽑고 난 후 stack_second 값이 있으면
                    if stack_second:
                        # 다시 위 연산과 동일하게 비교를 시행
                        if stack[-1] < stack_second[-1][0]:
                            # 그래서 값이 있는 경우 ans[i] 에 대응 되는 값 추가
                            ans[i] = num_list[stack_second[-1][1]]
                            # stack에서 값을 뽑아 stack_second 에 추가
                            stack_second.append((stack.pop(),i))
                            # 탈출
                            break
                # break 로 탈출하지 않았을 경우
                else:
                    # 오등큰수가 없기 때문에 ans[i] 에 -1
                    ans[i] = -1
                    # stack_secon에 stack의 값 추가
                    stack_second.append((stack.pop(),i))
    # 처음 시작할때 값 추가 후 그 자리 -1 처리
    else:
        stack_second.append((stack.pop(),i))
        ans[i] = -1
print(*ans)