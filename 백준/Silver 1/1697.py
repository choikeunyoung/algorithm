from collections import deque

N,K = map(int,input().split())
# popleft 를 사용하기 위해 deque 를 사용 => deque 의 경우 popleft 사용해도 시간 복잡도가 O(1)인 것으로 암
queue = deque([[N,0]])
# 방문했는지 체크를 10만개까지 생성함
visited = [False]*(2*10**5+1)
visited[N] = True
# 만약 위치가 같은 경우 시간이 0 초 걸렸으므로 0 출력
if N == K:
    print(0)
# 시작 위치가 종료위치보다 큰 경우 => -1 해서 도착하는 방법밖에 없다.
elif N > K:
    print(N-K)
# 그 외의 경우
else:
    # queue를 무한 반복
    while queue:
        # 제일 왼쪽 값 pop 하여
        check = queue.popleft()
        # visited 에 True로 변경
        visited[check[0]] = True
        # 2배, -1, +1 한 값들을 각각 변수에 저장
        check_twice = check[0] * 2
        check_minous = check[0] - 1
        check_plus = check[0] + 1
        # -1 했을때 값이 K*2를 넘지 않고 0 이상일때 실행
        if check_minous <= K*2 and check_minous >= 0:
            # 목표 값인 경우 check 에 저장된 count 변수를 출력 => check == [숫자,시간] 으로 구성됨
            if check_minous == K:
                print(check[1]+1)
                break
            # 방문하지 않은 경우
            if not visited[check_minous]:
                # queue에 -1 한값과 이전 값의 시간을 더해서 저장
                queue.append([check_minous,check[1]+1])
                # visted 변수 true로 변경
                visited[check_minous] = True
        # +1 했을때 값이 K*2를 넘지 않고 0 이상일때 실행
        if check_plus <= K*2 and check_plus >= 0:
            # 목표 값인 경우 check 에 저장된 count 변수를 출력 => check == [숫자,시간] 으로 구성됨
            if check_plus == K:
                print(check[1]+1)
                break
            if not visited[check_plus]:
                # queue에 +1 한값과 이전 값의 시간을 더해서 저장
                queue.append([check_plus,check[1]+1])
                visited[check_plus] = True
        # *2 했을때 값이 K*2를 넘지 않고 0 이상일때 실행
        if check_twice <= K*2 and check_twice >= 0:
            # 목표 값인 경우 check 에 저장된 count 변수를 출력 => check == [숫자,시간] 으로 구성됨
            if check_twice == K:
                print(check[1]+1)
                break
            if not visited[check_twice]:
                # queue에 *2 한값과 이전 값의 시간을 더해서 저장
                queue.append([check_twice,check[1]+1])
                visited[check_twice] = True